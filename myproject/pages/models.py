from django.db import models
from django.contrib.auth.models import User
# from abstractapp.manager import CommonManager

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
    name = models.CharField(max_length=50,null=True,blank=True,unique=True)
    info = models.CharField(max_length=100,null=True,blank=True)
    image = models.ImageField(upload_to='contact_information/images',null=True,blank=True)
    link_template = models.CharField(max_length=200, help_text="Use {{contact_info}} to insert contact info",null=True,blank=True)
    link = models.CharField(max_length=200,null=True,blank=True,editable=False)

    def __str__(self) -> str:
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
