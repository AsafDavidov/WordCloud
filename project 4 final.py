#Main word cloud function
#Asaf Davidov
from graphics import *
from random import *
from time import *
    
def drawButton(gwin, pt1, pt2, words, color):
    button = Rectangle(pt1, pt2)
    button.setFill(color)
    button.draw(gwin)

    #find the x and y coords of the middle of the button
    labelx = (pt1.getX() + pt2.getX())/2.0 
    labely = (pt1.getY() + pt2.getY())/2.0

    #use these coords for the position of the label
    label = Text(Point(labelx,labely),words)
    label.setFill("white")
    label.draw(gwin)

    return button

def isClicked(button, pt):
    x0 = button.getP1().getX()
    x1 = button.getP2().getX()
    y0 = button.getP1().getY()
    y1 = button.getP2().getY()
    if ((pt.getX() >= x0 and pt.getX() <= x1) and \
            (pt.getY() >= y0 and pt.getY() <= y1)):
        return True
    else:
        return False

    #isClicked function is the one we created in class

def byFreq(pair):
    return pair[1]
#This part of the wordcounter Function

def stopwords(wordlist):
#this is the stopwords function that I created in order to remove the stopwords from a certain
#wordlist
    stopFile = open('stopwords.txt','r')
    stopWords = stopFile.read()
    stopwords = stopWords.lower()
    splitstop = stopWords.split('\n')
    
#First I put the all the words into a list
#then I created two seperate lists
    finalwords = [] #This list is for the wordcloud
    trash = [] #this is for all the other words

    #'for' loop about each item in a wordlist that is given
    for item in wordlist:
        #i put items that are stopwords in the trash 
        if item in splitstop:
            trash.append(item)
        #all other words are put into a finalwords list
        else:
            finalwords.append(item)
    
    return finalwords #lastly I return just the finalwords

def wordcounter(fname):
#this is the wordcounter function that was given with a few adjustments
    #get the sequence of words from file

    filename = fname + '.txt'#I made it so you can simply put in the title without add .txt
    text = open(filename, 'r').read()
    text = text.lower()
    for ch in '!"#$%&()*+,-./:;<=>?@[\\]^_{|}~':
        text = text.replace(ch, ' ')
    words = text.split()

    #at this point i use my stopwords funtion to remove all the stopwords.
    Words = stopwords(words)

    #construct a dictionary of word counts
    counts = {}
    for w in Words:
        counts[w] = counts .get(w,0) + 1

    
    #output analysis of n most frequent
    items = list(counts.items())
    items.sort()
    items.sort(key=byFreq, reverse = True)
    wordlist = []
    for i in range (20):
        word, count = items[i]
        wordlist.append(word)
        
    
    #also i asked for it to return the wordlist of 20 
    return wordlist

def wordcloud(List, gwin):
    # this was the actually function that creates the word cloud

    #since the output is always 20 words i divided the length of the list by 4 since i split the words into four groups
    for i in range (int(len(List)/4)):

        #first i split the words into 4 separate groups
        #I also put the placements of Word1 and Word4 in the upper half of the window
        #and Word2 and Word3 on the lower half of the window
        Word1 = Text(Point(randrange(50, 800), randrange(65,443)), List[4*i])
        Word2 = Text(Point(randrange(50, 800), randrange(444,735)), List[4*i + 1])
        Word3 = Text(Point(randrange(50, 800), randrange(444,735)), List[4*i + 2])
        Word4 = Text(Point(randrange(50, 800), randrange(65,443)), List[4*i + 3])

       #then for each word i gave a different color
        #and by using the offset and for loop i was able to slowly reduce the font
        Word1.setTextColor(color_rgb(255,0,0))
        Word1.setSize(36-4*i)
        Word1.draw(gwin)
    
        Word2.setTextColor(color_rgb(0,0,255))
        Word2.setSize(36-(4*i + 1))
        Word2.draw(gwin)

        Word3.setTextColor(color_rgb(0,255,0))
        Word3.setSize(36-(4*i + 2))
        Word3.draw(gwin)

        Word4.setTextColor(color_rgb(255,0,255))
        Word4.setSize(36-(4*i + 3))
        Word4.draw(gwin)

def main():
    #creates the window
    win = GraphWin("Word Cloud ", 900, 800)

    #initial prompt text
    Itext = Text(Point(345, 40), "Text to create word cloud from:")
    Itext.draw(win)
    
    #Create and Exit Buttons
    createBtn = drawButton(win, Point(650, 30), Point(700, 55), "Create", "blue")
    exitBtn = drawButton(win, Point(710, 30), Point(760, 55), "Exit", "red")

    #initial entry box 
    textentry = Entry(Point(550,40), 20)
    textentry.setText("Siddartha")
    textentry.draw(win)

    pt = win.getMouse()#asked for a mouse click
    #created a while loop so that there are no breaks in the code
    while not isClicked(createBtn, pt) or  not isClicked(exitBtn, pt):

        
        if isClicked(createBtn, pt):
                WordList = wordcounter(textentry.getText())
                wordcloud(WordList, win)
                Text(Point(450, 740), "Click Anywhere to Close").draw(win)
                Text(Point(450, 755), "Or click create once to reset, and click it again to create another word cloud").draw(win)
                pt = win.getMouse()
                win.delete('all')

                Itext = Text(Point(345, 40), "Text to create word cloud from:")
                Itext.draw(win)
                #Create and Exit Buttons
                createBtn = drawButton(win, Point(650, 30), Point(700, 55), "Create", "blue")
                exitBtn = drawButton(win, Point(710, 30), Point(760, 55), "Exit", "red")

                #initial entry box 
                textentry = Entry(Point(550,40), 20)
                textentry.setText("Siddartha")
                textentry.draw(win)

                #created second while loop if user wants to create another word cloud
                while not isClicked(createBtn, pt):
                    win.close()
                    
                    if isClicked(createBtn, pt):
                        
                        WordList = wordcounter(textentry.getText())
                        wordcloud(WordList, win)
                        Text(Point(450, 740), "Click Anywhere to Close").draw(win)
                        Text(Point(450, 755), "Or click create once to reset, and click it again to create another word cloud").draw(win)
                        
                    
         #if statement for the exit button       
        if isClicked(exitBtn, pt):
                win.close()
        
        #this final prompt resets the while loop
        else:
            pt = win.getMouse()

#finally call the main function
main()
    
