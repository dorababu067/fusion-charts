from django.shortcuts import render
from django.template.loader import render_to_string
from django.http import JsonResponse,HttpResponse
from .weather_data import citys_temp
from .news_api import latest_news
import matplotlib.pyplot as plt 
import pandas as pd
from .fusioncharts import FusionCharts
from collections import OrderedDict

# Create your views here.
df = pd.read_csv('Departments_Data_Alapakam.csv')

def index(request):
    html = df.to_html()
    context = {
      'html' : html,
      "temp_news" : zip(citys_temp,latest_news)
     
    }
    # print(citys_temp)
    return render(request,'index.html',context)

ajax_emp_type = []
def managers_filter(request):
  if request.is_ajax:
    dept =  request.POST.get('dept')
    country =  request.POST.get('country')
    print(country)
    print(ajax_emp_type[0])
    select_dp = df[(df['Section']== ajax_emp_type[0]) & (df['Location']== country) & (df['Department']== dept)]
    # print(select_dp)
    raw_managers =  select_dp.iloc[:,3]
    # print(raw_managers)
    context = {
        "managers" : raw_managers.tolist()
    }
    html = render_to_string('managers_filter.html',context,request=request)
    # print(html)
    return JsonResponse({"html":html})
 

def emp_drp(request,emp_type=None):
    if request.method == "POST":
      dept = request.POST['department']
      con = request.POST['country']
      man = request.POST['managers']
      filter_data = df[(df['Department'] == dept) & (df['Location'] == con) & (df['MID'] == man ) & (df['Section'] == emp_type )]
      html = filter_data.to_html()
      #graph-data
      x = list(filter_data.columns.values[5:])
      raw_y = df[(df['Section'] == emp_type) & (df.Location == con ) & (df.Department ==dept ) & (df.MID == man) ]
      y_data = raw_y.values.tolist()
      y = y_data[0][5:]
      dataSource =  OrderedDict()
      dataSource["data"] = []
      for key, value in zip(x,y):
        data = {}
        data["label"] = key
        data["value"] = value
        dataSource["data"].append(data)
      # print(dataSource)
      column2D = FusionCharts("column2d", "ex1" , "600", "400", "chart-1", "json", dataSource)
      context = {
        "filter_data": html,
        "mydb" : emp_type,
        "temp_news" : zip(citys_temp,latest_news),
        'output' : column2D.render(), 
        'chartTitle': 'Simple Chart Using Array'
       
      }
      return render(request,'index.html',context)
    else:
      emp_type = emp_type.upper()
      # print(emp_type)
      if len(ajax_emp_type)>0:
        ajax_emp_type[0] = emp_type
      else:
        ajax_emp_type.append(emp_type)
      selected_data = df[(df.Section == emp_type)]
      # print(selected_data)
      html = selected_data.to_html()
      # print(type(html))
      context = {
        "emp_type" : emp_type,
        "html1" : html,
       "temp_news" : zip(citys_temp,latest_news)

      }
      return render(request,'index.html',context)
      
    
