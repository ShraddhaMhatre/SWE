//Check whether a linkedlist is cyclic
//Yahoo
import java.util.HashSet;

static class ListNode {
    int data;
    ListNode next;
    ListNode(int x) {
        data = x
        next = null;
    }
 }

public class Solution {


public void hasCycle(ListNode head) {
	Set<ListNode> hs = new HashSet<>();
	while (head!=null) {
		if (hs.contains(head){
			return true;
		} else {
			hs.add(head);
		}
		head = head.next;
	}
return false;	
}

}
