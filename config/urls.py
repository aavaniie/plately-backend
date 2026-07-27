from django.contrib import admin
from django.urls import include, path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


urlpatterns = [
    path("admin/", admin.site.urls),

    # Authentication
    path(
        "api/auth/",
        include("authentication.urls")
    ),

    path(
        "api/auth/login/",
        TokenObtainPairView.as_view(),
        name="token_obtain_pair"
    ),

    path(
        "api/auth/refresh/",
        TokenRefreshView.as_view(),
        name="token_refresh"
    ),


    # Orders
    path(
        "api/orders/",
        include("orders.urls")
    ),


    # Restaurant + Tables
    path(
        "api/",
        include("restaurant.urls")
    ),


    # Menu + Food
    path(
        "api/",
        include("menu.urls")
    ),
    
    path(
        "api/kitchen/",
        include("kitchen.urls")
    ),
]