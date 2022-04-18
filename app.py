import flask
from flask import request, jsonify

from chat_bot import *

app = flask.Flask(__name__)
app.config["DEBUG"] = False


@app.route('/api', methods=['GET', 'POST'])
def api():
    content_type = request.get_json()
    text = content_type['text']
    bot_answer = bot.run(text)
    print(bot_answer)
    result = {'text': bot_answer[0]['text']}
    return jsonify(result)


@app.route('/', methods=['GET', 'POST'])
def home():
    return "API CUA TUI NE"
