# @Author: 牛子铜 <niuzitong>
# @Date:   2017-05-04T22:44:48+08:00
# @Email:  niuzitong@nonobank.com
# @Filename: models.py
# @Last modified by:   niuzitong
# @Last modified time: 2017-05-05T23:46:18+08:00


from django.db import models
from django.template.defaultfilters import slugify


class Category(models.Model):

    name = models.CharField(max_length=128, unique=True)
    views = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.name


class Page(models.Model):
    category = models.ForeignKey(Category)
    title = models.CharField(max_length=128)
    url = models.URLField()
    views = models.IntegerField(default=0)

    def __unicode__(self):
        return self.title
