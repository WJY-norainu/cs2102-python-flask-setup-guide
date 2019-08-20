# CS2102 Python Flask Setup Guide

This guide provides a walk-through of python web development setup.

## Toolkits

### PostgreSQL
This guide assumes PostgreSQL has already been installed. If not, follow the separate installation guide for it to set up PostgreSQL.

Once you have installed PostgreSQL, run `init.sql` to set up the database.

### Python
Python 3.7.2 will be used in this guide, but it should work with any Python>=3.5.
However, if you want to use Python2, you may need to make adjustments to some of the sample scripts provided.
Also, there's no guarantee that this guide can work with Python2.

#### For Windows

#### For MacOS

#### For Linux

### Python Packages
The packages needed to run the scripts provided in this guide can be downloaded via:

`pip3 install -r requirements.txt`

The most important packages for this tutorial will be `Flask` and `SQLAlchemy`.

#### Flask

Flask is a lightweight package that...

##### flask
This package handles routing, request handling and HTML template rendering.

##### flask-bootstrap
This package provides web page style utilities.

##### flask-login
This package provides login-related utility functions.

##### flask-sqlalchemy
This package provides ORM classes that connect the Flask App to database,
and thus allow you to execute SQL queries in your App.

##### flask-wtf
This package handles form submission at client side and serialization at server side.

For example, when users sign up, they will provide certain information like username and password.
This package provides a class that can display a table on the web page for users to enter such information,
and then store such user-entered information into Python variables.

This package also helps perform validation check on user-entered fields.

### Pycharm (optional)
Pycharm is a popular IDE for Python.
If you have ticked IDLE when downloading Python, you should already have IDLE, which is a simple Python IDE for you to write and run your codes.
However, IDLE is quite minimalist and can be hard to debug if you intend to scale up your project.
Also, you will need to deal with other file types (html, css etc) so using Pycharm can provide you a centralised platform to view everything in one place.

## Sample Web App Walk-through

This should be the directory structure of this guide:
* cs2102-python-flask-setup-guide/
    * FlaskApp/
        * templates/
            * index.html
        * app.py
        * models.py
        * views.py
    * init.sql
    * README.md
    * requirements.txt

Open `app.py` and locate the following lines of codes:

```
# Config
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://{username}:{password}@{host}:{port}/{database}'\
    .format(
        username='<username>',
        password='<password>',
        host='localhost',
        port=<port number>,
        database='sample_database'
    )
```
Replace `<username>`, `<password>`, and `<port>` with the actual configuration of your database.

To run the web service, you must navigate to the `app` directory and run the following command:

`python3 app.py`

You should see some messages showing up in your terminal, with these last few lines:

```
 * Debugger is active!
 * Debugger PIN: 215-554-995
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)

```
There may be warnings for SQLAlchemy but you can ignore those.

Go back to `app.py` file and observe the following lines:

```
if __name__ == "__main__":
    app.run(
        debug=True,
        host='localhost',
        port=5000
    )
```

These few lines define the port to run the web server.
If you change the port number to 5001, the message shown at earlier stage will be changed accordingly.
For this walk-through (and also the CS2102 project), there is no need to change these settings.

To access the web server, open your favorite web browser (Chrome, Firefox, IE, etc) and enter the following into the address bar:

`localhost:5000/`

The page below should show up.

The logic for showing this web page can be found in `views.py`, specifically, these few lines:

```
@view.route('/', methods=['GET'])
def show_index():
    return render_template('index.html')
```

Notice that `localhost:5000` comes from `app.py` setting, and the extra `/` comes from the URL routing mapping in `views.py`.

The HTML template being rendered in the code is in `templates` folder.

Switch back to the browser and go to sign-up page 
(hint: try to figure out what to enter in address bar yourself).

Enter the relevant information and click the button to sign up.

Now you should see the following message.

Switch back to `psql` console and run the following command:

``

The information you just entered has been inserted into the database.



When you are done, close the browser and terminate web service by pressing `CTRL+C` in the terminal that's running the service.

## Additional Information
