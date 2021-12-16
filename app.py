from flask import Flask
from views import translate_func, index

app = Flask(__name__)

# index route
app.add_url_rule('/', view_func=index)

app.add_url_rule('/translate/<target_lang>/<from_lang>/<provider>/', 'translate', translate_func, methods=['GET', 'POST'])
app.add_url_rule('/translate/<target_lang>/<from_lang>/', 'translate', translate_func, methods=['GET', 'POST'], defaults={'provider': 'google'})
app.add_url_rule('/translate/<target_lang>/', 'translate', translate_func, methods=['GET', 'POST'], defaults={'from_lang': 'auto', 'provider': 'google'})


if __name__ == '__main__':
    app.run()
