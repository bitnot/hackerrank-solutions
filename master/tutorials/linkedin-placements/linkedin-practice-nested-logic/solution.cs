using System;
using System.Globalization;
using System.Collections.Generic;
using System.IO;
class Solution {
    static void Main(String[] args) {
        var culture = CultureInfo.CreateSpecificCulture("de-DE");
        var actual = DateTime.Parse(Console.ReadLine().Replace(" ", "-"), culture);
        var expected = DateTime.Parse(Console.ReadLine().Replace(" ", "-"), culture);
        
        Console.WriteLine(GetFine(expected, actual));
    }
    
    static int GetFine(DateTime expected, DateTime actual){
        if(actual <= expected)
            return 0;
        if(actual.Year > expected.Year)
            return 10000;
        if(actual.Month > expected.Month)
            return 500 * (actual.Month - expected.Month);
        return 15 * (actual.Day - expected.Day);
    }
}