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

def run(x,y):
    print(x,y)
    if x == 0:
        return y
    return run(x-1,x+y)

print(run(4,3))