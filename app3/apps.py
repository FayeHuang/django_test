from django.apps import AppConfig

from .signals import app3_init
from .App3 import App3
from django.core.cache import cache

# cache.set('my_key', 'hello, world!', 30)
# cache.get('my_key')


class App3Config(AppConfig):
    name = 'app3'

    def ready(self):
        # signals are imported, so that they are defined and can be used
        from app2.signal_handlers import app1_init_handler
        app = App3()
        app3_init.send(sender="app3", bot2=app)
