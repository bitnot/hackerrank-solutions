#!/usr/bin/perl

$t = <STDIN>;
chomp $t;
while($t--){
    $n = <STDIN>;
    chomp $n;
    
    my %dividers = (1=>1);
    for my $i(2..9){
        if($n % $i == 0){
            $dividers{$i} = $i;
        }
    }    
    
    my $sum = 0;
    my $l = length $n;
    while($l--){
        my $digit = int(substr($n, $l, 1));
        if(exists $dividers{$digit}){
            $sum++;
        };        
    }
    
    print $sum . "\n";
}
