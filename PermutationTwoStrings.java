package arraylist;

public class PermutationTwoStrings {
	static boolean result = true;

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		result = permutation("doggie","god");
		System.out.println(result);
	}
	
	static String sort(String s) {
		char[] content = s.toCharArray();
		java.util.Arrays.sort(content);
		return new String(content);
	}
	private static boolean permutation(String string, String string2) {
		// TODO Auto-generated method stub
		if (string.length() != string2.length()) {
			return false;
		}
		return sort(string).equals(sort(string2));
	}

	
}
