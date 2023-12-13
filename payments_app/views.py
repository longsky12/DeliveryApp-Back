from django.shortcuts import render, redirect
import requests, json, base64, time
from django.conf import settings
from django.http import HttpResponseRedirect,JsonResponse

from rest_framework import viewsets,status
from rest_framework.response import Response

from orders_app.models import Order, CartItem, Cart

def kakaoPay(request):
    return render(request,'payments/payTest.html')

def kakaoPayLogic(request):
    _url = 'https://kapi.kakao.com/v1/payment/ready'
    _admin_key = settings.ADMIN_KEY
    _headers = {
        'Authorization': f'KakaoAK {_admin_key}',
        'Content-type': 'application/x-www-form-urlencoded;charset=utf-8',
    }

    try:
        # partner_order_id = request.GET.get('orderId')
        # order = Order.objects.get(orderId=partner_order_id)
        # user = order.userId
        # cart = order.cartId
        # cart_items = CartItem.objects.filter(cartId=cart).first()

        # total_amount = sum(item.menuId.price * item.quantity for item in cart_items)

        # _params = {
        #     'cid': 'TC0ONETIME',
        #     'partner_order_id':order.orderId,
        #     'partner_user_id':user.userId,
        #     'item_name':cart_items.menuId.name,
        #     'quantity':cart_items.quantity,
        #     'total_amount':total_amount,
        #     'vat_amount':total_amount*0.1,
        #     'tax_free_amount':'0',
        #     'approval_url':'http://127.0.0.1:8000/paysuccess',
        #     'fail_url':'http://127.0.0.1:8000/payfail',
        #     'cancel_url':'http://127.0.0.1:8000/paycancel'
        # }

        _params = {
            'cid': 'TC0ONETIME',
            'partner_order_id':'1234',
            'partner_user_id':'1234',
            'item_name':'쌀 20Kg',
            'quantity':'3',
            'total_amount':'180000',
            'vat_amount':"18000",
            'tax_free_amount':'0',
            'approval_url':'http://127.0.0.1:8000/paysuccess',
            'fail_url':'http://127.0.0.1:8000/payfail',
            'cancel_url':'http://127.0.0.1:8000/paycancel'
        }

        _res = requests.post(_url,data=_params,headers=_headers)
        print("_res:",_res)
        _result = _res.json()
        print("_result:",_result)
        next_url = _result.get('next_redirect_pc_url')
        request.session['tid'] = _result.get('tid')
        return redirect(next_url)
    except Order.DoesNotExist:
        pass

    # 'approval_url':'http://127.0.0.1:8000/payment/kakaopay?partner_order_id=1234', 

def paySuccess(request):
    _url = 'https://kapi.kakao.com/v1/payment/approve'
    _admin_key = settings.ADMIN_KEY
    _headers = {
        'Authorization': f'KakaoAK {_admin_key}',
        'Content-type': 'application/x-www-form-urlencoded;charset=utf-8',
    }
    _params = {
        'cid':'TC0ONETIME',
        'tid': request.session.get('tid'),
        'partner_order_id':'1234',
        'partner_user_id':'partner_user_id',
        'pg_token': request.GET.get('pg_token')
    }
    _res = requests.post(_url,params=_params,headers=_headers)
    _result = _res.json()
    # print(_result)

    if _result.get('msg'):
        return redirect('payments:payFail')
    else:
        return render(request,'payments/paySuccess.html',{'result':_result})

def payFail(request):
    return render(request,'payments/payFail.html')

def payCancel(request):
    return render(request,'payments/payCancel.html')


# ===================================================
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import authentication_classes, permission_classes

# TOSS PAYMENT
def index(request):
    return render(
        request,
        'payments/index.html',
    )

@authentication_classes([TokenAuthentication])
@permission_classes([])
def window(request):
    print("window request user:",request.user)
    client_key = settings.TOSS_PAYMENTS_CLIENT_KEY

    # 가장 최근에 생성된 카트를 가져옴(유저가 있어야함)
    # user_cart = Cart.objects.filter(userId=request.user).order_by('-createdDate').first()
    
    # 해당하는 카트에 들어있는 모든 cartItem을 가져옴(하드 코딩된거 user가져올수 있을떄 바꿔주기)
    cart_items = CartItem.objects.filter(cartId=4).order_by('-menuId__price')

    # 주문 번호를 가져와서 넣어주어야 하나 주문은 생성되지 않았기에 랜덤 번호 넣어줌
    # 나중에는 주문 번호 가져와서 처리하기

    # 첫번째 물품명
    first_item_name = cart_items.first().menuId.name if cart_items else None

    # 전체 금액 계산
    total_price = request.session.get('total_price')
    
    # 사용자 이름(인증이 되었으면 가져와진다.)
    user_name = request.user.username if request.user.is_authenticated else None

    return render(
        request,
        'payments/window.html',
        {
            "client_key":client_key,
            "first_item_name":first_item_name,
            # "order_id":order_id,
            "customerName":user_name,
            "total_price":total_price,
        }
    )

@authentication_classes([TokenAuthentication])
@permission_classes([])
def totalPrice(request):
    print("total request user:",request.user)
    if request.method == 'POST':
        total_price = request.POST.get('total_price')
        request.session['total_price'] = total_price
        return JsonResponse({"message":"값 전달"})
    else:
        return JsonResponse({"message":"POST 요청이 아니거나 Ajax 요청이 아님"},status=status.HTTP_400_BAD_REQUEST)


def success(request):
    orderId = request.GET.get('orderId')
    amount = request.GET.get('amount')
    paymentKey = request.GET.get('paymentKey')

    url = "https://api.tosspayments.com/v1/payments/confirm"
    secretkey = settings.TOSS_PAYMENTS_SECRET_KEY

    userpass = secretkey + ":"
    encoded_u = base64.b64encode(userpass.encode()).decode()

    headers = {
        "Authorization" : "Basic %s" % encoded_u,
        "Content-Type":"application/json"
    }

    params = {
        "orderId":orderId,
        "amount":amount,
        "paymentKey":paymentKey,
    }

    res = requests.post(url,data=json.dumps(params),headers=headers)
    resjson = res.json()
    pretty = json.dumps(resjson,indent=4)

    print(res)
    print(resjson)
    print(pretty)

    respaymentKey = resjson["paymentKey"]
    resorderId = resjson["orderId"]
    
    # rescardcom = resjson["card"]["company"]
    # company는 존재하지 않는 필드
    rescardcom = resjson["card"]

    return render(
        request,
        "payments/success.html",
        {
            "res":pretty,
            "respaymentKey":respaymentKey,
            "resorderId":resorderId,
            "rescardcom":rescardcom,
        }
    )

def fail(request):
    code = request.GET.get('code')
    message = request.GET.get('message')

    return render(
        request,
        "payments/fail.html",
        {
            "code":code,
            "message":message,
        }
    )



#=====================================
# payment ready logic, make payment inform & redirect to payment page
class PaymentViewSet(viewsets.ViewSet):
    def create(self,request):
        _url = 'https://kapi.kakao.com/v1/payment/ready'
        _admin_key = settings.ADMIN_KEY
        _headers = {
            'Authorization': f'KakaoAK {_admin_key}',
            'Content-type': 'application/x-www-form-urlencoded;charset=utf-8',
        }
        _params = {
            'cid': 'TC0ONETIME',
            'partner_order_id':'1234',
            'partner_user_id':'partner_user_id',
            'item_name':'(Coupang) iphone15 pro',
            'quantity':'1',
            'total_amount':'1750000',
            'vat_amount':'175000',
            'tax_free_amount':'0',
            'approval_url':'http://127.0.0.1:8000/paysuccess',
            'fail_url':'http://127.0.0.1:8000/payfail',
            'cancel_url':'http://127.0.0.1:8000/paycancel'
        }

        _res = requests.post(_url,params=_params,headers=_headers)
        _result = _res.json()
        print(_result)
        next_url = _result.get('next_redirect_pc_url')
        request.session['tid'] = _result.get('tid')
        # return redirect(next_url)
        return HttpResponseRedirect(next_url)

# payment approve logic
class PaymentApprovalViewSet(viewsets.ViewSet):
    def create(self,request):
        _url = 'https://kapi.kakao.com/v1/payment/approve'
        _admin_key = settings.ADMIN_KEY
        _headers = {
            'Authorization': f'KakaoAK {_admin_key}',
            'Content-type': 'application/x-www-form-urlencoded;charset=utf-8',
        }
        _params = {
            'cid':'TC0ONETIME',
            'tid': request.session['tid'],
            'partner_order_id':'1234',
            'partner_user_id':'partner_user_id',
            'pg_token': request.data.get('pg_token') 
        }
        _res = requests.post(_url,params=_params,headers=_headers)
        _result = _res.json()

        if _result.get('msg'):
            return Response({'error':'Payment approval failed'},status=400)
        else:
            return Response({'result':_result},status=200)