#!/usr/bin/env python
# -*- coding: utf-8 -*-
import tweepy
from django.db import connection
from keijiban.models import Tweet,ID
import re
import urllib



class tweet:


 def tweetimport(username):
  CK = 'PT8KnQQMiN4zkkHRphTMkOBeV'                        # Consumer Key
  CS = 'c3XCPPDfxGU5thWFATcIhrUfJXVmA9nrHSAt1AnsYzyaZuu6Mi'         # Consumer Secret
  AT = '535210488-eF2rg8LdBgLvfRfTux1m3fvG3XxvwpwfzAVWY02N' # Access Token
  AS = '0H871S8YSmKhusbOdMYF2odaz0XPZCO2qk2WTdd5suwMu'         # Accesss Token Secert

  auth = tweepy.OAuthHandler(CK, CS)
  auth.set_access_token(AT, AS)
  api = tweepy.API(auth)

#全部のツイート、IDを格納
  gotwe = []
  gotid = []
#

  sldtwe =[] #取得したツイートからサンクラとyoutubeのツイートを取り出したやつを格納するやつ
  sldlink = []#ついーとへのりんく
  sldurl = []#ツイートに含まれているURLを展開したURL

 #username = input()

 #dbに以前格納したついーとの削除
  delete = Tweet.objects.all()
  delete.delete()
  delete2 = ID.objects.all()
  delete2.delete()
 #------------------------------

  try:
   u = str(username)
   saveid = ID(USERID=u)
   saveid.save()

   firsttweets = api.user_timeline(str(username),count=1,include_rts='false',exclude_replies='false')


   for i in firsttweets: #最新ツイートのidをfirst_idに代入
     i_json = i._json
     first_id = int(i_json["id"])




   for i in range(5):
     tweets = api.user_timeline(str(username),count = 200,max_id=first_id,include_rts='false',exclude_replies='false')
     for t in tweets:
         t_json = t._json      # statusおぶじぇくとをjson(dict)にへんかん

         #print(t_json["text"])
         gotwe.append(str(t_json["text"]))
         gotid.append(int(t_json["id"]))
         max_id = int(t_json["id"])
     first_id=max_id

   pattern = re.compile("(https://.+ )") #最後に空白のあるURL
   pattern2 = re.compile('https://.+$') #文末にあるURL
   zenkaku = re.compile(r'^[\x20-\x7E]+$')

   for i in range(len(gotwe)):
      #gotweからpattern,pattern2を検索
     m = pattern.search(gotwe[i])
     n = pattern2.search(gotwe[i])

     try:  #404対策
      if m: #gotweにpatternがあった場合
       q = m.group(0).replace(' ','') #mから空白を削除&str化
       r = zenkaku.search(q) #qがascii文字のみで構成されているかのチェック（ascii以外の文字があるとurlopenで開けない）
       if r != None: #rがasciiのみだった場合
        enc = urllib.request.urlopen(q).geturl() #q(短縮URL)を開きちゃんとしたURLを取得

       #以下、指定した語句がちゃんとしたURLに含まれているかのチェック
        if 'youtube.com' in enc:

         sldtwe.append(gotwe[i])
         sldlink.append('<a style="vertical-align: middle; display: block; width: 100%; height: 100%" href="http://twitter.com/'+str(username)+'/status/'+str(gotid[i])+'"target="_blank">Twitter</a>')
         sldurl.append(enc)

        elif 'soundcloud.com' in enc:

         sldtwe.append(gotwe[i])
         sldlink.append('<a style="vertical-align:middle; display: block; width: 100%; height: 100%" href="http://twitter.com/'+str(username)+'/status/'+str(gotid[i])+'"target="_blank">Twitter</a>')
         sldurl.append(enc)

        elif 'itunes.apple.com' in enc:
         sldtwe.append(gotwe[i])
         sldlink.append('<a style="vertical-align:middle; display: block; width: 100%; height: 100%" href="http://twitter.com/'+str(username)+'/status/'+str(gotid[i])+'"target="_blank">Twitter</a>')
         sldurl.append(enc)

        elif 'spotify.com' in enc:
         sldtwe.append(gotwe[i])
         sldlink.append('<a style="vertical-align:middle; display: block; width: 100%; height: 100%" href="http://twitter.com/'+str(username)+'/status/'+str(gotid[i])+'"target="_blank">Twitter</a>')
         sldurl.append(enc)

      if n:#gotweにpattern2があった場合
       q = n.group(0)#.replace(' ','')
       r = zenkaku.search(q)
       if r != None:
        enc = urllib.request.urlopen(q).geturl()

        if 'youtube.com' in enc:

         sldtwe.append(gotwe[i])
         sldlink.append('<a style="vertical-align: middle; display: block; width: 100%; height: 100%" href="http://twitter.com/'+str(username)+'/status/'+str(gotid[i])+'"target="_blank">Twitter</a>')
         sldurl.append(enc)

        elif 'soundcloud.com' in enc:

         sldtwe.append(gotwe[i])
         sldlink.append('<a style="vertical-align:middle; display: block; width: 100%; height: 100%" href="http://twitter.com/'+str(username)+'/status/'+str(gotid[i])+'"target="_blank">Twitter</a>')
         sldurl.append(enc)

        elif 'itunes.apple.com' in enc:
         sldtwe.append(gotwe[i])
         sldlink.append('<a style="vertical-align:middle; display: block; width: 100%; height: 100%" href="http://twitter.com/'+str(username)+'/status/'+str(gotid[i])+'"target="_blank">Twitter</a>')
         sldurl.append(enc)

        elif 'spotify.com' in enc:
         sldtwe.append(gotwe[i])
         sldlink.append('<a style="vertical-align:middle; display: block; width: 100%; height: 100%" href="http://twitter.com/'+str(username)+'/status/'+str(gotid[i])+'"target="_blank">Twitter</a>')
         sldurl.append(enc)




     except urllib.error.HTTPError: #404が返ってきたときはパスする
         pass

   #dbにツイートを格納
   for i in range(len(sldtwe)):
       t = sldtwe[i]
       l = sldlink[i]
       u = sldurl[i]
       db = Tweet(twidata=t,twilink=l,twiurl=u) #'''id=i'''
       db.save()

   return 0;
  except tweepy.error.TweepError:
   return 1;
