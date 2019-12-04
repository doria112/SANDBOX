"""
The read4 API is already defined for you.

    @param buf, a list of characters
    @return an integer
    def read4(buf):

# Below is an example of how the read4 API can be called.
file = File("abcdefghijk") # File is "abcdefghijk", initially file pointer (fp) points to 'a'
buf = [' '] * 4 # Create buffer with enough space to store characters
read4(buf) # read4 returns 4. Now buf = ['a','b','c','d'], fp points to 'e'
read4(buf) # read4 returns 4. Now buf = ['e','f','g','h'], fp points to 'i'
read4(buf) # read4 returns 3. Now buf = ['i','j','k',...], fp points to end of file
"""
class Solution:
    def __init__(self):
        self.res_buf = []
        
    def read(self, buf, n):
        """
        :type buf: Destination buffer (List[str])
        :type n: Number of characters to read (int)
        :rtype: The number of actual characters read (int)
        """
        if n <= len(self.res_buf):
            for i in range(n):
                buf[i] = self.res_buf[i]
            self.res_buf = self.res_buf[n:]
            return n
        else:
            i = len(self.res_buf)
            for j in range(i):
                buf[j] = self.res_buf[j]
            self.res_buf = self.res_buf[i:]
        while i < n:
            buf4 = ['']*4
            r4 = read4(buf4)
            if i + r4 >= n:
                for j in range(i,n):
                    buf[j] = buf4[j-i]
                self.res_buf = buf4[n-i:]
                return n
            elif r4 < 4:
                for j in range(r4):
                    buf[i+j] = buf4[j]
                return i+r4
            else:
                for j in range(4):
                    buf[i+j] = buf4[j]
                i += r4

                
# Version 2
# Shorter code, but should be slower and taking more space
"""
The read4 API is already defined for you.

    @param buf, a list of characters
    @return an integer
    def read4(buf):

# Below is an example of how the read4 API can be called.
file = File("abcdefghijk") # File is "abcdefghijk", initially file pointer (fp) points to 'a'
buf = [' '] * 4 # Create buffer with enough space to store characters
read4(buf) # read4 returns 4. Now buf = ['a','b','c','d'], fp points to 'e'
read4(buf) # read4 returns 4. Now buf = ['e','f','g','h'], fp points to 'i'
read4(buf) # read4 returns 3. Now buf = ['i','j','k',...], fp points to end of file
"""
class Solution:
    def __init__(self):
        self.buf = []

    def read(self, buf, n):
        """
        :type buf: Destination buffer (List[str])
        :type n: Number of characters to read (int)
        :rtype: The number of actual characters read (int)
        """
        while n > len(self.buf):
            buf4 = [' '] * 4
            n_read4 = read4(buf4)
            self.buf.extend(buf4[:n_read4])
            if n_read4 == 0: # end of file
                n_read = len(self.buf)
                for i,l in enumerate(self.buf):
                    buf[i] = l
                self.buf = []
                return n_read
        # in place assignment
        for i in range(n):
            buf[i] = self.buf[i]
        self.buf = self.buf[n:]
        return n
