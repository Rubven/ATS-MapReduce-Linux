import sys
import re

def map(dic, words):
    
    #MAP
    for i in range(len(words)):
        dic.append([words[i].lower(),1])
        
    dic.sort()
    return dic

def shuffle(dicShuffle, dic):
    #SHUFFLE

    for i in range(len(dic)):
        if dic[i][0] not in dicShuffle:
            dicShuffle[dic[i][0]] = []
        dicShuffle[dic[i][0]].append(dic[i][1])
       
    return dicShuffle
    
def reduce(dic):
     #REDUCE

     for word in dic:
         dic[word] = sum(dic[word])
     
def main():
  
    #Inicializamos variables
    path = "./textFiles/"
    
    words = []
    dic = []
   
    dicShuffle = {}
    
    for i in range(1, len(sys.argv)):
        
         #Abrimos y leemos el fichero   
        textfile = open(path+sys.argv[i], encoding="UTF-8")
        textfile = textfile.read()
     
        #Separamos las palabras
        textfile = re.sub("\n", ' ', textfile)
        textfile = re.sub("([^\w\sà-úÀ-Ú'-])", '', textfile)
        words = textfile.split(" ")
        
        dicmapped = map(dic, words)
        dicShuffled = shuffle(dicShuffle, dicmapped)  
        print(dicShuffled)
        reduce(dicShuffled)
       
       
if __name__ == '__main__':
    main()