#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import codecs
import re

def main():
    
    print 'Number of arguments:', len(sys.argv), 'arguments.'
    print 'Argument List:', str(sys.argv)
    print
    
    path = "./textFiles/"
    dic = []
    words = []
    
    
    for i in range(1, len(sys.argv)):
        
        textfile = open(path+sys.argv[i], "r")
#        textfile = codecs.open(path+sys.argv[i], "r", "utf-8")

        textfile = textfile.read()
        textfile = textfile.decode("UTF-8").encode(sys.stdin.encoding)
        textfile = re.sub(r'^\W+|\W+$', '', textfile)
        
        words = textfile.split(" ")
        
        
        """MAP"""
        for i in range(len(words)):
            words[i].lower()
            dic.append([words[i]])
            """SHUFFLE"""
            for d in dic:
                if words[i]  in d:
                    d.append("1")
             
        dic.sort()
        print dic
        
        
        """REDUCE"""
        previous = None
        sum = 0
        value = ""
        for i in range(len(dic)):
            key= dic[i][0]
            value = dic[i][1]
            
            if key != previous:
                if previous is not None:
                    print previous + " : " + str(sum) + '\t' 
                previous = key
                sum =0
            sum = sum + int(value)
        print previous + " : " + str(sum) 
    
    
if __name__ == '__main__':
    main()
    
    
    