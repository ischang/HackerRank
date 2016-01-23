import java.util.*;
	
	// array [1, 2, 3, 7, 6]
	//t = 9
	//given an array and target number,  return indices of one pair that adds up to the 
//number in the array

public class twoSum {
	public static int[] returnIndices (int t, int[] args){
		HashMap<Integer, Integer> hashTable = new HashMap<Integer, Integer>();
		int array[] = new int [2];
		for (int i = 0; i < args.length; i++){
			hashTable.put(args[i], i);
		}//putting in for loop

		for (int i = 0; i < args.length; i++){
			int difference = t - args[i];
			if (hashTable.containsKey(args[i])){
				array[0] = hashTable.get(difference);
				array[1] = i;
				return array;
			}//if
		}//for

		array[0] = -1;
		return array;
	}//blah
	public static void main (String[] args){
		int returnArr[] = new int[2];
		int testArr[] = new int[]{1,2,6,3,7,8};

		returnArr = returnIndices(9, testArr);
		System.out.println(returnArr[0]);
		System.out.println(returnArr[1]);

		//Hash array into a hashmap
		//key 
	}
}//twoSum