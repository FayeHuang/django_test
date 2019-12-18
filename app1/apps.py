from django.apps import AppConfig

from .signals import app1_init
from .App1 import App1

class App1Config(AppConfig):
    name = 'app1'

    def ready(self):
        # signals are imported, so that they are defined and can be used
        # signal refs : https://segmentfault.com/a/1190000008455657
        # signal refs : http://www.liujiangblog.com/course/django/170
        from app2.signal_handlers import app1_init_handler
        app = App1()
        app1_init.send(sender="app1", bot1=app)
