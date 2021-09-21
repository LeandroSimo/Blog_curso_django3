from django.db import models
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField

class Categorias(models.TextChoices):
    TECH = 'TC', 'Tecnologia'
    CR = 'CR', 'Curiosidades'
    GR = 'GR', 'Geral'


class Contact(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.name
    

class Post(models.Model):
    title = models.CharField(max_length=255)
    sub_title = models.CharField(max_length=255)
    content1 = RichTextUploadingField(max_length=300, blank=True, null=True)
    ##content2 =  RichTextField(blank=True, null=True)
    ##content = models.TextField()
    categories = models.CharField(
        max_length=4,
        choices=Categorias.choices,
        default=Categorias.GR,
    )

    deleted = models.BooleanField(default=False)
    imagem = models.ImageField(upload_to='posts', null=True, blank=True)


    def __str__(self):
        return self.title
    
    def full_name(self):
        return self.title + self.sub_title

    def get_category_label(self):
        return self.get_categories_display()
    
    full_name.admin_order_field = 'title'