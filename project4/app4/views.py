# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.shortcuts import redirect
from app4.models import mypage
import json
from django.core.serializers import serialize

# Create your views here.
def index(request):
    return render(request,'index.html')

def register(request):
    return render(request,'register.html')

def searchpage(request):
    return render(request,'searchpage.html')

def regcod(request):
    name=request.GET.get('name')
    address=request.GET.get('address')
    #m=mypage(myname=name, mailmyaddr=address)
    #m.save()
    m=mypage.objects.create(myname=name, myaddress=address)
    if(m!=None):
        data = {'sts':True,'msg':"saved data"}
        return JsonResponse(data)
    else:
        data = {'sts':False,'msg':"error..failed"}
        return JsonResponse(data)
    
def fillname(request):
    data1=mypage.objects.all()
    data = serialize("json", data1)
    return JsonResponse(data,safe=False)
    # output=list(data1)
    # data = {'datas':data1}
    # data =  dict()
    # data['names'] = model_to_dict(data1)
    # return JsonResponse({'data': output},safe=False)
    # return render(request,'student/viewdata.html',{'datas':data})

def searchcontent(request):
    nme=request.GET.get('nme')
    dataout=mypage.objects.filter(myname=nme)
    data = serialize("json", dataout)
    return JsonResponse(data,safe=False)
    
def updatecontent(request):
    nme=request.GET.get('nme')
    addr=request.GET.get('addr')
    dbobj=mypage.objects.filter(myname=nme)
    dbobj.update(myaddress=addr)
    if(dbobj!=None):
        data = {'sts':True,'msg':"saved data"}
        return JsonResponse(data)
    else:
        data = {'sts':False,'msg':"error..failed"}
        return JsonResponse(data)
    # dataout=mypage.objects.filter(myname=nme)
    # data = serialize("json", dataout)
    # return JsonResponse(data,safe=False)