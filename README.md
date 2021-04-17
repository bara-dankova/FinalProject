# FinalProject
Sky GIT Web App

application directory
- static directory
    - images directory
    - styles.css
- templates directory
    - layout.html: basic layout and style
    - html files that extend from layout: only insert blocks of code (body, footer, etc.)
- app.py: the file to run to actually open the web app
- __init__.py: imports Flask, instantiates Flask as an app, configures the connection to database to use SQLAlchemy
- routes.py: URL structure, renders html templates, middleman between html files and database
- forms.py: imports needed modules, instantiated Forms classes which are then used within html files and routes.py
- models.py: allows you to manipulate the database by using SQLAlchemy

other stuff
- requirements: list of required packages to install easily from one place
- .gitignore: stuff like virtual environments to avoid git mess

    
