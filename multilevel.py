
#program showing use of multilevel inheritance
class Website:
    def __first(self):
        print('freetimelearning.com')

class Web2(Website):
    def __sec(self):
        print('Busybee.com')

class Web3(Web2):
    def final(self):
        print('hobby.com')

a=Web3()
a.__first()
a.__sec()
a.final()
