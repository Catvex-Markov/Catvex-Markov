from django.urls import path
from .views import HomePageView
urlpatterns=[
    path("", HomePageView.as_view(),name="home"),
    path ("post/detail/<int:pk>",DetailPageView.as_view,name="detail")
    path("post/create",CreatePageView.as_view(),name="create")

]