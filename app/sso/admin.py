from django.contrib import admin

from sso.models import Token


class TokenAdmin(admin.ModelAdmin):
    pass


admin.site.register(Token, TokenAdmin)
