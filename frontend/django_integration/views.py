from django.views import View
from django.shortcuts import render

class Frontend(View):
    def get(self, request):
        return render(request, "build/index.html")
