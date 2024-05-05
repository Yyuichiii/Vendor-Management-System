
# Vendor Management System

Below are the steps to get started with the project.

## Cloning the Repository

To get started, clone this repository to your local machine using the following command:

```bash
git clone https://github.com/Yyuichiii/Vendor-Management-System.git
```

## Installing Dependencies

Navigate to the project directory and install the required dependencies using pip. We recommend using a virtual environment to manage your dependencies.

```bash
cd Vendor-Management-System
pip install -r requirements.txt
```

## Making Migrations

Before running the application, you need to make migrations for the database schema changes. Run the following command:

```bash
python manage.py makemigrations
```

## Migrating the Database

After making migrations, apply them to the database using the following command:

```bash
python manage.py migrate
```

## Creating Superuser

To have administrative privileges in the application, create a superuser account using the following command and follow the prompts:

```bash
python manage.py createsuperuser
```

## Running the Server

Finally, you can run the development server using the following command:

```bash
python manage.py runserver
```

The server will start running at http://127.0.0.1:8000/ by default. 
