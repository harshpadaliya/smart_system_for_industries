import requests
from django.shortcuts import render, redirect
# from django.http import HttpResponse
from django.contrib import messages
import datetime

# Create your views here.
contextlogin = {
    'login': False,
    'error': '',
    'user_name': 'USER-NAME',
    'user_role': 'USER-ROLE',
    'user_email': 'EMAIL-ID',
    'user_phone': 'PHONE-NO',
}


def index(request):
    context = {
        'projecttitle': 'IOT BASED SMART SYSTEM',
        'title': 'Login'
    }
    return render(request, 'adminlte/index.html', context)


def login(request):
    context = {
        'projecttitle': 'IOT BASED SMART SYSTEM',
        'title': 'Login'
    }
    if request.method == 'POST':

        email = request.POST.get("txt-email")
        password = request.POST.get("txt-password")
        url = "https://iotbasedsmartsystemforindustries.000webhostapp.com/authentication/LOGIN.php"
        params = {
            "email": email,
            "password": password
        }
        r2 = requests.post(url=url, data=params)
        print(r2.text)

        res = r2.json()
        ev = res['error']
        context['data'] = res

        # print(context)

        if not ev:
            if context['data']['user']['STATUS'] == "1":
                contextlogin['login'] = True
                contextlogin['error'] = ''
                contextlogin['user_id'] = context['data']['user']['LOGIN_ID']
                contextlogin['user_name'] = context['data']['user']['NAME']
                contextlogin['user_role'] = context['data']['user']['ROLE']
                contextlogin['user_email'] = context['data']['user']['EMAIL_ID']
                contextlogin['user_phone'] = context['data']['user']['PHONE_NO']
                return redirect('dashboard')
            else:
                messages.error(request, "Your Email is Inactive !! ")

        else:
            messages.error(request, "Invalid Email or Password !! ")

    else:
        contextlogin['login'] = False
        messages.error(request, contextlogin['error'])
        contextlogin['user_id'] = "USER-ID"
        contextlogin['user_name'] = "USER-NAME"
        contextlogin['user_role'] = "USER-ROLE"
        contextlogin['user_email'] = 'EMAIL-ID'
        contextlogin['user_phone'] = 'PHONE-NO'

    return render(request, 'adminlte/index.html', context)


def dashboard(request):
    if not contextlogin['login']:
        contextlogin['error'] = 'LoginFirst'
        return redirect('login')
    else:
        context = {
            'projecttitle': 'IOT BASED SMART SYSTEM',
            'title': 'Dashboard',
            'user_name': contextlogin['user_name'],
            'user_role': contextlogin['user_role'],
        }
        url = "https://iotbasedsmartsystemforindustries.000webhostapp.com/authentication/newapi.php"
        r6 = requests.post(url=url, data="this")

        newapi_res = r6.json()

        ev = newapi_res['error']
        context['data'] = newapi_res

        context['person_count_value'] = context['data']['sensor']['count']['COUNT']
        context['person_count_time'] = context['data']['sensor']['count']['ADDED_TIME']
        context['person_count_time'] = datetime.datetime.strptime(context['person_count_time'],
                                                                  '%Y-%m-%d %H:%M:%S')
        context['person_count_class'] = "bg-info"


        context['flame_sensor_value'] = context['data']['sensor']['flame']['FLAME_VALUE']
        context['flame_sensor_class'] = "bg-success"

        if context['flame_sensor_value'] == "0":
            context['flame_sensor_value'] ="FLAME DETECTED"
            context['flame_sensor_class'] = "bg-danger"
        else:
            context['flame_sensor_value'] = "NO FLAME DETECTED"
            context['flame_sensor_class'] = "bg-success"

        context['flame_sensor_time'] = context['data']['sensor']['flame']['READING_TIME']
        context['flame_sensor_time'] = datetime.datetime.strptime(context['flame_sensor_time'],
                                                                  '%Y-%m-%d %H:%M:%S')


        context['smoke_sensor_value'] = context['data']['sensor']['smoke']['SMOKE_VALUE']
        context['smoke_sensor_class'] = "bg-success"
        if context['smoke_sensor_value'] == "0":
            context['smoke_sensor_value'] ="SMOKE DETECTED"
            context['smoke_sensor_class'] = "bg-danger"
        else:
            context['smoke_sensor_value'] = "NO SMOKE DETECTED"
            context['smoke_sensor_class'] = "bg-success"
        context['smoke_sensor_time'] = context['data']['sensor']['smoke']['READING_TIME']
        context['smoke_sensor_time'] = datetime.datetime.strptime(context['smoke_sensor_time'],
                                                                  '%Y-%m-%d %H:%M:%S')


        context['temperature_sensor_value'] = context['data']['sensor']['temp']['TEMP_VALUE']
        context['temperature_sensor_time'] = context['data']['sensor']['temp']['READING_TIME']
        context['temperature_sensor_time'] = datetime.datetime.strptime(context['temperature_sensor_time'],
                                                                        '%Y-%m-%d %H:%M:%S')
        context['temperature_sensor_class'] = "bg-info"



        context['gas_sensor_value'] = context['data']['sensor']['mq4']['MQ4_VALUE']
        context['gas_sensor_class'] = "bg-success"
        if (int(context['gas_sensor_value'])) > 800:
            context['gas_sensor_value'] ="GAS DETECTED"
            context['gas_sensor_class'] = "bg-danger"
        else:
            context['gas_sensor_value'] = "NO GAS DETECTED"
            context['gas_sensor_class'] = "bg-success"
        context['gas_sensor_time'] = context['data']['sensor']['mq4']['READING_TIME']
        context['gas_sensor_time'] = datetime.datetime.strptime(context['gas_sensor_time'],
                                                                '%Y-%m-%d %H:%M:%S')


        context['pirmotion_sensor_value'] = context['data']['sensor']['ir']['IR_VALUE']
        context['pirmotion_sensor_time'] = context['data']['sensor']['ir']['READING_TIME']
        context['pirmotion_sensor_time'] = datetime.datetime.strptime(context['pirmotion_sensor_time'],
                                                                      '%Y-%m-%d %H:%M:%S')
        context['pirmotion_sensor_class'] = "bg-info"

        # print(datetime.datetime.now())
        pir_time = context['pirmotion_sensor_time']
        # print(pir_time)  # to time

        # format = "%Y/%m/%d %H:%M:%S"
        # print(datetime.datetime.now().strftime(format))

        # print(datetime.datetime.now()-pir_time)# time diff
        # print((datetime.datetime.now()-pir_time).total_seconds())  # time diff in sec
        pirtimediff = (datetime.datetime.now()-pir_time).total_seconds()
        if pirtimediff > 300:
            context['pirmotion_sensor_value'] = "NO MOVEMENT"
            context['pirmotion_sensor_time'] = datetime.datetime.now()
            # context['pirmotion_sensor_class'] = "bg-info"
        else:
            context['pirmotion_sensor_value'] = "MOVEMENT DETECTED"
            # context['pirmotion_sensor_time'] = datetime.datetime.now()
            context['pirmotion_sensor_class'] = "bg-warning"

        # print(context)
        if ev:
            messages.error(request, newapi_res['message'])
        return render(request, 'adminlte/dashboard.html', context)


def adminpanel(request):
    if not contextlogin['login']:
        contextlogin['error'] = 'LoginFirst'
        return redirect('login')
    else:

        context = {
            'projecttitle': 'IOT BASED SMART SYSTEM',
            'title': 'Add Admin',
            'user_name': contextlogin['user_name'],
            'user_role': contextlogin['user_role'],
            'user_email': contextlogin['user_email'],
            'user_phone': contextlogin['user_phone'],
        }
        if context['user_role'] != 'Admin':
            return render(request, 'adminlte/notadminerror.html', context)
        return render(request, 'adminlte/admin.html', context)


def profile(request):
    if not contextlogin['login']:
        contextlogin['error'] = 'LoginFirst'
        return redirect('login')
    else:

        context = {
            'projecttitle': 'IOT BASED SMART SYSTEM',
            'title': 'Profile',
            'user_id': contextlogin['user_id'],
            'user_name': contextlogin['user_name'],
            'user_role': contextlogin['user_role'],
            'user_email': contextlogin['user_email'],
            'user_phone': contextlogin['user_phone'],
        }

        return render(request, 'adminlte/profile.html', context)


def personcount_data(request):
    if not contextlogin['login']:
        contextlogin['error'] = 'LoginFirst'
        return redirect('login')
    else:
        context = {
            'projecttitle': 'IOT BASED SMART SYSTEM',
            'title': 'Person Count',
            'user_name': contextlogin['user_name'],
            'user_role': contextlogin['user_role'],
        }

        url = "https://iotbasedsmartsystemforindustries.000webhostapp.com/authentication/PERSONCOUNT.php"
        r5 = requests.post(url=url, data="this")

        pc_res = r5.json()

        ev = pc_res['error']
        context['data'] = pc_res
        # print(context)

        if ev:
            messages.error(request, pc_res['message'])
        return render(request, 'adminlte/personcount_data.html', context)


def smoke_data(request):
    if not contextlogin['login']:
        contextlogin['error'] = 'LoginFirst'
        return redirect('login')
    else:
        context = {
            'projecttitle': 'IOT BASED SMART SYSTEM',
            'title': 'Smoke Sensor',
            'user_name': contextlogin['user_name'],
            'user_role': contextlogin['user_role'],
        }

        url = "https://iotbasedsmartsystemforindustries.000webhostapp.com/authentication/SMOKESENSOR.php"
        r1 = requests.post(url=url, data="this")

        smoke_res = r1.json()

        ev = smoke_res['error']
        context['data'] = smoke_res
        # print(context)

        if ev:
            messages.error(request, smoke_res['message'])
        return render(request, 'adminlte/smoke_data.html', context)


def flame_data(request):
    if not contextlogin['login']:
        contextlogin['error'] = 'LoginFirst'
        return redirect('login')
    else:
        context = {
            'projecttitle': 'IOT BASED SMART SYSTEM',
            'title': 'Flame Sensor',
            'user_name': contextlogin['user_name'],
            'user_role': contextlogin['user_role'],
        }
        url = "https://iotbasedsmartsystemforindustries.000webhostapp.com/authentication/FLAMESENSOR.php"
        r3 = requests.post(url=url, data="this")

        flame_res = r3.json()

        ev = flame_res['error']
        context['data'] = flame_res
        # print(context)

        if ev:
            messages.error(request, flame_res['message'])
        return render(request, 'adminlte/flame_data.html', context)


def temperature_data(request):
    if not contextlogin['login']:
        contextlogin['error'] = 'LoginFirst'
        return redirect('login')
    else:
        context = {
            'projecttitle': 'IOT BASED SMART SYSTEM',
            'title': 'Temperature Sensor',
            'user_name': contextlogin['user_name'],
            'user_role': contextlogin['user_role'],
        }
        url = "https://iotbasedsmartsystemforindustries.000webhostapp.com/authentication/TEMPSENSOR.php"
        r6 = requests.post(url=url, data="this")

        pc_res = r6.json()

        ev = pc_res['error']
        context['data'] = pc_res
        # print(context)

        if ev:
            messages.error(request, pc_res['message'])
        return render(request, 'adminlte/temperature_data.html', context)


def gas_data(request):
    if not contextlogin['login']:
        contextlogin['error'] = 'LoginFirst'
        return redirect('login')
    else:
        context = {
            'projecttitle': 'IOT BASED SMART SYSTEM',
            'title': 'Gas Sensor',
            'user_name': contextlogin['user_name'],
            'user_role': contextlogin['user_role'],
        }
        url = "https://iotbasedsmartsystemforindustries.000webhostapp.com/authentication/MQSENSOR.php"
        r3 = requests.post(url=url, data="this")

        gas_res = r3.json()

        ev = gas_res['error']
        context['data'] = gas_res
        # print(context)

        if ev:
            messages.error(request, gas_res['message'])
        return render(request, 'adminlte/gas_data.html', context)


def pirmovement_data(request):
    if not contextlogin['login']:
        contextlogin['error'] = 'LoginFirst'
        return redirect('login')
    else:
        context = {
            'projecttitle': 'IOT BASED SMART SYSTEM',
            'title': 'PIR Movement Sensor',
            'user_name': contextlogin['user_name'],
            'user_role': contextlogin['user_role'],
        }
        url = "https://iotbasedsmartsystemforindustries.000webhostapp.com/authentication/PIRMOVEMENTSENSOR.php"
        r4 = requests.post(url=url, data="this")

        pir_res = r4.json()

        ev = pir_res['error']
        context['data'] = pir_res
        # print(context)

        if ev:
            messages.error(request, pir_res['message'])
        return render(request, 'adminlte/pirmovement_data.html', context)


def add_admin(request):
    if request.method == 'POST':
        name = request.POST.get("username")
        email = request.POST.get("useremail")
        password = request.POST.get("userpassword")
        phone = request.POST.get("userphone")
        role = request.POST.get("userrole")
        status = request.POST.get("userstatus")

        params = {
            "email": email,
            "password": password,
            "phone": phone,
            "role": role,
            "name": name,
            "status": status,
        }
        print(params)
        url = "https://iotbasedsmartsystemforindustries.000webhostapp.com/authentication/SIGNUP.php"
        r2 = requests.post(url=url, data=params)
        print(r2.text)

        res = r2.json()
        ev = res['error']

        if not ev:
            messages.success(request, "user added successfully!!")
            print("User added...")
            return adminpanel(request)
        else:
            messages.success(request, "Not Able to to add admin!!")
            return adminpanel(request)

    return adminpanel(request)
