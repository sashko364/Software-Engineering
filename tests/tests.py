from unittest import TestCase
from ..src.temperatures import mintemp, mediumtemp, maxtemp  # explicit relative import

import requests

data = requests.post('https://tues2022.proxy.beeceptor.com/my/api/test')
temperatures = []

for i in data.json()['data']:
    temp = i['temperature']
    temperatures.append(temp)
    
temperatures.sort()

class TestClass(TestCase):
    def Test_one(self):
        assert(mintemp(), temperatures[0])

    def Test_two(self):
        assert(mediumtemp(), temperatures[2])

    def Test_three(self):
        assert(maxtemp(), temperatures[4])