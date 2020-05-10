from django.http import HttpResponse
from django.core import serializers
from django.core.paginator import Paginator
from django.http import JsonResponse
import json

from store.models import Product, Order

import random

def get_all_products (request):
    
    products = Product.objects.all()
    
    page_size = request.GET.get('page_size', 25)
    paginator = Paginator(products, page_size)

    page_number = request.GET.get('page_number', 1)
    page_obj = paginator.get_page(page_number)

    products_json = serializers.serialize('json', page_obj)


    return HttpResponse(products_json, content_type='application/json')



def get_product_by_id (request, pk):
    try:
        product = Product.objects.get(pk=pk)
    except:
        return HttpResponse('product not found', status=400)
    
    orders = product.items.distinct('order').values('order')

    soldWithProducts = {}

    for order in orders: 
        products_ = Order.objects.get(pk=order['order']).items.exclude(product_id=pk)
        for product_ in products_:
            soldWithProducts[product_.product_id] = {"name": product_.product.name, "count": 0}
    

    for soldProduct in soldWithProducts:
        count = Product.objects.get(pk=soldProduct).items.count()
        soldWithProducts[soldProduct]["count"] = count
  
    soretedSoldWithProducts = sorted(soldWithProducts.values(), key=lambda k: k.get('count', 0), reverse=True)
    
    response = {}
    response["product"] = {"name": product.name, "stock": product.stock, "price": product.price}
    response["bougthWithProducts"] = soretedSoldWithProducts

    return HttpResponse(json.dumps(response), content_type='application/json')



def generate_data(request):
    data = []
    for i in range(20):
        data.append({
      "model": "store.Product",
      "pk": i,
      "fields": {
        "name": "flower_%d" % i,
        "stock": random.randint(1,100),
        "price": 1
      }
    })

    for i in range(50):

        randintQuantity = random.randint(1,100)
        data.append({
        "model": "store.Order",
        "pk": i,
        "fields": {
            "order_date": '201{}-0{}-12'.format(random.randint(1,9),random.randint(1,9)),
            "quantity": randintQuantity,
            "total":  randintQuantity
        }
      })
        for y in range(random.randint(1,5)):
            data.append({
            "model": "store.OrderItem",
            "pk": i,
            "fields": {
                "product": random.randint(1,19),
                "order": random.randint(1,49),
                "quantity": randintQuantity,
                "total":  randintQuantity
            }
          })
    
    return HttpResponse(json.dumps(data), content_type='application/json')
    