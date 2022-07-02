from django.urls import path,include
from profiles_api import views


from rest_framework.routers import DefaultRouter


# use to configure a router used in ViewSets
router = DefaultRouter()
router.register('hello-viewset',views.HelloViewSet, base_name = 'hello-viewset')
router.register('profiles',views.UserProfileViewSet)


urlpatterns = [
    path('hello-view/',views.HelloApiView.as_view()),
    path('',include(router.urls)),
]