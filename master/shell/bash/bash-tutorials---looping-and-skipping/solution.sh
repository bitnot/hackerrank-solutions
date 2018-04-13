for X in {1..99} 
do [ $(( X%2 )) -eq 1 ] && echo $X 
done