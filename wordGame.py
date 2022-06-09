
from random import randrange
import random
import time

wordlist = ['Abuse','maths','Adult', 'Agent', 'Anger', 'Apple', 'Award', 'Basis', 'Beach', 'Birth', 'Block', 'Blood', 'mouse', 'Board', 'Brain', 'Bread', 'Break', 'Brown', 'Buyer', 'Cause', 'Chain', 'Chair', 'Chest', 'Chief', 'Child', 'China', 'Claim', 'Class', 'Clock', 'Coach', 'Coast', 'Court', 'Cover', 'Cream', 'Crime', 'Cross', 'Crowd', 'Crown', 'Cycle', 'Dance', 'Death', 'Depth', 'Doubt', 'Draft', 'Drama', 'Dream', 'Dress', 'Drink', 'Drive', 'Earth', 'Enemy', 'Entry', 'Error', 'Event', 'Faith', 'Fault', 'Field', 'Fight', 'Final', 'Floor', 'Focus', 'Force', 'Frame', 'Frank', 'Front', 'Fruit', 'Glass', 'Grant', 'Grass', 'Green', 'Group', 'Guide', 'Heart', 'Henry', 'Horse', 'Hotel', 'House', 'Image', 'Index', 'Input', 'Issue', 'Japan', 'Jones', 'Judge', 'Knife', 'Laura', 'Layer', 'Level', 'Lewis', 'Light', 'Limit', 'Lunch', 'Major', 'March', 'Match', 'Metal', 'Model', 'Money', 'Month', 'Motor', 'Mouth', 'Music', 'Night', 'Noise', 'North', 'Novel', 'Nurse', 'Offer', 'Order', 'Other', 'Owner', 'Panel', 'Paper', 'Party', 'Peace', 'Peter', 'Phase', 'Phone', 'Piece', 'Pilot', 'Pitch', 'Place', 'Plane', 'Plant', 'Plate', 'Point', 'Pound', 'Power', 'Press', 'Price', 'Pride', 'Prize', 'Proof', 'Queen', 'Radio', 'Range', 'Ratio', 'Reply', 'Right', 'River', 'Round', 'Route', 'Rugby', 'Scale', 'Scene', 'Scope', 'Score', 'Sense', 'Shape', 'Share', 'Sheep', 'Sheet', 'Shift', 'Shirt', 'Shock', 'Sight', 'Simon', 'Skill', 'Sleep', 'Smile', 'Smith', 'Smoke', 'Sound', 'South', 'Space', 'Speed', 'Spite', 'Sport', 'Squad', 'Staff', 'Stage', 'Start', 'State', 'Steam', 'Steel', 'Stock', 'Stone', 'Store', 'Study', 'Stuff', 'Style', 'Sugar', 'Table', 'Taste', 'Terry', 'Theme', 'Thing', 'Title', 'Total', 'Touch', 'Tower', 'Track', 'Trade', 'Train', 'Trend', 'Trial', 'Trust', 'Truth', 'Uncle', 'Union', 'Unity', 'Value', 'Video', 'Visit', 'Voice', 'Waste', 'Watch', 'Water', 'While', 'White', 'Whole', 'Woman', 'World', 'Youth', 'Alcon', 'Aught', 'Hella', 'One’s', 'Ought', 'Thame', 'There', 'Thine', 'Thine', 'Where', 'Which', 'Whose', 'Whoso', 'Yours', 'Yours', 'Admit', 'Adopt', 'Agree', 'Allow', 'Alter', 'Apply', 'Argue', 'Arise', 'Avoid', 'Begin', 'Blame', 'Break', 'Bring', 'Build', 'Burst', 'Carry', 'Catch', 'Cause', 'Check', 'Claim', 'Clean', '', 'Climb', 'Close', 'Count', 'Cover', 'Cross', 'Dance', 'Doubt', 'Drink', 'Drive', 'Enjoy', 'Enter', 'Exist', 'Fight', 'Focus', 'Force', 'Guess', 'Imply', 'Issue', 'Judge', 'Laugh', 'Learn', 'Leave', 'Limit', 'Marry', 'Match', 'Occur', 'Offer', 'Order', 'Phone', 'Place', 'Point', 'Press', 'Prove', 'Raise', 'Reach', 'Refer', 'Relax', 'Serve', 'Shall', 'Share', 'Shift', 'Shoot', 'Sleep', 'Solve', 'Sound', 'Speak', 'Spend', 'Split', 'Stand', 'Start', 'State', 'Stick', 'Study', 'Teach', 'Thank', 'Think', 'Throw', 'Touch', 'Train', 'Treat', 'Trust', 'Visit', 'Voice', 'Waste', 'Watch', 'Worry', 'Would', 'Write', 'Above', 'Acute', 'Alive', 'Alone', 'Angry', 'Aware', 'Awful', 'Basic', 'Black', 'Blind', 'Brave', 'Brief', 'Broad',
            'Brown', 'alert','Cheap', 'Chief', 'Civil', 'Clean', '', 'Close', 'Crazy', 'Daily', 'Dirty', 'Early', 'Empty', 'Equal', 'Exact', 'Extra', 'Faint', 'False', 'Fifth', 'Final', 'First', 'Fresh', 'Front', 'Funny', 'Giant', 'Grand', 'Great', 'Green', 'Gross', 'Happy', 'Harsh', 'Heavy', 'Human', 'Ideal', 'Inner', 'Joint', 'Large', 'Legal', 'Level', 'Light', 'Local', 'Loose', 'Lucky', 'Magic', 'Major', 'Minor', 'Moral', 'Naked', 'Nasty', 'Naval', 'Other', 'Outer', 'Plain', 'Prime', 'Prior', 'Proud', 'Quick', 'Quiet', 'Rapid', 'Ready', 'Right', 'Roman', 'Rough', 'Round', 'Royal', 'Rural', 'Sharp', 'Sheer', 'Short', 'Silly', 'Sixth', 'Small', 'Smart', 'Solid', 'Sorry', 'Spare', 'Steep', 'Still', 'Super', 'Sweet', 'Thick', 'Third', 'Tight', 'Total', 'Tough', 'Upper', 'Upset', 'Urban', 'Usual', 'Vague', 'Valid', 'Vital', 'White', 'Whole', 'Wrong', 'Young', 'Afore', 'After', 'Bothe', 'Other', 'Since', 'Slash', 'Until', 'Where', 'WhileAback', 'Abaft', 'Aboon', 'About', 'Above', 'Accel', 'Adown', 'Afoot', 'Afore', 'Afoul', 'After', 'Again', 'Agape', 'Agogo', 'Agone', 'Ahead', 'Ahull', 'Alife', 'Alike', 'Aline', 'Aloft', 'Alone', 'Along', 'Aloof', 'Aloud', 'Amiss', 'Amply', 'Amuck', 'Apace', 'Apart', 'Aptly', 'Arear', 'Aside', 'Askew', 'Awful', 'Badly', 'Bally', 'Below', 'Canny', 'Cheap', 'Clean', 'clear', 'Coyly', 'Daily', 'Dimly', 'Dirty', 'Ditto', 'Drily', 'Dryly', 'Dully', 'Early', 'Extra', 'False', 'Fatly', 'Feyly', 'First', 'Fitly', 'Forte', 'Forth', 'Fresh', 'Fully', 'Funny', 'Gaily', 'Gayly', 'Godly', 'Great', 'Haply', 'Heavy', 'Hella', 'Hence', 'Hotly', 'Icily', 'Infra', 'Intl.', 'Jildi', 'Jolly', 'Laxly', 'Lento', 'Light', 'Lowly', 'Madly', 'Maybe', 'Never', 'Newly', 'Nobly', 'Oddly', 'Often', 'Other', 'Ought', 'Party', 'Piano', 'Plain', 'Plonk', 'Plumb', 'Prior', 'Queer', 'Quick', 'Quite', 'Ramen', 'Rapid', 'Redly', 'Right', 'Rough', 'Round', 'Sadly', 'Secus', 'Selly', 'Sharp', 'Sheer', 'Shily', 'Short', 'Shyly', 'Silly', 'Since', 'Sleek', 'Slyly', 'Small', 'So-So', 'Sound', 'Spang', 'Srsly', 'Stark', 'Still', 'Stone', 'Stour', 'Super', 'Tally', 'Tanto', 'There', 'Thick', 'Tight', 'Today', 'Tomoz', 'Truly', 'Twice', 'Under', 'Utter', 'Verry', 'Wanly', 'Wetly', 'Where', 'Wrong', 'Wryly', 'Abaft', 'Aboon', 'About', 'Above', 'Adown', 'Afore', 'After', 'Along', 'Aloof', 'Among', 'Below', 'Circa', 'Cross', 'Furth', 'Minus', 'Neath', 'Round', 'Since', 'Spite', 'Under', 'Until', 'Aargh', 'Adieu', 'Adios', 'Alack', 'Aloha', 'Avast', 'Bakaw', 'Basta', 'Begad', 'Bless', 'Blige', 'Brava', 'Bravo', 'Bring', 'Chook', 'Damme', 'Dildo', 'Ditto', 'Frick', 'Fudge', 'Golly', 'Gratz', 'Hallo', 'Hasta', 'Havoc', 'Hella', 'Hello', 'Howay', 'Howdy', 'Hullo', 'Huzza', 'Jesus', 'Kapow', 'Loose', 'Lordy', 'Marry', 'Mercy', 'Night', 'Plonk', 'Psych', 'Quite', 'Salve', 'Skoal', 'Sniff', 'Sooey', 'There', 'Thiam', 'Thwap', 'Tough', 'Twirp', 'Viola', 'Vivat', 'Wacko', 'Wahey', 'Whist', 'Wilma', 'Wirra', 'Woops', 'Wowie', 'Yecch', 'Yeeha', 'Yeesh', 'Yowch', 'Zowie']
length = len(wordlist)

#------------------------Wordle game ---------------------------------------------
def router():
    print("\n  \t \t _____________________________________________ \n ")
    print("\n 0 for exit")
    print("\n 1 for Main Menu")
    direction = input("\n Enter your choice: ")
    if direction == '0':
        bye()
    else:
        Main()

def wordle():
    print("\n \t \t  _____________________________________________ \n ")
    print("\n \t \t  \t \t WORDLE \n")
    print(" \t \t _____________________________________________ \n ")
    print(" \t \t Instruction \n ")
    print(" \t \t  *) Guess the 5 letter word \n  \t \t  *) You won't get any hint after 5 attempts \n  \t \t  *) The word must be a meaning full word \n  \t \t  *) Good luck \n  \t \t  *) 0 for exit \n")
    print(" \t \t _____________________________________________ \n ")
    try:
        input("\t \t  \t \t Press enter to start \n")
        start = time.time()
        WordleMain(start)

    except Exception as e:
        print(e)
        WordleMain(start)
        
def report(start, end, i,word):
    print(" \t \t _____________________________________________ \n")
    print(" \t \t \t \t Word found\n")
    print(" \t \t stats! \n")
    time = Time(start, end)
    print("\t  \t \t TIme taken  " + time)
    print("\t  \t \t The word is " + word)
    print("\t  \t \t Attempts: " + str(i+1))
    print("\n")


def Time(start, end):
    sec = end - start
    min = (sec/60)
    if sec < 60:
        return "{:.2f}".format(sec) + " sec"
    elif sec > 60 and min < 60:
        return "{:.2f}".format(min) + " Minute"
    else:
        hour = min / 60
        return "{:.2f}".format(hour) + " Hour"


def hint(checkWord,word):
    for i in range(5):
        if checkWord[i] in word:
            print(" \t \t \t \t" + str(checkWord[i] + " present in it"))
            if (checkWord[i] == word[i]):
                print(str(" \t \t \t \t" + checkWord[i]) +
                    " is in correct position (" + str(i+1) + ")\n")
            print("\n")


def matchCheck(checkWord):
    notfound = 0
    for wordz in wordlist:
        wordz = wordz.lower()
        if checkWord == wordz:
            notfound = 1
    return notfound


def WordleMain(start):
    word = wordlist[randrange(length)]
    word = word.lower()
    i= 0
    print(word)
    while(True):
        checkWord = input(" \t \t search for the word: ")
        print("\n")
        checkWord = checkWord.lower()
        lstring = len(checkWord)
        if checkWord == "0":
            end = time.time()
            print(" \t \t _____________________________________________")
            print("\n \t  \t \t   Better Luck Next Time \n ")
            report(start, end, i,word)
            router()
        if lstring != 5:
            print("\t  \t \t length doesn't match \n")
            continue
        notfound = matchCheck(checkWord)
        if notfound == 1 and checkWord != word:
            if i < 5:
                hint(checkWord,word)
            i = i+1

        elif notfound == 0:
            print("\t  \t \t word not in Dictionary")

        else:
            end = time.time()
            report(start, end, i,word)
            router()

        if checkWord != word:
            print(" \t \t try again")


#-------------------- End of wordle --------------------------------------------------



#-------------------- word scramble --------------------------------------------------        

def scamReport(start,j,word,end):
    print("\n \t \t  _____________________________________________ \n")
    print(" \t \t \t \t Word found\n")
    print(" \t \t stats! \n")
    time = Time(start, end)
    print("\t  \t \t TIme taken  " + time)
    print("\t  \t \t The word is " + word)
    print("\t  \t \t Attempts: " + str(j))
    print("\n")

def scamblerMain(start):
    word = wordlist[randrange(length)]
    word = word.lower()
    j = 0
    print(word)
    st = list(word)
    random.shuffle(st)
    shuffleword = ''.join(st)
    print("\t \t  \t \t ",shuffleword,'\n')
    while True:
        userword = input(" \t \t search for the word: ")
        userword = userword.lower()
        if len(userword) != 5:
            print("\n \t \t \t \t Length doesn't match")
        else:
            j += 1
            if userword == word:
                end = time.time()
                scamReport(start,j,word,end)
                router()
            elif userword == "0":
                end = time.time()
                scamReport(start,j,word,end)
                router()
            else: 
                print("\n")
                print(" \t \t try again")


def wordScambler():
    print(" \t \t _____________________________________________ \n ")
    print("\n \t \t  \t \t word scramble \n")
    print(" \t \t _____________________________________________ \n ")
    print(" \t \t Instruction \n ")
    print("\t \t \t *) Find the scramble word \n \t  \t \t *) 0 for exit \n")
    print(" \t \t _____________________________________________ \n ")
    try:
        input(" \t \t Enter to start")
        _start = time.time()
        scamblerMain(_start)
    except Exception as e:
        print(e)
        scamblerMain(_start)

#-------------------- End of word scramble --------------------------------------------------

def bye():
    print("\n \t \t _____________________________________________ \n")
    print(" \t \t \t \t bye bye")
    print("\n \t \t _____________________________________________ \n")
    exit()

def Main():
    while True:
        print("\n_____________________________________________ \n")
        print("\n \t \t WORD Games \n")
        print("_____________________________________________ \n ")
        print("\n \t !. Wordle")
        print("\n \t 2. Word Scramble")
        print("\n \t 0. Exit")
        choose = input("\nChoose the game: ")
        if choose == '1':
            wordle()
        elif choose == '2':
            wordScambler()
        else:
            bye()
Main()
