object Solution extends App{
    import scala.collection.mutable
    val sc = new java.util.Scanner (System.in);
    var s = sc.nextInt();
    implicit val memo = mutable.Map.empty[Int,Int]
    for(_ <- 0 until s){
        var n = sc.nextInt();
        println(getWays(n))
    }
    
    def getWays(n:Int)(implicit memo:mutable.Map[Int,Int]):Int = {
        if(n < 0)
            0
        else if(n == 0)
            1
        else if(memo.contains(n))
            memo(n)
        else {
            val result = getWays(n - 1) + getWays(n - 2) + getWays(n - 3)
            memo += n -> result
            result
        }
    }
}
