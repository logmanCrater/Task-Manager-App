# Welcome to the Django-Based Task Manager

## Project Description

The Task Manager Project is designed to facilitate efficient task management and collaboration among team members. With features including task creation, assignment to individuals or groups, and status tracking, it provides a robust solution for managing projects of any scale. The project leverages Django for the backend and provides a RESTful API for interaction.

## Features

- User Authentication and Authorization
- Task Creation and Management
- Assign Tasks to Individual Users or Groups
- Status Tracking and Updates
- Password Reset via Email
- Admin Interface for Managing Users and Tasks

## Technical Information

### Backend

- **Framework**: Django
- **Database**: SQLite (default configuration)
- **Authentication**: JWT (JSON Web Token) using `djangorestframework-simplejwt`
- **Email Service**: Configured for Gmail SMTP for password reset functionality

### API

The API is built using Django REST framework, providing endpoints for managing tasks, users, and authentication.

### Installation and Setup

To set up the project, clone the repository, create a virtual environment, and install the dependencies listed in the `requirements.txt` file. Run the migrations to set up the database schema and create a superuser to access the Django admin interface. Detailed setup instructions can be found in the `setup_instructions.txt` file.

### Email Configuration

The project is configured to use Gmail for sending password reset emails. Update the email settings in `settings.py` with your Gmail credentials. Use an App Password if two-factor authentication (2FA) is enabled.or else it won't work.To learn how go Setup Instructions Step 7

## Documentation and Resources

- [API documentation](docs/api_managment.md)
- [Setup Instructions](docs/setup_instruction.md)

Thank you for exploring the Task Manager Project. For any questions or contributions, please feel free to reach out or create a pull request.
