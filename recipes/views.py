from django.shortcuts import render


def index(request):
    context = {'Welcome': 'Welcome to My Recipe Website!'}
    return render(request, 'recipes/index.html', context)

def home(request):
    context = {'message': 'Welcome to the Home Page!'}
    return render(request, 'recipes/home.html', context)

def lunch(request):
    context = {
        'message': 'Find below all meal ideas for lunch. Each recipe comes with an ingredients list.',
        'recipes': [
            {'name': 'High Protein Stirfry', 'url': 'recipes:lunch'},
            {'name': 'Chicken and Avocado Wraps', 'url': 'recipes:lunch'},
            {'name': 'Soy Chicken', 'url': 'recipes:lunch'},
        ]
    }
    return render(request, 'recipes/lunch.html', context)


def SoyChicken(request):
    context = {'message': 'This is the Soy Chicken recipe.'}
    return render(request, 'recipes/SoyChicken.html', context)
