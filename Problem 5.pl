
$i = 20*20;
$found = 0;
while(!$found){
	for ($j = 20; $j > 2; $j--){
		if(!($i % $j == 0)){
			last;
			}
		}
		if($j == 2){
			$found = $i;
			}
	$i += 20;
	
	}
	
print "$found";