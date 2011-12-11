from django.db import models

# Create your models here.

class Artikel(models.Model):
    art_title = models.CharField(verbose_name="Titel",max_length=200)
    art_pub_date = models.DateTimeField('Datum')
    art_tags = models.CharField(verbose_name="Tags",max_length=1000)
    
    categories = (
        ('Allgemein', 'Allgemein'),
        ('Ubuntuusers', 'Ubuntuusers'),
        ('Blog', 'Blog'),
        ('Linux', 'Linux'),
    )
   
    art_category_first = models.CharField(verbose_name="Kategorie", max_length=50, choices=categories,default="Allgemein") 

    art_category_second = models.CharField(verbose_name="Kategorie 2",max_length=50,choices=categories,default="Allgemein")
    

    art_text = models.TextField(verbose_name="Text")
        


    def __unicode__(self):
        return self.art_title
    
    def get_absolute_url(self):
        return "/artikel/%i/" % self.id

    def get_categories(self):
        return (self.art_category_first,self.art_category_second)
        
    def get_description(self):
		return self.art_text

    class Meta:
        verbose_name_plural = "Artikel"


class Podcast(models.Model):
    article = models.ForeignKey(Artikel)
    pod_title = models.CharField(verbose_name="Titel",max_length=200)
    pod_pub_date = models.DateTimeField('Datum')

    pod_link = models.CharField(verbose_name="URL",max_length=300)
    pod_length = models.IntegerField("Length")
   
    mimetypes = (
        ('audio/mpeg','MP3'),
        ('audio/ogg','OGG'),
    )  

    pod_mime = models.CharField(verbose_name="Datentyp",max_length=30,choices=mimetypes)    
 
    def get_absolute_url(self):
        return "/artikel/podcast/%i/" % self.id

    def get_enclosure_url(self):
        return self.pod_link

    def get_enclosure_length(self):
        return self.pod_length

    def get_enclosure_mime_type(self):
        return self.pod_mime

    def get_podcast_desc(self):
        return self.article.art_text

    def __unicode__(self):
        return self.pod_title

    class Meta:
        verbose_name_plural = "Podcasts"


