from django.contrib import admin

from edu_app.models import Chapter, Material


@admin.register(Chapter)
class ChapterAdmin(admin.ModelAdmin):
    list_display = ("name", "description", "preview", "owner", "created", )
    search_fields = ('name', "owner", )
    list_filter = ('owner', 'created', )


@admin.register(Material)
class MaterialAdmin(admin.ModelAdmin):
    list_display = ("name", "description", "preview", "owner", "created", )
    search_fields = ('name', "owner", )
    list_filter = ('owner', 'created', )


# @admin.register(Answer)
# class AnswerAdmin(admin.ModelAdmin):
#     list_display = ("answer", )
#
#
# @admin.register(Question)
# class QuestionAdmin(admin.ModelAdmin):
#     list_display = ("question", "material", "owner", "answer", )
#     search_fields = ("material", )
#     list_filter = ('material', 'owner', )
#
#
# @admin.register(Subscription)
# class SubscriptionAdmin(admin.ModelAdmin):
#     list_display = ("chapter", "subscriber", )
#
#
# @admin.register(Test)
# class TestAdmin(admin.ModelAdmin):
#     list_display = ("material", )

