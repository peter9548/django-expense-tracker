# Django Expense Tracker

A Django-based web application for recording, managing, and reviewing
daily expenses. It includes user accounts, expense CRUD operations,
dashboard summaries, and profile settings.

## Features

-   User registration and login
-   Google sign-in (when django-allauth and Google OAuth are configured)
-   Add, view, edit, and delete expenses
-   Expenses associated with the logged-in user
-   Dashboard totals, expense count, and current-month spending
-   Category-wise and monthly expense summaries
-   View and edit profile details
-   Change password
-   Django admin interface

## Technologies Used

-   Python
-   Django
-   SQLite (default local database, unless configured otherwise)
-   HTML and CSS
-   Django Authentication
-   django-allauth (optional Google sign-in)

## Project Structure

``` text
expense_tracker/
├── config/          # Django project settings and main URLs
├── expenses/        # Expense app: models, views, URLs
├── templates/       # HTML templates (location may vary)
├── static/          # CSS and other static assets (if configured)
├── manage.py        # Django management commands
├── requirements.txt # Project dependencies
├── .gitignore       # Files Git should ignore
└── README.md        # Project documentation
```

Adjust this structure to match the actual folders in your repository.

## Getting Started

### 1. Clone the repository

Replace the example URL with your GitHub repository URL.

``` bash
git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY.git
cd YOUR-REPOSITORY
```

### 2. Create and activate a virtual environment

**Windows (Command Prompt):**

``` bash
python -m venv venv
venv\Scripts\activate
```

**macOS / Linux:**

``` bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

``` bash
python -m pip install -r requirements.txt
```

If `requirements.txt` does not exist yet, generate it from your project
environment:

``` bash
python -m pip freeze > requirements.txt
```

### 4. Configure Google sign-in (optional)

If Google sign-in is enabled, configure the Google provider in Django
admin / django-allauth and set the authorized callback URL for local
development to:

``` text
http://127.0.0.1:8000/accounts/google/login/callback/
```

Do not commit your Django `SECRET_KEY`, Google OAuth client secret, or
other credentials to GitHub. Keep them in environment variables or a
local `.env` file, and add `.env` to `.gitignore`.

### 5. Apply migrations

``` bash
python manage.py migrate
```

### 6. Create an admin user (optional)

``` bash
python manage.py createsuperuser
```

### 7. Run the development server

``` bash
python manage.py runserver
```

Open these URLs in your browser:

-   Application: http://127.0.0.1:8000/
-   Django admin: http://127.0.0.1:8000/admin/

## How to Use

1.  Register or log in.
2.  View your spending totals and summaries on the dashboard.
3.  Add an expense with its amount, title, category, date, and optional
    description.
4.  Edit or delete expenses as needed.
5.  Open **My Profile** to view or update profile details.
6.  Use **Change Password** to update your password.

## Screenshots

Add screenshots of your running project to a `screenshots/` folder and
update the links below.


## Screenshots

![Expense Tracker Dashboard](screenshots\Screenshot_29-10-2026_17472_127.0.0.1.jpeg)

![Expense Tracker Screenshot 2](screenshots\Screenshot_29-10-2026_174649_127.0.0.1.jpeg)

![Expense Tracker Screenshot 3](screenshots\Screenshot_29-10-2026_174718_127.0.0.1.jpeg)

![Expense Tracker Screenshot 4](screenshots\Screenshot_29-10-2026_174728_127.0.0.1.jpeg)


## Important Notes

-   This is a learning project built with Django.
-   Before public deployment, use a secure secret key and
    production-safe settings.
-   Make sure edit and delete views verify that the requested expense
    belongs to the logged-in user.
-   Make sure all dashboard summaries filter data by the logged-in user.
-   Google OAuth requires valid credentials and provider configuration.

## Future Improvements

-   Add automated tests for registration, expense CRUD, and
    user-specific access.
-   Improve validation and error messages.
-   Add date-range filters, charts, search, and pagination.
-   Deploy with production-safe settings.

## Author

**Your Name**

-   GitHub: https://github.com/peter9548

------------------------------------------------------------------------

If you find this project useful, feel free to star the repository.
