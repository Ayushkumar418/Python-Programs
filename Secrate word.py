import random
words=input("Enter the words: ").split(" ")
x=(input("Press 1 for Encrypted or Press 0 for  Decrypted: "))
if x=="1":
    st_word=["fkj","fhy","len","uvj","hgt","*ge","c@t","yui","v6f","vie","bxo","dog","e$g","a*a","dfj","ofs","qui","shu","yar","amu","kur","a&z","b^p","i*+","n/t","*x*",",-_","key","wow","<v>",">a<","u!b","q@a","n*l","uja","an.","etc","Ext","dkd","4k.","awm","bye"]
    nword=[]
    for word in words:
        if len(word)>=3:
            st1=random.choice(st_word)
            st2=random.choice(st_word)
            st_n=st1+word[1:]+word[0]+st2
            stnew = st_n[len(st_n)//2:] + st_n[:len(st_n)//2]
            nword.append(stnew)
        else:
            nword.append(word[::-1])
    print("Encrypted: "," ".join(nword))
elif  x=="0":
    nword=[]
    for word in words:
        if len(word)>=3:
            if len(word)%2 == 0:
                word = word[len(word)//2:] + word[:len(word)//2]
            else:
                word = word[len(word)//2+1:] + word[:len(word)//2+1]
            stnew=word[3:-3]
            stnew=stnew[-1]+stnew[:-1]
            nword.append(stnew)
        else:
            nword.append(word[::-1])
    print("Decrypted: "," ".join(nword))
else:
    print("Invalid input.")