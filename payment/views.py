import braintree
from django.shortcuts import render, redirect, get_object_or_404
from django.conf import settings
from orders.models import Order
from cart.cart import Cart
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.urls import reverse
from django.contrib import messages

# instantiate Braintree payment gateway
gateway = braintree.BraintreeGateway(settings.BRAINTREE_CONF)

@login_required
def payment_process(request):
    cart = Cart(request)
    order_id = request.session.get('order_id')
    order = get_object_or_404(Order, id=order_id)
    total_cost = order.get_total_cost()

    if request.method == 'POST':
        # retrieve nonce
        nonce = request.POST.get('payment_method_nonce', None)
        # create and submit transaction
        result = gateway.transaction.sale({
            'amount': f'{total_cost:.2f}',
            'payment_method_nonce': nonce,
            'options': {'submit_for_settlement': True}
        })

        if result.is_success:
            # mark the order as paid
            order.paid = True
            # store the unique transaction id
            order.braintree_id = result.transaction.id
            order.save()
            # launch asynchronous task
            cart.clear()
            return redirect('done')
        else:
            return redirect('canceled')
    else:
        # Check if the user is logged in
        if request.user.is_authenticated:
            # generate token
            client_token = gateway.client_token.generate()
            return render(request, 'payment/process.html', {'order': order, 'client_token': client_token})
        else:
            # User is not logged in, show a message and redirect to login page
            messages.error(request, 'Phải đăng nhập trước khi mua hàng.')
            return redirect('login')
@login_required
def payment_done(request):
    return render(request, 'payment/done.html')

@login_required
def payment_canceled(request):
    return render(request, 'payment/canceled.html')

