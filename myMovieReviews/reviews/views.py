from django.shortcuts import render
from .models import Review

# Create your views here.
def reviews_list(request):
    reviews = Review.objects.all()
    context = {"reviews": reviews}
    return render(request, 'reviews_list.html', context)

def reviews_detail(request, pk):
    review = Review.objects.get(id=pk)
    context = {"review": review}
    return render(request, 'reviews_detail.html', context)