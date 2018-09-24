import requests

class Employee:
    """" A sample employee class """
    raise_amount = 1.05

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay

    @property
    def email(self):
        return '{}{}@gmail.com'.format(self.first, self.last)

    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    def monthly_schedule(self, month):
        response = requests.get('http://somehting.com/{}/{}'.format(self.last, month))
        if response.ok:
            return response.text
        else:
            return 'Bad Response!'