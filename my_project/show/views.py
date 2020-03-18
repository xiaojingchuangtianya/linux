import datetime
from django.shortcuts import render_to_response
from .models import day_sight
from django.utils import timezone
from django.views.decorators.cache import cache_page

# Create your views here.
def show(request):
    today= timezone.now().date()#获取当天日期
    today_add=day_sight.objects.filter(read_date=today)
    if not request.COOKIES.get("sightseer"):
        if today_add:#已存在记录则直接在访问量加一
            today_add[0].day_count += 1
            today_add[0].save()
        else:#未存在当天记录
            read = day_sight()#先实例化
            read.day_count = 1
            read.read_date = today
            read.save()
    else:
        pass
    read_num=[]
    read_date=[]
    for i in range(7,0,-1):
        dates = today - datetime.timedelta(days=i)
        date_read=day_sight.objects.filter(read_date=dates)
        try :
            read_num.append(date_read[0].day_count )
            read_date.append("{}/{}".format(date_read[0].read_date.month,date_read[0].read_date.day))
        except:
            pass

    response=render_to_response("show.html",context={"num_list":read_num,
                                                   "date_list":read_date,
                                                    })
    response.set_cookie("sightseer","not_first_that_day",max_age=43200)
    return response