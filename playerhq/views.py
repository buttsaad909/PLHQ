from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse
from django.shortcuts import redirect
from playerhq.models import Games, Reviews, Categories,Comments
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
        comment = Comments.objects.order_by('GameName')
        reviews = []
        for review in allReviews:
            if review.GameName == game.GameName:
                reviews = reviews + [review]
        context_dict['comments'] = comment
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

#def display_game_images(request): 
  
#    if request.method == 'GET': 
  
        # getting all the objects of hotel. 
#        Games = Games.objects.get('GameImage')  
#        return render((request, 'playerhq/index.html', 
#                     {'games_images' : Games})) 


def review(request, category_name_slug):
    registered = False
    try:
        category = Categories.objects.get(slug=category_name_slug)
        category2 = Reviews.objects.all()
    except Games.DoesNotExist:
        category = None
    
    # You cannot add a page to a Category that does not exist...
    if category is None:
        return redirect('/playerhq/')
    
    form = Review()
    form2 = GameForm()
    if request.method == 'POST':
        form = Review(request.POST )
        form2 = GameForm(request.POST)
        if form.is_valid() and form2.is_valid():
            form.save(commit= True)
            profile = form2.save(commit=True)
            if 'GameImage'in request.FILES:
                profile.GameImage = request.FILES['picture']
            profile.save()
            registered = True
            return redirect('/playerhq/')
        else:
            print(form.errors, form2.errors)
    context_dict = {'form': form, 'category': category, 'game': category2, 'form2':form2, 'registered': registered}
    return render(request, 'playerhq/review.html', context=context_dict)

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