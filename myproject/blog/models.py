from django.db import models
# Create your models here.
'''
-В приложении blog создайте модель Post с полями: title (CharField) -
заголовок поста. content (TextField) - содержание поста. created_at
(DateTimeField) - дата и время создания поста. 

-Зарегистрируйте модель Post в админке. 

-Создайте и примените миграции для модели Post.'''


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(max_length=255)
    created_at = models.DateTimeField()

    def __str__(self):
        return self.title

