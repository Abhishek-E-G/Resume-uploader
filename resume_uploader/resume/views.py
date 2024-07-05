from django.shortcuts import render,redirect
from. models import Candidate
# Create your views here.
def index(request):
    return render(request,"index.html")

def upload_resume(request):
    if request.method == 'POST':
        nam = request.POST['name']
        email1 = request.POST['email']
        phone1 = request.POST['phone']
        resume1 = request.FILES['resume']

        if Candidate.objects.filter(email=email1).exists():
            error_message = "Email address already exists"
            return render(request,"index.html",{'error_message':error_message})

        
        candidate = Candidate(name=nam, email=email1, phone=phone1, resume=resume1)
        candidate.save()

        return redirect('success')  

    return render(request, 'index.html')


def success(request):
    candidates = Candidate.objects.all() 
    return render(request, 'success.html', {'candidates': candidates})