from esi.models import Alliance
from esi.routes.http import dispatch


def get_alliances_alliance_id(alliance_id: int) -> Alliance:
    record = Alliance.objects.filter(id=alliance_id).first()
    if not record:
        data = dispatch(
            method="GET",
            route=f"/alliances/{alliance_id}/",
        )
        record = Alliance(
            id=alliance_id,
            **data,
        )
        record.save()
    return record
