#!/usr/bin/perl
use POSIX;

my $t = <STDIN>;
chomp $t;
while($t--){
    my $tmp = <STDIN>;
    chomp $tmp;
    my ($x,$y) = split / /, $tmp;
    
    my $start = ceil(sqrt($x));
    my $end = floor(sqrt($y));
    
    print $end - $start + 1;
    print "\n";
}