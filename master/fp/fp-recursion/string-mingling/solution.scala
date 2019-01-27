object Solution extends App {
    import scala.io.StdIn._
    val p = readLine
    val q = readLine
    val pq = p.zip(q).map{case (a,b) => s"$a$b"}.mkString
    println(pq)
}