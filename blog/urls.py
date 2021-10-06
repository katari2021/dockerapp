from django.urls import path
from . import views
from . import restapi as restapi_views


app_name = 'blog'

urlpatterns = [
     path(r'getpost', restapi_views.RestApiViewSet.as_view({'get': 'display_post'}), name='getpost')
]