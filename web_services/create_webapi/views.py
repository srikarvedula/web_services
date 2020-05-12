from django.shortcuts import render
from web_services.ConnPool import db
from rest_framework.views import APIView
import json
from django.http import HttpResponse, JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
# Create your views here.


l_data_show={}

def showTable():
    l_data_show.clear()
    cursor = db.cursor()
    cursor.execute("select * from gen_table;")
    for random_int, random_str, random_date, name_of_file in cursor.fetchall():
        l_data_show[name_of_file]={"random_int": random_int
                            , "random_str": random_str
                            , "random_date": random_date}



    print("something")
    print(l_data_show)
showTable()

@api_view(['GET', 'POST'])
def get_json(request):
    showTable()
    print("l_data_show")
    print(l_data_show)
    rest_data=json.dumps(l_data_show)
    print(rest_data)

    #return HttpResponse(rest_data, content_type="application/json")
    return JsonResponse(l_data_show)

