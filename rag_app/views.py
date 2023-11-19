from django.shortcuts import render

def home(request):
    return render(request, 'RAG/templates/home.html')
