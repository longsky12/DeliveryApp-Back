from django.shortcuts import render, redirect
import requests
import json
from django.conf import settings

# Create your views here.


# def payReadyAPIView(request):
#     if request.method == "POST":
#         URL = 'https://kapi.kakao.com/v1/payment/ready'
#         headers = {
#             "Authorization": "KakaoAK " + ADMIN_KEY,
#             "Content-type": "application/x-www-form-urlencoded;charset=utf-8",
#         }
#         params = {
#             "cid": "TC0ONETIME",             # 테스트용 코드
#             "partner_order_id": "123",    # 주문 번호
#             "partner_user_id": "123",     # 유저 아이디
#             "item_name": "치킨",          # 구매 물품 이름
#             "quantity": "1",           # 구매 수량
#             "total_amount": "15000",   # 구매 물품 가격
#             "tax_free_amount": "0",    # 구매 물품 비과세
#             "approval_url": "https://developers.kakao.com/success",
#             "cancel_url": "https://developers.kakao.com/cancel",
#             "fail_url": "https://developers.kakao.com/fail",
#         }

#         res = requests.post(URL, headers=headers, params=params)
#         tid = res.json().get('tid')
#         request.session['tid'] = tid      # 결제 승인시 사용할 tid 세션에 저장
#         next_url = res.json().get('next_redirect_app_url')      # 결제 페이지로 넘어갈 url 저장
#         return redirect(next_url)

#     return render(request, 'payments/payTest.html')

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
    # 'approval_url':'http://127.0.0.1:8000/payment/kakaopay?partner_order_id=1234', 
    _res = requests.post(_url,params=_params,headers=_headers)
    # print(_res)
    _result = _res.json()
    # print(_result)
    next_url = _result.get('next_redirect_pc_url')
    request.session['tid'] = _result.get('tid')
    return redirect(next_url)


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
    print(_result)

    if _result.get('msg'):
        return redirect('payments:payfail')
    else:
        return render(request,'payments/paySuccess.html',{'result':_result})




def payFail(request):
    return render(request,'payments/payFail.html')

def payCancel(request):
    return render(request,'payments/payCancel.html')

