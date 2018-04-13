#!/usr/bin/perl

use Math::BigInt;

my $temp = <STDIN>;
chomp $temp;
my ($x,$y,$n) = split / /, $temp;

($x,$y) = (Math::BigInt->new($x), Math::BigInt->new($y));

my $z;
for (my $i=2; $i<$n; $i++){
    $z = $y**2 + $x;
    ($x,$y) = ($y,$z);
}
print $z;