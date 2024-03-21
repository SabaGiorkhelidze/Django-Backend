from django.db import models
from users.models import CustomUser
from treebeard.mp_tree import MP_Node
from ckeditor.fields import RichTextField

class Category(MP_Node):
    name = models.CharField(max_length=250)
    logo = models.ImageField(upload_to='category_logos', null=True, blank=True)
    node_order_by = ['name']

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Categories'

class Tag(models.Model):
    name = models.CharField(max_length=320)

    def __str__(self):
        return self.name

class Article(models.Model):
    title = models.CharField(max_length=500)
    description = RichTextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    tags = models.ManyToManyField(Tag, related_name='articles')
    main_image = models.ImageField(upload_to='article_images')
    is_published = models.BooleanField(default=False)

    def __str__(self):
        return self.title