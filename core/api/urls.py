from rest_framework import routers

from .views import NewsViewSet


router = routers.DefaultRouter()

router.register(r'news', NewsViewSet, base_name='news')

urlpatterns = router.urls
