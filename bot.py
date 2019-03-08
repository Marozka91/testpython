# -*- coding utf-8 -*-
import telebot
from telebot import types
import requests
import time

token = ""
bot = telebot.Telebot(token)
markup = types.ReplyKeyboardMarkup()
markup.row('karding', 'camoexenie')