from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth import login, logout, authenticate
from django.views.decorators.csrf import csrf_exempt
import logging
import json

# Get an instance of a logger
logger = logging.getLogger(__name__)

# Login view
@csrf_exempt
def login_user(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        username = data.get('userName')
        password = data.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return JsonResponse({"userName": username, "status": "Authenticated"})
        else:
            return JsonResponse({"userName": username, "status": "Failed"})
    return JsonResponse({"error": "Invalid request method"})

# Logout view
@csrf_exempt
def logout_request(request):
    logout(request)
    return JsonResponse({"userName": ""})

# Registration view
@csrf_exempt
def registration(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        username = data.get('userName')
        password = data.get('password')
        first_name = data.get('firstName')
        last_name = data.get('lastName')
        email = data.get('email')
        
        username_exist = False
        try:
            User.objects.get(username=username)
            username_exist = True
        except User.DoesNotExist:
            logger.debug("{} is new user".format(username))

        if not username_exist:
            user = User.objects.create_user(
                username=username,
                first_name=first_name,
                last_name=last_name,
                password=password,
                email=email
            )
            login(request, user)
            return JsonResponse({"userName": username, "status": "Authenticated"})
        else:
            return JsonResponse({"userName": username, "error": "Already Registered"})
    return JsonResponse({"error": "Invalid request method"})

# Get Cars placeholder
def get_cars(request, state=None, dealer_id=None, *args, **kwargs):
    return JsonResponse({"status": 200, "cars": [], "reviews": []})


