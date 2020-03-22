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
    #GameName = forms.CharField(max_length=128, help_text="Please enter the GameName of the page.")
    #GameCategory = forms.CharField(max_length=128, help_text="Please enter the category of the page.")
    #GameRating = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    Gamedescription = forms.CharField(widget=forms.Textarea)
    
    class Meta: 
        model = Games 
        fields = ('GameCategory','GameRating', 'Gamedescription')


        
class Review(forms.ModelForm):
    CHOICES = [
    (1, 1),
    (2, 2),
    (3, 3),
    (4, 4),
    (5, 5),
    ]
    #GameName = forms.CharField(max_length=128, help_text="Please enter the title of the page.")
    #ReviewerName = forms.CharField(max_length=128, help_text="Please enter the reviwername of the page.")
    Review = forms.CharField(widget=forms.Textarea, help_text="Please enter the reviwername of the page.")
    #GameImage = forms.ImageField()
    Graphics = forms.ChoiceField(widget=forms.RadioSelect(), choices=CHOICES,)
    Storyline = forms.ChoiceField(widget=forms.RadioSelect(), choices=CHOICES,)
    Gameplay = forms.ChoiceField(widget=forms.RadioSelect(), choices=CHOICES,)
    
    class Meta:
        model = Reviews

        fields = ( 'GameName','ReviewerName', 'Review', 'GameImage', 'Graphics', 'Storyline', 'Gameplay')
