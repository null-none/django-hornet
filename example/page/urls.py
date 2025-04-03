from django.urls import path, re_path

from .views import CounterView

urlpatterns = [
    path(
        "/counter",
        CounterView.as_view(),
        name="counter",
    ),
]
