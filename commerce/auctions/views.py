from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import *
from .models import *
from django.contrib.auth.decorators import login_required

from .models import User

def index(request):
    all_active_listings = Listing.objects.filter(is_active = True)
    return render(request, "auctions/index.html",
                  {
                      "listings" : all_active_listings,
                  })


def login_view(request):
    if request.method == "POST":

        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("auctions:index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("auctions:index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("auctions:index"))
    else:
        return render(request, "auctions/register.html")

@login_required
def create(request):
    if request.method == "POST":
        form = CreateListing(request.POST)
        if form.is_valid():
            id = request.user.id
            user = User.objects.get(id = id)
            starting = form.cleaned_data["starting_bid"]
            listing = Listing(title = form.cleaned_data["title"], image=form.cleaned_data["image"],description = form.cleaned_data["description"],starting = starting, price = starting)
            listing.save()
            listing.user.add(user)
        return HttpResponseRedirect(reverse("auctions:index"))
    return render(request,"auctions/create.html",{
        "form": CreateListing() 
    })



@login_required
def listing(request,id):
    user = User.objects.get(pk = request.user.pk)
    watch_lists = user.watchlist.all()
    if request.method == 'GET':
        listing = Listing.objects.get(id = id)
        form = BidForm(min_value = listing.price)
        in_watchlist = False
        if watch_lists:
            for item in watch_lists:
                if item.id == listing.id:
                    in_watchlist = True
        is_owner = False
        if listing.user.id == user.id:
            is_owner = True
        return render(request,'auctions/listing.html',{
            'listing' : listing,
            'form' : form,
            'in_watchlist' : in_watchlist,
            'is_owner' : is_owner, 
        })
    elif request.method == 'POST':
        listing = Listing.objects.get(id = id)
        bid_price = request.POST.get('bid')
        if bid_price:
            bid = Bid.objects.create(cash = bid_price, user=user)
            # bid.user.add(user)
            listing.bids.add(bid)
            all = listing.bids.all()
            for i in all:
                if i.cash > listing.starting:
                    listing.price = i.cash
            listing.save()
        in_watchlist = request.POST.get('in_watchlist')
        listing = Listing.objects.filter(id=id)
        if in_watchlist == 'remove from watchlist':
            user.watchlist.remove(id)
            return redirect(reverse('auctions:listing', args = [id]))
        elif in_watchlist == 'add to watchlist': 
            user.watchlist.add(id)
            return redirect(reverse('auctions:listing', args = [id]))
        return redirect(reverse('auctions:listing', args = [id]))


@login_required
def watchlist(request):
    if request.method == 'GET':
        user = User.objects.get(pk=request.user.pk)
        watchlist = user.watchlist.all()
        return render(request, 'auctions/watchlist.html', {'watchlist': watchlist})


def close_auction(request,id):
    if request.method == 'POST':
        close = request.POST.get('close')
        if close:
            listing = Listing.objects.get(id = id)
            listing.is_active = False
            try: 
                highest_bid = listing.bids.latest('id')
                winner = highest_bid.user
                listing.winner = winner
                listing.save()
            except Bid.DoesNotExist:
                listing.save()
    return redirect(reverse('auctions:index'))


def add_comments(request,id):
    comment_content = request.POST.get('comment')
    user = User.objects.get(pk = request.user.pk)
    comment = Comment.objects.create(content=comment_content,writer=user)
    # comment.save()
    # comment.writer.add(user)
    Listing.objects.get(id = id).comments.add(comment)
    return redirect(reverse('auctions:listing', args=[id]))


def categories(request):
    categories = list(Listing.AUCTION_CATEGORIES)
    return render(request,'auctions/categories.html',{
        'categories' : categories,
    })

def catigorized_index(request,category):
    all_active_listings = Listing.objects.filter(is_active = True, category = category.upper())
    return render(request, "auctions/index.html",
                  {
                      "listings" : all_active_listings,
                  })






        




