# -*- coding: utf-8 -*-
# =============================================================================
# Created By  : @thegoldencheesecake
# Created Date: Thursday February 18 20:17:00 GST 2022
# =============================================================================

# =============================================================================
# Packages
# pip install chatterbot chatterbot-corpus colorama termcolor art
# =============================================================================

"""Initializing the Chatbot using the chatterbot library"""

from chatterbot import ChatBot

name = 'bot'
bot = ChatBot(
    name,
    storage_adapter="chatterbot.storage.SQLStorageAdapter",
    logic_adapter=[
        "chatterbot.logic.MathematicalEvaluation",
        "chatterbot.logic.TimeLogicAdapter",
        "chatterbot.logic.BestMatch",
        {
            "import-path": "chatterbot.logic.BestMatch",
            "default_response": "I am sorry, I don't understand you.",
            "maximum_similarity_threshold": 0.50
        }
    ],
    database_uri = "sqlite:///database.sqlite3"
)

"""Making the trainers and training the bot using ready made data"""

from chatterbot.trainers import ListTrainer, ChatterBotCorpusTrainer, UbuntuCorpusTrainer

trainer = ListTrainer(bot)
trainerCorpus = ChatterBotCorpusTrainer(bot)
trainerUbuntuCorpus = UbuntuCorpusTrainer(bot)

trainerCorpus.train("chatterbot.corpus.english")

"""The Main Program"""

from colorama import init, Fore, Style
import art
import os

init()

print(art.text2art("Bot", "starwars")) 

uname = input("What is your name? ")
bname = input("What would you like to name the bot? ")
print("")

while True:
    if os.system('color') == 1:
      query = input(f"{Fore.WHITE}{uname}>{Style.RESET_ALL} ")
    else:
      query = input(f"{uname}> ")

    if query == "exit":
        print("Exiting...")
        break

    answer = bot.get_response(query)
    if os.system('color') == 1:
      print(f"{Fore.YELLOW}{bname}>{Style.RESET_ALL}", answer)
    else:
      print(f"{bname}>", answer)
