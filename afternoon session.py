#s="An avacado becomes an apple"
#count=0
#for i in s:
  #  if(i in "Aa"):
  #      count +=1
#print(count)                                                                                            

#lst=[1,23,4,5,6,7,8,9,0]
#lst.extend([99,89,90])

#s1={1,2,3}^
#s2={2,3,4}

#print(s1.union(s2))
#print(s1.intersection(s2))
#print(s1^s2)

#dictionary
#d1={'a':'apple','b':'banana'}
#d1['b']='ball'
#print(d1)
#print(d1.keys())
#print(d1.items())
#print(d1.update({'c':'cat'}))

data={'num1':100, 'num2':200, 'num3':300}
sum=0
for i in data.values():
    sum+=i
print(sum)
