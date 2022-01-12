from main import mintemp, mediumtemp, maxtemp

import requests

data = requests.post('https://tues2022.proxy.beeceptor.com/my/api/test')
temperatures = []

for i in data.json()['data']:
    temp = i['temperature']
    temperatures.append(temp)
    
temperatures.sort()

def checkMin():
    assert mintemp() == temperatures[0]

def checkMed():
    assert mediumtemp() == temperatures[2]

def checkMax():
    assert maxtemp() == temperatures[4]