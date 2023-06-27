from django.contrib import admin
from django.conf.urls.static import static
from django.urls import include, path, re_path
from quoraclone import settings 
from django.views.static import serve
from django.conf.urls import handler404
from authentication.views.error404 import error_404

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('authentication.urls')),
    path('', include('topics.urls')),
    path('', include('userprofile.urls')),
    path('', include('qna.urls')),
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
    re_path(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


handler404 = error_404
