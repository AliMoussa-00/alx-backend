#!/usr/bin/env python3
'''Force locale with URL parameter'''


from flask import Flask, render_template, request
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


@app.route('/')
def hello_world() -> str:
    '''rendering hello world page'''
    return render_template('4-index.html')


if __name__ == '__main__':
    app.run()
