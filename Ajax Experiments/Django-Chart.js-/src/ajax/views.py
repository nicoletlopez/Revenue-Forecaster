from django.contrib.auth import get_user_model
from django.shortcuts import render
from django.views.generic import View
from django.http import JsonResponse

from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Actual
User = get_user_model()
q = Actual.objects.values('actual_arr')
class HomeView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'charts.html', {})



def get_data(request, *args, **kwargs):
    data = {
        "sales": 100,
        "customers": 10,
    }
    return JsonResponse(data) #http repsonse

class ChartData(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        qs_count = User.objects.all().count()
        labels = ["Users", "Red", "Blue", "Yellow"]
        q = Actual.objects.values('actual_rev')
        default_items = []
        for item in q:
            for key, value in item.items():
                default_items.append(value)
        print(default_items)
        data = {
            "labels": labels,
            "default": default_items,
        }
        return Response(data)