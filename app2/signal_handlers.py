from django.dispatch import receiver
from app1.signals import app1_init
from app3.signals import app3_init
import time
 
 
# @receiver(app1_init, dispatch_uid="app1_init_receiver")
@receiver([app1_init, app3_init])
def app1_init_handler(sender, **kwargs):
    bot1 = None
    bot2 = None
    while not bot1 and not bot2:
        time.sleep(0.1)
        print(kwargs.keys())
        if 'bot1' in kwargs.keys() and not bot1:
            bot1 = kwargs['bot1']
            
        if 'bot2' in kwargs.keys() and not bot2:
            bot2 = kwargs['bot2']
    time.sleep(0.1)
    if bot1 and bot2:
        print('==> [{}] app1_init received =='.format(bot1.name))
        print('==> [{}] app3_init received =='.format(bot2.name))

    # bot1 = kwargs['bot1']
    # bot2 = kwargs['bot2']
    # print('== [{}] app1_init received =='.format(bot1.name))
    # print('== [{}] app3_init received =='.format(bot2.name))