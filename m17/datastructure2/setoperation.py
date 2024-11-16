# set operations
s1 = {'apple','orange','banana','kiwi','apple'}
s1.add('melon')
print(s1,type(s1))
# difference
s2 = {'apple','guava','papaya'}
print(s1.difference(s2))
# Symetric difference
print(s1.symmetric_difference(s2))