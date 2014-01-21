package projecteuler;

/**
 * Created by mmax on 1/21/14.
 */
public class Problem34 {

    public static int fact(int n){
        int result = 1;
        for (int i = 1; i <= n; i++) {
            result = result * i;
        }
        return result;
    }

    public static void main(String[] args){
        System.out.println(fact(7));

        int sums = 0;
        for(int i =3; i < 10000000; i++){
            int sum = 0;
            int number = i;
            while(number > 0){
                //System.out.println(number % 10);
                sum = sum + fact(number % 10);
                number = number / 10;
            }
            if(sum == i){
                sums += sum;
                System.out.println(i);
            }
        }
        System.out.print(sums);
    }

}
