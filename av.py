no_list = [22, 68, 90, 78, 90, 88]


def average(x):
    m=0
    for i in x:
        m=m+int(i)
    return (m/len(x))
print(average(no_list))