# -*- coding: utf-8 -*-

from chatterbot.trainers import ListTrainer  # trainer
from chatterbot import ChatBot  # chatbot
import os

rafael = ChatBot('Test', read_only=True)
rafael.set_trainer(ListTrainer)

for arquivo in os.listdir('arquivo'):
    chats = open('arquivo/'+ arquivo, 'r').readlines()
    rafael.train(chats)

while True:
    pergunta = input('Você: ')

    resposta = rafael.get_response(pergunta)
    print('Bot: ',resposta)