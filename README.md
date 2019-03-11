# Project Scope

1. Create a web application that allows users to **store** and easily **access** <del>cooking recipes</del> Surfing Locations
2. Design a **database schema** based on <del>recipes</del> Surfing Locations, and any other related properties and entities (e.g. views, upvotes, <del>ingredients, recipe authors, allergens, author’s country of origin, cuisine</del>surfing locations related information etc…). Make sure to put some thought into the relationships between them, and use either **foreign keys** (in the case of a **relational database**) <del>or nesting (in the case of a document store) to connect these pieces of data</del>

    Design a DB:
    -   What is it for?
        >   'we help customers find surfing locations, discover what other thought about them, contribute their own reviews and opinions, and learn about other locations they might like based on surfers with similar habits and surfing needs'

    -   What tables do you need?
        >   employee -> comment
        customer -> event
        product -> blog

3. Create the **backend code and frontend form** to allow users to **add new** <del>recipes</del> Surfing Locations to the site
4. Create the **backend code** to **group and summarise** the <del>recipes</del>Surfing Locations on the site, based on their attributes such as <del>cuisine, country of origin, allergens, ingredients</del>break type, direction of wave, bottom, etc. and a **frontend** page to **show this summary**, and make the **categories clickable** to drill down into a **filtered view based on that category**. This frontend page can be as simple or as complex as you’d like; you can use a Python library such as matplotlib, or a JS library such as d3/dc (that you learned about if you took the frontend modules) for visualisation
5. Create the **backend** code to **retrieve a list** of <del>recipes</del> Surfing Locations, filtered based on various criteria <del>(e.g. allergens, cuisine, etc…)</del> and **order them based on some reasonable aspect** (e.g. number of views or upvotes). Create a **frontend** page to **display** these, and to **show some summary statistics around the list** (e.g. number of matching <del>recipes</del> Surf Locations, number of new <del>recipes</del> Surf Locations. Optionally, add support for **pagination**, when the number of results is large
6. Create a detailed view for each <del>recipes</del> Surfing Location, that would just show all attributes for that <del>recipe, and the full preparation instructions</del>
7. Allow for **editing and deleting** of the <del>recipe</del> records, either on separate pages, or built into the list/detail pages
8. Optionally, you may choose to add basic user registration and authentication to the site. This can as simple as adding a username field to the recipe creation form, without a password (for this project only, this is not expected to be secure)

# Project guidelines

- **Logic must be written in Python**. HTML, CSS, and JavaScript can be used to enhance the look and feel of the cookbook.
- Whenever possible, strive to use semantic HTML5 elements to structure your HTML code better.
- The website **must be data-driven** and can rely on structured data, unstructured data or a mix of structured and unstructured data. 
- **CRUD (create read update delete) operations** can be carried out using either SQL (e.g. MySQL/SQLite/Postgres) or NoSQL (e.g. MongoDB).
- **Use Flask**, a micro-framework, to run your application. **Provide instructions on how to run your project locally in your README**.
- Make sure your site is as **responsive** as possible. You can test this by checking the site on different screen sizes and browsers.
- **Share details of how you created your database schema in your README**. Consider sharing working drafts or finalised versions of your database schema in a 'Database Schema' folder in your repo. Provide a link to this folder in your README.
- We advise that you write down **user stories** and **create wireframes/mockups** before embarking on full-blown development.
- The site can also make use of CSS frameworks such as **Bootstrap**, just make sure you maintain a clear separation between the library code and your code.
- Write a **README.md** file for your project that explains what the project does and the need that it fulfills. It should also describe the functionality of the project, as well as the technologies used. If some of the work was based on other code, explain what was kept and how it was changed to fit your need. A project submitted without a README.md file will FAIL.
- Use **Git** & GitHub for version control. Each new piece of functionality should be in a separate commit.
- **Deploy** the final version of your code to a hosting platform such as Heroku.


Error message for incomplete input fields, do one with JS, secondone with Python

# Project dependencies with CLI

## PyPI - Python + Flask packages

$ `sudo pip3 install -r requirements.txt`

# Steps to start the project

1. Install Flask `sudo pip install flask` or `sudo pip3 install Flask`
2. Create new Python file - e.g. `app.py`
3. Import flask functionality inside that file and create an instance of Flask: **OK**

```py
import os
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Helloooo World!'

if __name__ = '__main__':
    app.run(host=os.environ.get('IP),
    port=int(os.environ.get('PORT')),
    debug=True)
```

<u>There are usual ten lines of code that you would use to run a flask application:</u>

- The `app.run()` will run the server
- Importing `os` and then inside of our `app.run` we pass in the series of arguments so the first argument passing is the host name `os.environ.get` will allow us to get the IP address (this is so we can
tell flask which what the IP address we want to run this on)
- next is the `port` that we want to open for this, so next one we do is the port and we need to cast that to an `int` so `int(os.environ.get)`
- the debug mode is `True` because we're going to be developing and we want to be able to to do some debugging


# FLASKs flask installation steps:

1. We recommend using the latest version of Python 3
2. Install Flask `pip install Flask`
3. A minimal Flask Application looks like that: **Does not work with HEROKU**

```py
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'
```

4. To run the application you can either use the flask command or python’s -m switch with Flask. Before you can do that you need to tell your terminal the application to work with by exporting the FLASK_APP environment variable:

```
$ export FLASK_APP=hello.py
$ flask run
 * Running on http://127.0.0.1:5000/
```

# Steps to upload the page to Heroku (Medium article)

[Steps](https://medium.com/@gitaumoses4/deploying-a-flask-application-on-heroku-e509e5c76524)

1. Installing Heroku CLI
2. Creating a Heroku Account or Login to Heroku `heroku login`
3. Initializing a git repository if not already createad
4. Create a heroku application `heroku create your-first-heroku-app --buildpack heroku/python`
5. Add the remote heroku git repository `heroku git:remote -a your-first-heroku-app`
6. Install gunicorn (Gunicorn is a python WSGI HTTP server that will serve your Flask application at heroku) `pip install gunicorn`
7. Create requirements.txt file in your project root folder in order for heroku to detect it as a Python project `pip freeze > requirements.txt`
8. Adding a Procfile. Create a Procfile in the project root folder and add the following line: `web: gunicorn app:app` (The first app represents the name of the python file that runs your application or the name of the module it is in. The second app represents your app name.)
9. Committing the files to Heroku’s repository master branch `git add .` and `git commit -m "First commit for heroku"` Push the changes from your local master branch to heroku’s master branch `git push heroku master`
10. Done

# Steps to upload the page to Heroku (CI)

1. Login to Heroku `heroku login` **OK**
2. Initializing a git repository if not already createad
3. Create a heroku application `heroku create your-first-heroku-app --buildpack heroku/python` **(created in the app itself)**
4. Add the remote heroku git repository `heroku git:remote -a your-first-heroku-app` **OK**
5. Create requirements.txt file in your project root folder in order for heroku to detect it as a Python project `sudo pip3 freeze --local > requirements.txt` **(WORKED)**
6. Adding a Procfile `echo web: python app.py > Procfile` **OK**
7. Committing the files to Heroku’s repository master branch `git add .` and `git commit -m "First commit for heroku"` Push the changes from your local master branch to heroku’s master branch `git push heroku master`
8. Run the application `heroku ps:scale web=1` (This is a command to the Heroku to tell it to get up and running) **OK**
9. Heroku web app - go to Settings>Config Variables to specify our IP and PORT `IP = 0.0.0.0` and `PORT = 5000` **OK**
10. DONE 

# Connect Flask to MongoDB (CI)

1. To get Flask talking to Mongo, we're going to install a third party library called flask-pymongo `sudo pip3 install flask-pymongo`
2. We also need to install a package called dnsython to use the new style connection string for MongoDB Atlas `sudo pip3 install dnspython`
3. Add some additional imports to reflect our new installation in the app.py file and import something from the BSON library as well, which we'll use later on in the project
```py
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
```
4. Add the Mongo database name and the URL linking to that database.
5. Edit the `bashrc` via terminal `nano ~/.bashrc`
6. Include `export MONGO_URI=mongodb+srv://daniel:<password>@myfirstcluster-ggk14.mongodb.net/surfingeurope?retryWrites=true`

**Slack**
You need to edit bashrc
`nano ~/.bashrc`
Then add the variable in and save it (ctrl x) + Y enter
Then `source ~/.bashrc` to reload them

1. Put this line at the end of your `~/.bashrc` file and save it:
2. `export MONGO_URI=mongodb://username:password@ds139435.mlab.com:39435/dumpdinners`
3. Enter `. ~/.bashrc` or `source ~/.bashrc`  in your terminal.   You should get no errors, no output.
4. In the python3 shell, enter `import os` then `os.getenv("MONGO_URI")`   It should output the `mongodb://...` string.
5. If that all works you should be good to go in your app using `app.config["MONGO_URI"] = os.getenv("MONGO_URI")`.
