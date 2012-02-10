from django.contrib import admin
from main.models import Author, Article, Comment, Etiquette

class AuthorAdmin(admin.ModelAdmin):
	list_display = ('name', 'lastname', 'birthdate',)
	search_fields = ('name',)

class ArticleAdmin(admin.ModelAdmin):
	list_display = ('title', 'author', 'body', 'created_at',)
	search_fields = ('author',)

class CommentAdmin(admin.ModelAdmin):
	list_display = ('article', 'name', 'body', 'created_at',)

class EtiquetteAdmin(admin.ModelAdmin):
	list_display = ('name',)

admin.site.register(Author, AuthorAdmin)
admin.site.register(Article, ArticleAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Etiquette, EtiquetteAdmin)