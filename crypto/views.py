from django.shortcuts import render

def home(request):
    import requests
    import json


    #crypto ceny
    api_request = requests.get("https://min-api.cryptocompare.com/data/pricemultifull?fsyms=BTC&tsyms=USD,EUR")
    api = json.loads(api_request.content)







    # crypto newsy
    api_request = requests.get("https://min-api.cryptocompare.com/data/v2/news/?lang=EN")
    api = json.loads(api_request.content)
    return render(request, 'home.html', {'api': api})
# trzeba dac pip install requests, pip freeze, pip install json

# Create your views here.
