from cgitb import text
from statistics import multimode
from tabnanny import verbose
from django.db import models
from django.forms import CharField
from djrichtextfield.models import RichTextField

# from django.utils.translation import ugettext_lazy as _
# Create your models here.




class About(models.Model):
    image = models.ImageField('rasm', upload_to='about/')
    title = models.CharField('sarlavha', max_length=100)
    text = models.TextField('matn')
    
    class Meta:
        verbose_name='Biz haqimizda'
        verbose_name_plural='Biz haqimizda'
    
    
    def __str__(self):
        return self.title
    
    
    
class Products(models.Model):
    image = models.ImageField('rasm', upload_to='products/')
    title = models.CharField('sarlavha', max_length=100)
    text = models.TextField('matn', )
    price = models.PositiveIntegerField('narh', )
    
    class Meta:
        verbose_name='Mahsulotlar'
        verbose_name_plural='Mahsulotlar'
        
        
    def __str__(self):
        return self.title
    
    
class Video(models.Model):
    background_image = models.ImageField('orqa fon', upload_to='video_background')
    title = models.CharField('sarlavha', max_length=200)
    text = models.TextField('matn')
    video = models.CharField('video url', max_length=500)
    
    
    class Meta:
        verbose_name='Video'
        verbose_name_plural='Video'
        


class Client_feedback(models.Model):
    image = models.ImageField('rasm', upload_to='client feedback/')
    name = models.CharField('ism', max_length=150)
    feedback = models.TextField('fikr',)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name='Mijoz fikri'
        verbose_name_plural='Mijoz fikrlari'
    
    
    
class Information(models.Model):
    image = models.ImageField('rasm', upload_to='malumotlar')
    title = models.CharField('sarlavha', max_length=200)
    text = models.TextField('matn')
    
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name='Malumot'
        verbose_name_plural=' Malumotlar '
        
        

class Cause(models.Model):
    image = models.ImageField('rasm' , upload_to='causes/')
    title = models.CharField('sarlavha', max_length=150)
    text = models.TextField('matn',)
    
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name=' Yutuq '
        verbose_name_plural='Bizning yutuqlarimiz'
        
        
class Chat_id(models.Model):
    id_number = models.PositiveIntegerField('id raqam')
    
    
    class Meta:
        verbose_name='ID raqam'
        verbose_name_plural='ID raqamlar'
        
        
    def __str__(self):
        return str(self.id_number)