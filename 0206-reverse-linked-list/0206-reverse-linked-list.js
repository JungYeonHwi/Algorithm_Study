/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @return {ListNode}
 */
var reverseList = function(head) {
    let arr = [];

    for (let i = head; i != null; i = i.next) {
        arr.push(i.val);
    }

    let answer = new ListNode(0);
    let current = answer;

    for (let i = arr.length - 1; i >= 0; i--) {
        current.next = new ListNode(arr[i]);
        current = current.next;
    }

    return answer.next;
};