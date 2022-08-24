from django.shortcuts import render
from rest_framework.views import APIView


class Main(APIView):
    # noinspection PyMethodMayBeStatic
    def get(self, request):
        return render(request, "histagram/main.html")

    # noinspection PyMethodMayBeStatic
    def post(self, request):
        return render(request, "histagram/main.html")

