from django.urls import path, re_path

from .views import CounterView, FormsView, ExampleView

urlpatterns = [
    path(
        "/counter",
        CounterView.as_view(),
        name="counter",
    ),
    path(
        "/forms",
        FormsView.as_view(),
        name="forms",
    ),
    path(
        "/example",
        ExampleView.as_view(),
        name="example",
    ),
]
