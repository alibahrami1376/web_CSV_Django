from django.contrib.sitemaps import Sitemap
from projects.models import Projects


class ProjectSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.5

    def items(self):
        return Projects.objects.filter(status="completed")

    def lastmod(self, obj):
        return obj.published_date
