def prime ( number ) :
  d = 2 
  while number % d == 1 and d <= number / 2 :
    d = d + 1 


  print 'current number:' 
  print number 
  if ( d % 2 != 0 ) :
    print 'the number is prime' 
  else:
    print 'the number is not prime' 




prime ( 20 ) 
prime ( 5 ) 
  