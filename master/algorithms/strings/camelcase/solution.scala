object Solution {

    def camelcase(s: String): Int =  {
        val a = 'a'
        s.filter(_ < a).length + 1
    }

    def main(args: Array[String]) {
        val sc = new java.util.Scanner (System.in);
        var s = sc.next();
        val result = camelcase(s);
        println(result)
    }
}
