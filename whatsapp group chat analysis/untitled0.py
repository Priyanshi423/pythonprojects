# -*- coding: utf-8 -*-
"""
Created on Sat Apr  3 21:09:51 2021

@author: DELL

"""
import regex
import emoji
import advertools as adv

#print(" 😂😂❤❤")
t="hy 😂"
"""t=["hy 😂❤ ❤"]



emoji_list = []
emoji_list=adv.extract_emoji(t)
print(emoji_list)
n=emoji_list['emoji'][0]
print(n)            
orig_list = ['These 👧 Emojis, 😈 are 🤖 embedded 😺 within 😻 this 🙀 text.']

 ## Use advertools to process orig_list. A dictionary is returned. 
emoji_dict = adv.extract_emoji(orig_list)"""
""">>>
>>> ## This dictionary is packed with all sorts of statistical information about orig_list.
>>> ## We want specific information, which is enclosed in the ‘emoji’ key.
>>> ## Also the returned value is a list of lists. We need only the first list."""

"""emoji_list = []
data = regex.findall(r'\X', t)
for word in data:
        if word in emoji.UNICODE_EMOJI :
            emoji_list.append(word)

print(emoji_list)    """
import pandas as pd
csv=pd.read_csv('colors.csv',header=None)
print(csv)

  