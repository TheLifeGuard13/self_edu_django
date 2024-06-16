from django.urls import path

from edu_app.apps import EduAppConfig
from edu_app.views import ChapterListView, ChapterDetailView, ChapterCreateView, ChapterUpdateView, ChapterDeleteView

app_name = EduAppConfig.name

urlpatterns = [
    path("", ChapterListView.as_view(), name="chapter_list"),
    path("view_chapter/<int:pk>/", ChapterDetailView.as_view(), name="view_chapter"),
    path("add_chapter/", ChapterCreateView.as_view(), name="add_chapter"),
    path("update_chapter/<int:pk>/", ChapterUpdateView.as_view(), name="update_chapter"),
    path("delete_chapter/<int:pk>/", ChapterDeleteView.as_view(), name="delete_chapter"),
]
