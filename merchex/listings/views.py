from django.http import HttpResponse
from django.shortcuts import render

from .models import Band, Listing


def hello(request):
    bands = Band.objects.all()
    list_elements: str = ""
    for band in bands:
        list_elements += "<li>{}</li>".format(band.name)

    return HttpResponse(
        f"""
        <h1>Hello Merchex</h1>
        <p> My favorite bands are the following:<p>
        <ul>{list_elements}<ul>
    """
    )


def about(request):
    return HttpResponse("<h1>À propos</h1> <p>Nous adorons merch !</p>")


def contact(request):
    return HttpResponse(
        "<h1>Contact us</h1> <p>Pour nous contacter n'hésitez pas à nous joindre sur l'adresse suivante : <strong>contact@merchex.com</strong></p>"
    )


def listings(request):
    all_listings = Listing.objects.all()
    list_elements: str = ""
    for listing in all_listings:
        list_elements += "<li>{}</li>".format(listing.title)
    return HttpResponse(
        f"""
        <h1>Liste des annonces</h1>
        <ul>
            {list_elements}
        </ul>
    """
    )
