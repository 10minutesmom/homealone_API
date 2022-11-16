#from django.shortcuts import render
from rest_framework import viewsets
#from rest_framework.response import APIView
from my_api.serializers import KidSerializer,ScheduleSerializer,DictSerializer
from my_api.models import Kid,Schedule
#from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
import json
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
import pickle
#from .models import Kid
#from .serializers import SpeciesSerializer
from rest_framework.parsers import JSONParser

#file_open = open("file path", 'r', encoding="UTF-8")
def schedule_All(uid):
   file_path = r"C:\Users\조세연\Desktop\schedule.json"
   with open(file_path, 'r',encoding='UTF-8') as file:
      data = json.load(file)
      #print(type(data))
   return JsonResponse(data)

#def schedule_recent(uid):
   #file_path = r"C:\Users\조세연\myproject\Scripts\my_django_project\my_api\schedule.json"
   #with open(file_path, 'r',encoding='UTF-8') as file:
      #data=json.load(file)
   #day,time_hr,time_min='mon',str(13),str(20)
   #rst_data=data[day][time_hr][time_min]
   #return JsonResponse(rst_data)
class KidsViewSet(viewsets.ModelViewSet):
   queryset = Kid.objects.all()
   serializer_class = KidSerializer


class ScheduleViewSet(viewsets.ModelViewSet):
    queryset = Schedule.objects.all()
    serializer_class = ScheduleSerializer

@api_view(['POST'])
def schedule_recent(request):
    if request.method=='POST':
        #datas= JSONParser().parse(request)
        #serializer = ScheduleSerializer(data=request.data)
        body=json.loads(request.body.decode('EUC-KR'))
        #if serializer.is_valid():
           # serializer.save()
        #else:
            #HttpResponse("Bad")

        #mod_dict=Schedule.objects.values('schedule_dt')
        #serializer=ScheduleSerializer(mod_dict)
        #st_json=json.dumps(serializer)
        file_path = r"C:\Users\조세연\Desktop\schedule.json"
        with open(file_path,"w")as outfile:
            json.dump(body,outfile,ensure_ascii=False)
        return HttpResponse(body)
    else:
        return HttpResponse("Fail")
   #return HttpResponse(self)
   


