from django.shortcuts import render

# Create your views here.
def honey(request):
    d={'name':'SAI','age':22,'a':200,'b':300,'c':400}
    return render(request,'honey.html',context=d)
