import search
import pandas as pd
import numpy as np
import numpy.linalg as la









alphabet= {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7, 'i': 8, 'j': 9, 'k': 10, 'l': 11, 'm': 12, 'n': 13, 'o': 14, 'p': 15, 'q': 16, 'r': 17, 's': 18, 't': 19, 'u': 20, 'v': 21, 'w': 22, 'x': 23, 'y': 24, 'z': 25}

txt=pd.read_csv("text.txt",header=None).astype(str)
txt=txt.to_numpy()

def string_to_matrix(word):
  carrier=np.zeros((1,26))
  # print(word)
  for i in word:
    carrier[0][alphabet[i]]+=1
  return carrier
def list_to_matrix(txt):
  hold=np.zeros((len(txt),26))
  for i in range(len(txt)):
    txt[i][0]=str(txt[i][0])
    hold[i]=string_to_matrix(txt[i][0])
  return hold
hold=list_to_matrix(txt)
hold_N=(hold/(la.norm(hold,axis=1).reshape(-1,1)))
length=np.sum(hold,axis=1).reshape(-1,1)


def angle_matrix(word):
  word_=string_to_matrix(word)
  a=len(word)
  # l=(abs(length-a)/a-1)**(3)
  word_=word_/la.norm(word_)
  return np.arccos(np.round_(hold_N@word_.T,decimals=5))
def find_relative(word):
  angle=angle_matrix(word)
  idx = np.argpartition(angle,3, axis=0)
  return idx.reshape(-1,)
def relative_word(word,cut_off=5):
  a=find_relative(word)
  return txt[a][:cut_off,:].reshape(-1,)
def arrange(word,short):
  if not isinstance(short, list):
    short=short.tolist()
  short.sort(key=lambda x:abs(len(x)-len(word)))
  for i in range(len(short)):
    if short[i] ==word:
      a=short.pop(i)
      short.insert(0,a)
      return short
  return short
def relative_search(word,method):
    if method==1:
        return arrange(word,relative_word(word,7))
    elif method==2:

        a=search.bst(word)
        if search.get_value(a)==word:
            l=[word]
            
            l.append(search.get_value(a-2))
            l.append(search.get_value(a-1))
            l.append(search.get_value(a+1))
            l.append(search.get_value(a+2))
        else:
            l=[search.get_value(a-2+i) for i in range(7)]
        return l
    elif method==3:
        bigl=angle_matrix(word).T.tolist()[0]
        l=search.avl(bigl)
        return arrange(word,[txt[i][0] for i in l])
    elif method==4:
        a=search.bf(word)
        if a>0:
        
            return [search.get_value(a),search.get_value(a-1),search.get_value(a-2),search.get_value(a+1),search.get_value(a+2)]
        else: 
            return []
    
"""
if __name__ == "__main__":

    w="morning"
    print(relative_search(w,1))
    print(relative_search(w,2))
    print(relative_search(w,3))
    print(relative_search(w,4))

"""





















