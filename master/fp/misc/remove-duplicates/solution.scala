import collection.mutable.HashMap
    
object Solution {

    def main(args: Array[String]) {
        val str = readLine().trim()
        val abc = new HashMap[Char,Int]()
        val strf = str.filter(c=>{
            if (abc contains c)
                false
            else {
                abc.put(c,1)
                true
            }
        })
       println(strf)
    }
}