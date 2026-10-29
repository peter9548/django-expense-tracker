from django.urls import path
from .import views
from django.contrib.auth.views import LoginView, LogoutView


urlpatterns =[
    path('',views.expenses,name='expenses'),
    path('delete/<int:expense_id>/',views.delete_expense,name='delete_expense'),
    path('edit/<int:expense_id>/',views.edit_expense,name='edit_expense'),
    path('register/', views.register,name='register'),
    path('login/', LoginView.as_view(template_name='login.html'),name='login'),
    path('logout/', LogoutView.as_view(next_page='login'),name='logout'),
    path('profile/', views.profile, name='profile'),
    path('profile/edit/', views.edit_profile, name='edit_profile'),
    path('profile/change-password/',views.change_password,name='change_password'),
]