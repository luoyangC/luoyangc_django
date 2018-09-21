from django.shortcuts import render

# Create your views here.
from django.views import View


class Index(View):
    """
    主页测试
    """
    @staticmethod
    def get(request):
        return render(request, 'index.html')
