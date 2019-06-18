#import pandas as pd
#import numpy as np
#import PyPDF2
#import textract
import re
import matplotlib.pyplot as plt
import matplotlib as mpl
#import ctypes
import tkinter
import tkinter.messagebox as tk
from autocorrect import spell

'''''
filename ='JavaBasics-notes.pdf' 

pdfFileObj = open(filename,'rb')               
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)   
num_pages = pdfReader.numPages                 


count = 0
text = ""
                                                            
while count < num_pages:                       
    pageObj = pdfReader.getPage(count)
    count +=1
    text += pageObj.extractText()
    
if text != "":
    text = text
 
else:
    text = textract.process('http://bit.ly/epo_keyword_extraction_document', method='tesseract', language='eng')

print(len(text))
'''''

def validation(filename):
    text=[]
    f = open(filename)
    for word in f.read().split():
        text.append(word)
    #print(l1)
    #text = text.encode('ascii','ignore').lower()
    l=["java","in","at"]
    d={}
    c=0
    for i in l:
        #i=bytes(i, "utf8")
        for j in text:
            if i==j.lower():
                c=c+1
        #keywords = re.findall(i,text)
        #d[i]=len(keywords)
        d[i]=c
    print(d)
    #df = pd.DataFrame(list(set(keywords)),columns=['keywords'])





    #def weightage(word,text,number_of_documents=1):
        #word_list = re.findall(word,text)
        #number_of_times_word_appeared =len(word_list)
        #tf = number_of_times_word_appeared/float(len(text))
        #idf = np.log((number_of_documents)/float(number_of_times_word_appeared))
        #tf_idf = tf*idf
        #return number_of_times_word_appeared,tf,idf ,tf_idf 


    
    #df['number_of_times_word_appeared'] = df['keywords'].apply(lambda x: weightage(x,text)[0])
    #df['tf'] = df['keywords'].apply(lambda x: weightage(x,text)[1])
    #df['idf'] = df['keywords'].apply(lambda x: weightage(x,text)[2])
    #df['tf_idf'] = df['keywords'].apply(lambda x: weightage(x,text)[3])
    
    #df = df.sort_values('tf_idf',ascending=True)
    #df.head(1000)     


    #-----------------------severity--------------------------
    #--------------------keyword matching---------------------

    count=0
    total=len(text)
    #d1={b'java':7, b'in':6, b'at':5}
    d1={'java':7, 'in':6, 'at':5}
    for i in l:
        #i=bytes(i, "utf8")
        count=count+(d[i]*d1[i])

    sev=(count/(total+count))*100
    #print(sev)

    #---------------------semantic search---------------------

    def file_read(fname):
             with open(fname) as f:
                     #Content_list is the list that contains the read lines.     
                     content_list = f.readlines()
                     return content_list

    l2=[]
    l2=file_read('java.txt')
    #print(l2)

    def lcs(X, Y):
        mat = []
        for i in range(0,len(X)):
            row = []
            for j in range(0,len(Y)):
                if X[i] == Y[j]:
                    if i == 0 or j == 0:
                        row.append(1)
                    else:
                        val = 1 + int( mat[i-1][j-1] )
                        row.append(val)
                else:
                    row.append(0)
            mat.append(row)
        new_mat = []
        for r in  mat:
            r.sort()
            r.reverse()
            new_mat.append(r)
        lcs = 0
        for r in new_mat:
            if lcs < r[0]:
                lcs = r[0]
        return lcs
    def spellCorrect(string):
        words = string.split(" ")
        correctWords = []
        for i in words:
            correctWords.append(spell(i))
        return " ".join(correctWords)
    def semanticSearch(searchString, searchSentencesList):
        result = None
        searchString = spellCorrect(searchString)
        bestScore = 0
        for i in searchSentencesList:
            score = lcs(searchString, i)
            if score > bestScore:
                bestScore = score
                result = i
        return result


    result = semanticSearch("Primitive types are assigned, compared",l2)
    #print(result)

    l3=[]
    l3=re.findall(r'\w+', result)
    print(l3)
    s=0
    l4=['primitive','compared','copy']
    for i in l3:
        #print(i)
        if i.lower() in l4:
            s=s+1
    #print(s)

    if s>=len(l4):
        sev=sev+(3*(100-sev)/4)
    elif s>(3*len(l4)/4) and s<len(l4):
        sev=sev+(2*(100-sev)/3)
    elif s>(len(l4)/2) and s<(3*len(l4)/4):
        sev=sev+((100-sev)/2)
    elif s>(len(l4)/4) and s<(len(l4)/2):
        sev=sev+((100-sev)/3)
    elif s>0 and s<(len(l4)/2):
        sev=sev+((100-sev)/4)
    else:
        sev=sev
    
    print(sev)


    #-----------------------plot-----------------------

    fig, ax = plt.subplots(figsize=(6, 1))
    fig.subplots_adjust(bottom=0.5)

    cmap = mpl.colors.ListedColormap(['green', 'yellow', 'orange', 'red'])
    cmap.set_over('0.25')
    cmap.set_under('0.75')

    bounds = [1, 20, 40, 70, 100]
    norm = mpl.colors.BoundaryNorm(bounds, cmap.N)
    cb2 = mpl.colorbar.ColorbarBase(ax, cmap=cmap,
                                    norm=norm,
                                    boundaries=[0] + bounds + [13],
                                    extend='both',
                                    ticks=bounds,
                                    spacing='proportional',
                                    orientation='horizontal')
    cb2.set_label('Discrete intervals, some other units')
    fig.show()

    if(sev<20):
        tk.showinfo(title="Alert!", message="Severity is LOW")
        #ctypes.windll.user32.MessageBoxW(0, "severity is LOW", "Warning!", 1)
    elif(sev<40 and sev>=20):
        tk.showinfo(title="Alert!", message="Severity is MODERATE")
        #ctypes.windll.user32.MessageBoxW(0, "severity is MODERATE", "Warning!", 1)
    elif(sev>=40 and sev<70):
        tk.showinfo(title="Alert!", message="Severity is HIGH")
        #ctypes.windll.user32.MessageBoxW(0, "severity is HIGH", "Warning!", 1)
    else:
        tk.showinfo(title="Alert!", message="Severity is RISKY")
        #ctypes.windll.user32.MessageBoxW(0, "severity is RISKY", "Warning!", 1)

    return sev
