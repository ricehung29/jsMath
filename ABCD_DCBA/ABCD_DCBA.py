for a in range(0,10): 
  for b in range(0,10):
      for c in range(0,10):
          for d in range(0,10):
              x = a*1000+b*100+c*10+d
              y = d*1000+c*100+b*10+a 
              if x*4 == y : print(x,y) 
