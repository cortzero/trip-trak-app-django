A Django application that keeps track of all the trips a user has taken or is going to take. It also allows to add notes to each trip with an image. This application implements basic authentication for users, so that a user can only interact with his own trips and notes.

# Environment variables
DATABASE_NAME = the name of the databse.
DATABASE_USERNAME = the username to enter the database.
DATABASE_PASSWORD = the password of the user to enter the database.
DATABASE_HOST = the host where the database server is running.
DATABASE_PORT = the port of the host where the database is running.

# How to run
1. Create a virtual environment and activate it.
2. Install the dependencies from the `requirement.txt` file.
3. Run `python manage.py runserver`.
4. Go to `http://localhost:8000`.
