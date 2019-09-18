#!/usr/bin/env python
# coding: utf-8

# In[79]:


import math
import re
import operator
with open("DS/Corpus.txt","r+") as a:#importing the corpus
    corpus=a.read()
with open("DS/Stopwords.txt","r+") as b: #importing stopwords
    stopwords=b.read()


# In[80]:


def doc_ID(txt):
    if re.search("^Document.*\d$",txt): 
        return True
def number_check(txt):
    if re.search("\d",txt):
        return True
    else:
        return False
#imported from the inverted index project


# In[81]:


#term frequency weighting
def tf(t,d):
    term_frequency=0
    Doc_ID=0
    for i in corpus.split(" "):
        if doc_ID(i):
            Doc_ID+=1
        if Doc_ID==d:
            if i==t:
                term_frequency+=1
    return term_frequency
def w_tf(t_f):
    if t_f>0:
        return 1+math.log10(t_f)
    else:
        return 0


# In[82]:


#in this part we return the term frequency weighting for a given word in all the documents
# t=str(input("please enter the term "))
# for i in range(0,7):
#     print(t+"  "+str(w_tf(tf(t,i+1))))


# In[83]:


#idf score
def df(t):
    check=False  
    counter=0
    tf=0
    for i in corpus.split(" "):
        if doc_ID(i):
            check=False
        if i == t and check==False:
            counter+=1
            check=True
    tf=counter
    return counter
#the check variable is used to ignore the rest of the terms in a document when a matching term is found! it works like a flag

def idf(N,df):
    try:
        return math.log10(N/df)
    except: #since we can have term with zero document frequnecy,it is possible to face a division by zero error
        print("df value is equal to zero")


# In[84]:


#tf-idf weighting
def tf_idf_weighting(w_tf,idf):  #this fucntion needs idf and term frequency weighting(w_tf) as inputs
    try:
        return w_tf*idf
    except:
        print("df value is equal to zero so tf-idf value is")
#the term frequency used in this functin is just for one document...not for all of them                                
#we have to call this function multiple times for multiple use


# In[93]:


#we use the scoring method mentioned in the book
#by the term "score" we mean the sum of tf-idf weightings for term in a given query in a document
query=str(input("enter the query: "))
tf_idf_dict=dict()
for i in query.split(" "):
    for j in range(0,7):
        print("tf-idf weighting for term "+i+" in the given query: "+query+" in document number: "+str(j+1)+" is "+str(tf_idf_weighting(idf(7,df(i)),w_tf(tf(i,j+1)))))
        if tf_idf_weighting(idf(7,df(i)),w_tf(tf(i,j+1)))!=None:
            tf_idf_dict.update({str(j+1)+" "+i:tf_idf_weighting(idf(7,df(i)),w_tf(tf(i,j+1)))})#to store tf-idf weightings for different terms in a given query and documents


# In[94]:


print(tf_idf_dict)
#doc id , term , tf-idf-weighting


# In[95]:


try:
    sorted_tf_idf=sorted(tf_idf_dict.items(), key=operator.itemgetter(1))#givers items in decreasing order
    for i in reversed(sorted_tf_idf):
        print(i)
except:
    print("some sort of error occurred!")


# In[ ]:





# In[ ]:




