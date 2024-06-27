from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CreatorViewSet, ItemViewSet, BidViewSet, MakeBidViewSet, EventViewSet

router = DefaultRouter()
router.register(r'creators', CreatorViewSet, basename='creator')
router.register(r'items', ItemViewSet, basename='item')
router.register(r'bids', BidViewSet, basename='bid')
router.register(r'user-bids', MakeBidViewSet, basename='user_bid')
router.register(r'events', EventViewSet, basename='event')
urlpatterns = router.urls

urlpatterns = [
    path('', include(router.urls)),
]