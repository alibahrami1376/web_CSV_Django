from django.urls import path
from projects.views import projects_list, project_detail

app_name = "projects"

urlpatterns = [
    path("", projects_list, name="projects_list"),
    path("category/<str:category_slug>/", projects_list, name="projects_by_category"),
    path("<str:project_slug>/", project_detail, name="project_detail"),
    path("id/<int:project_id>/", project_detail, name="project_detail_by_id"),
]
