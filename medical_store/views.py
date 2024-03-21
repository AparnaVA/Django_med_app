from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
def signup_page(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})


from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login 

def login_page(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})


from django.contrib.auth.decorators import login_required
@login_required(login_url='/login/')
def welcome(request):
     return render(request,'welcome.html')



from .forms import ProductForm
@login_required(login_url='/login/')
def medicine_create(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('retrievemedicine')
    else:
        form =ProductForm()
    return render(request, 'create.html', {'form': form})



from .models import medicine
@login_required(login_url='/login/')
def medicine_read(request):
    medicine_list=medicine.objects.all()
    return render(request,'retrieve.html',{'medicine_list':medicine_list})
    
    


@login_required(login_url='/login/')
def medicine_update(request, pk):
    product = medicine.objects.get(pk=pk)
    if request.method == 'POST':
        form = ProductForm(request.POST,instance=product)
        if form.is_valid():
            form.save()
            return redirect('retrievemedicine')
    else:
        form =ProductForm(instance=product)           
    return render(request, 'update.html', {'form': form})



@login_required(login_url='/login/')
def medicine_delete(request,pk):
    product=medicine.objects.get(pk=pk)  
    if request.method == 'POST':
        product.delete()
        return redirect('retrievemedicine')
    
    return render(request,'delete.html',{'product':product})




@login_required(login_url='/login/')
def search(request):
    if request.method=="GET":
        search=request.GET.get('search','')
        data=medicine.objects.all().filter(name__istartswith=search).values()
        if not search:
            message = "Please enter a search."
            return render(request, 'searchbar.html', {'message': message})
        if data:
            return render(request, 'searchbar.html', {'data': data})
        else:
            return render(request, 'searchbar.html', {'message': 'Result not found for ','search': search})



from django.contrib.auth import logout
@login_required(login_url='/login/')
def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('login')

    context = {
        'user': request.user
    }

    return render(request, 'logout.html', context)


