from flask import Blueprint, redirect, render_template
from flask_login import current_user, login_required, login_user

from __init__ import db, login_manager
from forms import SignUpForm, LogInForm

view = Blueprint('view', __name__)


@login_manager.user_loader
def load_user(user_name):
    query = '''SELECT 1 FROM sample_table WHERE sample_user.name = {}'''.format(user_name)
    return db.session.execute(query).fetchone()


@view.route('/', methods=['GET'])
def show_index():
    return render_template('index.html')


@view.route('/signUp', methods=['GET', 'POST'])
def show_sign_up():
    form = SignUpForm()
    print(form.name.data)
    if form.validate_on_submit():
        name = form.name.data
        preferred_name = form.preferred_name.data
        password = form.password.data
        exists_user = login_user(name)
        if exists_user:
            return '''{} has already signed up.'''.format(name)
        else:
            query = '''INSERT INTO sample_table(name, preferred_name) VALUES ("{}", "{}", "{}")'''\
                .format(name, preferred_name, password)
            db.session.execute(query)
            db.session.commit()
            return '''You have successfully signed up!'''
    else:
        return render_template('sign-up.html', form=form)


@view.route('/logIn', methods=['GET', 'POST'])
def show_login():
    form = LogInForm()
    if form.validate_on_submit():
        name = form.name.data
        exists_user = login_user(name)
        if exists_user:
            return redirect('/logInSuccess')
        else:
            return '''{} has not signed up yet. We cannot log you in.'''.format(name)
    else:
        return render_template('log-in.html', form=form)


@view.route('/logInSuccess', methods=['GET'])
@login_required
def show_login_success():
    return '''Congratulations, {}! You have successfully logged in!'''.format(current_user.preferred_name)
