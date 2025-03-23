from django.contrib.auth.models import Group
from timeit import default_timer
from django.http import HttpResponse, HttpRequest
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.views import View
from django.views.generic import TemplateView
from .models import Product, Order
from .forms import ProductForm, OrderForm, GroupForm


class ShopIndexView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        products = [
            ('Laptop', 1999),
            ('Desktop', 2999),
            ('Smartphone', 999),
        ]
        context = {
            'time_running': default_timer(),
            'products': products,
        }
        return render(request, 'shopapp/shop-index.html', context=context)


class GroupsListView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        context = {
            'form': GroupForm,
            'groups': Group.objects.prefetch_related('permissions').all(),
        }
        return render(request, 'shopapp/groups-list.html', context=context)

    def post(self, request: HttpRequest) -> HttpResponse:
        form = GroupForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect(request.path)
        # return self.get(request)

class ProductDetailsView(View):
    def get(self, request: HttpRequest, pk: int) -> HttpResponse:
        product = get_object_or_404(Product,pk=pk)
        context = {
            'product': product
        }
        return render(request, 'shopapp/product-details.html', context=context)


class ProductsListView(TemplateView):
    template_name = 'shopapp/products-list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['products'] = Product.objects.all()
        return context


# def products_list(request: HttpRequest):
#     context = {
#         'products': Product.objects.all(),
#     }
#     return render(request, 'shopapp/products-list.html', context=context)


def create_product(request: HttpRequest) -> HttpResponse:
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            # name = form.cleaned_data['name']
            # price = form.cleaned_data['price']
            # description = form.cleaned_data['description']
            # Product.objects.create(**form.cleaned_data)
            form.save()
            url = reverse('shopapp:products_list')
            return redirect(url)
    else:
        form = ProductForm()
    context = {
        'form': form,
    }
    return render(request, 'shopapp/create-product.html', context=context)


def orders_list(request: HttpRequest):
    context = {
        'orders': Order.objects.select_related('user').prefetch_related('products').all(),
    }
    return render(request, 'shopapp/orders-list.html', context=context)


def create_order(request: HttpRequest) -> HttpResponse:
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            url = reverse('shopapp:orders_list')
    else:
        form = OrderForm()
    context = {
        'form': form,
    }
    return render(request, 'shopapp/create-order.html', context=context)

