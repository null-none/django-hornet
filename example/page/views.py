from hornet.views import HornetlView

from .forms import ExampleForm


class CounterView(HornetlView):
    template_name = "counter.html"
    component_name = "counter"

    def get(self, request, *args, **kwargs):
        return self.render_to_component(self.html)

    def post(self, request, *args, **kwargs):
        action = request.POST.get("action")
        if action == "increment":
            self.component.increment()
        elif action == "decrement":
            self.component.decrement()
        return self.update_to_component()


class FormsView(HornetlView):
    template_name = "forms.html"
    component_name = "forms"

    def get(self, request, *args, **kwargs):
        return self.render_to_component()

    def post(self, request, *args, **kwargs):
        form = ExampleForm(self.request.POST)
        form.is_valid()
        self.state["form"] = form
        return self.update_to_component()


class ExampleView(HornetlView):
    template_name = "example.html"
    component_name = "example"

    def get(self, request, *args, **kwargs):
        return self.render_to_component()

    def post(self, request, *args, **kwargs):
        return self.update_to_component()
