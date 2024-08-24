from django.db import models
from django.urls import reverse

class News(models.Model):
    title = models.CharField(max_length=150, verbose_name = 'Наименование')
    content = models.TextField(blank=True, verbose_name = 'Контент') #blank=True - обозначает поле необязательное к заполнению
    created_at = models.DateTimeField(auto_now_add=True, verbose_name = 'Дата публикации') # auto_now_add=True - обозначает, что дата и время будут создаваться автоматически и при редактировании не изменяться (не обновляться)
    updated_at = models.DateTimeField(auto_now=True, verbose_name = 'Обновлено') # auto_now=True при редактировании (обновлении) новости будет указано время ее редактирования
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name = 'Фото', blank=True) # сохранение по дате при загрузке %Y/%m/%d/
    is_published = models.BooleanField(default=True, verbose_name = 'Опубликовано')  # default=True - новость по умолчанию публикуется
    category = models.ForeignKey('Category', on_delete=models.PROTECT, null=True, verbose_name='Категория')
    views = models.IntegerField(default=0)

    def get_absolute_url(self):
        return reverse('view_news', kwargs={"pk": self.pk})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
        ordering = ['created_at']

class Category(models.Model):
    title = models.CharField(max_length=150, db_index=True, verbose_name='Наименование категории')

    def get_absolute_url(self):
        return reverse('category', kwargs={"category_id": self.pk})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['title']
