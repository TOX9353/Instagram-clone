from django.shortcuts import render
# Create your views here.
from rest_framework.views import APIView


class Join(APIView):
    def get(selfs, request):
        return render(request, 'user/join.html')