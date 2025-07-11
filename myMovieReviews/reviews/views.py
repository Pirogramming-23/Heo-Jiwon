from django.shortcuts import render

# Create your views here.
def reviews_list(request):
    return render(request, 'reviews_list.html')