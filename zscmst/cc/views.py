from django.shortcuts import render
from .models import CitizenCharter
from datetime import datetime
from django.http import JsonResponse, HttpResponse
from .models import *
from django.core import serializers
from django.db.models import Count
from django.template import loader
# from .models import Post
# from django.contrib.auth.decorators import login_required
# from . import forms

# def post_list(request):
#     posts = Post.objects.all().order_by('-date')
#     return render(request, 'posts/post_list.html', {'poat':posts})

# def post_page(request, slug):
#     post = Post.objects.get(slug=slug)
#     return render(request, 'posts/post_page.html', {'post':post})

# @login_required(login_url="/user/login/")
# def post_new(request):
#     form = forms.CreatePost()
#     return render(request,'posts/post_new.html', {'form':form})

def AdminDashboard(request):
    return render(request, 'dashboard.html')

def AdminLogin(request):
    return render(request, 'login-admin.html')


def BASE(request):
    office = TableOffice.objects.all()
    context = {
        "office":office
    }
    return render(request, 'base.html', context)
   # return render(request, 'base.html')


def insertEval(request):
    now = datetime.now()
    dt_string = now.strftime("%Y-%m-%d %H:%M:%S")
    
    v_clienType = request.POST.get('rdoClientType')
    # v_txtDate= request.POST.get('txtDate')
    v_txtDate= dt_string
    v_rdoSex = request.POST.get('rdoSex')
    v_txtAge = request.POST.get('txtAge')
    v_txtRegion = request.POST.get('txtRegion')
    v_txtService = request.POST.get('txtService')
    v_rdoCC1 = request.POST.get('rdoCC1')
    v_rdoCC2 = request.POST.get('rdoCC2')
    v_rdoCC3 = request.POST.get('rdoCC3')
    v_rdosqd0 = request.POST.get('rdosqd0')
    v_rdosqd1 = request.POST.get('rdosqd1')
    v_rdosqd2 = request.POST.get('rdosqd2')
    v_rdosqd3 = request.POST.get('rdosqd3')
    v_rdosqd4 = request.POST.get('rdosqd4')
    v_rdosqd5 = request.POST.get('rdosqd5')
    v_rdosqd6 = request.POST.get('rdosqd6')
    v_drdosqd7 = request.POST.get('rdosqd7')
    v_rdosqd8 = request.POST.get('rdosqd8')
    v_txtsuggestion = request.POST.get('txtsuggestion')
    v_textemail = request.POST.get('textemail')
    v_textname = request.POST.get('txtName')
    v_other = request.POST.get('txtOther')
    v_office = request.POST.get('slcoffice')

    eval = CitizenCharter(eval_citizenttype=v_clienType, eval_date=v_txtDate, eval_sex=v_rdoSex, eval_age=v_txtAge, eval_region=v_txtRegion, eval_service=v_txtService, eval_cc1=v_rdoCC1, eval_cc2=v_rdoCC2, eval_cc3=v_rdoCC3, eval_sqd0=v_rdosqd0, eval_sqd1=v_rdosqd1, eval_sqd2=v_rdosqd2, eval_sqd3=v_rdosqd3,eval_sqd4=v_rdosqd4, eval_sqd5=v_rdosqd5, eval_sqd6=v_rdosqd6, eval_sqd7=v_drdosqd7, eval_sqd8=v_rdosqd8,eval_suggestion=v_txtsuggestion,eval_email=v_textemail, eval_name=v_textname, eval_other=v_other, office_id=v_office)
  # eval = CitizenCharter(eval_citizenttype=v_clienType)
    eval.save()
    return render(request, 'thankyou.html', {})

def OfficeView(request):
    office = TableOffice.objects.all()
    context = {
        "office":office
    }
    return render(request, 'base.html', context)

def getProcess(request):
    office = request.GET.get('office')
    office = TableOffice.objects.filter(office_id=office)
    process = list(TableProcess.objects.filter(office_id__in=office).values('process_desc'))
    response_data = {
        "process" : process
    }
    return JsonResponse(response_data)

def getClientperMonth(request, queryset, **options):

    queryset = CitizenCharter.objects.values('office_id').annotate(count=Count('office_id'))
    
    context = {
        'office_id' : queryset,
    }

    return render(request, "dashboard.html",context)
