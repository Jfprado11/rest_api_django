from django.contrib import admin

from person.models import Person


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ["id", "document_type",
                    "document", "name", "last_name", "hobbie"]
