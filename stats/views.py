from django.shortcuts import render
from .models import Statistic, DataItem
from faker import Faker
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.db.models import Sum
# Create your views here.

fake = Faker()

def main(request):
    statistic_list = Statistic.objects.all()

    context = {'statistic_list':statistic_list}
    return render(request, 'stats/main.html', context)

def dashboard(request, slug):
    statistic = get_object_or_404(Statistic, slug=slug)
    context = {
        'name' : statistic.name,
        'slug' : statistic.slug,
        'data' : statistic.data,
        'user' : request.user.username if request.user.username else fake.name()
    }
    return render(request, 'stats/dashboard.html', context)


def chart_data(self, slug):
    statistic = get_object_or_404(Statistic, slug=slug)
    qs = statistic.data.values('user').annotate(Sum('value'))
    chart_data = [i['value__sum'] for i in qs]
    chart_labels = [i['user'] for i in qs]

    return JsonResponse({
        'chart_data' : chart_data,
        'chart_labels' : chart_labels
    })