from django.urls import path
from .Views.V_home import Home
from .Views.V_TestSlide import TestSlide
from .Views.V_auth import LoginPage,ResignPage,LogOutPage
from .Views.Product.V_Nem import Nem
from .Views.Product.V_ChanGaGoi import ChanGaGoi
from .Views.Product.V_ThuongHieu import ThuongHieu
from .Views.Product.V_BoSuuTap import BoSuuTap
from .Views.Product.V_ProductDetail import ProductDetail
from .Views.Product.V_Card import CardProduct
from .Views.Product.V_Order import OrderProduct

urlpatterns = [
    path('',Home,name='homepage'),
    path('test',TestSlide,name='testpage'),
    path('login',LoginPage,name='loginpage'),
    path('resign',ResignPage,name='resignpage'),
    path('logout',LogOutPage,name='logoutpage'),
    path('changagoi',ChanGaGoi,name='changagoipage'),
    path('nem',Nem,name='nempage'),
    path('thuonghieu/<slug:slug>',ThuongHieu,name='thuonghieupage'),
    path('bosuutap/<slug:slug>',BoSuuTap,name='bosuutappage'),
    path('sanpham/<slug:slug>',ProductDetail,name='productdetail'),
    path('card',CardProduct,name='cardpage'),
    path('order',OrderProduct,name='oderpage')

]