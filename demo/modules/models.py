from django.db import models
from content.models import Article, Category


class Menu(models.Model):
    name = models.CharField(max_length=250)
    link = models.URLField(null=True, blank=True)
    is_external = models.BooleanField(default=False)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    is_active = models.BooleanField(default=True)
    
    class Meta:
        ordering = ['name']
        
    def __str__(self) -> str:
        return self.name
    
class Block(models.Model):
    BLOCK_STYLE_CHOICES = [
        ('standard', 'Standard'),
        ('horizontal', 'Horizontal'),
        ('vertical', 'Vertical'),
    ]
    articles = models.ManyToManyField(Article, related_name='blocks')
    block_style = models.CharField(max_length=20, choices=BLOCK_STYLE_CHOICES)
    position = models.CharField(max_length=100)
    row = models.PositiveIntegerField(default=1)
    title = models.CharField(max_length=250)
    show_title = models.BooleanField(default=False)
    
    def __str__(self):
        return self.title