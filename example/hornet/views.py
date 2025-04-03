from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import render_to_string
from .component_manager import ComponentManager


def hornet(request):
    manager = ComponentManager(request)
    component = manager.load_component("counter")

    html = render_to_string("components/counter.html", component.__dict__)
    return render(request, "hornet.html", {"component_html": html})


def update_component(request, name):
    manager = ComponentManager(request)
    component = manager.load_component(name)
    for key in request.POST:
        method = getattr(component, key, None)
        if callable(method):
            method()
    manager.save_component(name, component)
    html = render_to_string(f"components/{name}.html", component.__dict__)
    return HttpResponse(html)
