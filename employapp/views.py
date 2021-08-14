from django.shortcuts import render
from .models import Task

# Create your views here.
def demo(request):
    employ = Task.objects.all().order_by('-id')
    if request.method == 'POST':
        name = request.POST.get('name')
        age = request.POST.get('age')
        address = request.POST.get('address')
        city = request.POST.get('city')
        state = request.POST.get('state')
        image = request.POST.get('image')
        country = request.POST.get('country')
        pincode = request.POST.get('pincode')
        code = request.POST.get('countryCode')
        mobile =request.POST.get('mobile')
        email =request.POST.get('email')
        obj = Task(name=name, age=age,address=address,city=city,state=state,zip_code=pincode,image=image,mobile=mobile,email=email,code=code)
        obj.save()
        return render(request, "registration.html", {'employ': employ})
    return render(request, 'registration.html')