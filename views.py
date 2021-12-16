from flask import request
import translators as ts


def index():
    return "<center><h1>flask translator</h1></center>"


def translate_func(target_lang, from_lang, provider):
    if request.method == 'GET':
        text = request.args['text']
        translate_text = getattr(ts, provider)(text, to_language=target_lang, from_language=from_lang)
        return f"{translate_text}"
    else:
        pass