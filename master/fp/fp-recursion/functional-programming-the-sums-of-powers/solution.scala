object Solution {
    def getPowers(X:Int, N:Int): Set[Int] = {
        val max = math.pow(X, 1.0/N).toInt 
        Set((1 to max).toList.map(math.pow(_,N).toInt) : _*)
    }
    
    def pickEl(S:Set[Int]):Int = {
        if(S.size == 0) 0
        else S.last
    }
    
    def calcWays(S:Set[Int],X:Int):Int = {
        X match {
            case 0 => 1
            case neg if neg < 0 => 0
            case _ => {
                val el = pickEl(S)
                el match{
                    case 0 => 0
                    case _ => calcWays(S - el, X- el) + calcWays(S - el, X) 
                }
            }
        }
    }
    
    def numberOfWays(X:Int,N:Int):Int = {
        val powers = getPowers(X,N)
        calcWays(powers, X)
    }

    def main(args: Array[String]) {
       println(numberOfWays(readInt(),readInt()))
    }
}