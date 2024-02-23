## MEDi

## Project Information

- Project Name: Med-Assistant Machine Learning Project

## How To Use This

1. Make sure PostgreSQL and pgadmin are installed on your system.
2. Manually create a DB instance on PostgreSQL named "predico" (you can use PgAdmin for that).
3. Make a new environment (recommended) and run the following commands:

   pip install -r requirements.txt
   python manage.py makemigrations
   python manage.py migrate
   python manage.py runserver

4. Navigate to [http://127.0.0.1:8000/](http://127.0.0.1:8000/) in your browser.
