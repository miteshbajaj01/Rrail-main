from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from .models import *
from django.db import connection
from collections import namedtuple

def namedtuplefetchall(cursor):
    "Return all rows from a cursor as a namedtuple"
    desc = cursor.description
    result = namedtuple('Result', [col[0] for col in desc])
    return [result(*row) for row in cursor.fetchall()]

app_name = 'website/'

def index(request):
    print("ZZ",request)
    return render(request, app_name + 'index.html')
def train_mitesh(request):
    return render(request, app_name + 'mitesh.html')


def train_enquiry(request):
    return render(request, app_name + 'train-enquiry.html')


def train_schedule(request):
    context = {'is_submit': False}
    if request.method == "POST":
        train_no = request.POST.get('train-no')
        with connection.cursor() as cursor:
            cursor.execute(f"SELECT * FROM `website_train` WHERE `train_no`='{train_no}'")
            train_obj = namedtuplefetchall(cursor)
        if not train_obj:
            messages.error(request, 'The given Train Number does not exist.')
        else:
            context['is_submit'] = True
            train_obj = train_obj[0]
            with connection.cursor() as cursor:
                cursor.execute(f"SELECT * FROM `website_trainschedule` INNER JOIN `website_station` ON (`website_trainschedule`.`station_id` =`website_station`.`station_code`) WHERE `train_id`='{train_no}' ORDER BY distance ASC")
                schedule_obj = namedtuplefetchall(cursor)
            context['train'] = train_obj
            context['schedules'] = schedule_obj
    return render(request, app_name + 'train-schedule.html', context=context)


def train_search(request):
    context = {"is_submit": False}
    if request.method == "POST":
        source = request.POST.get("source")
        destination = request.POST.get("destination")

        with connection.cursor() as cursor:
            cursor.execute(f"SELECT T1.train_id, T1.day FROM website_trainschedule as T1, website_trainschedule as T2 WHERE T1.station_id='{source}' AND T2.station_id='{destination}' AND T1.distance < T2.distance AND T1.train_id=T2.train_id")
            search = namedtuplefetchall(cursor)

            search_without_date = []
            for s in search:
                try:
                    search_without_date += cursor.fetchone()
                except:
                    pass
        
        trains_obj = []
        traintime = []

        with connection.cursor() as cursor:
            for train_no in search:
                print(train_no)
                train_no = train_no.train_id
                cursor.execute(f"SELECT * FROM `website_train` WHERE `train_no`='{train_no}'")
                trains_obj += namedtuplefetchall(cursor)
                l = {}
                cursor.execute(f"SELECT `arrival`, `day` FROM `website_trainschedule` WHERE `train_id`='{train_no}' AND `station_id`='{source}'")
                l['source'] = cursor.fetchone()
                cursor.execute(f"SELECT `arrival`, `day` FROM `website_trainschedule` WHERE `train_id`='{train_no}' AND `station_id`='{destination}'")
                l['destination'] = cursor.fetchone()
                traintime.append(l)

        if not trains_obj:
            messages.error(request, 'No Trains Found.')
        else:
            context['t1'] = zip(trains_obj, traintime)
            context['source'] = source
            context['destination'] = destination
            context['is_submit'] = True
    return render(request, app_name + 'train-search.html', context=context)

def pnr_status(request):
    context = {"is_submit": False}
    if request.method == "POST":
        pnr = request.POST.get("pnr-no")
        print(pnr)
        context['is_submit']=True
        with connection.cursor() as cursor:
            cursor.execute(f"SELECT * FROM  website_train join website_booking WHERE pnr={pnr} and train_no_id=train_no")
            details = namedtuplefetchall(cursor)
            if len(details)>0:
                context['obj']=details[0]
    return render(request, app_name+ 'pnr-status.html', context=context)