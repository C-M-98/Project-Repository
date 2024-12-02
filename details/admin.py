from django.contrib import admin
from .models import Styles, Skills,Education, EduStyles
# Register your models here.
class StylesAdmin(admin.ModelAdmin):
    pass

class SkillsAdmin(admin.ModelAdmin):
    pass
class AboutAdmin(admin.ModelAdmin):
    pass
class EduAdmin(admin.ModelAdmin):
    pass;
admin.site.register(Styles, StylesAdmin)
admin.site.register(Skills, SkillsAdmin)
admin.site.register(Education, AboutAdmin)
admin.site.register(EduStyles, EduAdmin)