from django.shortcuts import render
from .forms import *
from django.http import HttpResponse
# Create your views here.
from django.views.decorators.csrf import csrf_exempt
import razorpay


def pay(request):
    if request.method=="POST":

        amount=request.POST.get('amountid')
        amount=int(amount)*100



        client = razorpay.Client(auth=('rzp_test_vr6PzGtdffw2AT','BKneYPsbQGlak3C8sPUwMWYX'))
        payment = client.order.create({'amount': amount, 'currency': 'INR', 'payment_capture': '1'})
        print(payment)



        context={'payment':payment}

        return render(request, "payment.html",{'payment':payment})

    else:
        return render(request,"payment.html")


@csrf_exempt
def success(request):
    if request.method == "POST":


        print(request.POST)
        orderid=request.POST['razorpay_order_id']
        paymentid=request.POST['razorpay_payment_id']
        siganture=request.POST['razorpay_signature']

        client = razorpay.Client(auth=('rzp_test_vr6PzGtdffw2AT', 'BKneYPsbQGlak3C8sPUwMWYX'))
        params_dict = {
            'razorpay_order_id': orderid,
            'razorpay_payment_id': paymentid ,
            'razorpay_signature': siganture
        }



        try:

                status = client.utility.verify_payment_signature(params_dict)

                return HttpResponse("payemnet succesful")


        except:


                # if there is an error while capturing payment.
                return HttpResponse(" arey paymentfail.html")
        else:
            return HttpResponse("payemnet succesful")



from django.views.generic import CreateView
from django.urls import reverse_lazy, reverse
class createfundraise(CreateView):
    template_name = 'fundraiserpost.html'
    success_url = '/'
    form_class = fundraiserform
    
    def form_valid(self, form):
        user = self.request.user
        user.save()
        form.instance.user= user
        return super().form_valid(form)

def fundraiseposts(request):
    posts = fundraiser.objects.all()
    return render(request, "fundraisepost.html",{'posts': posts})