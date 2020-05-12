from django import forms
from django.shortcuts import render
from django.http import HttpResponse
from . import util
import random

class NewPage(forms.Form):
    title = forms.CharField(label="",widget=forms.TextInput(attrs={'placeholder':'Enter title'}))
    desc = forms.CharField(label="",widget=forms.Textarea(attrs={'placeholder':'Enter Description'}))

def index(request):
    if request.method=='GET':
        if ('q' in request.GET):
            query = request.GET['q']
            entries = util.list_entries()
            for i in entries:
                if query in i:
                    return render(request, "encyclopedia/search_result.html", {
                        "entry": i
                    })
            return render(request, "encyclopedia/search_result.html", {
                    "entry": ""
            })    
    
        else:
            return render(request, "encyclopedia/index.html", {
                "entries": util.list_entries()
            }) 

def load_title(request, TITLE):
    return render(request, "encyclopedia/title_page.html", {
        "title":TITLE,
        "content":util.get_entry(TITLE)
        })

def new_page(request):
    if (request.method=='POST'):
        form = NewPage(request.POST)
        if form.is_valid():
            title = form.cleaned_data["title"]
            desc = form.cleaned_data["desc"]
            util.save_entry(title, desc)
        else:
            return render(request, "encyclopedia/new_page.html", {
                "form": form
            })    

    return render(request, "encyclopedia/new_page.html", {
        "form": NewPage()
    })

def random_page(request):
    pages = util.list_entries()
    random_num = random.randint(0, len(pages)-1)
    return render(request, "encyclopedia/title_page.html", {
        "title":pages[random_num],
        "content":util.get_entry(pages[random_num])
        })