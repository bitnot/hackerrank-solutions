object Solution extends App {
    import scala.io.StdIn._
    val t = readInt
    (1 to t).foreach( _ => println(scramble(readLine.toList).mkString) )
    def scramble(l:List[Char]): List[Char] = l match {
        case Nil => Nil
        case (a::b::tail) => b::a::scramble(tail)
    }
}