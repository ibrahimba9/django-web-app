from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404, HttpResponse
from django.shortcuts import render

from .models import Band, Listing


def band_list(request):
    bands = Band.objects.all()
    return render(request, "listings/band_list.html", {"bands": bands})


def band_detail(request, band_id):
    try:
        band = Band.objects.get(id=band_id)
        return render(request, "listings/band_detail.html", {"band": band})
    except Band.DoesNotExist:
        # raise Http404("No Band matches the given query.")
        return HttpResponse(
            f"Oops! No Band with the id {band_id} was found.", status=404
        )


def about(request):
    return render(request, "listings/about.html")


def contact(request):
    return render(request, "listings/contact.html")


def listing_list(request):
    all_listings = Listing.objects.all()
    return render(request, "listings/listing_list.html", {"listings": all_listings})


def listing_detail(request, listing_id):
    try:
        listing = Listing.objects.get(id=listing_id)
        return render(request, "listings/listing_detail.html", {"listing": listing})
    except ObjectDoesNotExist as exc:
        return HttpResponse(
            f"Oops! No Listing with the id {listing_id} was found.", status=404
        )


def page_not_found(request):
    raise ObjectDoesNotExist
