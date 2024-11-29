from django.shortcuts import render

from .models import Topic

# 在这里创建视图
def index(request):
    """学习笔记的主页"""
    return render(request, 'learning_logs/index.html')

def topics(request):
    """显示所有主题"""
    topics = Topic.objects.order_by('date_added')
    context = {'topics': topics}
    return render(request, 'learning_logs/topics.html', context)

def topic(request, topic_id):
    """显示单个主题及其所有的条目"""
    topics = Topic.objects.get(id=topic_id)
    entries = topic.entry_set.order_by('-date_added')
    context = {'topics': topics, 'entries': entries}
    return render(request, 'learning_logs/topics.html', context)

