import sys
from io import StringIO
from lesson01.hello import print_hello

old_stdout = sys.stdout
sys.stdout = mystdout = StringIO()

# blah blah lots of code ...
print('Before')
print_hello()
print('After')
sys.stdout = old_stdout

print("GOT: " + mystdout.getvalue())
