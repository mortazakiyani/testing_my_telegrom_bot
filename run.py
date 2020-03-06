from uuid import uuid4
from telegram.ext import Updater
from telegram.ext import CommandHandler
from telegram.ext import CallbackQueryHandler
from telegram.ext import InlineQueryHandler

from telegram.chataction import ChatAction

from telegram import ReplyKeyboardMarkup
from telegram import InlineKeyboardButton
from telegram import InlineKeyboardMarkup
from telegram import InputTextMessageContent
from telegram import InlineQueryResultArticle

updater = Updater('972612062:AAGqgytN8LTYrCmDT1cUnhGoblSNCOkECgM')


def start(bot, update):
    #import pdb;pdb.set_trace()
    chat_id = update.message.chat_id
    first_name = update.message.chat.username
    first2_name = update.message.chat.first_name
    bot.send_chat_action(chat_id, ChatAction.TYPING)
    bot.sendMessage(chat_id, 'salam {} {}'.format(first_name, first2_name))


def service_keyboard(bot,update):
    chat_id = update.message.chat_id
    keyboard =[['part 1','part 4' , 'part3'],['part2']]
    bot.sendMessage(chat_id,'wich part do you want?',reply_markup= ReplyKeyboardMarkup(keyboard,resize_keyboard=True))


def favor_keyboard(bot,update):
    chat_id =update.message.chat_id
    keyboard =[
                [
                 InlineKeyboardButton('google', callback_data='1'),
                 InlineKeyboardButton('bing', callback_data='2')
                ]
               ]
    bot.sendMessage(chat_id, 'best searchEngine?',reply_markup=InlineKeyboardMarkup(keyboard))


def favor_handler_button(bot, update):
    query = update.callback_query
    data = query.data
    chat_id = query.message.chat_id
    message_id =query.message.message_id
    description = " choose best search engine between options{}", format(data)

    if data == '1':
        description = "you choose google for better search engine "
    else:
        description = "you choose bing for better search engine "
    bot.editMessageText(text=description,chat_id=chat_id,message_id=message_id)


def feature_inline_query(bot, update):
    query = update. inline_query.query

    result = list()

    result.append(InlineQueryResultArticle(id=uuid4(), title="UPERCASE"),input_message_content=InputTextMessageContent(query.upper()))
    result.append(InlineQueryResultArticle(id=uuid4(), title="lowercase"),input_message_content=InputTextMessageContent(query.lower()))

    bot.answerInlineQuery(result=result)


start_command = CommandHandler('start', start)
service_command= CommandHandler('service', service_keyboard)
favor_command= CommandHandler('favor', favor_keyboard)
favor_handler = CallbackQueryHandler(favor_handler_button)
feature_inlineQuery = InlineQueryHandler(feature_inline_query)

updater.dispatcher.add_handler(start_command)
updater.dispatcher.add_handler(service_command)
updater.dispatcher.add_handler(favor_command)
updater.dispatcher.add_handler(favor_handler)
updater.dispatcher.add_handler(feature_inlineQuery)

updater.start_polling()
updater.idle()
