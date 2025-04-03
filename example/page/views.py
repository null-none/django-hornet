from hornet.views import HornetlView


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
