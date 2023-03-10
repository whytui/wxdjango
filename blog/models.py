from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Category(models.Model):
    name = models.CharField('文章分类', max_length=100)
    index = models.IntegerField(default=999, verbose_name="分类排序")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "文章分类"


class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "标签"


class Article(models.Model):
    title = models.CharField('标题', max_length=100)
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING, verbose_name="分类", blank=True, null=True)
    img = models.ImageField(upload_to='article_img/%Y%m/%d', verbose_name="文章图片", blank=True, null=True)
    description = models.CharField('描述', max_length=200)
    content = models.TextField('正文')
    pub_date = models.DateField('发布时间', auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag, related_name='articles', blank=True)

    def __str__(self):
        return self.title
