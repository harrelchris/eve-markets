from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView

from esi.routes.alliance import get_alliances_alliance_id
from esi.routes.character import get_characters_character_id
from esi.routes.corporation import get_corporations_corporation_id


class IndexView(LoginRequiredMixin, TemplateView):
    template_name = "dashboard/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        character = get_characters_character_id(
            character_id=self.request.user.id,
        )
        corporation = get_corporations_corporation_id(
            corporation_id=character.corporation_id,
        )
        alliance = get_alliances_alliance_id(
            alliance_id=character.alliance_id,
        )
        context["character"] = character
        context["corporation"] = corporation
        context["alliance"] = alliance
        return context


class SettingsView(TemplateView):
    template_name = "dashboard/settings.html"
