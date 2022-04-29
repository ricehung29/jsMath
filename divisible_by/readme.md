# pyAdMath
## divisible_by

### Example 1 :
Given a four digits number 54b1 is divisible by 3 , find the least value of b.

Python Code :
```
for i in range(10,100,10):
    if (5401+i)%3 == 0:
        print(5401+i)
```

Output : 
```
5421
5451
5481
```

2<5<8 , b = 2


### Example 2 :
Given a eleven digits number 20222022xyz is divisible by 202 , find the largest value of x , y and z.

Python Code :
```
for i in range(0,999):
    if (20222022000+i)%202 == 0:
        print(20222022000+i)
```

Output : 
```
20222022040
20222022242
20222022444
20222022646
20222022848
```
x = 8 , y = 4 , z = 8
