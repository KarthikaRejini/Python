from django.urls import path
from . import views
app_name='ecommerceapp'
urlpatterns = [

    path('',views.Allproductcat,name='Allproductcat'),
    path('<slug:c_slug>/',views.Allproductcat,name='product_by_category'),
    path('<slug:c_slug>/<slug:product_slug>/',views.ProDetail,name='prodCatdetail')

]
