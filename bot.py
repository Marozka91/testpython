
import telebot
from telebot import types
import requests
import time

token = "751215261:AAEh5UXaN9kQp_M2aoaiHVCfeyoUKxlICqE"
bot = telebot.Telebot(token)
markup = types.ReplyKeyboardMarkup()
markup.row('karding', 'camoexenie')