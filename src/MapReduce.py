import sys
import re

def main():
  
    #Inicializamos variables
    path = "./textFiles/"
    dic = []
    words = []
    
    
    for i in range(1, len(sys.argv)):
        
         #Abrimos y leemos el fichero   
        textfile = open(path+sys.argv[i], encoding="UTF-8")
        textfile = textfile.read()
     
        #Separamos las palabras
        textfile = re.sub("\n", ' ', textfile)
        textfile = re.sub("([^\w\sà-úÀ-Ú'·-])", '', textfile)
        words = textfile.split(" ")
        
        
        #MAP      
        for word in words:
            dic.append([word.lower(),1])
        dic.sort()
        
    
        #SHUFFLE
        dicShuffle = {}
        for i in range(len(dic)):
            if dic[i][0] not in dicShuffle:
                dicShuffle[dic[i][0]] = []
            dicShuffle[dic[i][0]].append(dic[i][1])
      
        
        #REDUCE
        for word in dicShuffle:
            dicShuffle[word] = sum(dicShuffle[word])
        
        print(dicShuffle)
        
if __name__ == '__main__':
    main()