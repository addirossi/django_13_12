from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from main.models import Product


def test_view(request):
    return HttpResponse('Привет, Коллеги!!!')


def index_page(request):
    template_name = 'main/index.html'
    return render(request, template_name, context={})


def products_list(request):
    template_name = 'main/list.html'
    all_products = Product.objects.all()
    return render(request, template_name, context={'products': all_products})


def product_details(request, product_id):
    template_name = 'main/details.html'
    product = get_object_or_404(Product, id=product_id)
    print(dir(request))
    print('Тестовый принт!!!!')
    return render(request, template_name, context={'product': product})
