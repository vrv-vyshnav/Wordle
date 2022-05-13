from tabnanny import check


checkWord = input("enter word")
word = "hello"

for i in range(5):
    if checkWord[i] in word:
        print("\t \t" + str(checkWord[i] + " present in it"))
    if (checkWord[i] == word[i]):
        print(str("\t \t" + checkWord[i]) + " is in correct position" + str(i))
    print("\n")





# for i in checkWord:
#     for j in word:
#         print(j+ " ")
# j= 0
# for i in checkWord:
#     print(checkWord.index(i))
    # if checkWord.index(i) == word[j]:
        # print("index match" + i)
        # j+=1
        

# print(word[0])







# for letter in word:
#     for letters in checkWord:
#         if letters == letter:
#             print("\t \t", letters, " present in it ")
#             if word.index(letters) == checkWord.index(letter):
#                 print("\t \t", letter, " is at correct position(",
#                         checkWord.index(letter)+1, ")\n")
# def indices(lst, item):
#        return [i for i, x in enumerate(lst) if x == item]
   
# for letter in word:
#     if letter in checkWord:
#         print("letter exist") 
#         value = indices(word, letter)
#         print(letter, value)
#         print("\t \t", letter, " is at correct position(",
#         checkWord.index(letter)+1, ")\n")




# import time

# start = time.time()
# # for i in range(5):
# #     a = input("fgsd")

# end = time.time()

# def report(start, end):
#     # sec = end - start
#     sec = 5400
#     min = (sec/60)
#     if sec < 60:
#         print("{:.2f}".format(sec) + " sec")
#     elif sec > 60 and min < 60:
#         print("{:.2f}".format(min) + " Minute")
#     else:
#         hour = min / 60
#         print(str(hour)+" Hour")

# # report(start, end)

# def time(start, end):
#     # sec = end - start
#     sec = 40
#     min = (sec/60)
#     if sec < 60:
#         return "{:.2f}".format(sec) + " sec"
#     elif sec > 60 and min < 60:
#         return "{:.2f}".format(min) + " Minute"
#     else:
#         hour = min / 60
#         return str(hour)+" Hour"

# Time = time(start, end)
# print(Time)

# def run(x,y):
#     print(x,y)
#     if x == 0:
#         return y
#     return run(x-1,x+y)

# print(run(4,3))