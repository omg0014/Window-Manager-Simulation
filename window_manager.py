from collections import OrderedDict

class WindowManager:
    def __init__(self):
        self.state = {}         
        self.z_order = OrderedDict()  
    def open(self, id):
        if self.state.get(id) == 1:
            self.focus(id)
            return
        
        self.state[id] = 1
        self.z_order[id] = True
        self.z_order.move_to_end(id, last=False)  
    def focus(self, id):
        if self.state.get(id, 0) == 0:
            return
        
        if self.state[id] == 2:
            self.restore(id)
            return
        
        self.z_order.move_to_end(id, last=False)

    def minimize(self, id):
        if self.state.get(id) != 1:
            return
        
        self.state[id] = 2
        self.z_order.pop(id, None)

    def restore(self, id):
        if self.state.get(id) != 2:
            return
        
        self.state[id] = 1
        self.z_order[id] = True
        self.z_order.move_to_end(id, last=False)

    def close(self, id):
        if self.state.get(id, 0) == 0:
            return
        
        if self.state[id] == 1:
            self.z_order.pop(id, None)
        
        self.state[id] = 0

    def top(self):
        if not self.z_order:
            return -1
        return next(iter(self.z_order)) 

    def list(self):
        return list(self.z_order.keys())

wm = WindowManager()

q = int(input())

for _ in range(q):
    parts = input().split()
    op = parts[0]

    if op == "OPEN":
        wm.open(int(parts[1]))
    elif op == "FOCUS":
        wm.focus(int(parts[1]))
    elif op == "MINIMIZE":
        wm.minimize(int(parts[1]))
    elif op == "RESTORE":
        wm.restore(int(parts[1]))
    elif op == "CLOSE":
        wm.close(int(parts[1]))
    elif op == "TOP":
        print(wm.top())
    elif op == "LIST":
        print(*wm.list())  
