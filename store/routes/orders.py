from django.http import HttpResponse
from django.core import serializers
from django.core.paginator import Paginator

from store.models import Order, Product


def get_all_orders (request):
    orders = Order.objects.all()
    
    page_size = request.GET.get('page_size')
    paginator = Paginator(orders, page_size)

    page_number = request.GET.get('page_number')
    page_obj = paginator.get_page(page_number)

    orders_json = serializers.serialize('json', page_obj)


    return HttpResponse(orders_json, content_type='application/json')
