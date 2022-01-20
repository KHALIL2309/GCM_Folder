from django.shortcuts import render , redirect
from django.http import HttpResponse
# Create your views here.
from .forms import *
from .models import *
# Create your views here.


def home(request):
    vpatient = Patient.objects.all()
    context = {'vpatients' : vpatient,}
    return render (request , 'cabinetMedical/home.html',context) 

def patient(request,pk):
    vpatient = Patient.objects.get(id=pk)
    rdv = vpatient.rdv_set.all()
    context={
        'patient' : vpatient , 
        'rdv' : rdv ,
    }
    return render (request , 'cabinetMedical/patient.html',context)


def create(request):
    form = PatientForm()
    if request.method == 'POST':    # pour sécurité
        form = PatientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')  # pour rediriger les informations sur la page
    context = {'form' : form}
                
    return render (request , 'cabinetMedical/My_Rdv_Patient_form.html',context)



def update(request , pk):
    patinte = Patient.objects.get(id=pk)
    form = PatientForm(instance=patinte)
    if request.method == 'POST':
        form = PatientForm(request.POST , instance=patinte)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form' : form}
                
    return render (request , 'cabinetMedical/My_Rdv_Patient_form.html',context)



def delete(request , pk):
    patiente = Patient.objects.get(id=pk)
    context = {'patiente' : patiente}
    if request.method == 'POST':
        patiente.delete()
        return redirect('/')
                
    return render (request , 'cabinetMedical/delete_form.html',context)