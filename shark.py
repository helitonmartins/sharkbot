#!/usr/bin/python
# -*- coding: utf-8 -*-
#Raimundo Chatter Bot GaragemHacker Curitiba HackerSpace
#https://github.com/python-telegram-bot/python-telegram-bot/wiki/Extensions-%E2%80%93-Your-first-Bot

import sys,os
import time
import telegram
#import ipdb
from telegram.ext import Updater,CommandHandler,MessageHandler,Filters
import logging
import random
import json

token='thegrouphash'  #freenasBRbot
bot=telegram.Bot(token)
updater = Updater(token)
dispatcher = updater.dispatcher
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',level=logging.INFO)
#logging.basicConfig(level=logging.DEBUG,format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

moderacoes=""
pingado = time.time() - 60
pingadostr = ""
fale = None
myid = thebotid

help_text = 'Meu nome eh *Shark*, eu costumo aparecer no FreeNAS BR.\n' \
            'Esse é meu manual de comandos, até agora...\n' \
            '/modera - Como você deve usar este grupo\n' \
            '/help - Lista este menu comandos'

def load_modera():
    global moderacoes
    with open("modera.txt", 'r') as file:
        linhas = file.readlines()
        for line in linhas:
            moderacao = line
            moderacoes = moderacoes + moderacao

load_modera()

def eloquencia():
	global fale
	with open("phrases.json") as perulas:
		fale = json.load(perulas)

eloquencia()

# Print help text
def helpnow(bot, update):
    """ Prints help text """

    chat_id = update.message.chat.id

    bot.sendMessage(chat_id=chat_id,
                    text=help_text,
                    parse_mode=telegram.ParseMode.MARKDOWN,
                    disable_web_page_preview=True)


def modera(bot, update):
	#ipdb.set_trace()
	global moderacoes
	global pingado
	global pingadostr
	disturbio = 60

	if (time.time() - disturbio) > pingado:
		bot.sendMessage(chat_id=update.message.chat_id, text=moderacoes, parse_mode=telegram.ParseMode.HTML) 
		pingado = time.time();pingadostr = time.strftime("%S")
	else:

		atual = int(time.strftime("%S"))
		ultimo_ping = int(pingadostr)
		if ( atual < ultimo_ping ):
			moderados = (atual + 60) - ultimo_ping
		else: 
			moderados = atual - ultimo_ping

		#testando frase escolhida pra ver se splita para concatenar depois
		escolha = random.randrange(len(fale["modera"]))
		if "|" not in fale["modera"][escolha]:
			bot.sendMessage(chat_id=update.message.chat_id, text=fale["modera"][escolha])
		else:
			#quando tem | na frase splite naquele ponto pra concatenar com str(moderados)
			partes = fale["modera"][escolha].split("|",2)
			junta = partes[0]+str(moderados)+partes[2]
			bot.sendMessage(chat_id=update.message.chat_id, text=junta)

	return
		
def echo(bot, update):
	
	global myid
	#bot.sendMessage(chat_id=update.message.chat_id, text=update.message.text)
	atualizador = update.message
	#ipdb.set_trace()
	#user = atualizador.from_user
	#print atualizador
    #ipdb.set_trace()
    #bot.sendMessage(chat_id=update.message.chat_id, reply_to_message_id=atualizador.message_id, text="respondendo")
	#print atualizador.new_chat_participant
	#print atualizador.new_chat_member
	#if message.left_chat_participant.first_name is not None:
	#	print atualizador
	
	print "Mensagem ==",\
			"[",atualizador.from_user.username,"]",\
			"[",atualizador.from_user.id,"]",\
			"--> [",atualizador.text,"]",\
			"via [",atualizador.chat.title,"]",\
			"[",atualizador.chat.type,"]",\
			"[",atualizador.chat_id,"]"

	#low_newmesg pega a mensagem que vier pro ray e converte pra lower case
	#low_newmesg = atualizador.text.decode('utf-8').lower().encode('utf-8')
	#ipdb.set_trace()
	#Procurando por shark nas mensagens ou se foi respondida a ele...
#	if any(st in atualizador.text.lower() for st in fale["greets"]):
#		resposta = random.randrange(len(fale["greetings"]))
#		bot.sendMessage(chat_id=update.message.chat_id, reply_to_message_id=resposta_mesg, text=fale["greetings"][resposta])

	if any(st in atualizador.text.lower() for st in fale["shark"]) or atualizador.reply_to_message is not None and atualizador.reply_to_message.from_user.id == myid:
		
		#Se for uma resposta seta o message id pra resposta
		if atualizador.reply_to_message is not None:
			print "Estao me respondendo alguma coisa"
			resposta_mesg = atualizador.message_id
		else:
			print "Opa estao me chamando..."
			resposta_mesg = ""

		if any(st in atualizador.text.lower() for st in fale["greets"]):
			resposta = random.randrange(len(fale["greetings"]))
			bot.sendMessage(chat_id=update.message.chat_id, reply_to_message_id=resposta_mesg, text=fale["greetings"][resposta])

		elif any(st in atualizador.text.lower() for st in fale["moderando"]):
			"""Respondendo moderacoes in-line"""
			modera(bot,update)
		
		elif any(st in atualizador.text.lower() for st in fale["perguntas"]):
			resposta = random.randrange(len(fale["perguntas"]))
			if resposta%2 == 0:
				resposta = resposta + 1
				print resposta, "Vai de respota em perguntas..."
			bot.sendMessage(chat_id=update.message.chat_id, reply_to_message_id=resposta_mesg, text=fale["perguntas"][resposta])

		else:
			print "Vou responder que nao sei..."
			resposta = random.randrange(len(fale["naosei"]))
			bot.sendMessage(chat_id=update.message.chat_id, reply_to_message_id=resposta_mesg, text=fale["naosei"][resposta])

def echo_commands(bot, update):
	"""Monitora entradas e saidas do canal, e comandos enviados ao bot"""

	atualizador = update.message
	if atualizador.left_chat_member is not None or atualizador.new_chat_member is not None:
		if atualizador.left_chat_member is not None:

			print "Saindo ==",\
					"[",atualizador.left_chat_member.username,"]",\
					"[",atualizador.left_chat_member.id,"]",\
					"--> [",atualizador.chat.title,"]",\
					"[",atualizador.chat.type,"]",\
					"[",atualizador.chat_id,"]"

		elif atualizador.new_chat_member is not None:

			print "Entrando ==",\
					"[",atualizador.new_chat_member.username,"]",\
					"[",atualizador.new_chat_member.id,"]",\
					"--> [",atualizador.chat.title,"]",\
					"[",atualizador.chat.type,"]",\
					"[",atualizador.chat_id,"]"

			newuser = atualizador.new_chat_member
			welcome = "Saudacoes "+newuser.first_name+" "+newuser.last_name+". Leia a conduta do grupo que esta pinada no topo ou consulte a minha moderacao em private com o comando modera... Enjoy! ;-)"
			bot.sendMessage(chat_id=atualizador.chat_id,text=welcome)
			#bot.sendMessage(chat_id=atualizador.chat_id, text=moderacoes, parse_mode=telegram.ParseMode.HTML) 


def main():

	#Para comandos unicos.
	#start_handler = update.dispatcher()
	#start_handler = CommandHandler('quemtala', quemtala)

	#Definindo start_handler pra ficar atualizando os comando pro dispatcher
	#start_handler = updater.dispatcher
	#Recebendo Comandos:
	start_modera = CommandHandler('modera', modera)
	start_help = CommandHandler('help', helpnow)
	start_echo = MessageHandler([Filters.text], echo)
	start_commands = MessageHandler([Filters.status_update], echo_commands)
	
	#Inciando Dispatcher 
	dispatcher.add_handler (start_modera)
	dispatcher.add_handler (start_help)
	dispatcher.add_handler (start_echo)
	dispatcher.add_handler (start_commands)


	#Iniciando Bot
	updater.start_polling()
	#logger = logging.getLogger()
	print logger.debug
	updater.idle()

if __name__ == '__main__':
	main()
