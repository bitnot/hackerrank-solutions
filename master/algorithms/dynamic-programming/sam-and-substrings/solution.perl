#!/usr/bin/perl

my $n = <STDIN>;
chomp $n;

my $len = length $n;

my $MOD = 10**9 + 7;
my $sum = 0;

my $position_mask = 1;

while($len--){
    my $digit = substr($n, $len, 1);
    my $position_occurences = $len + 1;
    
    $sum = ($sum + $digit * $position_mask * $position_occurences) % $MOD;
    $position_mask = (($position_mask * 10) + 1) % $MOD;
}

print $sum;
