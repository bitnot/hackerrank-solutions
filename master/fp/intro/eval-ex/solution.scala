def eterm(n: Int, x:Double): Double = 
    n match {
        case 0 => 1.0
        case _ => x * eterm(n-1,x)/n
    }
def f(x: Float):Float = (0 to 9)
    .map( n => eterm(n,x).toFloat )
    .foldLeft(0.toFloat)(_+_)