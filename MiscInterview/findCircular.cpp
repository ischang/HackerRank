bool findCirculoar (Node *head){
	Node *turtlePtr, *harePtr;

	turtlePtr = head;
	harePtr = head->next.next;

	while (true){
		if (!harePtr || harePtr->next == NULL){
			return false;
		}//if

		else if (turlePtr == harePtr || turtlePtr == harePtr->next){
			return true;
		}//else if

		else{
			turtlePtr = turtlePtr ->next;
			harePtr = (harePtr->next)->next;
		}//else

		return false
	}//while
}//bool findCircular

//Python implementation

//def findCircular (Node head):
//	Node turtlePtr
//	Node harePtr

//	turtlePtr = head
//	harePtr = head.next.next

//	while True:
//		if not(harePtr) or (harePtr.next is None):
//			return False
//		elif (tutrtlePtr == harePtr) or (turtlePtr == harePtr.next):
//			return True
//		else:
//			turtlePtr = turtlePtr.next
//			harePtr = harePtr.nex.next 

//		return False