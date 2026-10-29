from django.shortcuts import render
from .models import Expenses
from django.shortcuts import redirect, get_object_or_404
from django.db.models import Sum
from django.utils import timezone
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login,authenticate
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.decorators import login_required
from django import forms
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
# Create your views here.




def validate_amount(amount):
            try:
                amount = float(amount)
                if amount <=0:
                    return None

                return amount
            except( ValueError,TypeError):
                    return None


@login_required       
def expenses(request):
    # records = Expenses.objects.all()
    # return render(request, 'expenses.html', {'records': records})



    if request.method == 'POST':
        amount = request.POST.get('amount')
        title = request.POST.get('title')
        category = request.POST.get('category')
        description = request.POST.get('description')
        date = request.POST.get('date')

        
        validated_amount = validate_amount(amount)

        if validated_amount is None:
            return render(request, 'expenses.html', {
                'error': 'Invalid amount. Please enter a positive number.'
         })

        amount = validated_amount

        if not title or not category or not date:
            return render(request, 'expenses.html', {
                'error': 'Please fill in all required fields.'

         })
            

        
        Expenses.objects.create(
            amount=amount,
            title=title,
            category=category,
            description=description,
            date=date,
            user=request.user    
        )
        return redirect('expenses')

    
    user_expenses = Expenses.objects.filter(user=request.user)  

    # 1. Total expenses--
    total_expenses = user_expenses.aggregate(Sum('amount'))['amount__sum'] or 0

    # 2. Total number of expense records
    total_count = user_expenses.count()

     # 3. Current month's expenses--
    today = timezone.localdate()

    monthly_expenses = user_expenses.filter(
        date__month=today.month,
        date__year=today.year
    ).aggregate(
         Sum('amount')
    )['amount__sum'] or 0



    monthly_summary = Expenses.objects.values(
        'date__year',
        'date__month'
    ).annotate(
        total=Sum('amount')
    ).order_by('date__year', 'date__month')

    category_summary = user_expenses.values('category').annotate(total=Sum('amount')).order_by('-total')

     


    # All expense records--
    records = user_expenses    ## (Iska matlab: Jo user login hai, uske account ke hi expenses dikhenge.)

    # Pass all values to HTML--
    return render(request, 'expenses.html', {'records':records,'total_expenses': total_expenses,'total_count': total_count,'monthly_expenses': monthly_expenses, 'category_summary': category_summary,'monthlty_summary':monthly_summary})




def delete_expense(request,expense_id):
    if request.method == 'POST':
        expense =get_object_or_404(Expenses, id=expense_id)
        expense.delete()
    return redirect('expenses')



def edit_expense(request, expense_id):
    expense = get_object_or_404(Expenses, id=expense_id)
    if request.method == 'POST':
        expense.amount = request.POST.get('amount')
        expense.title =request.POST.get('title')
        expense.category = request.POST.get('category')
        expense.description = request.POST.get('description')
        expense.date = request.POST.get('date')
        expense.save()
        return redirect('expenses')
    return render(request, 'edit_expense.html', {'expense':expense})




def register(request):
    if request.method =='POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
            return redirect('expenses')
    else:
        form = UserCreationForm()

    return render(request, 'register.html', {'form':form})




@login_required
def profile(request):
    return render(request, 'profile.html')

class ProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']



def edit_profile(request):
    if request.method == 'POST':
        form = ProfileForm(
            request.POST,
            instance=request.user
        )

        if form.is_valid():
            form.save()
            return redirect('profile')

    else:
        form = ProfileForm(instance=request.user)

    return render(request, 'edit_profile.html', {'form': form })




@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(
            user=request.user,
            data=request.POST
        )

        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            return redirect('profile')
    else:
        form = PasswordChangeForm(user=request.user)

    return render(request, 'change_password.html', {
        'form': form
    })