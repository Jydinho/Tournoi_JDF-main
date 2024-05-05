
from django.shortcuts import redirect

def index(request):
    #return redirect('/api/tournois/')
    #return redirect('templates/base.html')
    return redirect('users/login')

    