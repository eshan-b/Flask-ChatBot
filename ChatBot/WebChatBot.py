''' Notes: 
Chatterbot modules only work in Python 3.5 - 3.7
Chatterbot only works with spaCY v2
'''

from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

from flask import Flask, render_template, request

app = Flask(__name__)

english_bot = ChatBot(
    "Gideon", storage_adapter="chatterbot.storage.SQLStorageAdapter")
trainer = ChatterBotCorpusTrainer(english_bot)
trainer.train("chatterbot.corpus.english")


@app.route('/')
def home():
    return render_template("index.html")


@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    return str(english_bot.get_response(userText))


if __name__ == '__main__':
    app.run()
