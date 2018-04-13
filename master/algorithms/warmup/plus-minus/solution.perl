#!/usr/bin/perl

$n = <STDIN>;
chomp $n;
$arr_temp = <STDIN>;
@arr = split / /,$arr_temp;
chomp @arr;
$positive = 0;
$negative = 0;
$zeros = 0;
for my $i (@arr) {
  if($i>0){ $positive++; }
  elsif($i<0){ $negative++; }
  else{ $zeros++; }
}
my $arrSize = @arr;
printf("%.6f\n", $positive/$arrSize);
printf("%.6f\n", $negative/$arrSize);
printf("%.6f\n", $zeros/$arrSize);

