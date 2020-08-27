from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'pages/index.html')

def admin_login(request):
    return render(request, 'pages/admin_login.html')