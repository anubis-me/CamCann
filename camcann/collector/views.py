from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.template import loader
import json
from .models import *
from .forms import DataForm
from datetime import datetime, timedelta
from django.views.decorators.csrf import csrf_exempt
import subprocess,os
from channels import Group
from random import shuffle

def index(request):
    all_data = Data.objects.all()
    html = ''
    for data in all_data:
        url = '/collector/' + str(data.id) + '/'
        html += '<a href="' + url + '">' + data.camera + '</a><br>'
    return HttpResponse(html)

last_played_time = datetime.now()
p = None


@csrf_exempt
def data_create_view(request):
    global p
    rp = json.loads(request.body.decode("utf-8"))
    d = Data.objects.create(Age=rp['Age'],Gender=rp['Gender'],Frame_Shape='',Image=rp['img64'])
    d.save()
    print(rp['Age'],rp['Gender'])
    m = Ads.objects.filter(target_gender=rp['Gender']).order_by("?")
    print(m)
    for i in m:
        if i.target_age_start <= rp['Age'] and i.target_age_end >= rp['Age']:
            a = AdTarget.objects.create(ad=i,person=d)
            a.save()
            q = Queue.objects.create(ad=i)
            q.save()

    return HttpResponse("Created")


def detail(request, data_id):
    return HttpResponse("<h2> Details for the id: " + str(data_id) + "</h2>")


def index_graphs(request):
    ts = datetime.now() - timedelta(hours=17)
    td = datetime.now() - timedelta(hours=24)
    total_visits = Data.objects.count()
    visits_today = len(Data.objects.filter(Timestamp__gte=td))
    unique_targets = AdTarget.objects.count()
    ds = Data.objects.filter(Timestamp__gte=ts)
    time_age = dict()
    time_gender = dict()
    time_gender["Male"] = dict()
    time_gender["Female"] = dict()
    for i in ds:
        hour = i.Timestamp.day * 24 + (i.Timestamp.hour + 5) % 24
        if hour in time_age.keys():
            time_age[hour].append(i.Age)
        else:
            time_age[hour] = list()
            time_age[hour].append(i.Age)
        if hour in time_gender[i.Gender].keys():
            time_gender[i.Gender][hour].append(i.Age)
        else:
            time_gender[i.Gender][hour] = list()
            time_gender[i.Gender][hour].append(i.Age)
    time_range = [str((i%24)) + ":00" for i in sorted(time_age.keys())]
    age_count = []
    male_count = []
    female_count = []
    print(time_gender)
    for i in sorted(time_age.keys()):
        age_count.append(sum(time_age[i]) / len(time_age[i]))
        if i not in time_gender["Male"].keys():
            male_count.append(0)
        else:
            male_count.append(len(time_gender["Male"][i]))
        if i not in time_gender["Female"].keys():
            female_count.append(0)
        else:
            female_count.append(len(time_gender["Female"][i]))
    resp = {"time_range": time_range, "male_count": male_count, "female_count": female_count,"age_count":age_count ,"total_visits":total_visits, "visits_today":visits_today,"unique_targets":unique_targets}
    return JsonResponse(resp)

def tag_data(request):
    th = TagHistory.objects.all()
    time_series = []
    time_tags = dict()
    tag_names = []
    for i in th:
        hour = i.timestamp.day * 24 + (i.timestamp.hour + 5) % 24
        if i.tag.name not in tag_names:
            tag_names.append(i.tag.name)
        if hour not in time_series:
            time_series.append(hour)
        if i.tag.name not in time_tags.keys():
            time_tags[i.tag.name] = dict()
        if hour not in time_tags[i.tag.name].keys():
            time_tags[i.tag.name][hour] = 0
        time_tags[i.tag.name][hour] += 1

    time_range = [str((i % 24)) + ":00" for i in sorted(time_series)]
    time_data = dict()
    for j in tag_names:
        time_data[j] = []
        for i in sorted(time_series):
            if i not in time_tags[j].keys():
                time_data[j].append(0)
            else:
                time_data[j].append(time_tags[j][i])
    resp = {"time_range":time_range,"time_data":time_data}
    return JsonResponse(resp)

def colors(request):
    ch = Tag.objects.all()
    ch_resp = []
    for color in ch:
        resp = {"tag_id":color.tag_id , "image": color.image}
        ch_resp.append(resp)
    resp = {"colors":ch_resp}
    return JsonResponse(resp)

def target_api(request):
    ts = datetime.now() - timedelta(hours=8)
    hist = AdTarget.objects.all()
    resp = dict()
    for i in hist:
        product = i.ad.campaign_name
        if product not in resp.keys():
            resp[product] = []
        image = i.person.Image
        count = i.count
        resp[product].append({"image":image,"count":count})
    return JsonResponse(resp)