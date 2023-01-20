from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from ClassApp.models import AccountHolder
from django.contrib.auth.forms import UserCreationForm

from ClassApp.support_functions import import_from_menu, get_recipe_options


# Create your views here.
def home(request):
    data = dict()
    import datetime
    time = datetime.datetime.now()
    print(time)
    data["time_of_day"] = time
    ingredients_data = dict()
    choice = 'NONE'
    tester = ['hello', 'strawberry']
    try:
        choice = request.GET['selection']
        choice=[choice]
        data['selection'] = choice
        # Printing this to display in console that we can access form data
        print(choice)
        # Simple logic to show we can create logic with our form data
        if choice[0] == tester[0]:
            print("Yes all ingredients here")
        else:
            print('Need more ingredients')
        return render(request, 'results.html', context=data)            # how to add this back to page
    except:
        pass
    return render(request, "home.html", context=data)


def results(request):
    data = dict()
    choice = 'NONE'
    # adding another comment
    # tester = ['hello', 'strawberry']

    try:
        choice = request.GET['selection']
        choice = [choice]

        recipe_list = import_from_menu()
        selected_recipes = get_recipe_options(choice, recipe_list)
        data['selection'] = choice
        data['selected_recipes']=selected_recipes
        print(data['selection'])
        print(data['selected_recipes'])
        # Printing this to display in console that we can access form data
        print(choice)
        # Simple logic to show we can create logic with our form data
        if choice[0] == tester[0]:
            print("Yes all ingredients here")
        else:
            print('Need more ingredients')
        return render(request, "results.html", context=data)
    except:
        pass
    return render(request, "results.html", context=data)

#TRYING SOMETHING HERE

'''def contact(request):
    test =[]
    if request.method == 'POST': # If the form has been submitted...
        try:
            choice = ContactForm(request.POST) # A form bound to the POST data
            if choice == "hello ":
                print("Yes it worked")
                print (form.cleaned_data['my_form_field_name'])

            return HttpResponseRedirect(reverse('home')) # Redirect after POST
        except:
            pass

    return render(request, "maintenance.html")



# Create your views here.
def home_view(request):
    data = request.GET['selection']
    print(data)
    return render(request, 'home.html', {'data': data})
'''


def selected_recipe(request):
    selected_data = dict()
    return render(request, "selected_recipe.html", context=selected_data)


def maintenance(request):
    maintenance_data = dict()
    choice = 'NONE'
    try:
        choice = request.GET['selection']
        choice = [choice]
    except:
        pass
    print(choice)
    return render(request, "maintenance.html", context=maintenance_data)

def register_new_user(request):
    context = dict()
    form = UserCreationForm(request.POST)
    if form.is_valid():
        new_user = form.save()
        acct_holder = AccountHolder(user=new_user)
        acct_holder.save()
        return render(request,"home.html",context=dict())
    else:
        form = UserCreationForm()
        context['form'] = form
        return render(request, "registration/register.html", context)
