use strict;
use warnings;
use Math::Complex;

my $max_j = 1;
my $max = 1;

for(my $i = 1; $i < 1000000; $i++){
	my $n = $i;
	my $j = 0;
	while($n != 1){
		$j++;
		if($n % 2 == 0){
			$n = $n/2;
		}else{
			$n = $n * 3 + 1;
		}
		}
	print $i, " ", $j, "\n";
	if($j > $max_j){
		$max_j = $j;
		$max = $i;
		}
	}
	
print $max, " ", $max_j;