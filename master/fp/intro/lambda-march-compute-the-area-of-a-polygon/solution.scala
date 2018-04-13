object Solution {
    import scala.io.StdIn.readInt
    import scala.math.abs
    
    def main(args: Array[String]) {
        val n = readInt()
        val nodes = (1 to n)
            .map(_ => readLine().split(" ").map(_.toInt))
            .map{case Array(x,y,_*) => (x,y)}
        val shifted = nodes.drop(1) :+ nodes(0)            
        val totalArea = abs(
            nodes.zip(shifted)
            .map{case ((x1,y1),(x2,y2)) => (x1*y2 - x2*y1) * 0.5 }
            .reduce(_ + _))
        println(totalArea)
    }
}