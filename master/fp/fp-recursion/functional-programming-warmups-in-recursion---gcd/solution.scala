object Solution {
    
    def gcd(x: Int, y: Int): Int = 
        y match {
            case 0 => x
            case _ => gcd(y,x%y)
        }

    def acceptInputAndComputeGCD(pair:List[Int]) = 
      println(gcd(pair.head,pair.last))

    def main(args: Array[String]) =
         acceptInputAndComputeGCD(readLine().trim().split(" ").map(x=>x.toInt).toList)
}