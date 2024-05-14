#!/usr/bin/env python3
'''Mock logging in'''


from typing import Dict, Optional
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


@babel.localeselector
def get_locale() -> str:
    '''get the best match language'''

    if 'locale' in request.args and \
            request.args['locale'] in app.config["LANGUAGES"]:
        return request.args['locale']
    return request.accept_languages.best_match(app.config["LANGUAGES"])
    # return 'fr'


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user() -> Optional[Dict[str, Optional[str]]]:
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
    return render_template('5-index.html', user=g.user)


if __name__ == '__main__':
    app.run()
