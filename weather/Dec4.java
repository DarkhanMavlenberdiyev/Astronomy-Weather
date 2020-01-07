import java.util.*;
class Dec4 {
	public static void main(String[] args) {
		Scanner in = new Scanner(System.in);
		int n = in.nextInt();
		int [] lis = new int[n];
		for (int i=0; i<n;i++ ) {
			lis[i] = in.nextInt();
		}
		int[] res = sort(lis);
		for (int i=0;i<lis.length;i++ ) {
			System.out.println(reverse(lis[i]));
		}
	}


	public static String isFibo(int n){
		long f = 1;
		long s = 1;
		while(s<=n){
			if (s==n){
				return "isFib";

			}else{
				long temp = s+ f;
				f = s;
				s = temp;
			}
		}return "isNotFib";
	}

	public static String solve(int n){
		int[] lis = new int[] {9,90,99,900,909,999,9000,9009,9099,9999};
		for (int i=0;i<lis.length;i++ ) {
			if (lis[i]%n==0) {
				return lis[i]+"";
			}
		}return "";
	}


	public static int[] sort(int[] lis){
		int a = 0;
		while(a<lis.length-1){
			if (reverse(lis[a])>reverse(lis[a+1])) {
				int temp = lis[a];
				lis[a]=lis[a+1];
				lis[a+1] = temp;
				a=0;
			}else{
				a++;
			}
		}
		return lis;

	} 
	public static int reverse(int n){

		String res = "";
		while(n!=0){
			res += n%10;
			n/=10;
		}
		return Integer.parseInt(res);
	}


}