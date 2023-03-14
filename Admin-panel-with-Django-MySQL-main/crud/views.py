from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import *
from .forms import schedularForm
from .filters import schedularFilter

from django.db import transaction





# Create your views here.

def crud_view1(request):
    schedular_all = schedular.objects.all()

    # schedular_get = schedular.objects.get()
    myFilter = schedularFilter(request.GET, queryset=schedular_all)              # for search bar
    schedular_all = myFilter.qs


    # creating new schedular
    form = schedularForm()
    if request.method == 'POST':
        form = schedularForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/crud')

    context = {'schedular_all':schedular_all, 'myFilter':myFilter, 'form':form}
    return render(request, 'crud/front.html', context)



###################################################################################################################3


# def new_schedular(request):
#     form = schedularForm()

#     if request.method == 'POST':
#         form = schedularForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('/crud')

#     context = {'form':form}
#     return render(request, 'crud/schedular_form.html', context)


def update_schedular(request, s):
    schedular_all = schedular.objects.get(id=s)
    form = schedularForm(instance=schedular_all)

    if request.method=='POST':
        form = schedularForm(request.POST, instance=schedular_all)
        if form.is_valid():
            form.save()
            return redirect('/crud')

    context = {'form':form}
    return render(request, 'crud/schedular_form.html', context)
    


def delete_schedular(request, s):
    schedular_all = schedular.objects.get(id=s)

    if request.method=="POST":
        schedular_all.delete()
        return redirect('/crud')

    context = {'item':schedular_all}
    return render(request, 'crud/delete.html', context)



# /////////////////////////////////////////////////////////////////////////////////////////////////

# for bulk upload
def entry(request):#for bulk input
    lo=schedular.objects.all()
    return render(request,"crud/entry.html")


def csvinput(request):#for bulk input code
    if request.method=="POST":
        new=request.FILES['file'].readlines()
        
        for i in range(len(new)):
            new[i]=str(new[i])[2:-5]
            new[i]=new[i].split(",")
        
        with transaction.atomic():
            
            for i in range(1,len(new)):
                schedular_fields=schedular(
                    staff_email_id=new[i][0],
                    associated_program_code=new[i][1],
                    academic_year_code=new[i][2],
                    batch=new[i][3],
                    semester=new[i][4],
                    class_type=new[i][5],
                    day=new[i][6],
                    venue=new[i][7],
                    start_time=new[i][8],
                    end_time=new[i][9],
                    status=new[i][10]
                    )

                schedular_fields.save()
    return redirect('/crud')


#/////////////////////////////////////////////////////////////////////////////////////////////////////////