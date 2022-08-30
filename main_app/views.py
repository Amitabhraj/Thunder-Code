from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect,JsonResponse
from .models import *
from django.contrib.auth.decorators import login_required
from django.db.models import Count
from django.contrib.auth import login as auth_login
from django.core.paginator import Paginator, EmptyPage
from django.contrib.auth.models import *
from django.db.models import Count
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
import os
import datetime
from datetime import datetime as dt
import calendar
from django.db.models import Sum
from calendar import monthrange
from own_business.settings import BASE_DIR
from django.views.decorators.csrf import csrf_exempt
import time


# Create your views here.






def index(request):
    return render(request, 'index.html')












