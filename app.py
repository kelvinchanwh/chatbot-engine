import os
import logging
import uuid
from flask import Flask, render_template, request
from flask_socketio import SocketIO
from utils.bot_factory import BotFactory

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
                    datefmt='%m-%d %H:%M')

app = Flask(__name__)
socketio = SocketIO(app)

# Side effect: pre load the default lang
BotFactory.getInstance('en')


@app.route("/")
def home():
    return render_template("index.html")


@socketio.on('session_request')
def on_session_request(message):
    session_id = message.get('session_id', uuid.uuid4().hex)
    socketio.emit('session_confirm', session_id)


@socketio.on('user_uttered')
def on_user_uttered(message, methods=['GET', 'POST']):
    custom_data = message.get('customData', {})
    lang = custom_data.get('lang', 'en')
    bot_request = {'text': message.get('message', '')}
    bot_response = {'text': str(BotFactory.getInstance(lang).get_response(bot_request))}
    socketio.emit('bot_uttered', bot_response, room=request.sid)


if __name__ == '__main__':
    host = os.getenv('HOST', '0.0.0.0')
    port = os.getenv('PORT', 5000)
    socketio.run(app, host=host, port=port, use_reloader=False, debug=True)
