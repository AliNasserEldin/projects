from django.urls import path

from .views import *


app_name = 'auctions'

urlpatterns = [
    path("", index, name="index"),
    path("login", login_view, name="login"),
    path("logout", logout_view, name="logout"),
    path("register", register, name="register"),
    path("create/", create, name="create"),
    path("listing/<int:id>", listing, name = 'listing'),
    path("watchlist/", watchlist, name = 'watchlist'),
    path("add_comments/<int:id>", add_comments, name = 'add_comments'),
    path("close_auction/<int:id>", close_auction, name = 'close_auction'),
    path("categories/", categories, name = 'categories'),
    path("catigorized_index/<str:category>", catigorized_index, name = 'categorized'),
]

# close_auction