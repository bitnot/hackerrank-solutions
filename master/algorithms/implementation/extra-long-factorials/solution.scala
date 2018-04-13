object Solution {

    def extraLongFactorials(n: Int) =  {
        var result = BigInt(1)
        for(i <- 1 to n){
            result = result * i
        }
        println(result)
    }

    def main(args: Array[String]) {
        val sc = new java.util.Scanner (System.in);
        var n = sc.nextInt();
        extraLongFactorials(n);
    }
}
