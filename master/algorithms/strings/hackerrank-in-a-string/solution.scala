object Solution {

    def hackerrankInString(s: String): String =  {
        var word = "hackerrank"
        for(c <- s if word.nonEmpty)
            if(c == word(0)) 
                word = word.drop(1)
        if(word.isEmpty) "YES"
        else "NO"
    }

    def main(args: Array[String]) {
        val sc = new java.util.Scanner (System.in);
        var q = sc.nextInt();
        var a0 = 0;
        while(a0 < q){
            var s = sc.next();
            val result = hackerrankInString(s);
            println(result)
            a0+=1;
        }
    }
}
