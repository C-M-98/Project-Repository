
from django.urls import path
from .views import HomePage, Qualifications 
from django.conf.urls.static import static
from django.conf import settings

app_name = 'details'

urlpatterns = [
    path('', HomePage.as_view(), name="index"),
    path('about/', Qualifications.as_view(), name="about")
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)