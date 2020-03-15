from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User

class Users(models.Model):
    NAME_MAX_LENGTH = 128
    #userid = models.IntegerField(default=0, primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    picture = models.ImageField(upload_to='profile_images', blank=True)
    
    def __str__(self):
        return self.username
    
#class Categories(models.Model):
#    TITLE_MAX_LENGTH = 128
    
#    RPGs = models.CharField(max_length=TITLE_MAX_LENGTH, blank = True)
#    Racing = models.CharField(max_length=TITLE_MAX_LENGTH, blank = True)
#    SuperHero = models.CharField(max_length=TITLE_MAX_LENGTH, blank = True)
#    Others = models.CharField(max_length=TITLE_MAX_LENGTH, blank = True)
    
#    def __str__(self):
#        return self.RPGs, self.Racing, self.SuperHeoro, self.Others
    
class Games(models.Model):
    TITLE_MAX_LENGTH = 128
    
    #user = models.ManyToManyField(Users, on_delete=models.CASCADE)
    #categories = models.ForeignKey(Categories, on_delete=models.CASCADE)
    #GameID = models.IntegerField(default=0, primary_key=True)
    GameName = models.CharField(max_length=TITLE_MAX_LENGTH, default ="")
    GameRating = models.IntegerField(default=0)
    GameImage = models.ImageField(upload_to='profile_images', blank=True)
    Gamedescription = models.TextField(max_length = 200)
    GameCategory = models.CharField(max_length=50, blank = True )
    
    slug = models.SlugField(blank=True)
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.GameName)
        super(Games, self).save(*args, **kwargs)
    
    def __str__(self):
        return self.GameName

class Reviews(models.Model):
    TITLE_MAX_LENGTH = 128
    
    #user = models.ForeignKey(Users, on_delete=models.CASCADE)
    games = models.ForeignKey(Games, on_delete=models.CASCADE)
    #ReviewID = models.IntegerField(default=0, primary_key=True)
    GameName = models.CharField(max_length=TITLE_MAX_LENGTH, default ="")
    GameImage = models.ImageField(upload_to='profile_images', blank=True)
    ReviewerName = models.CharField(max_length=TITLE_MAX_LENGTH)
    Review = models.TextField(max_length = 200)
    Graphics = models.IntegerField(default=0)
    Storyline = models.IntegerField(default=0)
    Gameplay = models.IntegerField(default=0)
    
    slug = models.SlugField(blank=True)
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.GameName)
        super(Reviews, self).save(*args, **kwargs)

    
    def __str__(self):
        return self.ReviewerName
    
class Comments(models.Model):
    TITLE_MAX_LENGTH = 128
    
    reviews = models.ForeignKey(Reviews, on_delete=models.CASCADE)
    #Commentgame = models.ForeignKey(Reviews, on_delete=models.CASCADE)
    GameName = models.CharField(max_length=TITLE_MAX_LENGTH, default ="")
    CommentName = models.CharField(max_length=TITLE_MAX_LENGTH)
    Comments = models.TextField(max_length = 200, blank = True)
    
    #slug = models.SlugField(blank=True)
    
    #def save(self, *args, **kwargs):
     #   self.slug = slugify(self.GameName)
      #  super(Comments, self).save(*args, **kwargs)
    
    def __str__(self):
        return self.GameName
