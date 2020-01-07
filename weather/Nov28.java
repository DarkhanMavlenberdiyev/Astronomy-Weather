import java.util.*;

class Nov28 {
	public static void main(String[] args) {
		Scanner in = new Scanner(System.in);
		/*
		int n = in.nextInt();

		int[] lis = new int[n];
		for (int i=0;i<n;i++ ) {
			lis[i] = in.nextInt();
		}*/
		System.out.println(true ^ true);

		/*
		int[][] nums= new int[n][n];
		for (int i=0;i<n;i++ ) {
			for (int j=0;j<n;j++ ) {
				nums[i][j]=in.nextInt();
			}
		}
		System.out.print(sumArr(nums));*/
		/*

		String[] lis = new String[n];
		in.nextLine();
		for (int i=0;i<n ;i++ ) {
			lis[i]=in.nextLine();
		}

		sort(lis);*/

		/*
		int[][] arr1 = new int[2][2];
		int[][] arr2 = new int[2][2];

		for (int i=0;i<arr1.length;i++ ) {
			for (int j=0;j<arr1.length;j++ ) {
				arr1[i][j]=in.nextInt();
			}
		}for (int i=0;i<arr2.length;i++ ) {
			for (int j=0;j<arr2.length;j++ ) {
				arr2[i][j]=in.nextInt();
			}
		}
		int[][] res = multiplMatrices(arr1,arr2);
		for (int i=0;i<2;i++ ) {
			for (int j=0;j<2;j++ ) {
				System.out.print(res[i][j]+" ");
			}System.out.println();
		}
		int[][] arr = {
			{1, 2, 3},
			{4, 5, 6},
			{7, 8, 9},
		};

		int answer = 1;
		for(int i = 0; i < arr.length; i++){
			answer = answer * arr[i][i];
		}

		int answer2 = 1;
		for(int i = 0, j = arr.length-1; i < arr.length; i++, j--) {
				answer2 = answer2 * arr[i][j];
		}

		System.out.println(answer2-answer)
		*/
	}
	public static int[] removeDuplicate(int[] nums){
	
		ArrayList<Integer> list = new ArrayList<>();
		list.add(nums[0]);
		for (int i=1;i<nums.length;i++ ) {
			if(!list.contains(nums[i])){
				list.add(nums[i]);
			}
		} 
		int[] res = new int[0];
		return res;


	}
	public static int sumArr(int[][] nums){
		
		int sum = 0;
		for (int i=0;i<nums.length ;i++ ) {
			for (int j=0;j<nums.length ;j++ ) {
				sum+=nums[i][j];
			}
		}
		return sum;
	}



	public static int[][] multiplMatrices(int[][] arr1,int[][] arr2){
		int[][] res = new int[2][2];
  
		res[0][0] =  arr1[0][0]*arr2[0][0] + arr1[0][1]*arr2[1][0];
		res[0][1] =  arr1[0][0]*arr2[0][1] + arr1[0][1]*arr2[1][1];
		res[1][0] =  arr1[1][0]*arr2[0][0] + arr1[1][1]*arr2[1][0];
		res[1][1] =  arr1[1][0]*arr2[0][1] + arr1[1][1]*arr2[1][1];

		return res;



	}	

	public static void sort(String[] nums){

		int[] s = new int[nums.length];
	
		for (int i=0;i<nums.length;i++ ) {
			String[] l = new String[] {"4","+","8"};

			int k = 0;
			for (int j=0;j<nums[i].length();j++ ) {
					if (!Character.isDigit(nums[i].charAt(j))){
						k++;
						l[k]= ""+nums[i].charAt(j);
						k++;
					}else{

						l[k]+=nums[i].charAt(j);
					}
			}
			
			switch(l[1]){
				case "+": s[i]=Integer.parseInt(l[0])+Integer.parseInt(l[2]);break;
				case "-":s[i]=Integer.parseInt(l[0])-Integer.parseInt(l[2]);
			}
			

		}
		int a = 0;
		while (a<s.length-1){
			if (s[a]>s[a+1]){
				int temp = s[a];
				s[a]=s[a+1];
				s[a+1]=temp;

				String temp2 = nums[a];
				nums[a]=nums[a+1];
				nums[a+1]=temp2;
				a=0;
			}else{
				a++;
			}
		}
		for (int i=0;i<nums.length ;i++ ) {
			System.out.println(nums[i]);
		}

	}


}

class BinaryNumbers {
	String value;
	public BinaryNumbers(String value){
		if (value.length()>16 || value.length()<16) {
			value = "0000000000000000";
					
					
		}else{
			this.value = value;
		}
	}

	public void and(String v){
		String s = "";
		for (int i=0;i<v.length();i++ ) {
			if (v.charAt(i)=='1' && this.value.charAt(i)=='1') {
				s+='1';
			}else {
				s+='0';
			}
		}
	}public void or(String v){
		String s = "";
		for (int i=0;i<v.length();i++ ) {
			if (v.charAt(i)=='1' || this.value.charAt(i)=='1') {
				s+='1';
			}else {
				s+='0';
			}

	}
}	public void xor(String v){
			String s = "";
		for (int i=0;i<v.length();i++ ) {
			if (v.charAt(i)=='1' ^ this.value.charAt(i)=='1') {
				s+='1';
			}else {
				s+='0';
			}
	}
}

	public void invertBits(char c){
		if (c=='1') {
			c = '0';
		}else{
			c = '1';
		}
	}	
	public void print(){
		System.out.println(value);
	}
	public boolean isValidBinary(String v){
		for (int i=0;i<v.length() ;i++ ) {
			if (v.charAt(i)!='1' || v.charAt(i)!='0') {
				return false;
			}
		}
		return true;
	}
}