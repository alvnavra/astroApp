#Source
#Referencias en otras herramientas (si es posible. Aquí utilizaríamos Fermi)
#Enlaces a publicaciones cientificas relacionadas con ese sistema (Por simbad)
#Periodo de rotación
#
#   Tool:Maxi
#   Source : <name source> Polaris
#   Source Type: Pulsar
#   References: [S400Polar,PolarStar]
#   PublishLinks: [http://]
#   Periodo de Rotacion: 1000
#   Ligth Curve: []
#  turbo-gears


from djongo import models
# Create your models here.

class ParamsContent(models.Model):
    _id         = models.ObjectIdField
    tool_name   = models.CharField(max_length=30)
    url         = models.CharField(max_length=255)
    url_sources = models.CharField(max_length=255)
    type        = models.CharField(max_length=20)
    class Meta:
        abstract = True

class Reference(models.Model):
    source      = models.CharField(max_length=30)
    class Meta:
        abstract = True

class PublishUrls(models.Model):
    publish_url  = models.CharField(max_length=200)
    class Meta:
        abstract = True

class Maxi(models.Model):
    source = models.CharField(max_length=100)
    url    = models.CharField(max_length=255)


class Params(models.Model):
    param = models.EmbeddedModelField(model_container=ParamsContent)
    objects = models.DjongoManager()

class SourceContent(models.Model):
    tool_name   = models.CharField(max_length=30)
    source      = models.CharField(max_length=30)
    references  = models.ArrayModelField(Reference)
    publishLnks = models.ArrayModelField(PublishUrls)
    rotationPeriod = models.IntegerField
    objects = models.DjongoManager()

class Fuente(models.Model):
    fuente = models.EmbeddedModelField(model_container=SourceContent)