from django.apps import apps
from django.views.generic.base import TemplateView


class HomeView(TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context["app_list"] = ["polls", "books"]
        dict_verbose = dict()
        for app in apps.get_app_configs():
            if "site-packages" not in app.path:
                dict_verbose[app.label] = app.verbose_name
        context["verbose_dict"] = dict_verbose
        return context
