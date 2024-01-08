'''import re
haystack = 'sadbutsad'
needle='sad'
temp = re.finditer('sad',haystack)
if(re.search(needle,haystack)is not None):
    for i in temp:
        return (i.start())
else:return -1'''



'''import re
s = 'Hello World'
temp = re.findall(r'[a-z|A-Z]+',s)
print(len(temp[-1]))'''''



'''def kiemtra(num):
    soluong = f'{num:b}'.count('1')
    return (soluong,num)
def kiemtra1(num):
    return num
arr = [0,1,4,3,6,8,5,2,7]
arr.sort(key = lambda x: (f'{x:b}'.count('1'),x) )

print(arr)'''


'''s='paper'
t = 'title'
print(set(zip(s,t)))'''


'''s = 'edcab'
t = 'baca'
#a = (list(s).sort())
a = list(set(s))
a.sort()
#a.sort()
print(a)'''



#MODULE COLLECTION.COUNTER : đếm số lần các phần tử xuất hiện và đưa gia trị thành key và số lần đếm là value cho vao 1 dict
'''from collections import Counter
s = 'abcade'
t = 'cbaade'
print(Counter(s))
print(Counter(t))'''




