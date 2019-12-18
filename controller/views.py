from django.shortcuts import render
from django.http import HttpResponse
import time
# Create your views here.
from django.core.cache import cache
class Controller:
    def __init__(self):
        while not cache.get('cp_bot') and not cache.get('sen_bot') and not cache.get('chitchat_bot'):
            print('-- sleep --')
            time.sleep(0.1)
        self.cp_bot = cache.get('cp_bot')
        self.sen_bot = cache.get('sen_bot')
        self.chitchat_bot = cache.get('chitchat_bot')

c = Controller()
def index(request):
    print(c.cp_bot.bot_name)
    print(c.sen_bot.bot_name)
    print(c.chitchat_bot.bot_name)
    return HttpResponse("Hello, world. You're at the polls index.")

