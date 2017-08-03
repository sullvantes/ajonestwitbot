# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse,redirect,reverse
from models import *


def contribute(request):
    context= {
        'quotes':Quote.objects.filter(approved=True)[:10]
    }
    return render(request,"get_quotes/contribute.html",context)

def add_quote(request):
    # if not request.session['current_id']:
    # #     return redirect('/main')
    if request.method!='POST':
        return redirect('/quotes')
    #errors = Quote.objects.quote_validator(request.POST)
    quote=request.POST['quote']
    print quote
    tags=request.POST['tags']
    print tags
    #user_id=request.POST['user_id']
    Quote.objects.create(quote=quote, tags=tags)
    return redirect(reverse('quotes:contribute'))

def admin_quote(request):
    quotes=Quote.objects.filter(approved=False)
    for quote in quotes:
        print quote.quote
        print '\t',quote.tags

    context= {
        'quotes':quotes
    }
    return render(request,"get_quotes/admin.html",context)

def approve_quote(request,quote_id):
    # if not request.session['current_id']:
    # #     return redirect('/main')
    #errors = Quote.objects.quote_validator(request.POST)
    quote=Quote.objects.get(id=quote_id)
    quote.approved=True
    quote.save()
    return redirect(reverse('quotes:admin'))

def delete_quote(request,quote_id):
    # if not request.session['current_id']:
    # #     return redirect('/main')
    #errors = Quote.objects.quote_validator(request.POST)
    Quote.objects.get(id=quote_id).delete()
    return redirect(reverse('quotes:admin'))

def add_tag(request, quote_id):
    if request.method!='POST':
        return redirect(reverse('quotes:contribute'))
    tag = request.POST['tags']
    print 'tag :',tag
    if tag:
        quote=Quote.objects.get(id=quote_id)
        quote.save()
        quote.tags.add(tag)
    return redirect(reverse('quotes:contribute'))
    