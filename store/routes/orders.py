from django.http import HttpResponse
from django.core import serializers
from django.core.paginator import Paginator
from django.shortcuts import render


from store.models import Order, Product


def get_all_orders (request):
    orders = Order.objects.all()
    
    page_size = request.GET.get('page_size', 25)
    paginator = Paginator(orders, page_size)

    page_number = request.GET.get('page_number', 1)
    page_obj = paginator.get_page(page_number)

    orders_json = serializers.serialize('json', page_obj)


    return HttpResponse(orders_json, content_type='application/json')


def order_detail(request, pk):

    order = Order.objects.get(pk=pk)

    items = order.items.all()

    context = {

        "order": order,

        "items": items,

    }

    return render(request, "order_detail.html", context)