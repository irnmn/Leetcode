# -*- coding: utf-8 -*-
"""
Created on Mon Aug 10 06:02:59 2020

@author: ademiray
"""


#1119 Remove Vovels from a string

#Given a string s, remove vovels 'a', 'e', 'i','o' and 'u' from it, and return new string


vovels = ['a','e','i','o','u']

test = "leetcodeisacommunityforcoders"


def remove_vovels(test):
    
    vovels = ['a','e','i','o','u']

    for v in test.lower():
        if v in vovels:
            
            test = test.replace(v,"")
            
    return test

print(remove_vovels(test))