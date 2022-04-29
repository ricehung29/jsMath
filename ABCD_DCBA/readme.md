# pyAdMath
## ABCD_DCBA Questions

### Example 1 :
  Find A,B,C and D if 
  `ABCD*4 = DCBA`
  
Python code :
  
  ```
  for a in range(0,10): 
    for b in range(0,10):
        for c in range(0,10):
            for d in range(0,10):
                x = a*1000+b*100+c*10+d
                y = d*1000+c*100+b*10+a 
                if x*4 == y : print(x,y) 
                
``` 
Output :
```
0 0
2178 8712
```

### Example 2 :
  Find A,B,C,D and E if 
  `ABCDE*9 = EDCBA`
  
Python code :
  
  ```
for a in range(0,10):
    for b in range(0,10):
        for c in range(0,10):
            for d in range(0,10):
                for e in range(0,10):
                    x = a*10000+b*1000+c*100+d*10+e
                    y = e*10000+d*1000+c*100+b*10+a 
                    if x*9 == y : print(x,y)                
``` 
Output :
```
0 0
10989 98901
```

---
