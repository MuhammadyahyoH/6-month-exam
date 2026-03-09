from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from products.models import ProductModel
from .models import Order, OrderItem  # ← only one import, remove duplicate


def basket(request):
    basket = request.session.get('basket', {})
    basket_items = []
    total = 0

    for product_id, quantity in basket.items():
        try:
            product = ProductModel.objects.get(pk=product_id)
            if product.discount:
                price = product.price * (1 - product.discount / 100)
            else:
                price = product.price
            item_total = price * quantity
            total += item_total
            basket_items.append({
                'product': product,
                'quantity': quantity,
                'item_total': item_total,
            })
        except ProductModel.DoesNotExist:
            pass

    return render(request, 'products/cart.html', {
        'basket_items': basket_items,
        'total': total,
    })


def basket_add(request, product_id):
    product = get_object_or_404(ProductModel, pk=product_id)
    basket = request.session.get('basket', {})

    if str(product_id) in basket:
        basket[str(product_id)] += 1
    else:
        basket[str(product_id)] = 1

    request.session['basket'] = basket
    messages.success(request, f'{product.title} added to basket!')
    return redirect(request.META.get('HTTP_REFERER', 'products:list'))


def basket_remove(request, product_id):
    basket = request.session.get('basket', {})
    product_id_str = str(product_id)

    if product_id_str in basket:
        del basket[product_id_str]
        request.session['basket'] = basket
        request.session.modified = True
        messages.success(request, 'Item removed!')

    return redirect('basket:detail')


def basket_update(request, product_id):
    if request.method == 'POST':
        quantity = int(request.POST.get('quantity', 1))
        basket = request.session.get('basket', {})

        if quantity > 0:
            basket[str(product_id)] = quantity
            messages.success(request, 'Basket updated!')
        else:
            if str(product_id) in basket:
                del basket[str(product_id)]
                messages.success(request, 'Item removed!')

        request.session['basket'] = basket
    return redirect('basket:detail')


def checkout(request):
    basket = request.session.get('basket', {})

    if not basket:
        messages.warning(request, 'Your basket is empty!')
        return redirect('basket:detail')

    basket_items = []
    total = 0

    for product_id, quantity in basket.items():
        try:
            product = ProductModel.objects.get(pk=product_id)
            price = product.price * (1 - product.discount / 100) if product.discount else product.price
            item_total = price * quantity
            total += item_total
            basket_items.append({
                'product': product,
                'quantity': quantity,
                'price': price,
                'item_total': item_total,
            })
        except ProductModel.DoesNotExist:
            pass

    if request.method == 'POST':
        first_name = request.POST.get('first_name', '').strip()
        last_name = request.POST.get('last_name', '').strip()
        email = request.POST.get('email', '').strip()
        phone = request.POST.get('phone', '').strip()
        country = request.POST.get('country', '').strip()
        address = request.POST.get('address', '').strip()
        apartment = request.POST.get('apartment', '').strip()
        city = request.POST.get('city', '').strip()
        state = request.POST.get('state', '').strip()
        postcode = request.POST.get('postcode', '').strip()
        notes = request.POST.get('notes', '').strip()
        company_name = request.POST.get('company_name', '').strip()

        if not all([first_name, last_name, email, phone, country, address, city, postcode]):
            messages.error(request, 'Please fill in all required fields.')
        else:
            order = Order.objects.create(
                first_name=first_name,
                last_name=last_name,
                company_name=company_name,
                country=country,
                address=address,
                apartment=apartment,
                city=city,
                state=state,
                postcode=postcode,
                phone=phone,
                email=email,
                notes=notes,
                total=total,
            )
            for item in basket_items:
                OrderItem.objects.create(
                    order=order,
                    product=item['product'],
                    quantity=item['quantity'],
                    price=item['price'],
                )

            request.session['basket'] = {}
            request.session.modified = True
            return redirect('basket:order_success')

    return render(request, 'products/checkout.html', {
        'basket_items': basket_items,
        'total': total,
    })


def order_success(request):
    return render(request, 'products/order-success.html')