package projecteuler;

/**
 * Created by mmax on 1/21/14.
 */
public class Problem36 {
    private static int SIZE = 1000000;

    public static void main(String args[]){
        int sum = 0;
        for(int i = 0; i <= SIZE; i++){
            if(isPalindrome(String.valueOf(i)) && isPalindrome(Integer.toBinaryString(i))){
                sum += i;
            }
        }
        System.out.println(sum);
    }

    private static boolean isPalindrome(String n){
        return new StringBuilder(n).reverse().toString().equals(n);
    }

}
