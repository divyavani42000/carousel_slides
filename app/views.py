from django.shortcuts import render

# Create your views here.
def slides(request):
    return render(request,'slides.html')