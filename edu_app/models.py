from django.conf import settings
from django.db import models

from config.settings import NULLABLE


class Chapter(models.Model):
    """
    Модель Раздела
    """

    name = models.CharField(max_length=150, unique=True, verbose_name="Название")
    description = models.TextField(**NULLABLE, verbose_name="Описание")
    preview = models.ImageField(upload_to="chapter/", **NULLABLE, verbose_name="Превью")
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL, default="", on_delete=models.CASCADE, **NULLABLE, verbose_name="Владелец"
    )
    created = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")

    def __str__(self) -> str:
        return f"{self.name}"

    class Meta:
        verbose_name = "раздел"
        verbose_name_plural = "разделы"
        ordering = ['id']


class Material(models.Model):
    """
    Модель Материала
    """

    name = models.CharField(max_length=150, verbose_name="Название")
    description = models.TextField(**NULLABLE, verbose_name="Описание")
    preview = models.ImageField(upload_to="material/", **NULLABLE, verbose_name="Превью")
    url = models.CharField(max_length=150, **NULLABLE, verbose_name="Ссылка")
    course = models.ForeignKey(Chapter, on_delete=models.CASCADE, **NULLABLE, verbose_name="Раздел")
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL, default="", on_delete=models.CASCADE, **NULLABLE, verbose_name="Владелец"
    )
    created = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")

    def __str__(self) -> str:
        return f"{self.name}"

    class Meta:
        verbose_name = "материал"
        verbose_name_plural = "материалы"
        ordering = ['id']


# class Answer(models.Model):
#     """
#     Модель Ответа
#     """
#
#     answer = models.CharField(max_length=50, verbose_name="Ответ")
#     owner = models.ForeignKey(
#         settings.AUTH_USER_MODEL, default="", on_delete=models.CASCADE, **NULLABLE, verbose_name="Владелец"
#     )
#
#     def __str__(self) -> str:
#         return f"{self.answer}"
#
#     class Meta:
#         verbose_name = "ответ"
#         verbose_name_plural = "ответы"
#
#
# class Question(models.Model):
#     """
#     Модель Вопроса
#     """
#
#     question = models.CharField(max_length=150, verbose_name="Вопрос", unique=True)
#     material = models.ForeignKey(Material, on_delete=models.CASCADE, **NULLABLE, verbose_name="Материал")
#     owner = models.ForeignKey(
#         settings.AUTH_USER_MODEL, default="", on_delete=models.CASCADE, **NULLABLE, verbose_name="Владелец"
#     )
#     answer = models.OneToOneField(Answer, on_delete=models.CASCADE, **NULLABLE, related_name='correct_answer',
#                                   verbose_name="Правильный ответ")
#     choices = models.ManyToManyField(Answer, related_name='choices')
#
#     def __str__(self) -> str:
#         return f"{self.question}, {self.material}"
#
#     class Meta:
#         verbose_name = "вопрос"
#         verbose_name_plural = "вопросы"
#         ordering = ['id']
#
#
# class Test(models.Model):
#     """
#     Модель Теста
#     """
#     material = models.OneToOneField(Material, on_delete=models.CASCADE, verbose_name="Материал")
#     question = models.ManyToManyField(Question, verbose_name="Вопросы")
#     owner = models.ForeignKey(
#         settings.AUTH_USER_MODEL, default="", on_delete=models.CASCADE, **NULLABLE, verbose_name="Владелец"
#     )
#
#     def __str__(self) -> str:
#         return f"{self.material}, {self.question}"
#
#     class Meta:
#         verbose_name = "тест"
#         verbose_name_plural = "тесты"

