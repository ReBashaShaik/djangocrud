from django.shortcuts import render, redirect, get_object_or_404

from crudapp.models import employee

from crudapp import forms


# Create your views here.

def retrieve_view(request):
    employees=employee.objects.all()   # used to get all data and then we will send to index.html page
    return render(request,'crudapp/index.html',{'employees':employees})

# insert data into table
def create_view(request):
    form=forms.employeeform()
    if request.method=='POST':
        form=forms.employeeform(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/index')
    return render(request,'crudapp/create.html',{'form':form})


# used to delete record from table
def delete_view(request, id):
    employe = get_object_or_404(employee, id=id)  # Fetch or 404 if not found
    employe.delete()  # Delete the employee
    return redirect('/index/')  # Redirect to index or your desired URL



#
# def delete_view(request, id):
#     # Fetch the employee object or raise a 404 if it doesn't exist
#     employee = get_object_or_404(Employee, id=id)
#     employee.delete()  # Delete the object
#     return redirect('your-success-url')  # Redirect after deletion




def update_view(request, id):
    employe = employee.objects.get(id=id)
    if request.method == 'POST':
        form = forms.employeeform(request.POST, instance=employe)
        if form.is_valid():
            form.save()
            return redirect('/index')  # Use redirect to navigate back to index page

    return render(request, 'crudapp/update.html', {'employe': employe})