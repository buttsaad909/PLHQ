from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse
from django.shortcuts import redirect
from playerhq.models import Games, Reviews, Categories
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from playerhq.forms import UserForm, UserProfileForm, Review, GameForm

def index(request):
    games_list = Games.objects.order_by('-GameRating')[:5]
    context_dict = {}
    context_dict['categories'] = Categories.objects.order_by('catName')
    context_dict['games'] = games_list
    context_dict['image'] = Games.objects.order_by('GameImage')
    context_dict['topGame'] = Games.objects.order_by('-GameRating')[0]
    
    return render(request, 'playerhq/index.html', context_dict)

def about(request):
    context_dict = {}
    context_dict['categories'] = Categories.objects.order_by('catName')
    return render(request, 'playerhq/about.html', context_dict)

def game(request, game_name_slug):
    context_dict = {}

    try:
        game = Games.objects.get(slug=game_name_slug)
        allReviews = Reviews.objects.order_by('ReviewerName')
        reviews = []
        for review in allReviews:
            if review.GameName == game.GameName:
                reviews = reviews + [review]
        context_dict['reviews'] = reviews
        context_dict['game'] = game
    except Games.DoesNotExist:
        context_dict['game'] = None

    context_dict['categories'] = Categories.objects.order_by('catName')

    return render(request, 'playerhq/game.html', context_dict)

def category(request, category_name_slug):
    context_dict = {}

    try:
        catName = Categories.objects.get(slug=category_name_slug)
        allGames = Games.objects.order_by('GameRating')
        games = []
        for game in allGames:
            if game.GameCategory == catName.catName:
                games = games + [game]
                
        context_dict['games'] = games
        context_dict['catName'] = catName
    except Games.DoesNotExist:
        context_dict['catName'] = None

    context_dict['categories'] = Categories.objects.order_by('catName')

  #  print(context_dict['games'])

    return render(request, 'playerhq/category.html', context_dict)

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return redirect(reverse('playerhq:index'))
            else:
                return HttpResponse("Your PlayerHQ account is disabled.")
        else:
            print(f"Invalid login details: {username}, {password}")
            return HttpResponse("Invalid login details supplied.")
    else:
        return render(request, 'playerhq/login.html')


def addGame(request, category_name_slug):
    form2 = GameForm()
    form = Review()
    category = Categories.objects.get(slug=category_name_slug)

    if request.method == 'POST':
        form2 = GameForm(request.POST)
        form = Review(request.POST)
        if form.is_valid() and form2.is_valid():
            game = form2.save(commit=False)
            review = form.save(commit=False)
            
            review.GameName = game.GameName
            review.save()
            
            image = request.FILES['GameImage']
            game.GameImage = image
            game.save()
            return redirect(reverse('playerhq:index'))
        else:
            print(form.errors)
            print(form2.errors)

    return render(request, 'playerhq/addGame.html',
                  context = {'form': form,
                             'form2' : form2,
                             'category': category})

def signup(request):
    registered = False

    if request.method == 'POST':
        user_form = UserForm(request.POST)
        profile_form = UserProfileForm(request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']

            profile.save()
            registered = True
        else:
            print(user_form.errors, profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()

    return render(request, 'playerhq/signup.html',
                  context = {'user_form': user_form,
                             'profile_form': profile_form,
                             'registered': registered})
@login_required
def user_logout(request):
    # Since we know the user is logged in, we can now just log them out.
    logout(request)
    # Take the user back to the homepage.
    return redirect(reverse('playerhq:index'))
