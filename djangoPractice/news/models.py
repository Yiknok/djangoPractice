from django.db import models
from django.urls import reverse


class News(models.Model):
    title = models.CharField(max_length=150, verbose_name='News Title')
    content = models.TextField(blank=True, verbose_name='News Content')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Created At:')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Last Update:')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True, verbose_name='Photo')
    is_published=models.BooleanField(default=True,verbose_name='Published')
    category = models.ForeignKey('Category', on_delete=models.PROTECT, verbose_name='News Category')

    def get_absolute_url(self):
        return reverse('view_news',kwargs={'pk':self.pk})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'News'
        verbose_name_plural = 'News'
        ordering = ['-created_at']


class Category(models.Model):
    title = models.CharField(max_length=150, db_index=True, verbose_name='Category title')

    def get_absolute_url(self):
        return reverse('category',kwargs={'category_id':self.pk})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        ordering = ['title']
