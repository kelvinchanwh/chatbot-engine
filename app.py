import logging
import uuid
from flask import Flask, render_template, request
from flask_socketio import SocketIO
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer


logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
                    datefmt='%m-%d %H:%M')

app = Flask(__name__)
app.config['SECRET_KEY'] = 'vnkdjnfjknfl1232#'
socketio = SocketIO(app)

chatbot = ChatBot('Ron Obvious')

# Create a new trainer for the chatbot
trainer = ChatterBotCorpusTrainer(chatbot)

# Train the chatbot based on the english corpus
trainer.train("chatterbot.corpus.english")


@app.route("/")
def home():
    return render_template("index.html")


@socketio.on('session_request')
def on_session_request(message):
    session_id = message.get('session_id', uuid.uuid4().hex)
    socketio.emit('session_confirm', session_id)


@socketio.on('user_uttered')
def on_user_uttered(message, methods=['GET', 'POST']):
    bot_request = {'text': message.get('message', '')}
    bot_response = {'text': str(chatbot.get_response(bot_request))}
    socketio.emit('bot_uttered', bot_response, room=request.sid)


if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=8080, use_reloader=False, debug=True)
