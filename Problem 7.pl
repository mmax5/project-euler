#!/usr/bin/perl -w

use strict;
use warnings;
use Math::Complex;

my $count = -1;
my $result = 0;
for(my $i = 2;$count != 10001; $i++){
	if(is_prime($i)){
		$count++;
		}
		if($count == 10001){
			$result = $i;
			}
	}

print "$result";
	
	sub is_prime{
	my $max = int($_[0]);
	my $n = $max/2;
	for(my $j = 2; $j < $n; $j++){
		if ($max % $j == 0){
			return 0;
			}
		}
		return 1; 
	}
