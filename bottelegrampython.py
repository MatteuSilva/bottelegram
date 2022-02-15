import logging
import telebot

from zabbix_api import ZabbixAPI
zapi = ZabbixAPI(server='http://170.0.61.162/zabbix')
zapi.login("Admin", "zabbix")

bot = telebot.TeleBot("5226426683:AAG8ZzGquH1SgDg9vMs7NZwf_UX_03e4CEM")

# logging.basicConfig(
#     format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
# )
# logger = logging.getLogger(__name__)

@bot.message_handler(commands=['start','retornar'])
def start(mensagem):
        bot.reply_to(mensagem, 'Olá, por favor selecione umas das opções:')
        bot.send_message(mensagem.chat.id, "/hosts")
        bot.send_message(mensagem.chat.id, "/templates")
        bot.send_message(mensagem.chat.id, "/grupodehosts")
        bot.send_message(mensagem.chat.id, "/finalizar_bot")


@bot.message_handler(commands=['hosts'])
def hosts(mensagem):
    var_hosts = zapi.host.get({
        "output":[
            "hostid",
            "host"
        ], 
        "sortfield":"hostid"
    })
    for x in var_hosts:
        msg = "ID "+x['hostid']+" - "+"/"+x['host']
        bot.send_message(mensagem.chat.id, msg)
    bot.send_message(mensagem.chat.id, "/retornar")
    bot.send_message(mensagem.chat.id, "/finalizar_bot")

@bot.message_handler(commands=['grupodehosts'])
def grupodehosts(mensagem):
    var_grupo_hosts = zapi.hostgroup.get({
        "output":[
            "groupid",
            "name"
        ], 
        "sortfield":"groupid"
    })
    for x in var_grupo_hosts:
        msg = "ID "+x['groupid']+" - "+"/"+x['name']
        bot.send_message(mensagem.chat.id, msg)
    bot.send_message(mensagem.chat.id, "/retornar")
    bot.send_message(mensagem.chat.id, "/finalizar_bot")

@bot.message_handler(commands=['Servicos'])
def servicos(mensagem):
    var_hosts_servicos = zapi.host.get({
        "output":[
            "hostid",
            "host"
        ],
        "groupids":"18"   
    })
    for x in var_hosts_servicos:
        msg = "ID "+x['hostid']+" - "+"/"+x['host']
        bot.send_message(mensagem.chat.id, msg)
    bot.send_message(mensagem.chat.id, "/retornar")
    bot.send_message(mensagem.chat.id, "/finalizar_bot")

@bot.message_handler(commands=['Backbone'])
def backbone(mensagem):
    var_hosts_backbone = zapi.host.get({
        "output":[
            "hostid",
            "host"
        ],
        "groupids":"19"   
    })
    for x in var_hosts_backbone:
        msg = "ID "+x['hostid']+" - "+"/"+x['host']
        bot.send_message(mensagem.chat.id, msg)
    bot.send_message(mensagem.chat.id, "/retornar")
    bot.send_message(mensagem.chat.id, "/finalizar_bot")

@bot.message_handler(commands=['SW_SURUBIM'])
def backbone(mensagem):
    var_hosts_swsurubim = zapi.host.get({
        "filter":{
            "host":[
                "SW_SURUBIM"
            ]
        }   
    })
    for x in var_hosts_swsurubim:
        msg = "ID "+x['hostid']+" - "+"/"+x['host']
        bot.send_message(mensagem.chat.id, msg)
    bot.send_message(mensagem.chat.id, "/retornar")
    bot.send_message(mensagem.chat.id, "/finalizar_bot")


@bot.message_handler(commands=['finalizar_bot'])
def finalizar(mensagem):
    bot.send_message(mensagem.chat.id, "Ok, para reinicar o bot basta clicar em /start")

bot.infinity_polling()