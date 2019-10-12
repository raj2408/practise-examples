from django.shortcuts import render
from django.http import HttpResponseRedirect
from django import forms

# Create your views here.
def bmi(request):

    if request.method == 'POST':
        height =  request.POST.get('height','')
        h_unit = request.POST.get('unit_height', '')
        weight = request.POST.get('weight','')
        w_unit = request.POST.get('unit_weight','')

        bmi_val = float(weight)/(float(height)/100)**2
    return render(request,'bmi.html', locals())