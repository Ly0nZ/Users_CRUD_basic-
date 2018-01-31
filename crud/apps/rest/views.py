# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, HttpResponse
from .models import *
from django.contrib import messages
from django.db.models import Count

# Create your views here.
def index(request):
	users = User.objects.all()
	context = {
		'users': users
		}
	return render(request, 'rest/users.html', context)

def create(request):
 	user = User.objects.create(first_name = request.POST['first_name'],\
						last_name = request.POST['last_name'],\
						email = request.POST['email'])
	request.session['user_id'] = user.id
	return redirect('/index')

def del_user(request, user_id):
	user = User.objects.get(id=user_id)
	user.delete()
	return redirect('/')


def users(request):
	context = {

	}

def new(request):
	return render(request, 'rest/add_user.html')

def logout(request):
	request.session.clear()
	return redirect('/')

def show(request, user_id):
	user = User.objects.get(id=user_id)
	context = {
	'user': user
	}

	return render(request, 'rest/show.html', context)

def edit(request, user_id):
	user = User.objects.get(id=user_id)
	context = {
	'user': user
	}

	return render(request, 'rest/edit.html', context)

def editChange(request, user_id):
	user = User.objects.get(id=user_id)
	user.first_name = request.POST['first_name']
	user.last_name = request.POST['last_name']
	user.email = request.POST['email']
	user.save()
	return redirect('/index')

