from django.apps import AppConfig
from django.core.cache import cache
from .RuleBot import RuleBot
import sys


class RuleEngineConfig(AppConfig):
    name = 'rule_engine'

    def ready(self):
        if sys.argv.count('migrate') == 0  and sys.argv.count('makemigrations') == 0:
            cp_bot = RuleBot('cp_rule')
            sen_bot = RuleBot('sen_rule')
            chitchat_bot = RuleBot('chitchat_rule')
            cache.set('cp_bot', cp_bot)
            cache.set('sen_bot', sen_bot)
            cache.set('chitchat_bot', chitchat_bot)