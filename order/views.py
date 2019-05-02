from django.shortcuts import render, get_object_or_404, redirect
from .extra_func import generate_ref_code
from catalog.models import Product, Category
from .models import Order
from .forms import CustomerForm
# Create your views here.


def view_cart(request):
    product_ids = request.session.get('cart', [])

    categories = Category.objects.all()

    products = Product.objects.filter(id__in=product_ids)
    total = sum(Product.objects.filter(id__in=product_ids).values_list('price', flat=True))
    form = CustomerForm

    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            ref_code = generate_ref_code()
            customer_email = form.cleaned_data['customer_email']
            order = Order.objects.create(ref_code=ref_code, customer_email=customer_email, total=float(total))

            order.products.set(products)

            request.session['cart'].clear()

            return redirect('/catalog/order/{}/'.format(ref_code))

    return render(request, 'shopping-cart.html', {'products': products, 'total': total, 'form': form,
                                                  'categories': categories})


def add_to_cart(request, product_id):
    cart = request.session.get('cart', [])

    if product_id not in cart:
        cart.append(product_id)
        request.session['cart'] = cart
        product = get_object_or_404(Product, pk=product_id)
    else:
        product = None

    return render(request, 'item-added.html', {'cart': cart, 'product': product})


def delete_from_cart(request, product_id):
    cart = request.session['cart']
    cart.remove(product_id)
    request.session['cart'] = cart
    product = get_object_or_404(Product, pk=product_id)
    return render(request, 'item-deleted.html', {'product': product})


def checkout(request, ref_code):
    order = get_object_or_404(Order, ref_code=ref_code)
    products = order.products.all()
    return render(request, 'checkout.html', {'products': products, 'ref_code': ref_code})
