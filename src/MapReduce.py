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
        textfile = re.sub("([^\w\sà-úÀ-Ú'-])", '', textfile)
        words = textfile.split(" ")
        
        
        #MAP
        for i in range(len(words)):
            words[i].lower()
            dic.append([words[i],1])
        dic.sort()
        
               
        #SHUFFLE
        dic2 = {}
        for i in range(len(dic)):
           if dic[i][0] in dic2:
                dic2[dic[i][0]].append(dic[i])
           else:
                dic2[dic[i][0]] = dic[i]

        #REDUCE
        previous = None
        sum = 0
        value = ""
        for i in range(len(dic)):
            key= dic[i][0]
            value = dic[i][1]
            
            if key != previous:
                if previous is not None:
                    print(previous + " : " + str(sum) + '\t')
                previous = key
                sum =0
            sum = sum + int(value)
       
if __name__ == '__main__':
    main()