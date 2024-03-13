from django.shortcuts import render

from .models import Student


# Create your views here.
def home(request):
    return render(request, 'home.html')


def addStudent(request):
    if request.method == 'POST':
        sname = request.POST['sname']
        course = request.POST['course']
        fees = request.POST['fees']
        Student(sname=sname, course=course, fees=fees).save()
        msg='data inserted sucessuful'
        return render(request, 'addStudent.html', {'saved': True,'msg':msg})
    else:
        return render(request, 'addStudent.html', {'saved': True})
