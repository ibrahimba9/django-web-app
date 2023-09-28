from django.core.exceptions import ObjectDoesNotExist
from django.core.mail import send_mail
from django.http import Http404, HttpResponse
from django.shortcuts import render, redirect
from setuptools._distutils.command.install_data import install_data

from .forms import ContactUsForm, BandForm, ListingForm
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


def band_create(request):
    if request.method == "POST":
        form = BandForm(request.POST)
        if form.is_valid():
            band = form.save()
            return redirect("band-detail", band.id)
    else:
        form = BandForm()
    return render(request, "listings/band_create.html", {"form": form})


def band_update(request, band_id):
    band = Band.objects.get(id=band_id)
    if request.method == "POST":
        form = BandForm(request.POST, instance=band)
        if form.is_valid():
            form.save()
            return redirect("band-detail", band.id)
    else:
        form = BandForm(instance=band)
    return render(request, "listings/band_update.html", {"form": form})


def about(request):
    return render(request, "listings/about.html")


def contact(request):
    if request.method == "POST":
        form = ContactUsForm(request.POST)
        if form.is_valid():
            send_mail(
                subject=f'Message from {form.cleaned_data["name"] or "anonyme"} via MerchEx Contact Us form',
                message=form.cleaned_data["message"],
                from_email=form.cleaned_data["email"],
                recipient_list=["admin@merchex.xyz"],
            )
            return redirect("email-sent")
    else:
        form = ContactUsForm()
    return render(request, "listings/contact.html", {"form": form})


def email_sent(request):
    return render(request, "listings/email_sent.html")


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


def listing_create(request):
    if request.method == "POST":
        form = ListingForm(request.POST)
        if form.is_valid():
            listing = form.save()
            return redirect("listing-detail", listing.id)
    else:
        form = ListingForm()
    return render(request, "listings/listing_create.html", {"form": form})


def listing_update(request, listing_id):
    listing = Listing.objects.get(id=listing_id)
    if request.method == "POST":
        form = ListingForm(request.POST, instance=listing)
        if form.is_valid():
            form.save()
            return redirect("listing-detail", listing.id)
    else:
        form = ListingForm(instance=listing)
    return render(request, "listings/listing_update.html", {"form": form})


def page_not_found(request):
    raise ObjectDoesNotExist
