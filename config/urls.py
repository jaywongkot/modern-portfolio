from django.conf import settings  # new
from django.conf.urls.static import static  # new
from django.contrib import admin
from django.urls import path, include  # new

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('pages.urls')),  # new
    path('projects/', include('portfolio.urls')),  # new
    path('blog/', include('blog.urls')),  # new
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)  # new
