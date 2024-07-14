# Task Manager API Documentation

This document explains how the Task Manager API works, providing all the necessary information for front-end developers to interact with the API.

## Base URL


```
http://127.0.0.1:8000/
```


 ## Authentication

The API uses token-based authentication. You need to obtain a token and include it in the Authorization header for all requests.

### Login to Obtain Token

##### `POST /api/token/`

**Request Body:**


```
{
  "username": "your_username",
  "password": "your_password"
}
```


**Response:**


```
{
  "access": "your_access_token",
  "refresh": "your_refresh_token"
}
```


**Include the token in the Authorization header for all API requests:**


##### `Authorization: Bearer your_access_token`

### Password Reset

The API provides endpoints for users to reset their passwords via email.

#### Request Password Reset

##### `POST /password_reset/`

**Request Body:**


```
{
  "email": "user@example.com"
}
```


**Response:**


```
{
  "detail": "Password reset e-mail has been sent."
}
```


#### Confirm Password Reset

The user will receive an email with a link to reset their password. The link will direct them to a form where they can enter a new password.

##### `POST /reset/<uidb64>/<token>/`

**Request Body:**


```
{
  "new_password1": "new_password",
  "new_password2": "new_password"
}
```


**Response:**


```
{
  "detail": "Password has been reset with the new password."
}
```


API Endpoints
-------------

### Tasks

#### Get All Tasks


##### `GET /api/tasks/`

**Response:**



```
[
  {
    "id": 1,
    "title": "Task Title",
    "description": "Task Description",
    "status": "pending",
    "assigned_to": [1, 2],
    "assigned_group": 1,
    "created_by": 1,
    "created_at": "2024-07-12T12:34:56Z",
    "updated_at": "2024-07-12T12:34:56Z"
  },
  ...
]
```


#### Get a Single Task





##### `GET /api/tasks/{id}/`

**Response:**



```
{
  "id": 1,
  "title": "Task Title",
  "description": "Task Description",
  "status": "pending",
  "assigned_to": [1, 2],
  "assigned_group": 1,
  "created_by": 1,
  "created_at": "2024-07-12T12:34:56Z",
  "updated_at": "2024-07-12T12:34:56Z"
}
```


#### Create a Task





##### `POST /api/tasks/`

**Request Body:**


```
{
  "title": "Task Title",
  "description": "Task Description",
  "status": "pending",
  "assigned_to": [1, 2],  # Optional if assigning manually
  "assigned_group": 1     # Optional if assigning to a group
}
```


**Response:**


```
{
  "id": 1,
  "title": "Task Title",
  "description": "Task Description",
  "status": "pending",
  "assigned_to": [1, 2],
  "assigned_group": 1,
  "created_by": 1,
  "created_at": "2024-07-12T12:34:56Z",
  "updated_at": "2024-07-12T12:34:56Z"
}
```


#### Update a Task

##### `PUT /api/tasks/{id}/`

**Request Body:**


```
{
  "title": "Updated Task Title",
  "description": "Updated Task Description",
  "status": "in_progress",
  "assigned_to": [1, 2],
  "assigned_group": 1
}
```


**Response:**


```
{
  "id": 1,
  "title": "Updated Task Title",
  "description": "Updated Task Description",
  "status": "in_progress",
  "assigned_to": [1, 2],
  "assigned_group": 1,
  "created_by": 1,
  "created_at": "2024-07-12T12:34:56Z",
  "updated_at": "2024-07-12T12:34:56Z"
}
```


#### Delete a Task

##### `DELETE /api/tasks/{id}/`

**Response:**


```
{
  "message": "Task deleted successfully."
}
```


### Users

#### Get All Users

##### `GET /api/users/`

**Response:**


```
[
  {
    "id": 1,
    "username": "user1",
    "email": "user1@example.com",
    "is_staff": true,
    "is_superuser": false
  },
  ...
]
```

#### Get a Single User

##### `GET /api/users/{id}/`

**Response:**


```
{
  "id": 1,
  "username": "user1",
  "email": "user1@example.com",
  "is_staff": true,
  "is_superuser": false
}
```


### Task Groups

#### Get All Task Groups

##### `GET /api/task_groups/`

**Response:**


```
[
  {
    "id": 1,
    "name": "Task Group 1",
    "director": 1,
    "staff_members": [1, 2]
  },
  ...
]
```


#### Get a Single Task Group

##### `GET /api/task_groups/{id}/`

**Response:**


```
{
  "id": 1,
  "name": "Task Group 1",
  "director": 1,
  "staff_members": [1, 2]
}
```


#### Create a Task Group

##### `POST /api/task_groups/`

**Request Body:**


```
{
  "name": "Task Group 1",
  "director": 1,
  "staff_members": [1, 2]
}
```


**Response:**


```
{
  "id": 1,
  "name": "Task Group 1",
  "director": 1,
  "staff_members": [1, 2]
}
```


#### Update a Task Group

##### `PUT /api/task_groups/{id}/`

**Request Body:**


```
{
  "name": "Updated Task Group",
  "director": 2,
  "staff_members": [3, 4]
}
```

**Response:**


```
{
  "id": 1,
  "name": "Updated Task Group",
  "director": 2,
  "staff_members": [3, 4]
}
```


#### Delete a Task Group

##### `DELETE /api/task_groups/{id}/`

**Response:**


```
{
  "message": "Task group deleted successfully."
}
```


### Status Change Requests

#### Get All Status Change Requests

##### `GET /api/status_change_requests/`

**Response:**


```
[
  {
    "id": 1,
    "task": 1,
    "requested_by": 1,
    "current_status": "pending",
    "requested_status": "in_progress",
    "is_approved": false
  },
  ...
]
```


#### Get a Single Status Change Request

##### `GET /api/status_change_requests/{id}/`

**Response:**


```
{
  "id": 1,
  "task": 1,
  "requested_by": 1,
  "current_status": "pending",
  "requested_status": "in_progress",
  "is_approved": false
}
```


#### Create a Status Change Request

##### `POST /api/status_change_requests/`

**Request Body:**


```
{
  "task": 1,
  "requested_by": 1,
  "current_status": "pending",
  "requested_status": "in_progress"
}
```


**Response:**


```
{
  "id": 1,
  "task": 1,
  "requested_by": 1,
  "current_status": "pending",
  "requested_status": "in_progress",
  "is_approved": false
}
```

#### Approve a Status Change Request

##### `PUT /api/status_change_requests/{id}/approve/`

**Response:**


```
{
  "id": 1,
  "task": 1,
  "requested_by": 1,
  "current_status": "pending",
  "requested_status": "in_progress",
  "is_approved": true
}
```


#### Delete a Status Change Request

##### `DELETE /api/status_change_requests/{id}/`

**Response:**


```
{
  "message": "Status change request deleted successfully."
}
```


Summary
-------

This document provides all the necessary endpoints and their usage for interacting with the Task Manager API. Front-end developers can use this documentation to integrate the API into their front-end applications.

Notes
-----

-   Ensure all requests include the Authorization header with the access token.
-   Validate all inputs before making API requests to avoid errors.
-   Handle responses and errors appropriately in the front-end application.

This documentation should help front-end developers understand and use the API effectively. If there are any changes to the API, make sure to update this document accordingly.
                                                             