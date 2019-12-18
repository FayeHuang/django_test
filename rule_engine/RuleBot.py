import time
class RuleBot:
    def __init__(self, bot_name):
        self.bot_name = bot_name
        time.sleep(0.5)
        print('== init {} =='.format(bot_name))

