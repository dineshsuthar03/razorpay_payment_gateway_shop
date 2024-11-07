# from django.shortcuts import render

# # Create your views here.
# import os
# import razorpay
# from django.shortcuts import render, redirect
# from django.http import JsonResponse
# from django.conf import settings

# # Initialize Razorpay client
# razorpay_client = razorpay.Client(auth=(settings.RAZORPAY_KEY_ID, settings.RAZORPAY_SECRET_KEY))

# def index(request):
#     return render(request, 'payments/index.html')

# def create_checkout_session(request):
#     if request.method == "POST":
#         product_id = request.POST.get('product_id')
#         quantity = int(request.POST.get('quantity', 1))
#         amount = int(float(request.POST.get('amount')) * 100)  # Razorpay expects amount in paise (1 INR = 100 paise)

#         # Create order with Razorpay
#         order = razorpay_client.order.create({
#             'amount': amount,
#             'currency': 'INR',
#             'payment_capture': 1
#         })

#         # Get the order ID and create a session
#         order_id = order['id']
#         return JsonResponse({'id': order_id})

# def success(request):
#     return render(request, 'payments/success.html')

# def cancel(request):
#     return render(request, 'payments/cancel.html')






import razorpay
from django.conf import settings
from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

client = razorpay.Client(auth=(settings.RAZORPAY_KEY_ID, settings.RAZORPAY_SECRET_KEY))

def index(request):
    return render(request, 'payments/index.html')

@csrf_exempt  # Since you're using AJAX for POST request, mark this route with csrf_exempt
def create_checkout_session(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        product_id = data.get('product_id')
        quantity = data.get('quantity', 1)
        amount = data.get('amount')  # Total amount for the order in paise

        order_data = {
            'amount': amount,
            'currency': 'INR',
            'receipt': f'order_rcptid_{product_id}',
            'payment_capture': 1
        }

        try:
            order = client.order.create(data=order_data)
            return JsonResponse({'id': order['id']})
        except Exception  as e:
            print(f'error: str{e}')
            return JsonResponse({'error': str(e)}, status=400)
    return JsonResponse({'error': 'Invalid request'}, status=400)

def success(request):
    razorpay_payment_id = request.GET.get('razorpay_payment_id')
    razorpay_order_id = request.GET.get('razorpay_order_id')

    # You can verify payment here, if necessary.
    return render(request, 'payments/success.html', {'razorpay_payment_id': razorpay_payment_id, 'razorpay_order_id': razorpay_order_id})

def cancel(request):
    return render(request, 'payments/cancel.html')







