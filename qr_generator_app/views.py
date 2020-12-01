from django.shortcuts import render
from .models import *
from django.views.generic import View

# Create your views here.
def sites_list(request):
    sites=Site.objects.all()
    return render(request,'qr_generator_app/index.html',context={'sites':sites})
class ImageGenerator(View):
    def get(self,request,id):
        site=Site.objects.get(id=id)
        return render(request,'qr_generator_app/image.html',context={'site':site})