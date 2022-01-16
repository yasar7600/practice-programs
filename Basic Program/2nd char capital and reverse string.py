a = 'hii my name is yasar'

al = len(a)
a = a[al::-1]

a = "".join([x.upper() if i % 2 != 0 else x for i, x in enumerate(a)])

print(a)


#def capital(n):
#    count = 0
#    x = ''
#    for ns in n:
#        if count % 2 == 0:
#            count = count + 1
#            ns.upper()
#            x = x + ns
#        else:
#            count = count + 1
#            x = x + ns
#    print(x)

#capital(a)

# s = 'canada'
# s = "".join([x.upper() if i % 2 != 0 else x for i, x in enumerate(s)])
 
# print(s)

