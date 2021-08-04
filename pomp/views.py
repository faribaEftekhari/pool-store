from django.shortcuts import render
from . import models

# Create your views here.
def pomplist(request):
    # return render(request,'pomp/pomplist.html')
    ps=models.pomps.objects.all().order_by('brand')
    args={'pomps':ps}
    return render(request,'pomp/pomplist.html',args)
