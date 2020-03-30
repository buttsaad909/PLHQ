from django import forms
from playerhq.models import Users, Games, Reviews
from django.contrib.auth.models import User

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    
    class Meta:
        model = User
        fields = ('username', 'password',)

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = Users
        fields = ( 'picture',)
        
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

    def clean(self):
        #data from the form is fetched using super functionn
        super(GameForm, self).clean()
        
        # extract the username and text field from the data
        game = self.cleaned_data['GameName']
        
        #conditions to be met for the username length
        if Games.objects.filter(GameName=game).exists():
            self._errors['GameName'] = self.error_class(['Game name already exits'])
        return self.cleaned_data
        
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
        