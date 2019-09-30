from django.contrib import admin
from django.conf.urls import url, include
from django.conf import settings
from django.conf.urls.static import static
import jobs.views

urlpatterns = [
    url('admin/', admin.site.urls),
    url('', jobs.views.home, name='home'),
    url('blog/', include('blog.urls')),
        ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
