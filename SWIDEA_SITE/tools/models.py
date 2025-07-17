from django.db import models

# Create your models here.
class Tool(models.Model):
    name = models.CharField('이름', max_length=32)
    kind = models.CharField('종류', max_length=32)
    content = models.TextField('내용')
    
    def __str__(self):
        return self.name