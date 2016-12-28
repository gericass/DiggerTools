from django.shortcuts import render
from keijiban.forms import idkakikomi
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from keijiban.twitter import tweet
from keijiban.models import Tweet,ID
from django.template.loader import get_template
# Create your views here.
from keijiban.twitter import tweet
from django.http import HttpResponseRedirect
from django.shortcuts import render
from keijiban.forms import idkakikomi

def kakikomi(request):
  if request.method=='POST':
     f = idkakikomi(request.POST)
     if f.is_valid():
      userid = f.cleaned_data['id']
      q = tweet.tweetimport(str(userid))
      #tweets = Tweet.objects.all()
      #link = get_template('results.html')
      #return link.render(request)#,{'form2':tweets}) #{'id':f}
      if q==0:
       return HttpResponseRedirect('/keijiban/idinput/results/')
      else:
        return HttpResponseRedirect('/keijiban/idinput/ineeyo/')
  else:
     f = idkakikomi()

  return render(request,'templates.html',{'form1':f})


def results(request):
    tweets = Tweet.objects.all().order_by('id')
   # id = ID.objects.all()

    return render(request,'results.html',{'tweets':tweets})


def inee(request):
    return render(request,'inee.html',{})

