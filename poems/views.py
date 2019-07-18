import random
from cgitb import text

from django.shortcuts import render, redirect

# Create your views here.

from poems.models import Poem


def read(request):
    # получаем все закончиенные тексты
    if "id" in request.GET:
        poem = Poem.objects.get(pk=request.GET['id'])
        return render(request, 'FinalText.html', {'poem': poem})
    else:
        poems = Poem.objects.filter(ended=True)
        return render(request, 'rot.html', {'poems': poems})



def write(request):
    if request.method == 'GET':
        # TODO: стоит добавить возможность добавить возможность написать с нуля, даже если тексты уже есть
        poems = Poem.objects.filter(ended=False)
        if poems.count() == 0 or "new" in request.GET:
            # создаем новый текст
            poem = Poem()
            poem.text = ""
            poem.save()
        else:
            poem = random.choice(poems)
        return render(request, 'write.html', {'poem': poem})
    if request.method == 'POST':
        ui = request.POST['id']
        poem = Poem.objects.get(pk=ui)
        if request.POST['button'] == 'Добавить абзац':
            if "name" in request.POST:
                poem.name = request.POST['name']
            poem.text = poem.text + request.POST['text1'] + '\n'
            poem.save()
            return redirect('/')
        if request.POST['button'] == 'Закончить текст':
            if "name" in request.POST:
                poem.name = request.POST['name']
            poem.text = poem.text + request.POST['text1'] + '\n'
            poem.ended = True
            poem.save()
            return redirect('/rot?id={}'.format(poem.id))
        return redirect('/')
