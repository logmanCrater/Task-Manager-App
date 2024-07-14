# Project Setup Instructions

Follow these steps to set up the Task Manager project on your local machine.

## Prerequisites

- Python 3.x
- pip (Python package installer)

# Step 1: Clone the Repository

Clone the project repository from GitHub (or any other source).
```
git clone <repository_url>
cd <repository_directory>
```
# Step 2: Create a Virtual Environment

Create a virtual environment to isolate the project's dependencies.
### On Windows use:
```
python -m venv venv
`venv\Scripts\activate`
```
### On Linux/MacOS use:
```
python -m virtualenv venv
source venv/bin/activate   
```

# Step34: Change directory to django project

To run project we need redirect terminal to task_manager
```
cd task_manager
```

# Step 4: Install Dependencies

Install the required Python packages using `pip`.
```
pip install -r requirements.txt
```
# Step 5: Configure the Database

Update the database settings in `settings.py` according to your database setup. For SQLite (default), no changes are needed.

# Step 6: Run Migrations

Apply database migrations to set up the database schema.
```
python manage.py makemigrations
python manage.py migrate
```

# Step 7: Configure Email Settings

Update the email settings in `settings.py` to use Gmail for sending password reset emails. Add the following configuration:
```
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'your_email@gmail.com'
EMAIL_HOST_PASSWORD = 'your_email_password'  # Use an App Password if 2FA is enabled
DEFAULT_FROM_EMAIL = 'your_email@gmail.com'
```
# Step 8: Create a Superuser

Create a superuser to access the Django admin interface.
```
python manage.py createsuperuser
```
# Step 9: Run the Development Server

Start the Django development server.
```
python manage.py runserver
```
# Access the Application

- Open your browser and go to <http://127.0.0.1:8000/> to access the application.
- Go to <http://127.0.0.1:8000/admin/> to access the Django admin interface.

# Additional Information

### Resetting Password

To reset a user's password, go to the login page and click the "Forgot Password?" link. Follow the instructions to reset the password via email.

### API Documentation

Refer to the [API documentation](api_managment) for details on how to interact with the Task Manager API.
### Requirements

See [`requirements.txt`](../task_manager/requirements.txt) for details on which libraries this file downloads to your computer when you perform [Step 4]().
