from django.shortcuts import render, redirect
from .models import Event, Activity, Subscriber
from django.contrib import messages

def index(request):
    events = Event.objects.all()
    activities = Activity.objects.all()
    context = {
        'events_list': events,
        'activities_list': activities,
    }
    return render(request, 'index.html', context)

def subscribe(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        subscriber = Subscriber.objects.filter(email=email).first()
        if subscriber:
            messages.error(request, 'Вы уже подписаны на рассылку')
            return redirect('index')
        else:
            Subscriber.objects.create(email=email)
            messages.success(request, 'Вы успешно подписались на рассылку')
        return redirect('index')
    messages.error(request, 'Неверный метод запроса')
    return redirect('index')
