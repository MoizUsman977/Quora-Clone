from django.shortcuts import render
from topics.models import Topic

def search_topics(request):
    query = request.GET.get('q')
    topics = Topic.objects.filter(title__icontains=query)
    return render(request, 'search.html', {'topics': topics, 'query': query})