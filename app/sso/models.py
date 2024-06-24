from django.db import models
from django.utils import timezone

from sso import services


class Token(models.Model):
    character_id = models.IntegerField()
    character_name = models.CharField(max_length=256)
    access_token = models.CharField(max_length=8192)
    expiration = models.DateTimeField()
    refresh_token = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.character_name} - {self.expiration}"

    @property
    def _is_expired(self):
        return self.expiration <= timezone.now()

    def _refresh_access_token(self):
        oauth_token = services.refresh_oauth_token(refresh_token=self.refresh_token)
        self.access_token = oauth_token["access_token"]
        self.expiration = oauth_token["expiration"]
        self.save()

    def get_access_token(self):
        if self._is_expired:
            self._refresh_access_token()
        return self.access_token
