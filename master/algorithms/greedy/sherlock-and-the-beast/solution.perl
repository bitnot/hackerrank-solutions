#!/usr/bin/perl

$t = <STDIN>;
chomp $t;
for my $a0 (0..$t-1){
    $n = <STDIN>;
    chomp $n;

    my $number_5s = $n;
    while($number_5s >= 5 && $number_5s % 3 > 0){
        $number_5s = $number_5s - 5;
    }
    
    if($number_5s % 3 == 0){
        my $number_3s = $n - $number_5s;
        print "5" x $number_5s . "3" x $number_3s . "\n";
    }else{        
        print "-1\n";
    }
    
}
