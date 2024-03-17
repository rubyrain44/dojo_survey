from django.shortcuts import render, redirect

def index(request):
    # this is the route that shows the form
    return render(request,"index.html")

def create_user(request):
    # this is the route that processes the form
    name = request.POST['name']
    location = request.POST['location']
    language = request.POST['language']
    comment = request.POST['comment']
    context = {
        "name" : name,
        "location" : location,
        "language" : language,
        "comment" : comment,
    }
    return render(request, "show.html",context)

# def success(request):
#     # this is the success route
#     return render(request,"show.html")