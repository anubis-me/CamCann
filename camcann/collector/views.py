from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Data
from .forms import DataForm


def index(request):
    all_data = Data.objects.all()
    html = ''
    for data in all_data:
        url = '/collector/' + str(data.id) + '/'
        html += '<a href="' + url + '">' + data.camera + '</a><br>'
    return HttpResponse(html)


def data_create_view(request):
    form = DataForm(request.POST or None)
    if form.is_valid():
        form.save()
    context = {
        'form': form
    }
    return render(request, "collector/data_create.html",context)


def detail(request, data_id):
    return HttpResponse("<h2> Details for the id: " + str(data_id) + "</h2>")
