from django.urls import path,include
from rest_framework import routers
from .views import SubscribeViewSet,UnsubscribeViewSet

app_name = 'subscriptions'
data_routers = routers.SimpleRouter()

data_routers.register(
    r"subscribe", viewset=SubscribeViewSet, basename="subscribe",
)

data_routers.register(
    r"unsubscribe", viewset=UnsubscribeViewSet, basename="unsubscribe",
)
# data_routers.register(
#     r"subscription-status/?P<email>\d+)", viewset=SubscriptionStatus
# )

urlpatterns = [
    path('user_details/', include(data_routers.urls)),
]
Cuppiee