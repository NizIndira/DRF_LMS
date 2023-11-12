from django.db import models

from users.models import User

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


class Lesson(models.Model):
    course = models.ForeignKey('Course', on_delete=models.CASCADE, verbose_name='курс')
    title = models.CharField(max_length=200, verbose_name='название')
    description = models.TextField(**NULLABLE, verbose_name='описание')
    image = models.ImageField(upload_to='lessons', verbose_name='превью', **NULLABLE)
    video_url = models.URLField(verbose_name='ссылка на видео', **NULLABLE,)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='дата и время создания')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'урок'
        verbose_name_plural = 'уроки'
        ordering = ('created_at',)


class Payment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='пользователь', **NULLABLE)
    payment_date = models.DateField(verbose_name='дата оплаты', auto_now_add=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='курс', **NULLABLE)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, verbose_name='урок', **NULLABLE)
    amount = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='сумма оплаты', **NULLABLE)
    payment_method = models.CharField(
        max_length=20,
        choices=[
            ('cash', 'наличные'),
            ('transfer', 'перевод на счет')
        ],
        verbose_name='способ оплаты',
        default='transfer'
    )

    def __str__(self):
        return f'{self.user} - {self.course} - {self.lesson}'

    class Meta:
        verbose_name = 'платеж'
        verbose_name_plural = 'платежи'
        ordering = ('payment_date',)
