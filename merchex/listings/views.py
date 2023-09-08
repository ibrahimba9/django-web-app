from django.http import HttpResponse
from django.shortcuts import render

from .models import Band, Listing


def hello(request):
    bands = Band.objects.all()
    return render(request, "listings/hello.html", {"bands": bands})


def about(request):
    return render(request, "listings/about.html")


def contact(request):
    return render(request, "listings/contact.html")


def listings(request):
    all_listings = Listing.objects.all()
    list_elements: str = ""
    return render(request, "listings/listings.html", {"listings": all_listings})
