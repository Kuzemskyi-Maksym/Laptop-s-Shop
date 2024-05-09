from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

app_name = "shop"

urlpatterns = [
    path("", views.home, name="home"),  #  shop/
    path(
        "detail/<int:id>/", views.product_detail, name="product_detail"
    ),  #  shop/detail/<int:id>/
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
