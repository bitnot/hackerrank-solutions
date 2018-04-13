#!/usr/bin/perl

$n = <STDIN>;
chomp $n;
$a_i = 0;
$diff = 0;
while($a_i < $n){
   my $a_temp = <STDIN>;
   my @a_t = split / /,$a_temp;
   chomp @a_t;
   $diff = $diff + $a_t[$a_i] -  $a_t[-$a_i-1];
   $a_i++;
}
$diff = abs($diff);
print $diff;
