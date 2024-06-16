import typing

from django.contrib.auth.mixins import UserPassesTestMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView

from edu_app.models import Chapter


class ChapterListView(ListView):
    """Контроллер для просмотра сущностей"""

    model = Chapter
    login_url = reverse_lazy("edu_app:chapter_list")

    def get_context_data(self, **kwargs: typing.Any) -> typing.Any:
        context = super().get_context_data(**kwargs)
        context["title"] = "Разделы"
        return context


class ChapterDetailView(DetailView):
    """Контроллер для просмотра сущности"""
    pass
    # model = Client
    #
    # def get_context_data(self, **kwargs: typing.Any) -> typing.Any:
    #     context = super().get_context_data(**kwargs)
    #     context["title"] = self.object.name
    #     return context
    #
    # def get_object(self, queryset: typing.Any = None) -> typing.Any:
    #     self.object = super().get_object(queryset)
    #     user = self.request.user
    #     if not user.is_superuser and self.object.owner != user:
    #         raise Http404("Доступ запрещен")
    #     return self.object


class ChapterCreateView(UserPassesTestMixin, CreateView):
    """Контроллер для создания сущности"""
    pass
    # model = Client
    # form_class = ClientForm
    # success_url = reverse_lazy("clients:clients_page")
    #
    # def get_context_data(self, **kwargs: typing.Any) -> typing.Any:
    #     context = super().get_context_data(**kwargs)
    #     context["title"] = "Добавление клиента"
    #     return context
    #
    # def form_valid(self, form: typing.Any) -> typing.Any:
    #     self.object = form.save()
    #     self.object.owner = self.request.user
    #     self.object.save()
    #     return super().form_valid(form)
    #



class ChapterUpdateView(UpdateView):
    """Контроллер для изменения сущности"""
    pass

    # model = Client
    # form_class = ClientForm
    #
    # def get_success_url(self) -> typing.Any:
    #     return reverse("clients:view_client", args=[self.kwargs.get("pk")])
    #
    # def get_context_data(self, **kwargs: typing.Any) -> typing.Any:
    #     context = super().get_context_data(**kwargs)
    #     context["title"] = "Обновление данных клиента"
    #     return context
    #
    # def get_object(self, queryset: typing.Any = None) -> typing.Any:
    #     self.object = super().get_object(queryset)
    #     user = self.request.user
    #     if not user.is_superuser and self.object.owner != user:
    #         raise Http404("Доступ запрещен")
    #     return self.object


class ChapterDeleteView(DeleteView):
    """Контроллер для удаления сущности"""
    pass
    # model = Client
    # success_url = reverse_lazy("clients:clients_page")
    #
    # def get_context_data(self, **kwargs: typing.Any) -> typing.Any:
    #     context = super().get_context_data(**kwargs)
    #     context["title"] = "Удаление данных клиента"
    #     return context
    #
    # def get_object(self, queryset: typing.Any = None) -> typing.Any:
    #     self.object = super().get_object(queryset)
    #     user = self.request.user
    #     if not user.is_superuser and self.object.owner != user:
    #         raise Http404("Доступ запрещен")
    #     return self.object
