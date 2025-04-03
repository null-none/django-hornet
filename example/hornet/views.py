from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import render_to_string
from .component_manager import ComponentManager


def counter(request):
    manager = ComponentManager(request)
    component = manager.load_component("counter")

    html = render_to_string("components/counter.html", component.__dict__)
    return render(request, "hornet.html", {"component_html": html})


def update_component(request, name):
    manager = ComponentManager(request)
    component = manager.load_component(name)
    state = component.__dict__
    if "increment" in request.POST["action"]:
        state["count"] = int(state["count"]) + 1
    elif "decrement" in request.POST["action"]:
        state["count"] = int(state["count"]) - 1
    manager.save_component(name, component)
    html = render_to_string(f"components/{name}.html", state)
    return HttpResponse(html)
