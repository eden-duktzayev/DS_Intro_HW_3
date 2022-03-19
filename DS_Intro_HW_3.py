#QA:
def read_line(n,file):
    x='invalid input detected'
    ON_OFF = False
    if type(n)==str:
        return x
    else:
        try:
            text = open(file,'r')
        except FileNotFoundError :
            x='file not found'
            ON_OFF==True
        if ON_OFF==False:
            f_Lines=text.readlines()
            if n > len(f_Lines):
                x = "line {num} doesn't exist".format(num=n)
                ON_OFF==True
            if ON_OFF==False:
                counter=0
                for word in f_Lines:
                    word=word.rstrip()
                    counter+=1
                    if counter==n:
                        x=word
                        break
        return x

#QB:
def longest_words(file):
    try:
        myText=open(file, 'r')
    except:
        err = "file npt found"
        ON_OFF = True
        return err
    if ON_OFF == False:
        myText=myText
        f_words=myText.read()
        f_words_split=re.split('[\s+ . )]' , f_words)
        for word in f_words_split:
            if word in freqlist or '-' in word:
                continue
            else:
                freqlist.append(word)
        freqlist=sorted(freqlist, key=len , reverse=True)[:5]
        return freqlist
