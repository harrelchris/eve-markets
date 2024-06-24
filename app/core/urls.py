from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from django.views import defaults

admin.site.index_title = "Site administration"
admin.site.name = "Django Admin"
admin.site.site_header = "Django administration"
admin.site.site_title = "Django site admin"

urlpatterns = [
    path("", include("public.urls"), name="public"),
    path("admin/", admin.site.urls),
    path("dashboard/", include("dashboard.urls"), name="dashboard"),
    path("sso/", include("sso.urls"), name="sso"),
]

if settings.DEBUG:
    urlpatterns.extend(
        [
            path("__debug__/", include("debug_toolbar.urls")),
            path(
                "400/",
                defaults.bad_request,
                kwargs={"exception": Exception("Bad Request")},
            ),
            path(
                "403/",
                defaults.permission_denied,
                kwargs={"exception": Exception("Permission Denied")},
            ),
            path(
                "404/",
                defaults.page_not_found,
                kwargs={"exception": Exception("Not Found")},
            ),
            path("500/", defaults.server_error),
        ],
    )
    urlpatterns.extend(static(settings.STATIC_URL, document_root=settings.STATIC_ROOT))
