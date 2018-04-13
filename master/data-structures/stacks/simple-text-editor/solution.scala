object Solution extends App {
    import scala.io.StdIn
    import scala.collection.mutable.Stack
    
    
    val lines = Stack[String]()
    var str = ""
    
    val t = StdIn.readInt()
    for(_ <- 1 to t) {
        val line = StdIn.readLine()
        val parts = line.split(' ')
        val opType = parts.head.toInt
        def k = parts(1).toInt
        opType match {
            case 1 => 
                lines.push(str)
                str += parts(1)
            case 2 => 
                lines.push(str)
                str = str.dropRight(k)
            case 3 => println(str(k - 1))
            case 4 => str = lines.pop()
        }
    }
}