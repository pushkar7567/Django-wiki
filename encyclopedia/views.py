from django import forms
from django.shortcuts import render
from django.http import HttpResponse
from . import util

class NewPage(forms.Form):
    title = forms.CharField(label="",widget=forms.TextInput(attrs={'placeholder':'Enter title'}))
    desc = forms.CharField(label="",widget=forms.Textarea(attrs={'placeholder':'Enter Description'}))

def index(request):
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
       