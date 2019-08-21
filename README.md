# CS2102 Python Flask Setup Guide

This guide provides a walk-through of python web development setup.

## Toolkit

### Browser
This guide contains screenshots taken from Firefox browser,
but it should work for any other commonly-used browser.
There may be some minor differences in terms of alignments and element rendering,
so it is encouraged that once you decided to use a browser for testing, stick to it
all the way and standardize across the team.

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

Here is a list of flask-related packages and its main usages:
* flask
    * This package handles routing, request handling and HTML template rendering.
* flask-login
    * This package provides login-related utility functions.
* flask-sqlalchemy
    * This package provides ORM classes that connect the Flask App to database,
    and thus allow you to execute SQL queries in your App.
* flask-wtf
    * This package handles form submission and pass user-entered values into Python objects.
    It also provides other utilities such as validation checks on user-entered fields.

Note that it is fully compatible with normal `html`, `css` and `javascript` files.

### Pycharm (optional)
Pycharm is a popular IDE for Python.
If you have ticked IDLE when downloading Python, you should already have IDLE, which is a simple Python IDE for you to write and run your codes.
However, IDLE is quite minimalist and can be hard to debug if you intend to scale up your project.
Also, you will need to deal with other file types (html, css etc) so using Pycharm can provide you a centralised platform to view everything in one place.

## Sample Web App Walk-through

This should be the directory structure of this guide:
* cs2102-python-flask-setup-guide/
    * FlaskApp/
        * static/
            * <css, js, img, etc...>
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
If you are not sure about `<port>` and don't recall changing such a value during initial setup or launching of PostgreSQL server, then it should be `5432` by default.

To run the web service, you must navigate to the `app` directory and run the following command:

`python3 app.py`

You should see some messages showing up in your terminal, with these last few lines:

```
 * Debugger is active!
 * Debugger PIN: 215-554-995
 * Running on http://localhost:5000/ (Press CTRL+C to quit)

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
If you change the port number to `5001`, the message shown at earlier stage will be changed accordingly.
For this walk-through (and also the CS2102 project), there is no need to change these settings.

To access the web server, open your favorite web browser (Chrome, Firefox, IE, etc) and enter `localhost:5000/` in the address bar.

Press `Enter` then the page below should show up.

`<index page>`

The logic for showing this web page can be found in `views.py`, specifically, these few lines:

```
@view.route('/', methods=['GET'])
def show_index():
    return render_template('index.html')
```

Notice that `localhost:5000` comes from `app.py` setting, and the extra `/` comes from the URL routing mapping in `views.py`.
The web page you are seeing is a rendered HTML file from `index.html` in `templates` folder.
You can drop any `html` files into the same folder for usage. 
Additionally, `Flask` has its own syntax support for writing `html` templates which are rendered on-the-fly. Refer to `log-in.html` and `sign-up.html` for examples.

Switch back to the browser and go to sign-up page like below
(hint: take a look at other URL routing and try to figure out the URL address for sign-up page by yourself).

`<sign-up page>`

Without entering any information, click `submit`.
Sign-up should fail and you should see compulsory fields getting highlighted like below:

`<sign-up page with error msg>`

Now enter the relevant information and click `submit` again.
Sign-up should succeed and you should see a page with success message.

Switch to `psql` console and run the following command:

`SELECT * FROM sample_user`

You should see that the information entered has been inserted into the database.

Switch to your browser again and this time open log-in page, which should look like below:

`<log-in page>`

Observe what happens when you:
* try to log in without entering any information
* try to log in with a non-existing name
* try to log in with an existing name but wrong password
* try to log in with an existing name and correct password

When you are done, close the browser and stop web server by pressing `CTRL+C` in the terminal running it.

## Additional Information

* how to use Bootstrap template in flask project
* flask session
* 

## Acknowledgement

The templates used in this guide are modified from the ones listed [here](https://colorlib.com/wp/free-bootstrap-registration-forms/).
