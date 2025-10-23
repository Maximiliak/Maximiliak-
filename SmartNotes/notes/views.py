from django.shortcuts import render,redirect
from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.urls import reverse

def index(request, notes_id):
    if notes_id > 3:
        uri = reverse('notes',args=(1, ))
        return redirect(uri)
    return HttpResponse(f'<h1>Страница приложения</h1><p>id: {notes_id}</p>')

def page_not_found(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')
