# -*- coding: utf-8 -*-

from chatterbot.trainers import ListTrainer  # trainer
from chatterbot import ChatBot  # chatbot
import os

bot = ChatBot('Test', read_only=True)
bot.set_trainer(ListTrainer)

for arquivo in os.listdir('arquivo'):
    chats = open('arquivo/'+ arquivo, 'r').readlines()
    bot.train(chats)

while True:
    pergunta = input('Você: ')

    resposta = bot.get_response(pergunta)
    print('Bot: ',resposta)
