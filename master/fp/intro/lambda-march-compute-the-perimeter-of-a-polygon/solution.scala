object Solution {
    import scala.io.StdIn.{readInt,readBoolean}
    import scala.math.sqrt
    
    def main(args: Array[String]) {
        val n = readInt()
        if (n < 3) {
            println(0)
            return
        }
        def edgeLength(x1:Int,y1:Int, x2:Int,y2:Int):Double = {
            sqrt((x2-x1)*(x2-x1)+(y2-y1)*(y2-y1))
        }
        val nodes = (1 to n)
            .map(_ => readLine().split(" ").map(_.toInt))
            .map{case Array(x,y,_*) => (x,y)}
        val prev = nodes.drop(1) :+ nodes(0)
        val perimeter = nodes.zip(prev)
            .map{case ((x1,y1),(x2,y2)) => edgeLength(x1,y1,x2,y2)}
            .reduce(_ + _)
        println(perimeter)
    }
}