import time

class App3:
    def __init__(self):
        self.name = 'app3'
        print ('==== begin init {} ==='.format(self.name))
        time.sleep(1)
        print('=== [OK] init {} ==='.format(self.name))