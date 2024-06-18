from django.contrib import admin
from .models import Category, Difficulty, Moves
# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    ...

class DifficyltyAdmin(admin.ModelAdmin):
    ...

class MovesAdmin(admin.ModelAdmin):
    ...

admin.site.register(Category, CategoryAdmin)
admin.site.register(Difficulty, DifficyltyAdmin)
admin.site.register(Moves, MovesAdmin)