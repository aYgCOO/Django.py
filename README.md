# Django.py
Let's Start !

# Basic cmd for Django users 

`django-admin startproject [project_name]`: Creates a new Django project with the given name.

`python manage.py startapp [app_name]`: Creates a new Django app within your project.

`python manage.py runserver`: Starts the development server.

`python manage.py migrate`: Applies any pending database migrations.

`python manage.py makemigrations [app_name]`: Creates new database migrations based on changes to your models.

`python manage.py createsuperuser`: Creates a superuser account for administrative access to the Django admin interface.

`python manage.py shell`: Opens up a Python shell with Django environment loaded, useful for testing and debugging.

`python manage.py collectstatic`: Collects static files from your apps into a single location for deployment.

`python manage.py test [app_name]`: Runs tests for the specified app(s).

`python manage.py shell_plus`: Opens a Python shell with Django environment loaded and includes all the models from your apps. (Requires django-extensions)

`python manage.py dbshell`: Opens a database shell for the default database.

`python manage.py check`: Checks for any issues in your project without making migrations or touching the database.
