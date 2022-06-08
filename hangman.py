import random
import time
name = input("What is your name?: ")
print ("Hello, " + name, "Time to play hangman!")
print ("")
print ("You have only 5 lives")
print ("")
time.sleep(0.5)
print ("Start guessing...")
print ("")
print ("Its a country")
time.sleep(0.5)
x=0
while x==0:
    f=open('countries.txt')
    fh=f.readlines()
    lst=fh
    word = random.choice(lst)
    p=word
    word=word.lower()
    word=word[0:len(word)-1]
    guesses = ''
    turns = 5

    while turns > 0:   
        failed = 0           
        for i in word:   
            if i in guesses:    
                print (i,end='')    
            else:
                if i==' ':
                    print(' ',end=' ')
                else:
                    print ("_",end=' '), 
                    failed += 1    
        if failed == 0:        
            print ("""\nYou won!""")  
            break
        print                    
        print()
        guess = input("guess a character:") 
        guesses += guess                    
        if guess not in word: 
            turns -= 1   
            print ("Wrong")
            print ("You have", + turns, 'more lives') 
            if turns == 0:
                print ("You Loose!")
                print ("")
                print ("The country is",p)
    c=input('Want to play again??  :').lower()
    if c=='y' or c=='yes':
        continue
    else:
        print('Bye!!')
        break
    
        
