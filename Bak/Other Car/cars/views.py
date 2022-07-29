from django.shortcuts import render, redirect
from django.urls import reverse
from . forms import ReviewForm


# Create your views here.
def rental_review(req):
    if req.method == 'POST':
        form = ReviewForm(req.POST)

        if form.is_valid():
            form.save()
            return redirect(reverse('cars:thanks'))
        else:
            return render(req, 'cars/review.html', context={'form': form})
    else:
        form = ReviewForm()
        return render(req, 'cars/review.html', context={'form': form})


def thank_you(req):
    return render(req, 'cars/thank_you.html')
