# Simple CRM Application

This is a Customer Relationship Management (CRM) tool designed for admin users to manage records. Admin users can register, log in, log out, and perform CRUD operations on customer records.

![Screenshot](https://i.imgur.com/nrYMJ55l.png)

## Features

- **User Authentication**: Admin users can register, log in, and log out.
- **Add Records**: Admin users can add new customer records.
- **Update Records**: Admin users can update existing customer records.
- **Delete Records**: Admin users can delete customer records.
- **View Records**: Admin users can view detailed information about each customer.

## Tech Stack

- **Backend**: Django (Python)
- **Frontend**: HTML, CSS, Bootstrap
- **Database**: MySQL
- **Authentication**: Django's built-in user authentication

## Setup Instructions

1. **Clone the repository**:
    ```sh
    git clone https://github.com/yourusername/yourprojectname.git
    cd yourprojectname
    ```

2. **Create a virtual environment**:
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the dependencies**:
    ```sh
    pip install -r requirements.txt
    ```

4. **Apply migrations**:
    ```sh
    python manage.py makemigrations
    python manage.py migrate
    ```

5. **Create a superuser**:
    ```sh
    python manage.py createsuperuser
    ```

6. **Run the development server**:
    ```sh
    python manage.py runserver
    ```

7. **Access the application**:
    Open your web browser and navigate to `http://127.0.0.1:8000/`.


