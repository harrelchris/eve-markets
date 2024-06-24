from esi.models import Character
from esi.routes.http import dispatch


def get_characters_character_id(character_id: int) -> Character:
    record = Character.objects.filter(id=character_id).first()
    if not record:
        data = dispatch(
            method="GET",
            route=f"/characters/{character_id}/",
        )
        record = Character(
            id=character_id,
            **data,
        )
        record.save()
    return record
