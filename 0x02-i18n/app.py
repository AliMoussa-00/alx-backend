#!/usr/bin/env python3
'''Display the current time'''


from datetime import datetime
from typing import Dict, Optional
from flask import Flask, g, render_template, request
from flask_babel import Babel, format_datetime
import pytz


class Config:
    '''class configuration for babel'''
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_locale() -> str:
    '''get the best match language'''

    if 'locale' in request.args and request.args['locale'] in Config.LANGUAGES:
        return request.args['locale']

    if g.user and g.user.get('locale', None) and \
            g.user['locale'] in Config.LANGUAGES:
        return g.user['locale']

    if request.headers.get('Accept-Language', None) and \
            request.headers.get('Accept-Language') in Config.LANGUAGES:
        return request.headers.get('Accept-Language')

    return request.accept_languages.best_match(Config.LANGUAGES)


def get_timezone() -> str:
    '''get the timezone'''

    if 'timezone' in request.args:
        try:
            tz = request.args['timezone']
            pytz.timezone(tz)
            return tz
        except pytz.exceptions.UnknownTimeZoneError:
            pass

    if g.user and g.user.get('timezone', None):
        try:

            tz = g.user.get('timezone')
            pytz.timezone(tz)
            return tz
        except pytz.exceptions.UnknownTimeZoneError:
            pass

    return Config.BABEL_DEFAULT_TIMEZONE


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)
babel.init_app(app, locale_selector=get_locale, timezone_selector=get_timezone)


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
def before_request():
    '''store the user in flask.g'''
    g.user = get_user()


@app.route('/')
def hello_world():
    '''rendering hello world page'''
    return render_template(
        'index.html',
        user=g.user,
        timestamp=format_datetime()
    )


if __name__ == '__main__':
    app.run()
