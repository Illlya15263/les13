from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.http import require_GET, require_POST
from .models import get_product_all, check_user
# Create your views here.


def index(request):
    return render(request, 'main/index.html')


