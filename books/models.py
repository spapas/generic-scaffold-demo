from django.db import models
from generic_scaffold import get_url_names
from django.core.urlresolvers import reverse



class Category(models.Model):
    name = models.CharField(max_length=50)

    def __unicode__(self):
        return self.name
        
    def get_absolute_url(self):
        return reverse(get_url_names(prefix='categories')['detail'], args=(self.id, ) )
        
        
class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

    def get_absolute_url(self):
        return reverse(get_url_names(prefix='authors')['detail'], args=(self.id, ) )

    def __unicode__(self):
        return self.first_name + ' ' + self.last_name
        

        
class Book(models.Model):
    title = models.CharField(max_length=50)
    publish_date = models.DateField(blank=True, null=True)
    category = models.ForeignKey('Category', blank=True, null=True)
    author = models.ForeignKey('Author', blank=True, null=True, on_delete=models.SET_NULL)

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        #return reverse(get_url_names(prefix='books')['detail'], args=(self.id, ) )
        from generic_scaffold_demo.urls import book_crud
        return reverse(book_crud.detail_url_name, args=(self.id, ) )
        #return reverse(get_url_names(prefix='books')['detail'], args=(self.id, ) )
