from django.db import models

from abstractapp.models import BaseModel

# Create your models here.

class HomeCarouselImage(BaseModel):
    image = models.ImageField(upload_to='home/carousel/image',null=True,blank=True)
    header = models.CharField(max_length=200,null=True,blank=True)
    paragraph = models.TextField(null=True,blank=True)
    learn_more = models.CharField(max_length=200,null=True,blank=True)

    def __str__(self) -> str:
        return self.image.url
    


class ContactInformation(BaseModel):
    CONTACT_CHOICES = (
        ('email', 'Email'),
        ('phone', 'Phone'),
        ('whatsapp', 'Whatsapp'),
        ('qq', 'QQ'),
        ('wechat', 'Wechat'),
        ('address', 'Address'),
        # ... 其他选项
    )
    name = models.CharField(max_length=50, choices=CONTACT_CHOICES, null=True, blank=True)
    info = models.CharField(max_length=100, null=True, blank=True)
    image = models.ImageField(upload_to='contact_information/images', null=True, blank=True)
    link_template = models.CharField(max_length=200, help_text="Use {info} to insert contact info", null=True, blank=True)
    link = models.CharField(max_length=200, null=True, blank=True, editable=False)

    def save(self, *args, **kwargs):
        if not self.link_template:
            if self.name == 'email':
                self.link = f'mailto:{self.info}'
            elif self.name == 'phone':
                self.link = f'tel:{self.info}'
            elif self.name == 'whatsapp':
                self.link = f'https://wa.me/{self.info}'
            elif self.name == 'qq':
                self.link = f'https://wpa.qq.com/msgrd?v=3&uin={self.info}&site=qq&menu=yes'
            # ... 其他联系方式的逻辑
        else:
            # 使用 link_template 和 format 方法来渲染 link
            self.link = self.link_template.format(info=self.info)
            
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class SocialMedia(BaseModel):
    name = models.CharField(max_length=50,null=True,blank=True,unique=True)
    link = models.CharField(max_length=100,null=True,blank=True)

    def __str__(self) -> str:
        return self.name
    
class Faq(BaseModel):
    question = models.TextField()
    answer = models.TextField()

class Banner(BaseModel):
    image = models.ImageField(upload_to='home/cta/images',blank=True,null=True)

    def __str__(self) -> str:
        return self.image.url

