from djongo import models
# Create your models here.

class BlogContent(models.Model):
    comment = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    class Meta:
        abstract = True

class Entry(models.Model):
    blog = models.EmbeddedModelField(model_container=BlogContent)
    headline = models.CharField(max_length=255)

class ParamsContent(models.Model):
    tool_name   = models.CharField(max_length=30)
    url         = models.CharField(max_length=255)
    url_sources = models.CharField(max_length=255)
    type        = models.CharField(max_length=20)
    class Meta:
        abstract = True

class MBlkHole(models.Model):
    measure1 = models.FloatField
    measure2 = models.FloatField
    measure3 = models.FloatField
    class Meta:
        abstract = True

class Maxi(models.Model):
    source = models.CharField(max_length=100)
    url    = models.CharField(max_length=255)
    blkh   = models.EmbeddedModelField(model_container=MBlkHole)

class Params(models.Model):
    param = models.EmbeddedModelField(model_container=ParamsContent)