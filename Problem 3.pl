#!/usr/bin/perl -w
 use Math::Complex;

$num = 600851475143;
$largest = 2;

for($i = int(sqrt($num)); $i > 2; $i--){
	if(($num % $i ==0) and (is_prime($i))){
		$largest = $i;
		last;
	}
	}

print "$largest";

sub is_prime{
	$n = $_[0];
	for($j = 2; $j < $n/2; $j++){
		if ($n % $j == 0){
			return 0;
			}
		}
		return 1; 
	}