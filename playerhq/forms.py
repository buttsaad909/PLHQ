from django import forms
from playerhq.models import Users, Games, Reviews
from django.contrib.auth.models import User

'''
Form for user sign up.
'''
class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    
    class Meta:
        model = User
        fields = ('username', 'password',)

'''
Form for user sign up.
Allows for profile customisation. E.g. Adding a picture
'''
class UserProfileForm(forms.ModelForm):
    class Meta:
        model = Users
        fields = ( 'picture',)

'''
A form for adding a game
Users must add a unique game name, a description, a rating, a category.
Users may add an image for a game, otherwise the game will be given a default
image.
'''        
class GameForm(forms.ModelForm): 
    INTEGER_CHOICES= [tuple([x,x]) for x in range(1,6)]
    GAME_CHOICES= [
    ('RPGs', 'RPGs'),
    ('Racing', 'Racing'),
    ('SuperHero', 'SuperHero'),
    ('Others', 'Others'),
    ]
    GameName = forms.CharField(max_length=128, help_text="Please enter the GameName of the page.")
    GameImage = forms.ImageField(required=False, initial="NewGame.jpg")
    Gamedescription = forms.CharField(widget=forms.Textarea)
    GameRating= forms.IntegerField(label="Overall GameRating", widget=forms.Select(choices=INTEGER_CHOICES))
    GameCategory= forms.CharField(label='Category of Games?', widget=forms.Select(choices=GAME_CHOICES))
    
    class Meta: 
        model = Games 
        fields = ('GameName', 'GameImage', 'GameCategory','GameRating', 'Gamedescription',)

    # Checks if the game name is unique and flags an error if it is not.
    def clean(self):
        super(GameForm, self).clean()
        
        game = self.cleaned_data['GameName']
        
        if Games.objects.filter(GameName=game).exists():
            self._errors['GameName'] = self.error_class(['Game name already exits'])
        return self.cleaned_data

'''
A form for adding a review.
Users must add their name, the review, adn ratings for gameplay, storyline and graphics
'''     
class Review(forms.ModelForm):
    INTEGER_CHOICES= [tuple([x,x]) for x in range(1,6)]
    
    ReviewerName = forms.CharField(max_length=128, help_text="Please enter the reviewers name.")
    Review = forms.CharField(widget=forms.Textarea, help_text="Type your review here!")
    
    Gameplay= forms.IntegerField(label="Gameplay", widget=forms.Select(choices=INTEGER_CHOICES))
    Storyline= forms.IntegerField(label="Storyline", widget=forms.Select(choices=INTEGER_CHOICES))
    Graphics= forms.IntegerField(label="Graphics", widget=forms.Select(choices=INTEGER_CHOICES))
    
    class Meta:
        model = Reviews
        fields = ('ReviewerName', 'Review', 'Graphics', 'Storyline', 'Gameplay')
        
