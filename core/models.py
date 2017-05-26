from django.db import models


class News(models.Model):
    """
    It's doc string and it's important
    """
    title = models.CharField('title', max_length=100)
    description = models.TextField('description')
    is_published = models.BooleanField('publish', default=True)
    created = models.DateTimeField('created')

    class Meta:
        verbose_name = 'news'
        verbose_name_plural = 'news'
        ordering = ('-created',)

    def __str__(self):
        return self.title
