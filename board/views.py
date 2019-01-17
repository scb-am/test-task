# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from .models import Topic
from django.http import HttpResponse, HttpResponseRedirect, Http404
import datetime
from .forms import TopicForm



# Create your views here.

def show_tasks(request):
    context = {}
    if request.user.is_authenticated:
        topics_t = Topic.objects.filter(owner=request.user, table='T').order_by('date_added')
        topics_i = Topic.objects.filter(owner=request.user, table='I').order_by('date_added')
        topics_d = Topic.objects.filter(owner=request.user, table='D').order_by('date_added')
        context['topics_t'] = topics_t
        context['topics_i'] = topics_i
        context['topics_d'] = topics_d
    return render(request, 'tasks.html', context)


def change_table(request):
    if request.is_ajax():
        topic_id = request.GET['topic_id']
        topic_table = request.GET['topic_table']
        current_topic = Topic.objects.get(id=topic_id)
        current_topic.table = topic_table
        current_topic.date_added = datetime.datetime.now()
        current_topic.save()
        return HttpResponse('')


def add_topic(request):
    if request.is_ajax():
        topic_text = request.GET['topic_text']
        form = TopicForm(data={'text': topic_text, 'table': "T"})
        newtopic = form.save(commit=False)
        newtopic.owner = request.user
        newtopic.save()
        data = {}
        data[newtopic.id] = newtopic.id
        return HttpResponse(data)


def del_topic(request):
    if request.is_ajax():
        topic_id = request.GET['topic_id']
        topic = Topic.objects.get(id=topic_id)
        topic.delete()
        return HttpResponse('')


def edit (request, id):
    topic = Topic.objects.get(id=id)
    if topic.owner != request.user:
        raise Http404
    else:
        if request.method != 'POST':
            form = TopicForm(instance=topic, prefix='form')
            request.session['return_path'] = request.META.get('HTTP_REFERER','/')
        else:
            form = TopicForm(request.POST, instance=topic, prefix='form')
            if form.is_valid():
                topic = form.save(commit=False)
                topic.save()
            return HttpResponseRedirect(request.session['return_path'])
        context = {'form': form}
        return render(request, 'edit.html', context)
