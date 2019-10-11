from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponse
from .func_modules import searchword, sorting, word_filter
import json, os, re


def index(request):
    word_data = word_filter()
    return render(request, "autocomplete/index.html", {"all_data": word_data})


def search(request):
    all_words = word_filter()
    if request.method == 'GET':
        query = request.GET.get('word')
        if query:
            searchResult = sorting(searchword(query.lower()), query.lower())
            if len(searchResult) == 0:
                return JsonResponse({'Search_Result': "Word not found."})
            else:
                return JsonResponse({'Search_Result': searchResult})
        else:
            return redirect('/')
