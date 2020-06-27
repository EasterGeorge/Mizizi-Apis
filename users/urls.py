from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('api/firstaid/create', views.FirstAidListCreate.as_view() ),
    path('api/firstaid/list', views.FirstAidList.as_view() ),
    path('api/user/register', views.MiziziUserListCreate.as_view() ),
    path('api/user/list', views.MiziziUserList.as_view() ),

]
if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)