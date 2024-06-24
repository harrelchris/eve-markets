import json
import urllib.request

from sso.models import Token

ESI_DOMAIN = "https://esi.evetech.net"
ESI_VERSION = "latest"
ESI_DATASOURCE = "tranquility"


def dispatch(method: str, route: str, protected: bool = False, token: Token = None):
    route = route.strip("/")
    url = f"{ESI_DOMAIN}/{ESI_VERSION}/{route}/?datasource={ESI_DATASOURCE}"

    headers = {}
    if protected:
        headers["Authorization"] = f"Bearer {token.get_access_token()}"

    request = urllib.request.Request(
        headers=headers,
        method=method,
        url=url,
    )
    response = urllib.request.urlopen(request)
    content = response.read()
    return json.loads(content)
