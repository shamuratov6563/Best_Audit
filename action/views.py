from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
import requests
from bs4 import BeautifulSoup
from django.urls import reverse_lazy
from action.models import Message, Videos, Rate
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
import telebot
from termcolor import colored
token = '2142956792:AAHsITOmzE4iDafHHjZdyQxmd6Mb30SodA4'
bot = telebot.TeleBot(token)
chat_id = '5139402876'


def home():
    DOLLAR_RUB = 'https://nbu.uz/uz/exchange-rates/'
    headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36'}
    full_page = requests.get(DOLLAR_RUB, headers)
    soup = BeautifulSoup(full_page.content, 'html.parser')
    a = soup.findAll('a', {'href': '/uz/exchange-rates/', }, 'span')
    r = soup.findAll('td')
    r = str(r)
    r = r[574:580]
    e = a[4].text
    a = a[1].text
    a = a[6:]
    e = e[6:]
    c = [a, e, r]
    return c


def message(request):
    rate = Rate.objects.all()
    a = home()

    if request.method == 'POST':
        UserName = request.POST.get('name')
        UserNumber = request.POST.get('number')
        SaveValue = Message()
        SaveValue.name = UserName
        SaveValue.phone_number = UserNumber
        print(UserName, UserNumber)
        SaveValue.save()
        sms = f"Username:  {UserName}\n\nUserNUmber:  {UserNumber}"
        try:
            bot.send_message(chat_id, sms)
        except:
            HttpResponse('Try again')
    context = {
        'a': a[0],
        'e': a[1],
        'r': a[2],
        'rates': rate,
    }

    return render(request, 'index.html', context)


class RateUpdateView(UpdateView):
    model = Rate
    template_name = 'rate/rate_edit.html'
    fields = ['title', 'first', 'second', 'third', 'prize']
    success_url = reverse_lazy('home')



