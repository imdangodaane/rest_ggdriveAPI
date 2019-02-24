from django.urls import path, include
from snippets import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'snippets', views.SnippetViewSet)

urlpatterns = [
    # path('snippets/', views.snippet_list),
    # path('snippets/<int:pk>/', views.snippet_detail),
    path('', include(router.urls))
]