class ListNode():
    def __init__(self, val, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next
class BrowserHistory:
    def __init__(self, homepage: str): # Initialise homepage
        self.node = ListNode(homepage)
    

    def visit(self, url: str) -> None: # This means go to URL
        curr = self.node
        self.node = ListNode(url)
        curr.next = self.node
        self.node.prev = curr


    def back(self, steps: int) -> str:
        curr, prev = self.node, self.node.prev
        for _ in range(steps):
            if self.node.prev:
                self.node = self.node.prev
                continue
            else:
                break
        return self.node.val
                
                
    def forward(self, steps: int) -> str:
        curr, tail = self.node, self.node.next
        for _ in range(steps):
            if self.node.next:
                self.node = self.node.next
                continue
            else:
                break
        return self.node.val


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)