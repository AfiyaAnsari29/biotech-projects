#MAKE A LIST
jn1= ['N450D', 'E484K', 'F486L', 'R403K', 'L455S', 'V445D', 'V445L',
'F486S', 'G339R', 'K356T', 'G446S', 'L452L', 'I332V']
delta= ['T478K', 'E484K', 'L452R', 'L455S', 'I332V']

#length
print(f"JN.1 Mutation count:{len(jn1)}")
print(f"Delta Mutation count:{len(delta)}")

#8th position
print(f"8th mutation in JN.1:{jn1[7]}")

#reversing
jn1.reverse()
delta.reverse()
print(f"reversed JN.1 string:{jn1}")
print(f"reversed Delta string:{delta}")

#removing elements (mutation numbers 4, 6, 11 so indices are 3, 5, 10)
for index in sorted([3,5,10],reverse=True):
    jn1.pop(index)
print(f"JN.1 after removing 4,6,11:{jn1}")

#correcting error
if 'V445L' in jn1:
    jn1.remove('V445L')
delta.append('V445L')
print(f"Updated JN.1:{jn1}")
print(f"Updated Delta:{delta}")

#checking for retained muations
set_jn1= set(jn1)
set_delta= set(delta)
print(f"Updated JN.1:{set_jn1}")
print(f"Updated Delta:{set_delta}")

#shared mutations between JN.1 and Delta
shared= set_jn1.intersection(set_delta)
print(f"Shared mutations:{shared}")

#mutations unique to JN.1
only_jn1= set_jn1.difference(set_delta)
print(f"Only in JN.1:{only_jn1}")

#mutations unique to Delta
only_delta= set_delta.difference(set_jn1)
print(f"Only in Delta:{only_delta}")

