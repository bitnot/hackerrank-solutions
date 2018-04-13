#!/usr/bin/perl

use Date::Parse;

$time = <STDIN>;
chomp $time;
($ss,$mm,$hh) = strptime($time);
printf "%02d:%02d:%02d",$hh,$mm,$ss;