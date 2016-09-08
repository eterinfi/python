class fib(object):
    def __init__(self, max):
        self.a, self.b, self.max = 0, 1, max # Initiate
    
    def __len__(self):
        a, b, le = 1, 1, 0
        while a <= self.max:
            a, b = b, a + b
            le += 1
        return le

    def __getitem__(self, n): # Indexing
        if isinstance(n, int):
            a, b = 1, 1
            for x in range(n):
                a, b = b, a + b
                if a > self.max: # Beyond Limit
                    return None
            return a
        elif isinstance(n, slice):
            l = len(self)
            if n.step is None:            step = 1
            elif isinstance(n.step, int): step = n.step
            else: raise TypeError('slice indices must be integers or None')
            if step > 0:
                if n.start is None:            start = 0
                elif isinstance(n.start, int): start = n.start
                else: raise TypeError('slice indices must be integers or None') 
                if start < 0: start += l        # Reversed Start Index
                if start < 0: start = 0         # Reset Start Index to Min
                if n.stop is None:            stop = l
                elif isinstance(n.stop, int): stop = n.stop
                else: raise TypeError('slice indices must be integers or None')
                if stop < 0: stop += l          # Reversed Stop Index
                if stop > l: stop = l           # Reset Stop Index to Max
                # print 'FOR %d TO %d STEP %d' % (start, stop - 1, step)
            elif step < 0:
                if n.start is None:            start = -1
                elif isinstance(n.start, int): start = n.start
                else: raise TypeError('slice indices must be integers or None')
                if start < 0:     start += l    # Reversed Start Index
                if start > l - 1: start = l - 1 # Reset Start Index to Max
                if n.stop is None:            stop = 0
                elif isinstance(n.stop, int): stop = n.stop
                else: raise TypeError('slice indices must be integers or None')
                if stop < 0: stop += l          # Reversed Stop Index
                if stop < 0: stop = 0           # Reset Stop Index to Min
                if n.stop is None: stop = -1    # Down to the End
                # print 'FOR %d DOWNTO %d STEP %d' % (start, stop + 1, step)
            else:
                raise ValueError('slice step cannot be zero')
            L = [self[x] for x in range(start, stop, step) if not self[x] is None]
            return L
        else:
            raise TypeError('list indices must be integers')
    
    def __iter__(self):
        return self   # Self-iterable
    
    def next(self): # Iteration
        self.a, self.b = self.b, self.a + self.b # Next Value
        if self.a > self.max: # Beyond Limit
            raise StopIteration()
        return self.a # Return Next Value

f = fib(1000)
for i in f:  # Start Iterating
    print i,
print; j = 0 # Start Indexing
while True:
    if f[j]:
        print 'f[%d] = %d' % (j, f[j]),
        j += 1
    else:
        break