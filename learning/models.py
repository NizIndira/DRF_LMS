from django.db import models

NULLABLE = {'blank': True, 'null': True}

class Course(models.Model):
    title = models.CharField(max_length=255, verbose_name='название')
    image = models.ImageField(upload_to='courses', verbose_name='превью', **NULLABLE)
    description = models.TextField(verbose_name='описание', **NULLABLE)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='дата и время создания')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'курс'
        verbose_name_plural = 'курсы'
        ordering = ('title',)


# Класс модели "Урок": курс, название, описание, превью (картинка), ссылка на видео
class Lesson(models.Model):
    course = models.ForeignKey('Course', on_delete=models.CASCADE, verbose_name='курс')
    title = models.CharField(max_length=200, verbose_name='название')
    description = models.TextField(**NULLABLE, verbose_name='описание')
    image = models.ImageField(upload_to='lessons', verbose_name='первью', **NULLABLE)
    video_url = models.URLField(verbose_name='ссылка на видео', **NULLABLE,)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='дата и время создания')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'урок'
        verbose_name_plural = 'уроки'
        ordering = ('created_at',)
