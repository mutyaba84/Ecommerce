from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.template.loader import get_template
from django.shortcuts import render
from django.template import Context
import stripe

stripe.api_key = settings.STRIPE_SECRET_KEY

# Create your views here.
@login_required(login_url='/accounts/login/')
def checkout(request):
    publishKey = settings.STRIPE_PUBLISHABLE_KEY
    customer_id = request.user.userstripe.stripe_id

    if request.method =='POST':
        token = request.POST.get('stripeToken')
        try:
         customer = stripe.Customer.retrieve(customer_id)
         charge = stripe.Charge.create(
          amount=1000, # $15.00 this time
          currency="gbp",
          customer=customer,
          statement_descriptor="Custom descriptor",
          capture=False,
          metadata={"order_id": 6735},
          description='Example',
          source=token,
         )
         stripe.Product.create(
          name='T-shirt',
          description='Comfortable cotton t-shirt',
          attributes=['size', 'gender']
         )

          # Previously stored, then retrieved
            
         
          
        except stripe.error.CardError as e:
         pass
    context = {'publishKey': publishKey}
    template = 'checkout.html'
    return render(request,template,context)




