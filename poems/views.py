import random
from cgitb import text

from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.

from poems.models import Poem


def read(request):
    # получаем все закончиенные тексты
    if "id" in request.GET:
        poem = Poem.objects.get(pk=request.GET['id'])
    else:
        poems = Poem.objects.filter(ended=True)
        poem = random.choice(poems)
    return render(request, 'rot.html', {'poem': poem})



def write(request):
    if request.method == 'GET':
        # TODO: стоит добавить возможность добавить возможность написать с нуля, даже если тексты уже есть
        poems = Poem.objects.filter(ended=False)
        if poems.count() == 0:
            # создаем новый текст
            poem = Poem()
            poem.text = ""
            poem.save()
        else:
            # выбираем один из текущих
            poem = random.choice(poems)
        # TODO: сделать шаблон для написания абзаца
        return render(request, 'write.html', {'poem': poem})
    if request.method == 'POST':
        ui = request.POST['id']
        # находим нашу поэму с конкретным id...
        poem = Poem.objects.get(pk=ui)

        if request.POST['button'] == 'Добавить абзац':
            poem.text = poem.text + request.POST['text1']
            poem.save()
            return redirect('/')
        if request.POST['button'] == 'Закончить текст':
            poem.text = poem.text + request.POST['text1']
            poem.ended = True
            poem.save()
            return redirect('/rot?id={}'.format(poem.id))
        if request.POST['button'] == 'Создать новый текст':
            return redirect('/write')