#!/usr/bin/env python3
'''Get locale from request'''


from flask import Flask, render_template, request
from flask_babel import Babel


class Config:
    '''class configuration for babel'''
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


@babel.localeselector
def get_locale() -> str:
    '''get the best match language'''
    return request.accept_languages.best_match(Config.LANGUAGES)


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@app.route('/')
def hello_world() -> str:
    '''rendering hello world page'''
    return render_template('2-index.html')


if __name__ == '__main__':
    app.run()
