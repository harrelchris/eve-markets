from esi.routes.http import dispatch
from sso.models import Token


def get_characters_character_id_location(character_id: int, token: Token) -> dict:
    return dispatch(
        method="GET",
        protected=True,
        route=f"/characters/{character_id}/location/",
        token=token,
    )
