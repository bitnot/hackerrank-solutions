#!/usr/bin/perl

sub search_pos {    
    my ($min, $max, $value,@array) = ($_[0], $_[1], $_[2], @{$_[3]});
    
    my $mid = $min + int(($max - $min) / 2);
    
    if($array[$mid] == $value){
        # gotcha
        return $mid;
    }
    
    if($min == $max || $mid<0 || $mid >= scalar @array){
        # not found
        return -1;
    }    
    
    if($array[$mid] > $value){        
        return search_pos($min, $mid-1, $value, \@array) ;
    }
    
    return search_pos($mid+1, $max, $value, \@array);
}

my $V = <STDIN>;
chomp $V;

my $N = <STDIN>;
chomp $N;

my $temp = <STDIN>;
chomp $temp;
my @arr = split / /, $temp;

print search_pos(0, $N - 1, $V, \@arr);

