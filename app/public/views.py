from django.views.generic import TemplateView

from public.mixins import LoggedInRedirectMixin


class IndexView(LoggedInRedirectMixin, TemplateView):
    template_name = "public/index.html"
