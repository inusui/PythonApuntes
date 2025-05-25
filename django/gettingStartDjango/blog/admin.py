from django.contrib import admin
from .models import Post

# Register your models here.

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    """Configuracion del admin para el modelo Post"""

    readonly_fields = ('created', 'modified')
    # Mostrar los campos de fecha creada y moificadacomo solo lectura
    list_display = ('title', 'created', 'modified') # Mostrar los campos en la lista del admin (para que no salga object(1))

    date_hierarchy = 'created'  # Permite filtrar por fecha de creacion


# Esto es para que el modelo Post se pueda ver en el admin de Django
admin.site.register(Post, PostAdmin)
