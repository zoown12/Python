def f2():
    print("start f2")
    print("end f2")
    return
def f1():
    print("start f1")
    f2()
    print("end f2")
    return

print('start main')
f1()
print('end main')
