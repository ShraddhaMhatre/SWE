package arraylist;

public class PermutationStringsCharArray {

	static boolean result = false;
	public static void main(String[] args) {
		result = permutation("dogy","godi");
		System.out.println(result);
	}
	
	static boolean permutation(String s, String t) {
		if (s.length() != t.length()) return false;
		
		char content[] = s.toCharArray();
		int letters[] = new int[128];
		for(char c: content) {
			letters[c]++;
		}
		
		for(int i = 0; i < t.length(); i++) {
			int c = (int) t.charAt(i);
			letters[c]--;
			if(letters[c] < 0) return false;
		}
		
		return true;
	}

}
