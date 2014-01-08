use strict;
use warnings;
use Math::Complex;

my $sum = 2;
for(my $i = 2; $i < 2000000; $i++){
	$sum += is_prime($i) ? $i : 0;
	}
	
print "$sum";

	sub is_prime{
	my $max = $_[0];
	my $n = sqrt($max);
	for(my $j = 2; $j < $n+1; $j++){
		if ($max % $j == 0){
			return 0;
			}
		}
		return 1; 
	}