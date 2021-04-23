from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [



    path('online-supermarket.com/', include('store.urls', namespace='store')),
    path('about/', include('webdes.urls', namespace='webdes')),
    path('orders/', include('orders.urls', namespace='orders')),
    path('coupons/', include('coupons.urls', namespace='coupons')),
    path('cart/', include('cart.urls', namespace='cart')),
    path('admin/', admin.site.urls),


    # path('payment/', include('payment.urls', namespace='payment')),








]













if settings.DEBUG:
	urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
	urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
admin.site.index_title = 'Online-Supermarket'
admin.site.site_title = 'Online-Supermarket'
admin.site.site_header = 'Online-Supermarket'