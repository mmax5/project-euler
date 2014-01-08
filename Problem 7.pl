#!/usr/bin/perl -w

use strict;
use warnings;
use Math::Complex;

$count = -1;
$result = 0;
for($i = 2;$count != 10001; $i++){
	if(is_prime($i)){
		$count++;
		}
		if($count == 10001){
			$result = $i;
			}
	}

print "$result";
	
	sub is_prime{
	$max = int($_[0]);
	$n = $max/2;
	for($j = 2; $j < $n; $j++){
		if ($max % $j == 0){
			return 0;
			}
		}
		return 1; 
	}
