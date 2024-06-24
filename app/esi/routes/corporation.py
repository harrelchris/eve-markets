from esi.models import Corporation
from esi.routes.http import dispatch


def get_corporations_corporation_id(corporation_id: int) -> Corporation:
    record = Corporation.objects.filter(id=corporation_id).first()
    if not record:
        data = dispatch(
            method="GET",
            route=f"/corporations/{corporation_id}/",
        )
        record = Corporation(
            id=corporation_id,
            **data,
        )
        record.save()
    return record
