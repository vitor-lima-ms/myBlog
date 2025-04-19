from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from django.contrib.auth.decorators import login_required
from django.views.generic import DetailView

from publication.models import Publication, Comment
from publication.myForms import CreatePublicationForm, SearchPublicationForm ,CommentForm

# Create your views here.

def home(request):
    publications = Publication.objects.filter(published=True)
    form = SearchPublicationForm()
    context = {
        'publications': publications,
        'form': form,
    }
    return render(request, 'home.html', context)

def searchPublication(request):
    form = SearchPublicationForm(request.POST or None)
    if form.is_valid():
        query = form.cleaned_data['query']
        publications = Publication.objects.filter(title__icontains=query, published=True)
        context = {
            'form': form,
            'publications': publications,
        }
    return render(request, 'searchPublication.html', context)

@login_required
def createPublication(request):
    if request.method == 'POST':
        form = CreatePublicationForm(request.POST)
        if form.is_valid():
            publication = form.save(commit=False) # Não salva na base de dados ainda pois ainda não tem autor
            publication.author = request.user
            publication.save() # Salva na base de dados após atribuição do autor
            return redirect('publication:home')
    else:
        form = CreatePublicationForm()
    return render(request, 'createPublication.html', {'form': form})

def detailsPublication(request, id):
    publication = get_object_or_404(Publication, id=id)
    comments = Comment.objects.filter(publication=publication).order_by('-createdAt')
    form = CommentForm()
    context = {
        'publication': publication,
        'comments': comments,
        'form': form,
    }
    return render(request, 'detailsPublication.html', context)

@login_required
def createComment(request, id):
    publication = get_object_or_404(Publication, id=id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.publication = publication
            comment.author = request.user
            comment.save()
            return redirect('publication:detailsPublication', id=publication.id)

def newsPublication(request):
    publications = Publication.objects.filter(category='news', published=True)
    return render(request, 'newsPublication.html', {'publications': publications})

def sportsPublication(request):
    publications = Publication.objects.filter(category='sports', published=True)
    return render(request, 'sportsPublication.html', {'publications': publications})

def entertainmentPublication(request):
    publications = Publication.objects.filter(category='entertainment', published=True)
    return render(request, 'entertainmentPublication.html', {'publications': publications})

def technologyPublication(request):
    publications = Publication.objects.filter(category='technology', published=True)
    return render(request, 'technologyPublication.html', {'publications': publications})

def healthPublication(request):
    publications = Publication.objects.filter(category='health', published=True)
    return render(request, 'healthPublication.html', {'publications': publications})

def otherPublication(request):
    publications = Publication.objects.filter(category='other', published=True)
    return render(request, 'otherPublication.html', {'publications': publications})