object Solution extends App {
    val sc = new java.util.Scanner (System.in);
    var p = sc.nextInt();
    for(_ <- 0 until p){
        var n = sc.nextLong();
        println(if(isPrime(n)) "Prime" else "Not prime")
    }
    
    import math._
    def isPrime(n:Long):Boolean = if(n < 2) false else (2L to round(sqrt(n))).forall(n % _ != 0)
}
