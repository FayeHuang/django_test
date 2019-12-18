import time

class App1:
    def __init__(self):
        self.name = 'app1'
        print ('==== begin init {} ==='.format(self.name))
        time.sleep(1)
        print('=== [OK] init {} ==='.format(self.name))