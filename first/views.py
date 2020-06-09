from django.shortcuts import render

# Create your views here.
def main(request):
    return render(request, 'first/main.html')

def one(request):
    return render(request, 'first/one.html')
    
def two(request):
    return render(request, 'first/two.html')
    
def three(request):
    return render(request, 'first/three.html')

def four(request):
    return render(request, 'first/four.html')

def five(request):
    return render(request, 'first/five.html')