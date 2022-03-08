from django.contrib import admin
from .models import Genre, Filmwork, GenreFilmwork, Person, PersonFilmWork


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')


class GenreFilmworkInline(admin.TabularInline):
    model = GenreFilmwork


@admin.register(Filmwork)
class FilmworkAdmin(admin.ModelAdmin):
    inlines = (GenreFilmworkInline,)
    list_display = ('title', 'type', 'creation_date',
                    'rating', 'created', 'modified')
    list_filter = ('type', 'rating')
    search_fields = ('title', 'description', 'id')


@admin.register(PersonFilmWork)
class PersonAdmin(admin.ModelAdmin):
    pass
    
    
@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    pass
