from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from .models import formModel
from .form import MyForm


def form(request):
    if request.method == "POST" :
        frm = MyForm(request.POST)
        if frm.is_valid():
            frm.save()
            #return redirect ('/not-found')
    else:
        frm = MyForm()
        print("this form is not valid")
    context = {'frm':frm}
    return render(request, 'index.html', context)
    #return HttpResponse("This is the main page")

