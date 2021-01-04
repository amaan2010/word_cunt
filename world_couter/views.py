from django.shortcuts import render
from django.http import HttpResponse
import operator
def homepage(request):
    return render(request,'index.html')


def count(request):
    data = request.GET['fulltextarea']
    word_list = data.split()    
    list_len = len(word_list) 

    worddictionary = {}
    for Word in word_list:
        if Word in worddictionary:
            worddictionary[Word] += 1
        else:
            worddictionary[Word] = 1
    Sorted_list = sorted(worddictionary.items(),key = operator.itemgetter(1),reverse=True)
    return render(request,'Count.html',{'fulltext':data, 'Words': list_len, 'worddictionary': Sorted_list })
    