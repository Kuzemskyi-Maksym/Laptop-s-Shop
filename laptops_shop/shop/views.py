from django.shortcuts import get_object_or_404
from django.shortcuts import render
from .models import Product
from . import choises


def home(request):
    products = Product.objects.all()

    # paginator = Paginator(products, 36)
    # page_request_variable = "page"
    # page = request.GET.get(page_request_variable, 1)
    # try:
    #     products = paginator.page(page)
    # except PageNotAnInteger:
    #     products = paginator.page(1)
    # except EmptyPage:
    #     products = paginator.page(1)
    context = {
        "title": "Online Shop",
        "products": products,
        # "page_request_variable": page_request_variable,
        "producers": choises.BRAND,
        "processors": choises.PROCESSOR,
        "screen_coatings": choises.SCREEN_COATING,
        "screen_diagonals": choises.SCREEN_DIAGONAL,
        "screen_resolutions": choises.SCREEN_RESOLUTION,
        "rams": choises.RAM,
        "processor_cores": choises.PROCESSOR_CORES,
        "ssd_scopes": choises.SSD_SCOPE,
        "oss": choises.OS,
        "video_card_types": choises.VIDEO_CARD_TYPE,
        "colors": choises.COLOR,
        "additionallyes": choises.ADDITIONALLY,
    }
    return render(request, "home.html", context)


def product_detail(request, id=None):
    instance = get_object_or_404(Product, id=id)
    context = {"title": instance.name, "object": instance}
    return render(request, "product_detail.html", context)
