#!/usr/bin/perl -w

use strict;
use warnings;
use Math::Complex;

my $sum_of_squares = 0;
my $sum = 0;
for(my $i = 1; $i < 101; $i++){
	$sum_of_squares += $i*$i;
	$sum += $i;
	}
printf "%d", $sum*$sum - $sum_of_squares;
