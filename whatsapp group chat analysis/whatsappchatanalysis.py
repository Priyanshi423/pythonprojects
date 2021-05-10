# -*- coding: utf-8 -*-
"""
Created on Thu Apr  1 17:46:06 2021

@author: DELL
"""
import advertools as adv
import regex 
import pandas as pd
import numpy as np
import emoji
from collections import Counter
from os import path
from PIL import Image
from wordcloud import WordCloud,STOPWORDS,ImageColorGenerator
import plotly.express as px
import matplotlib.pyplot as plt
#to check if a line starts with date and time . if it is the it is a new message
#import regex as re
import regex as re
def startsWithDateAndTime(s):
    pattern = '^([0-9]+)(\/)([0-9]+)(\/)([0-9]+), ([0-9]+):([0-9]+)[ ]?(AM|PM|am|pm)? -'
    result=re.match(pattern, s)
    if result:
        return True
    else:
        return False
#startsWithDateAndTime('22/09/21, 12:09pm -')
#######################################
def findauthor(s):
    s=s.split(":")
    if(len(s)==2):
        return True
    else:
        return False
def getdatapoint(line):
    splitline=line.split(' - ')
    dateTime=splitline[0]
    date,time=dateTime.split(', ')
    message=' '.join(splitline[1:])
    if findauthor(message):
        splitmessage=message.split(': ')
        author=splitmessage[0]
        message=' '.join(splitmessage[1:])
    else:
        author=None
    return date, time, author, message

#from google.colab import files
#uploaded=files.upload()
import os 

data=[]

with open ('whatsapp.txt',encoding="utf-8") as fp:
    fp.readline()
    messagebuffer=[]
    parsedData=[]
    date,time,author=None,None,None
    while True:
        line=fp.readline()
        if not line:
            break;
        line=line.strip()
        if startsWithDateAndTime(line):
            if len(messagebuffer) >0:
                parsedData.append([date,time,author,' '.join(messagebuffer)])
            messagebuffer.clear()
            date,time,author,message=getdatapoint(line)
            messagebuffer.append(message)
        else:
            messagebuffer.append(line)
            
df=pd.DataFrame(parsedData,columns=['date','time','author','message'])
df['date']=pd.to_datetime(df["date"])
print(df.tail(5))   
#GET THE NAMES OF ALL PARITIPANTS OF THE GROUP


df=df.dropna()

print(df.author.unique())
total_message=df.shape[0]
#print(total_message)
media_messages=df[df['message']=='<Media omitted>'].shape[0]# shape[0] is telling the number of rows


text="hy this is priya"
data = regex.findall(r'\X', text)
#print(data)
#print(media_messages)
def split_count(text):
    li=[text]
    
    n = []
    emoji_list=adv.extract_emoji(li)
    
    n=emoji_list['emoji'][0]
         

    return n

df["emoji"] = df["message"].apply(split_count)
  
#df["emoji"]=df["message"].apply(split_count)

#print(df["emoji"])
emojis=sum(df['emoji'].str.len())
total_messages=df.shape[0]

URLPATTERN=r'(https?://\S+)'
df['urlcount']=df.message.apply(lambda x:re.findall(URLPATTERN, x)).str.len()
#print(df['urlcount'])
links=np.sum(df.urlcount)
print('data science  community') 
print('messages',total_messages)
print("media:",media_messages)
print("emojis:",emojis)
print("links:",links)
#print(df.head(20))
#print(df[df['urlcount']>0]['message'])
media_messages_df=df[df['message']=='<Media omitted>']
message_df=df.drop(media_messages_df.index)
print(message_df.info())
print(df.info())
message_df['letter count']=df.message.apply(lambda s: len(s))
message_df['word count']=df.message.apply(lambda s: len(s.split(" ")))
message_df['messagecount']=1
l=["Nidhi","Priyanshi Agarwal","Shefali","Simran","Pranjal Vyas"]
for i in range (len(l)):
    req_df=message_df[message_df["author"]==l[i]]
    print(f'stats of {l[i]} -')
    print("messages sent:",req_df.shape[0])
    wor=(np.sum(req_df['word count']))/req_df.shape[0]
    print("words per message",wor)
    media=media_messages_df[media_messages_df['author']==l[i]].shape[0]
    print("media messages:",media)
    e=sum(req_df['emoji'].str.len())
    print("emojis sent",e)
    li=sum(req_df["urlcount"])
    print("links:",li)
total_emoji_list=list([a for b in message_df.emoji for a in b ])
emoji_dict=dict(Counter(total_emoji_list) )
#print(emoji_dict)
emoji_dict=sorted(emoji_dict.items(),key=lambda x:x[1],reverse=True)
for i in emoji_dict:
    print(i)
text=" ".join(r for r in message_df.message) 
print(text) 
print("there are {} words in the message",format(len(text)))
stopwords=set(STOPWORDS)
stopwords=["kya","toh","toh","ki","hai","se","koi","haan","hi","me","h","ky","nahi","yr","m","ye","he","are","to","abhi","ka","tho","or","na","haa","han","fir"]
wordcloud=WordCloud(stopwords=stopwords,background_color="white").generate(text)
plt.figure(figsize=(10,5))
plt.imshow(wordcloud,interpolation="bilinear")
plt.axis("off")
plt.show()
l=["Shefali","Simran","Pranjal Vyas","Nidhi","Priyanshi Agarwal"]
for i in range(len(l)):
    dummy_df=message_df[message_df["author"]==l[i]]
    text=" ".join(r for r in dummy_df.message)
    stopwords=set(STOPWORDS)
    stopwords=["kya","toh","toh","ki","hai","se","koi","haan","hi","me","h","ky","nahi","yr","m","ye","he","are","to","abhi","ka","tho","or","na","haa","han","fir"]

    wordcloud=WordCloud(stopwords=stopwords,background_color="white").generate(text)
    print(l[i])
    plt.figure(figsize=(10,5))
    plt.imshow(wordcloud,interpolation="bilinear")
    plt.axis("off")
    plt.show()
    



  


