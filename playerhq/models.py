from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User

# A model to hold user information
# Has a username and an optional picture
class Users(models.Model):
    NAME_MAX_LENGTH = 128
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    picture = models.ImageField(upload_to='profile_images', blank=True)
    
    def __str__(self):
        return self.username

# A model to hold different Categories
# Categories have a name and a slug to help traversal across the wbesite
class Categories(models.Model):
    TITLE_MAX_LENGTH = 128
    
    catName = models.CharField(max_length=TITLE_MAX_LENGTH, default ="")
    slug = models.SlugField(blank=True)

    # Generates a slug from a given category name
    def save(self, *args, **kwargs):
        self.slug = slugify(self.catName)
        super(Categories, self).save(*args, **kwargs)
    
    def __str__(self):
        return self.catName

# A model to hold information on Games
# Games have a name, rating, image, description, category and a generated slug
class Games(models.Model):
    TITLE_MAX_LENGTH = 128
    
    GameName = models.CharField(max_length=TITLE_MAX_LENGTH, default ="")
    GameRating = models.IntegerField(default=0)
    GameImage = models.ImageField(upload_to='images', blank=True)
    Gamedescription = models.TextField(max_length = 200)
    GameCategory = models.CharField(max_length=50)
    
    slug = models.SlugField(blank=True)

    # Creates a slug from a given game name
    def save(self, *args, **kwargs):
        self.slug = slugify(self.GameName)
        super(Games, self).save(*args, **kwargs)
    
    def __str__(self):
        return self.GameName

# A model to hold each Review
# A Review has a game name, an image, reviewer name, 200 character review,
# and ratings for Graphics, Storyline and Gameplay
# Slugs are generated for each review
class Reviews(models.Model):
    TITLE_MAX_LENGTH = 128
    
    GameName = models.CharField(max_length=TITLE_MAX_LENGTH, default ="")
    GameImage = models.ImageField(upload_to='images', blank=True)
    ReviewerName = models.CharField(max_length=TITLE_MAX_LENGTH)
    Review = models.TextField(max_length = 200)
    Graphics = models.IntegerField(default=0)
    Storyline = models.IntegerField(default=0)
    Gameplay = models.IntegerField(default=0)
    
    slug = models.SlugField(blank=True)

    # Creates a slug from a given game name
    def save(self, *args, **kwargs):
        self.slug = slugify(self.GameName)
        super(Reviews, self).save(*args, **kwargs)

    
    def __str__(self):
        return self.ReviewerName
    
