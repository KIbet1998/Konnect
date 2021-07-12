from django.db import models


class Profile(models.Model):
    profile_pic=models.ImageField(default='default.jpg',upload_to='profile')
    bio=models.TextField(max_length=500)
    user=models.OneToOneField(User,null=True,on_delete=models.CASCADE)

    def _str_(self):
        return self.bio
        


class Image(models.Model):
    image=models.ImageField(blank=True,null=False)
    name=models.CharField(max_length=100)
    caption=models.TextField(max_length=400)
    liked=models.ManyToManyField(User,default=0,blank=True,related_name='liked')
    comments=models.TextField(max_length=100)
    profile=models.ForeignKey(Profile,on_delete=models.CASCADE,null=True)
    author=models.ForeignKey(User,on_delete=models.CASCADE,related_name='author',null=True)

    def _str_(self):
        return self.name

class Like(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    image=models.ForeignKey(Image,on_delete=models.CASCADE)
    value=models.CharField(choices=LIKE_CHOICES,default='Like',max_length=10)
    
    def _str_(self):
        return self.image