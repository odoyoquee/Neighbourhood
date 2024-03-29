from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from tinymce.models import HTMLField
from pyuploadcare.dj.models import ImageField

class Profile(models.Model):
    prof_pic = ImageField(blank=True, manual_crop='800x800')
    bio = HTMLField()
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key = True)

    def save_profile(self):
        self.save()
    
    @classmethod
    def search_profile(cls, name):
        profile = Profile.objects.filter(user__username__icontains = name)
        return profile

    @classmethod
    def get_by_id(cls, id):
        profile = Profile.objects.get(user = id)
        return profile

    @classmethod
    def filter_by_id(cls, id):
        profile = Profile.objects.filter(user = id).first()
        return profile

class Neighbourhood(models.Model):
    name = models.CharField(max_length=60)
    location = models.CharField(max_length=60)
    population = models.IntegerField()
    image = ImageField(blank=True, manual_crop='800x800')

    def create_neighbourhood(self):
        self.save()

    def delete_neighbourhood(self):
        self.delete()

    @classmethod
    def search_by_name(cls,id):
        neighbourhood=cls.objects.filter(name__icontains=id)
        return neighbours

class Business(models.Model):
    name = models.CharField(max_length=60)
    description = models.CharField(max_length=200)
    user= models.OneToOneField(User, on_delete=models.CASCADE, primary_key = True)
    neighbourhood = models.ForeignKey(Neighbourhood,on_delete=models.CASCADE)
    email = models.EmailField()

    def create_business(self):
        self.save()

    def delete_business(self):
        self.delete()

class Post(models.Model):
    # image_pic = models.ImageField(upload_to = 'p/', default='Image')
    photo = ImageField(blank=True, manual_crop='800x800')
    post_name = models.CharField(max_length = 50)
    post_caption = HTMLField(blank=True)
    post_date = models.DateTimeField(auto_now=True)
    likes = models.BooleanField(default=False)
    profile = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        ordering = ('-post_date',)

    def save_post(self):
        self.save()
    
    @classmethod
    def update_caption(cls, update):
        pass
    
    @classmethod
    def get_post_id(cls, id):
        post = Post.objects.get(pk=id)
        return post
    
    @classmethod
    def get_profile_posts(cls, profile):
        posts = Post.objects.filter(profile__pk = profile)
        return posts
    
    @classmethod
    def get_all_posts(cls):
        posts = Post.objects.all()
        return posts

class Comments(models.Model):
    comment = HTMLField()
    posted_on = models.DateTimeField(auto_now=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def save_comment(self):
        self.save()
    
    @classmethod
    def get_comments_by_posts(cls, id):
        comments = Comments.objects.filter(post__pk = id)
        return comments

        
