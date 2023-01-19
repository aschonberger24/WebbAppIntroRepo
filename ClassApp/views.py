from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse


# Create your views here.
def home(request):
    data = dict()
    import datetime
    time = datetime.datetime.now()
    print(time)
    data["time_of_day"] = time
    ingredients_data = dict()
    choice = 'NONE'
    tester = ['hello','strawberry']
    try:
        choice = request.GET['selection']
        data['selection'] = request.GET['selection']
        #Printing this to display in console that we can access form data
        print(choice)
        #Simple logic to show we can create logic with our form data
        if choice[0] == tester[0]:
            print("Yes all ingredients here")
        else:
            print('Need more ingredients')
        return render(request,'results.html',context=data)            #how to add this back to page
    except:
        pass
    return render(request, "home.html", context=data)

def results(request):
    data = dict()
    choice = 'NONE'
    # adding another comment
    tester = ['hello', 'strawberry']
    try:
        choice = request.GET['selection']
        choice = [choice]
        data['selection'] = choice
        print (data['selection'])
        # Printing this to display in console that we can access form data
        print(choice)
        # Simple logic to show we can create logic with our form data
        if choice[0] == tester[0]:
            print("Yes all ingredients here")
        else:
            print('Need more ingredients')
        return HttpResponseRedirect(reverse('selection'))# how to add this back to page
    except:
        pass
    return render(request, "results.html", context = data)

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


