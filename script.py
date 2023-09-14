# Script for adding data directly to the database

import os
from django.core.wsgi import get_wsgi_application
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "raildost.settings")
application = get_wsgi_application()
import random
from website.models import *

demo.objects.create(id=1, name="lol")

def create_station(station_code, station_name):
    Station.objects.create(station_code=station_code, station_name=station_name)

def create_train(train_no, train_name, source_code, destination_code, run_days, first_ac, second_ac, third_ac, sleeper, dates):
    source = Station.objects.get(station_code=source_code)
    destination = Station.objects.get(station_code=destination_code)
    train_obj = Train.objects.create(train_no=int(train_no), train_name=train_name, source=source, destination=destination, run_days=run_days)
    for d in dates:
        print(d)
    

def create_schedule(train_no, station_code, arrival, departure, day, distance):
    train = Train.objects.get(train_no=int(train_no))
    station = Station.objects.get(station_code=station_code)
    TrainSchedule.objects.create(train=train, station=station, arrival=arrival, departure=departure, distance=distance, day=day)

def create_seats(train_no, date, seats):
    train = Train.objects.get(train_no=int(train_no))
    Seats.objects.create(train=train, date=date, seats=seats)




# create_train(13307, "GANGASUTLEJ EXPRESS", "DHN", "BSB", "SUN MON WED FRI", 0, 0, 20, 20, 0)
create_station('KIK','KARAIKAL')
create_station('NCR','NAGORE')
create_station('NGT','NAGAPPATTINAM')
create_station('TVR','THIRUVARUR JN')
create_station('PEM','PERALAM JN')
create_station('MV','MAYILADUTURAJ JN')
create_station('SY','SIRKAZHI')
create_station('CDM','CHIDAMBRAM')
create_station('CUPJ','CUDDALORE PORT')
create_station('TDPR','TIRUPADRIPULYUR')
create_station('VM','VILLUPURAM JN')
create_station('TMV','TINDIVANAM')
create_station('MLMR','MELMARUVATTUR')
create_station('CGL','CHENGALPATTU')
create_station('TBM','TAMBARAM')
create_station('MS','CHEENAI EGMORE')
create_station('DBG','DARBHANGA JN')
create_station('SPJ','SAMASTIPUR JN')
create_station('MFP','MUZZAFARPUR JN')
create_station('HJP','HAJIPUR JN')
create_station('SEE','SONPUR JN')
create_station('CPR','CHHAPRA')
create_station('SV','SIWAN JN')
create_station('GKP','GORAKHPUR JN')
create_station('LKO','LUCKNOW NR')
create_station('CNB','KANPUR CENTRAL')
create_station('NDLS','NEW DELHI')
create_station('CSTM','MUMBAI CST')
create_station('DR','DADAR')
create_station('TNA','THANE')
create_station('PNVL','PANVEL')
create_station('MNI','MANGAON')
create_station('KHED','KHED')
create_station('CHI','CHIPLUN')
create_station('SGR','SANGMESHWAR')
create_station('RN','RATNAGIRI')
create_station('ADVI','ADAVALI')
create_station('RAJP','RAJAPUR ROAD')
create_station('VBW','VAIBHAVWADI RD')
create_station('KKW','KANKAVALI')
create_station('SNDD','SINDHUDURG')
create_station('KUDL','KUDAL')
create_station('SWV','SWANTWADI ROAD')
create_station('PERN','PERNEM')
create_station('THVM','THIVIM')
create_station('KRMI','KARMALI')
create_station('MAO','MADGAON')
create_station('BJU','BARAUNI JN')
create_station('DSS','DALSINGH SARAI')
create_station('DEOS','DEORIA SADAR')
create_station('KLD','KHALILABAD')
create_station('BST','BASTI')
create_station('GD','GONDA JN')
create_station('BBK','BARABANKI JN')
create_station('ETW','ETAWAH')
create_station('TDL','TUNDLA JN')
create_station('ALJN','ALIGARH JN')
create_station('GZB','GHAZIABAD')
create_station('MUV','MANDUADIH')
create_station('ASN','ASANSOL')
create_station('BVC','BHAVNAGAR TRMUS')
create_station('LTT','LOKMANYA TILAK')

d = ['2019-11-28', '2019-11-29']
for i in range(1,32):
    if (i<10):
        s='2019-12-0'+str(i)
    else:
        s='2019-12-'+str(i)
    d.append(s)

create_train('10103','MANDOVI EXP','CSTM','MAO','SUN MON TUE WED THU FRI SAT',10,74,288,560,d)
create_train('12553','VAISHALI EXP','BJU','NDLS','SUN MON TUE WED THU FRI SAT',20,128,216,720,d)
create_train('12565','BIHAR S KRANTI','DBG','NDLS','SUN MON TUE WED THU FRI SAT',32,94,72,1040,d)
create_train('16176','CHENNAI EXP','KIK','MS','SUN MON TUE WED THU FRI SAT',10,74,144,560,d);
create_train('12581','SHIVGANGA EXP','MUV','NDLS','SUN MON TUE WED THU FRI SAT',10,74,288,560,d)
create_train('12942','PARASNATH EXP','ASN','BVC','SUN MON TUE WED THU FRI SAT',10,74,288,560,d)
create_train('12167','LTT-MUV EXP','LTT','MUV','SUN MON TUE WED THU FRI SAT',10,74,288,560,d)

create_schedule('12581','MUV','22:30','22:30',1,0)
create_schedule('12581','NDLS','12:15','12:15',2,766)

create_schedule('12942','ASN','19:45','19:45',1,0)
create_schedule('12942','BVC','11:10','11:10',3,2316)

create_schedule('12167','LTT','00:35','00:35',1,0)
create_schedule('12167','MUV','04:25','04:25',2,1497)

create_schedule('16176','KIK','21:00','21:00',1,0)
create_schedule('16176','NCR','21:08','21:10',1,11)
create_schedule('16176','NGT','21:25','21:35',1,19)
create_schedule('16176','TVR','22:15','22:25',1,42)
create_schedule('16176','PEM','22:50','22:51',1,65)
create_schedule('16176','MV','23:18','23:20',1,81)
create_schedule('16176','SY','23:46','23:47',1,101)
create_schedule('16176','CDM','00:05','00:06',2,117)
create_schedule('16176','CUPJ','00:41','00:42',2,156)
create_schedule('16176','TDPR','00:49','00:50',2,160)
create_schedule('16176','VM','02:00','02:10',2,202)
create_schedule('16176','TMV','02:44','02:45',2,240)
create_schedule('16176','MLMR','03:09','03:10',2,270)
create_schedule('16176','CGL','03:43','03:45',2,305)
create_schedule('16176','TBM','04:14','04:15',2,336)
create_schedule('16176','MS','05:15','05:15',2,361);

create_schedule('10103','CSTM','7:10','7:10',1,0)
create_schedule('10103','DR','07:22','07:25',1,9)
create_schedule('10103','TNA','07:47','07:50',1,34)
create_schedule('10103','PNVL','08:25','08:30',1,69)
create_schedule('10103','MNI','10:33','10:35',1,188)
create_schedule('10103','KHED','11:25','11:27',1,284)
create_schedule('10103','CHI','11:57','11:59',1,325)
create_schedule('10103','SGR','12:35','12:36',1,384)
create_schedule('10103','RN','13:10','13:15',1,431)
create_schedule('10103','ADVI','13:43','13:44',1,475)
create_schedule('10103','RAJP','14:17','14:18',1,520)
create_schedule('10103','VBW','14:39','14:40',1,543)
create_schedule('10103','KKW','15:19','15:20',1,587)
create_schedule('10103','SNDD','15:35','15:36',1,612)
create_schedule('10103','KUDL','15:49','15:50',1,626)
create_schedule('10103','SWV','16:15','16:16',1,655)
create_schedule('10103','PERN','16:41','16:42',1,686)
create_schedule('10103','THVM','16:53','16:55',1,701)
create_schedule('10103','KRMI','17:13','17:14',1,725)
create_schedule('10103','MAO','18:45','18:45',1,765);


create_schedule('12553','BJU','9:30','9:30',1,0)
create_schedule('12553','DSS','10:00','10:01',1,28)
create_schedule('12553','SPJ','10:25','10:30',1,51)
create_schedule('12553','MFP','11:15','11:20',1,103)
create_schedule('12553','HJP','12:08','12:10',1,157)
create_schedule('12553','SEE','12:20','12:22',1,163)
create_schedule('12553','CPR','13:40','13:45',1,216)
create_schedule('12553','SV','14:30','14:30',1,277)
create_schedule('12553','DEOS','15:29','15:30',1,347)
create_schedule('12553','GKP','16:50','17:05',1,396)
create_schedule('12553','KLD','17:43','17:45',1,431)
create_schedule('12553','BST','18:10','18:15',1,460)
create_schedule('12553','GD','19:35','19:40',1,550)
create_schedule('12553','BBK','21:08','21:10',1,638)
create_schedule('12553','LKO','21:55','22:05',1,674)
create_schedule('12553','CNB','23:40','23:50',1,748)
create_schedule('12553','ETW','01:41','01:43',2,886)
create_schedule('12553','TDL','03:05','03:10',2,978)
create_schedule('12553','ALJN','04:11','04:16',2,1056)
create_schedule('12553','GZB','05:55','05:57',2,1162)
create_schedule('12553','NDLS','06:45','06:45',2,1187);

create_schedule('12565','DBG','8:35','8:35',1,0)
create_schedule('12565','SPJ','09:25','09:45',1,38)
create_schedule('12565','MFP','10:35','10:40',1,90)
create_schedule('12565','HJP','11:23','11:25',1,143)
create_schedule('12565','SEE','11:38','11:40',1,149)
create_schedule('12565','CPR','12:45','12:50',1,203)
create_schedule('12565','SV','13:40','13:45',1,263)
create_schedule('12565','GKP','15:50','16:10',1,383)
create_schedule('12565','LKO','20:55','21:10',1,661)
create_schedule('12565','CNB','22:48','22:58',1,735)
create_schedule('12565','NDLS','05:35','05:35',2,1174)


def update_station(station_code, station_name,station_master):
    Station.objects.filter(station_code=station_code).update(station_code='',station_name='',station_master='')
    

stations = Station.objects.all()
for station in stations:
    s = str(random.randint(6,9))
    s = s + str(random.randint(109912309, 989790809))
    Station.objects.filter(station_code=station.station_code).update(station_master=s)


create_seats('10103','2022-11-18',100)
