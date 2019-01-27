object Solution extends App{for{i<-1 to 100}println{var x=""
if(i%3==0)x="Fizz"
if(i%5==0)x+="Buzz"
if(x>"")x else i}}