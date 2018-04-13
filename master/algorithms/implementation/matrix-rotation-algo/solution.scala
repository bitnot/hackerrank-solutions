object Solution {

    def rotate(matrix: Array[Array[Int]], times: Int) : Array[Array[Int]]  =  {
        val m = matrix.size
        val n = matrix(0).size
        val result = Array.ofDim[Int](m,n)
        val nrLayers = m.min(n) / 2
        for(l <- 0 until nrLayers){
            val lm = m - 2*l
            val ln = n - 2*l
            val length = 2*(lm + (ln-2))
            val offset = times % length
            for(i <- 0 until length){
                val ri = 
                    if (i >= offset) i - offset 
                    else (i + length) - offset
                val (x,y) = find(lm,ln,i)
                val (rx,ry) = find(lm,ln,ri)
                result(rx+l)(ry+l) = matrix(x+l)(y+l)
            }
        }
        result
    }
    
    // Finds i-th element (clockwise, 0-based) in the oughter layer of a m*n matrix
    def find(m: Int, n: Int, i: Int): (Int,Int) = {
        val (tl, tr, br, bl, end) = (0, n-1, n+m-2, n+m+n-3, n+m+n+m-4)
        if(0 <= i && i <= tr){
            (0, i)
        }
        else if(tr < i && i < br ){
            ( (m-1) - (br-i), n-1)
        }
        else if(br <= i && i <= bl){
            (m-1, bl - i)
        }
        else if(bl < i && i < end){
            ( (m-1) - (i-bl), 0)
        }
        else{
            throw new IllegalArgumentException()
        }
    }
    
    def printArray(matrix:Array[Array[Int]]){
        for(line <- matrix){
            println(line.mkString(" "))
        }
    }

    def readInput():(Array[Array[Int]], Int) = {
        val sc = new java.util.Scanner (System.in);
        var m = sc.nextInt();
        var n = sc.nextInt();
        var r = sc.nextInt();
        var matrix = Array.ofDim[Int](m,n);
        for(matrix_i <- 0 to m-1) {
           for(matrix_j <- 0 to n-1){
              matrix(matrix_i)(matrix_j) = sc.nextInt();
           }
        }
        (matrix, r)
    }
    
    def main(args: Array[String]) {
        val (matrix, times) = readInput()
        val result = rotate(matrix, times)
        printArray(result)
    }
}
