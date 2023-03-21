from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('blog/', include('blog.urls')), # blog한테 떠넘기기 !?
    path('admin/', admin.site.urls),
    path('', include('single_pages.urls'))
]
