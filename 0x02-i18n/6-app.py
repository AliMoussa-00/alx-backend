#!/usr/bin/env python3
'''Use user locale'''


from typing import Dict, Union
from flask import Flask, g, render_template, request
from flask_babel import Babel


class Config:
    '''class configuration for babel'''
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


@babel.localeselector
def get_locale() -> str:
    '''get the best match language'''

    if 'locale' in request.args and \
            request.args['locale'] in app.config["LANGUAGES"]:
        return request.args['locale']

    if g.user and g.user.get('locale', None) and \
            g.user['locale'] in app.config["LANGUAGES"]:
        return g.user['locale']

    if request.headers.get('Accept-Language', None) and \
            request.headers.get('Accept-Language') in app.config["LANGUAGES"]:
        return request.headers.get('Accept-Language')

    return request.accept_languages.best_match(app.config["LANGUAGES"])


def get_user() -> Union[Dict, None]:
    '''get the user according to id'''

    if 'login_as' in request.args:
        try:
            id = int(request.args['login_as'])
            return users.get(id, None)
        except ValueError:
            pass
    return None


@app.before_request
def before_request() -> None:
    '''store the user in flask.g'''
    g.user = get_user()


@app.route('/')
def hello_world() -> str:
    '''rendering hello world page'''
    return render_template('6-index.html', user=g.user)


if __name__ == '__main__':
    app.run()
