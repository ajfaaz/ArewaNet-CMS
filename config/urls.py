from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path


urlpatterns = [
    path("admin/", admin.site.urls),
    # Modules
    path("about/", include("apps.about.urls")),
    path("programs/", include("apps.programs.urls")),
    path("projects/", include("apps.projects.urls")),
    path("gallery/", include("apps.gallery.urls")),
    path("blog/", include("apps.blog.urls")),
    path("donate/", include("apps.donations.urls")),
    path("volunteer/", include("apps.volunteers.urls")),
    path("contact/", include("apps.contact.urls")),
    path("", include("apps.website.urls")),
    path(
        "builder/",
        include("apps.builder.urls"),
    ),
    path("cms/", include("apps.cms.urls")),
    path("/cms/pages/", include("apps.pages.cms_urls")),
    path("/cms/menus/", include("apps.website.cms_urls")),
    # Core page slugs and home page must come last so they do not
    # swallow reserved paths like /cms/.
    path("", include("apps.core.urls")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
