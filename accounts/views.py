from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib import messages
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
import datetime
from .models import *
from django.db import connection
from collections import namedtuple

def namedtuplefetchall(cursor):
    "Return all rows from a cursor as a namedtuple"
    desc = cursor.description
    result = namedtuple('Result', [col[0] for col in desc])
    return [result(*row) for row in cursor.fetchall()]

app_name = 'accounts/'

def login(request):
    if request.user.is_authenticated:
        return redirect('profile')
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('index')
        else:
            messages.error(request, "Invalid Credentials")
    return render(request, app_name + 'login.html')

def logout(request):
    auth.logout(request)
    messages.success(request, "You have been successfully logged out.")
    return redirect('login')

def register(request):
    if request.user.is_authenticated:
        return redirect('profile')
    context = {'username': '', 'email': '', 'first_name': '', 'last_name': '', 'gender': 'M', 'date_of_birth': '', 'phone_number': '', 'address': ''}
    if request.method == "POST":
        username = request.POST.get('username')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        email = request.POST.get('email')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        gender = request.POST.get('gender')
        date_of_birth = request.POST.get('date_of_birth')
        phone_number = request.POST.get('phone_number')
        address = request.POST.get('address')
        context['username'] = username
        context['email'] = email
        context['first_name'] = first_name
        context['last_name'] = last_name
        context['gender'] = gender
        context['date_of_birth'] = date_of_birth
        context['phone_number'] = phone_number
        context['address'] = address

        if password1 == password2:
            if not username.isalnum():
                messages.error(request, 'Username must not be blank and must contain only letters and numbers')
            elif len(password1) < 6:
                messages.error(request, 'Password length must be atleast 6')
            elif User.objects.filter(username=username.lower()):
                messages.error(request, f'The username {username} is already taken')
            elif User.objects.filter(email=email.lower()):
                messages.error(request, f'The email {email} is already taken')
            elif first_name == "":
                messages.error(request, 'First name must not be blank')
            else:
                user = User.objects.create_user(username=username.lower(), password=password1, email=email.lower(), first_name=first_name, last_name=last_name)
                with connection.cursor() as cursor:
                    cursor.execute(f"INSERT INTO `accounts_profile` (`user_id`, `gender`, `phone_number`, `date_of_birth`, `address`) VALUES ('{user.id}', '{gender}', '{phone_number}', '{date_of_birth}', '{address}')")
                messages.success(request, 'Registration successful! Please log in.')
                return redirect('login')
        else:
            messages.error(request, 'Passwords do not match')
        return render(request, app_name + 'register.html', context=context)
    return render(request, app_name + 'register.html', context=context)

def profile(request):
    context = {}
    if request.method == "POST":
        old_password = request.POST['oldpassword']
        new_password1 = request.POST['newpassword1']
        new_password2 = request.POST['newpassword2']
        user = auth.authenticate(request, username=request.user.username, password=old_password)
        if user is not None:
            if new_password1 != new_password2:
                messages.error(request, "Confirmation Password did not match")
            else:
                user.set_password(new_password1)
                user.save()
                messages.success(request, "Password successfully changed")
        else:
            messages.error(request, "Old Password entered is incorrect")
    with connection.cursor() as cursor:
        cursor.execute(f"SELECT * FROM `accounts_profile` INNER JOIN `auth_user` ON (`accounts_profile`.`user_id` = `auth_user`.`id`) WHERE `auth_user`.`id` = '{request.user.id}'")
        profile_obj = namedtuplefetchall(cursor)
    try:
        context['profile'] = profile_obj[0]
    except:
        return redirect('/')
    return render(request, app_name + 'profile.html', context=context)

def create_profile(request):
    context = {}
    context['user'] = request.user
    if request.method == "POST":
        gender = request.POST.get('gender')
        date_of_birth = request.POST.get('date_of_birth')
        phone_number = request.POST.get('phone_number')
        address = request.POST.get('address')
        if request.POST.get('email'):
            User.objects.filter(username=request.user).update(email=request.POST.get('email'))
        context['gender'] = gender
        context['date_of_birth'] = date_of_birth
        context['phone_number'] = phone_number
        context['address'] = address

        with connection.cursor() as cursor:
            cursor.execute(f"INSERT INTO `accounts_profile` (`user_id`, `gender`, `phone_number`, `date_of_birth`, `address`) VALUES ('{request.user.id}', '{gender}', '{phone_number}', '{date_of_birth}', '{address}')")
        messages.success(request, 'Profile Successfully Created.')
        return redirect('profile')
        return render(request, app_name + 'register.html', context=context)
    return render(request, app_name + 'create-profile.html', context=context)

def edit_profile(request):
    return render(request, app_name + 'edit-profile.html')

def book_ticket(request):
    if not request.user.is_authenticated:
        return redirect('login')
    
    context = {'is_submit':False}

    context['user']= request.user
    if request.method=="GET":
        return render(request, app_name + 'book-ticket.html', context=context)
    

    if request.method=="POST" and (not request.POST.get('train_id') or not request.POST.get('train_seats')):
        context['is_submit']=True
        source = request.POST.get('source')
        destination = request.POST.get('destination')
        date_of_journey = request.POST.get('date_of_journey')
        seats = request.POST.get('seats')
        context['src']=source
        context['dest']=destination
        context['date_of_journey']=date_of_journey
        context['seats']=seats
        print("DATE",date_of_journey)
        with connection.cursor() as cursor:
            cursor.execute(f"SELECT * FROM website_train natural join website_seats WHERE seats>={seats} AND date='{date_of_journey}' AND train_id in (SELECT T1.train_id FROM website_trainschedule as T1, website_trainschedule as T2 WHERE T1.station_id='{source}' AND T2.station_id='{destination}' AND T1.distance < T2.distance AND T1.train_id=T2.train_id) and train_no=train_id")
            trains = namedtuplefetchall(cursor)
            if(len(trains)>0):
                train_obj = trains
                context['details']=train_obj
        return render(request, app_name + 'book-ticket.html', context=context)
    else:
        from random import randint
        pnr=randint(100000,999999)
        messages.success(request, f"Booked! Your PNR: {pnr}")

        # pnr = models.CharField(max_length=10, primary_key=True)
        # username = models.CharField(max_length=20)
        # train_no = models.ForeignKey(Train, max_length=5, on_delete=models.CASCADE)
        # journey_date = models.DateField()
        # seats = models.IntegerField()

        user_id=request.user.id
        train_id=request.POST.get('train_id')
        journey_date=request.POST.get('date')
        train_seats=request.POST.get('train_seats')
        source = request.POST.get('source')
        destination = request.POST.get('destination')
        
        with connection.cursor() as cursor:
            cursor.execute(f"INSERT INTO `website_booking` (`pnr`, `username`, `journey_date`, `seats`, `train_no_id`,`source`,`destination`) VALUES ('{pnr}', '{user_id}', '{journey_date}', '{train_seats}', '{train_id}', '{source}', '{destination}')")
        with connection.cursor() as cursor:
            cursor.execute(f"UPDATE `website_seats` SET seats=seats-{train_seats} WHERE train_id={train_id}")
        return redirect('book-ticket')


def bookings(request):
    context={}
    user_id=request.user.id
    with connection.cursor() as cursor:
        cursor.execute(f"SELECT * FROM website_train join website_booking WHERE username={user_id} and train_no_id=train_no")
        pnrs = namedtuplefetchall(cursor)
    context["data"]=pnrs
    return render(request, app_name + 'bookings.html', context=context)