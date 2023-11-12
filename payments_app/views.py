from django.shortcuts import render, redirect
import requests
from django.conf import settings
from django.http import HttpResponseRedirect

from rest_framework import viewsets
from rest_framework.response import Response

from .serializers import PaymentSerializer

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
            'approval_url':'http://127.0.0.1:8000/payment/paysuccess',
            'fail_url':'http://127.0.0.1:8000/payment/payfail',
            'cancel_url':'http://127.0.0.1:8000/payment/paycancel'
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

















# render 부분 수정이 필요 -> 목표는 REST API를 만드는것

def kakaoPay(request):
    return render(request,'payments/payTest.html')

def kakaoPayLogic(request):
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
        'approval_url':'http://127.0.0.1:8000/payment/paysuccess',
        'fail_url':'http://127.0.0.1:8000/payment/payfail',
        'cancel_url':'http://127.0.0.1:8000/payment/paycancel'
    }

    _res = requests.post(_url,data=_params,headers=_headers)
    # print(_res)
    _result = _res.json()
    # print(_result)
    next_url = _result.get('next_redirect_pc_url')
    request.session['tid'] = _result.get('tid')
    return redirect(next_url)

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
        'tid': request.session['tid'],
        'partner_order_id':'1234',
        'partner_user_id':'partner_user_id',
        'pg_token': request.GET.get('pg_token')
    }
    _res = requests.post(_url,params=_params,headers=_headers)
    _result = _res.json()
    # print(_result)

    if _result.get('msg'):
        return redirect('payments:payfail')
    else:
        return render(request,'payments/paySuccess.html',{'result':_result})

def payFail(request):
    return render(request,'payments/payFail.html')

def payCancel(request):
    return render(request,'payments/payCancel.html')