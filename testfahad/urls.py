from django.contrib import admin
from django.urls import path, include

# ✅ لإظهار الصور من مجلد media أثناء التطوير
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),

    # ✅ الصفحة الرئيسية من تطبيق المنتجات
    path('', include('products.urls')),

    # ✅ بقية التطبيقات
    path('accounts/', include('accounts.urls')),
    path('products/', include('products.urls')),
    path('orders/', include('orders.urls')),
]

# ✅ دعم ملفات media أثناء التطوير
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
