use strict;
use warnings;

for(my $i = 1; $i < 500 ; $i++){
		
		for(my $j = 1; $j < 500; $j++){
			my $c = 1000 - $j - $i;				
			my $a = 1000 - $c - $i;
			my $b = $i;
			if(($a*$a+$b*$b == $c*$c)){
				printf "%d\n", $a*$b*$c;
				printf "%d %d %d", $a, $b, $c;
				last;
			}
		}		
		
	}