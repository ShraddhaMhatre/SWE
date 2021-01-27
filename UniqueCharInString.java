package arraylist;

//Cracking-the-code-interview 1.1
public class UniqueCharInString {

	static boolean uniqChar = true;
	
	public static void main(String[] args) {

		uniqChar = isUniqueChars("Darshin");
		System.out.println(uniqChar);
	}

	private static boolean isUniqueChars(String string) {
		if (string.length() > 128) return false;
		
		boolean[] char_set = new boolean[128];
		for (int i = 0; i < string.length(); i++) {
			int val = string.charAt(i);
			if (char_set[val]) {
				return false;
			}
			char_set[val] = true;
		}
		
		return true;
	}
	
	

}
