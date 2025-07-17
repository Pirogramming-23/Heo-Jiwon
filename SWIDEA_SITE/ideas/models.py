from django.db import models
from django.contrib.auth.models import User
from tools.models import Tool

# Create your models here.
class Idea(models.Model):
    title = models.CharField('제목', max_length=32)
    photo = models.ImageField('이미지', blank=True, upload_to='ideas/%Y%m%d')
    content = models.TextField('내용')
    interest = models.CharField(max_length=32)
    devtool    = models.ForeignKey(
                   Tool,
                   verbose_name='개발툴',
                   on_delete=models.SET_NULL,
                   null=True,
                   blank=True
               )
    created_at = models.DateTimeField('등록일', auto_now_add=True)

    def star_count(self):
        return self.ideastar_set.count()

class IdeaStar(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    idea = models.ForeignKey(Idea, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'idea')