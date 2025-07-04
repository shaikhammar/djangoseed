from django.shortcuts import render

# def home(request):
#     return render(request, 'home/home.html')

class Home:
    def home(request):
        return render(request, 'home/home.html')
    
