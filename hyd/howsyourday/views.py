from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .models import ColorDecision
from django.views.decorators.csrf import csrf_protect
import datetime

@csrf_protect
def index(request):
    if request.method == 'GET':
        today_min = datetime.datetime.combine(datetime.date.today(), datetime.time.min)
        today_max = datetime.datetime.combine(datetime.date.today(), datetime.time.max)
        latest_colors = ColorDecision.objects.filter(publishDate__range=(today_min, today_max))
        latest_colors_chunked = (latest_colors[i:i+6] for i in range(0, len(latest_colors), 6))
        template = loader.get_template('howsyourday/index.html')
        context = {
            'colorTodays': latest_colors_chunked,
            'situation': ""
        }
        return HttpResponse(template.render(context, request))
    elif request.method == 'POST':
        name = request.POST.get("submitNAME")
        text = request.POST.get("submitTEXT")
        color = request.POST.get("submitCOLOR")
        time = datetime.date.today()
        cda = ColorDecision(userText=text, userName=name, userColor=color, publishDate=time)
        cda.save()
        today_min = datetime.datetime.combine(datetime.date.today(), datetime.time.min)
        today_max = datetime.datetime.combine(datetime.date.today(), datetime.time.max)
        latest_colors = ColorDecision.objects.filter(publishDate__range=(today_min, today_max))
        latest_colors_chunked = (latest_colors[i:i+6] for i in range(0, len(latest_colors), 6))
        template = loader.get_template('howsyourday/index.html')
        context = {
            'colorTodays': latest_colors_chunked,
            'situation': ""
        }
        return HttpResponse(template.render(context, request))

def upvote(request, color_id):
    cda = ColorDecision.objects.get(pk = color_id)
    cda.votes += 1
    cda.save()
    return HttpResponseRedirect('/')
