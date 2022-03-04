from sys import api_version
from django.urls import path
from .Views.Home.V_home import HomePage
from .Views.V_TestSlide import TestSlide
from .Views.V_auth import LoginPage,ResignPage,LogOutPage
from .Views.Product.V_Nem import Nem
from .Views.Product.V_ChanGaGoi import ChanGaGoi
from .Views.Product.V_ThuongHieu import ThuongHieu
from .Views.Product.V_BoSuuTap import BoSuuTap
from .Views.Product.V_ProductDetail import ProductDetail
from .Views.Product.V_Card import CardProduct
from .Views.Product.V_Order import OrderProduct
from .Views.API.V_Apisession import ApiSession,ApiSession1

from .Views.TESTFILE.testfilelist import testfileList
from .Views.TESTFILE.testfiledetail import testfileDetail
app_name = 'bedlinh'
urlpatterns = [
    path('',HomePage,name='homepage'),
    path('test',TestSlide,name='testpage'),
    path('login',LoginPage,name='loginpage'),
    path('resign',ResignPage,name='resignpage'),
    path('logout',LogOutPage,name='logoutpage'),
    path('changagoi',ChanGaGoi,name='changagoipage'),
    path('nem',Nem,name='nempage'),
    path('thuonghieu/<slug:slug>',ThuongHieu,name='thuonghieupage'),
    path('bosuutap/<slug:slug>',BoSuuTap,name='bosuutappage'),
    path('sanpham/<slug:slug>',ProductDetail,name='productdetai'),
    path('card',CardProduct,name='cardpage'),
    path('order',OrderProduct,name='oderpage'),
    path('apisession',ApiSession.as_view(),name='apisession'),
    path('apisession1',ApiSession1,name='apisession1'),

    path('testfilelist',testfileList,name='testfilelist'),
    path('testfilelist/<slug:slug>',testfileDetail,name='testfiledetail'),


]