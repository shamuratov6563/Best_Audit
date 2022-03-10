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
    response = requests.get('https://v6.exchangerate-api.com/v6/d88fe1b17f05efb286a522b5/pair/USD/UZS')
    response_e = requests.get('https://v6.exchangerate-api.com/v6/d88fe1b17f05efb286a522b5/pair/EUR/UZS')
    response_r = requests.get('https://v6.exchangerate-api.com/v6/d88fe1b17f05efb286a522b5/pair/RUB/UZS')
    a = round(response.json()['conversion_rate'], 2)
    e = round(response_e.json()['conversion_rate'], 2)
    r = round(response_r.json()['conversion_rate'], 2)
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


def upload_video(request):
    if request.method == 'POST':
        title = request.POST['title']
        video = request.POST['video']

        content = Videos(title=title, video=video)
        content.save()
        return redirect('home')

    return render(request, 'upload.html')


class RateUpdateView(UpdateView):
    model = Rate
    template_name = 'rate/rate_edit.html'
    fields = ['title', 'first', 'second', 'third', 'prize']
    success_url = reverse_lazy('home')



