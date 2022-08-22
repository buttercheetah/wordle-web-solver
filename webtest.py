from flask import Flask, redirect, url_for, request, render_template
app = Flask(__name__)
import os
import random
import time
import platform
letter1 = letter2 = letter3 = letter4 = letter5 = "_"
letter1isnt, letter2isnt, letter3isnt, letter4isnt, letter5isnt, niw, inw, dalst, guesls, toberem, guesses = (([], ) * 11)
def getwordlist():
    f = open(str(os.path.dirname(os.path.realpath(__file__))) + "/Words.txt", "r")
    x = str(f.readline())
    x = x.split(",")
    return x
def reset():
    global dalst, guesls, toberem, guesses, letter1, letter2, letter3, letter4, letter5, letter1isnt, letter2isnt, letter3isnt, letter4isnt, letter5isnt, niw, inw
    dalst = getwordlist()
    print(type(dalst))
    guesls = dalst.copy()
    toberem = []
    for word in guesls:
        letter = []
        for letters in word:
            if letters in letter:
                toberem.append(word)
            else:
                letter.append(letters)
    for i in toberem:
        try:
            guesls.remove(i)
        except:
            pass
    letter1 = letter2 = letter3 = letter4 = letter5 = "_"
    letter1isnt, letter2isnt, letter3isnt, letter4isnt, letter5isnt, niw, inw, guesses = (([], ) * 8)
def emptyguessletrem(letter):
    global dalst, guesls, toberem, guesses, letter1, letter2, letter3, letter4, letter5, letter1isnt, letter2isnt, letter3isnt, letter4isnt, letter5isnt, niw, inw
    removewords = []
    for word in guesls:
        if letter in word:
            #add word tobe removed
            removewords.append(word)
    for i in removewords:
        try:
            guesls.remove(i)
        except:
            pass
def excludeletterfromlist(letter):
    global dalst, guesls, toberem, guesses, letter1, letter2, letter3, letter4, letter5, letter1isnt, letter2isnt, letter3isnt, letter4isnt, letter5isnt, niw, inw
    removewords = []
    if letter.lower() in niw:
        pass
    else:
        niw.append(letter)
        print("Adding letter " + str(letter) + " at line 53")
    for word in dalst:
        if letter.lower() in word:
            #add word tobe removed
            if word in removewords:
                pass
            else:
                removewords.append(word) 
    print("[exclude letter] removing ",end="")
    if len(removewords) == 1:
        print("1 word")
    else:
        print(str(len(removewords)) + " words")
    for i in removewords:
        try:
            dalst.remove(i)
        except:
            pass
def includeletter(letter):
    global dalst, guesls, toberem, guesses, letter1, letter2, letter3, letter4, letter5, letter1isnt, letter2isnt, letter3isnt, letter4isnt, letter5isnt, niw, inw
    removewords = []
    if letter.lower() in inw:
        pass
    else:
        inw.append(letter)
        print("inncluding letter "+ str(letter) + " at line 78" )
    for word in dalst:
        if letter.lower() in word:
            pass
        else:
            #add word tobe removed
            if word in removewords:
                pass
            else:
                removewords.append(word) 
    print("[include letter] removing ",end="")
    if len(removewords) == 1:
        print("1 word")
    else:
        print(str(len(removewords)) + " words")
    for i in removewords:
        try:
            dalst.remove(i)
        except:
            pass
def findletterpos(lettertofind, word):
    for i in range(len(word)):
        if lettertofind == word[i]:
            return i
def countallleters():
    global dalst
    q=w=e=r=t=y=u=i=o=p=a=s=d=f=g=h=j=k=l=z=x=c=v=b=n=m=0
    for word in dalst:
        for letter in word:
            if letter == "q" : q += 1
            elif letter == "w": w += 1
            elif letter == "e": e += 1
            elif letter == "r": r += 1
            elif letter == "t": t += 1
            elif letter == "y": y += 1
            elif letter == "u": u += 1
            elif letter == "i": i += 1
            elif letter == "o": o += 1
            elif letter == "p": p += 1
            elif letter == "a": a += 1
            elif letter == "s": s += 1
            elif letter == "d": d += 1
            elif letter == "f": f += 1
            elif letter == "g": g += 1
            elif letter == "h": h += 1
            elif letter == "j": j += 1
            elif letter == "k": k += 1
            elif letter == "l": l += 1
            elif letter == "z": z += 1
            elif letter == "x": x += 1
            elif letter == "c": c += 1
            elif letter == "v": v += 1
            elif letter == "b": b += 1
            elif letter == "n": n += 1
            elif letter == "m": m += 1
    tmp = {}
    # I Know there is a better way to do this
    tmp['q']=q
    tmp['w']=w
    tmp['e']=e
    tmp['r']=r
    tmp['t']=t
    tmp['y']=y
    tmp['u']=u
    tmp['i']=i
    tmp['o']=o
    tmp['p']=p
    tmp['a']=a
    tmp['s']=s
    tmp['d']=d
    tmp['f']=f
    tmp['g']=g
    tmp['h']=h
    tmp['j']=j
    tmp['k']=k
    tmp['l']=l
    tmp['z']=z
    tmp['x']=x
    tmp['c']=c
    tmp['v']=v
    tmp['b']=b
    tmp['n']=n
    tmp['m']=m
    return max(tmp, key=tmp.get)

@app.route('/success/<name>')
def success(name):
   return 'welcome %s' % name

@app.route('/')
def maint():
   return render_template('wrong-page.html')

@app.route('/guess',methods = ['POST', 'GET'])
def guess():
    global dalst, guesls, toberem, guesses, letter1, letter2, letter3, letter4, letter5, letter1isnt, letter2isnt, letter3isnt, letter4isnt, letter5isnt, niw, inw
    if request.method == 'POST':
        try:
            t = request.form['1']
            c1 = True
        except:
            c1 = False
        try:
            t = request.form['2']
            c2 = True
        except:
            c2 = False
        try:
            t = request.form['3']
            c3 = True
        except:
            c3 = False
        try:
            t = request.form['4']
            c4 = True
        except:
            c4 = False
        try:
            t = request.form['5']
            c5 = True
        except:
            c5 = False
        try:
            if (request.form['cl'] == 'clear'):
                reset()
        except:
            guess = request.form['nm']
            if guess != "":
                guesses.append(str(guess))
                guesword = guess
                for letter in guesword:
                    emptyguessletrem(str(letter).lower())
                    if letter == letter.lower():
                        if letter.upper() not in inw:
                            excludeletterfromlist(letter)
                    if letter == letter.upper():
                        letterpos = findletterpos(letter, guesword) # get letter pos
                        if (letterpos) == 0: 
                            if c1 or letter1 == letter.lower():
                                cor = "Y"
                            else:
                                cor = "N"
                        elif (letterpos) == 1:
                            if c2 or letter2 == letter.lower():
                                cor = "Y"
                            else:
                                cor = "N"
                        elif (letterpos) == 2:
                            if c3 or letter3 == letter.lower():
                                cor = "Y"
                            else:
                                cor = "N"
                        elif (letterpos) == 3:
                            if c4 or letter4 == letter.lower():
                                cor = "Y"
                            else:
                                cor = "N"
                        elif (letterpos) == 4:
                            if c5 or letter5 == letter.lower():
                                cor = "Y"
                            else:
                                cor = "N"
                        if letter not in inw:
                            includeletter(letter) # include letter
                        if cor.upper() == "Y":
                            if (letterpos) == 0: letter1 = letter.lower()
                            elif (letterpos) == 1: letter2 = letter.lower()
                            elif (letterpos) == 2: letter3 = letter.lower()
                            elif (letterpos) == 3: letter4 = letter.lower()
                            elif (letterpos) == 4: letter5 = letter.lower()
                            wordstoremove = []
                            for word in dalst:  # goes through words inlist
                                if letter.lower() != word[int(letterpos)]: 
                                    wordstoremove.append(word)
                            for word in wordstoremove:
                                dalst.remove(word)
                        else:
                            if (letterpos) == 0: letter1isnt.append(letter.lower)
                            elif (letterpos) == 1: letter2isnt.append(letter.lower)
                            elif (letterpos) == 2: letter3isnt.append(letter.lower)
                            elif (letterpos) == 3: letter4isnt.append(letter.lower)
                            elif (letterpos) == 4: letter5isnt.append(letter.lower)
                            wordstoremove = []
                            for i in dalst:
                                #print(i[int(letterpos - 1)])
                                if letter.lower() == i[int(letterpos)]:
                                    wordstoremove.append(i)
                            for word in wordstoremove:
                                dalst.remove(word)
    else:
        user = request.args.get('nm')
    if len(dalst) == 1:
        answer = str("Answer is " + str(dalst).replace("]", "").replace("[", "").replace("'", ""))
    elif len(dalst) == 0:
        answer = 'There is no possible solution'
    elif len(dalst) <= 10:
        answer = str("Possible solutions remaining: ") + str(dalst).replace("]", "").replace("[", "").replace("'", "")
    else:
        answer = ""
    try:
        sg = "suggested guess: "
        tmp = ""
        tmpcount = 0
        good = ""
        mostlet = countallleters()
        while (mostlet not in tmp) and good != "good":
            tmp = (dalst[random.randrange(0,len(dalst))])
            good = ""
            for letter in tmp:
                co = tmp.count(letter)
                if co > 1:
                    good = "false"
            print("discarding " + str(tmp))
            if good == "": good = "good"
            tmpcount += 1
            if tmpcount == 50:
                sg = sg + "possibly "
                break
        sg = sg + tmp
        try:
            ag = ("Alternative guess: " + str(guesls[random.randrange(0,len(guesls))]))
        except Exception as e:
            print(e)
            pass
    except Exception as e:
        print(e)
        sg = ""
        ag = ""
    letters = letter1 + letter2 + letter3 + letter4 + letter5
    icll = str(inw).replace("]", "").replace("[", "").replace("'", "")
    nicll = str(niw).replace("]", "").replace("[", "").replace("'", "")
    print(icll)
    print(inw)
    print(niw)
    print(nicll)
    return render_template('guess.html', icll=icll, nicll=nicll, letters=letters, sg=sg, ag=ag, ps=str(len(dalst)), answer=answer, guesses=str(guesses).replace("[","").replace("]","").replace("'",""))
  
if __name__ == '__main__':
    reset()
    app.run(host="0.0.0.0", port=8000, debug = True)