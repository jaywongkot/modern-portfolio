from django.contrib import admin
from .models import Project, Category


# class ProjectAdmin(admin.ModelAdmin):
#     pass


# class CategoryAdmin(admin.ModelAdmin):
#     pass


admin.site.register(Category)
admin.site.register(Project)
