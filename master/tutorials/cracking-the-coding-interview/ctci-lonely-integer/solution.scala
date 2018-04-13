object Solution {

    def main(args: Array[String]) {
        val sc = new java.util.Scanner (System.in);
        var n = sc.nextInt();
        var a = new Array[Int](n);
        for(a_i <- 0 to n-1) {
           a(a_i) = sc.nextInt();
        }
        println(getTheOne(a))
    }
    
    def getTheOne(a:Array[Int]):Int = a.reduce(_ ^ _)
}
