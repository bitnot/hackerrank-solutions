class Calculator 
    implements AdvancedArithmetic {    
    
    public int divisorSum(int n)
    {
        int sum = 0; 
        int i = 1;
        while(i <= Math.sqrt(n))
        {
            if(n % i == 0) {
                sum += i;
                if (i != (n / i)) {
                    sum +=  n/i;
                }
            } 
            i++;
        }
        return sum;
    }   
}