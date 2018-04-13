object Solution {

    def prefix(x: String, y:String)={
        val (xlen:Int,ylen:Int) = (x.size,y.size)
            
        def pre_tail(plen:Int):Int = {
            plen match {
                case i 
                    if i >= xlen ||
                       i >= ylen ||
                       x(i) != y(i) 
                    => i
                case _ => pre_tail(plen + 1)
            }
        }
        
        val plen = pre_tail(0)
        (x.substring(0,plen),x.substring(plen),y.substring(plen))
    }
    
    def main(args: Array[String]) {
        val x = readLine()
        val y = readLine()
        
        val (p,x1,y1) = prefix(x,y)
        println(s"${p.size} ${p}")
        println(s"${x1.size} ${x1}")
        println(s"${y1.size} ${y1}")
    }
}