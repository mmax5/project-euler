 use Math::Complex;

$sum_of_squares = 0;
for($i = 1; $i < 101; $i++){
	$sum_of_squares += $i*$i;
	$sum += $i;
	}
printf "%d", $sum*$sum - $sum_of_squares;