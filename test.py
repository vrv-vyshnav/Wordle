import time

start = time.time()
for i in range(5):
    a = input("fgsd")

end = time.time()


def report(start, end):
    print(f"{(end - start):.4f} seconds")


report(start, end)
