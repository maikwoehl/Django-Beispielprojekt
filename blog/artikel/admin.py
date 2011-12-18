from artikel.models import Artikel, Podcast
#from artikel.widgets import RichTextEditorWidget

from django.contrib import admin

class PodcastInline(admin.TabularInline):
    model = Podcast
    extra = 0
    max_num = 2

class ArtikelAdmin(admin.ModelAdmin):
    #formfield_overrides = {
    #    models.TextField: {'widget': RichTextEditorWidget},
    #}
    fieldsets = [
        ('Allgemeines', {'fields': ['art_title','art_pub_date', 
'art_tags','art_category_first','art_category_second']}),
        (None, {'fields': ['art_text']}),
    ]	

    list_display = ('id','art_title','art_pub_date', 'art_tags')
    list_filter = ['art_pub_date']
    search_fields = ['art_title']
    date_hierarchy = 'art_pub_date'
    inlines = [PodcastInline]

class PodcastAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['pod_title','pod_pub_date','pod_link']}),
    ]

    list_display = ('id','pod_title','pod_pub_date')
    list_filter = ['pod_pub_date']
    search_fields = ['pod_title']
    date_hierarchy = 'pod_pub_date'

admin.site.register(Artikel, ArtikelAdmin)
#admin.site.register(Podcast, PodcastAdmin)

