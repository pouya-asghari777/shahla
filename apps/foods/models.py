from django.db import models


class Food(models.Model):
    name = models.CharField(verbose_name='Name', max_length=32, unique=True)
    description = models.TextField(verbose_name='Description', max_length=256, blank=True, null=True)
    price = models.PositiveIntegerField(verbose_name='Price')
    TYPE_MAIN = 'Main'
    TYPE_SIDE = 'Side and Salad'
    TYPE_DRINK = 'Drink'
    TYPE_CHOICES = (
        (TYPE_MAIN, TYPE_MAIN),
        (TYPE_SIDE, TYPE_SIDE),
        (TYPE_DRINK, TYPE_DRINK),
    )
    type = models.CharField(verbose_name='Type', choices=TYPE_CHOICES, max_length=32)
    picture = models.ImageField(verbose_name='Picture', upload_to='foods', blank=True, null=True)

    created = models.DateTimeField('Created', auto_now_add=True)
    updated = models.DateTimeField('Updated', auto_now=True)

    class Meta:
        verbose_name = 'Food'
        verbose_name_plural = 'Foods'
        ordering = ['type']

    def __str__(self):
        return self.name
