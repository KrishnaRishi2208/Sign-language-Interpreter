from django.shortcuts import render
from django.http import HttpResponse
from . import ml.test

# exec(compile(open("ml/test.py", "rb").read(), "ml/trst.py", 'exec'))
# Create your views here.
def home(request):
    return render(request,'home.html',{"value":ml.label[ml.index]})