from django.contrib import admin
from django.conf.urls import include
from django.urls import path
from rest_framework import routers
from levelupapi.views import register_user, login_user, GameTypeView, EventView, GameView, EventDetailView, GamerView

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'gametypes', GameTypeView, 'gametype')
router.register(r'events', EventView, 'event')
router.register(r'games', GameView, 'game')

urlpatterns = [
    path('register', register_user),
    path('login', login_user),
    path('admin/', admin.site.urls),
    path('events/<int:pk>/', EventDetailView.as_view(), name='event-detail'),
    path('gamers/by_user', GamerView.as_view({'get': 'by_user'}), name='gamer-by-user'),
    path('', include(router.urls)),
]
