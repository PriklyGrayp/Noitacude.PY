'''Function Arguments in detail'''
import time
time.ctime()

def show_default(arg=time.ctime()):
    print(arg)


'''def Variable Scoping():
Scopes ar contexts in whioch named references can be looked up.
'''

'''LEGB rule'''
# Local : Inside the current function
# Enclosing :Any and all enclosing functions
# Global :Top-level of module
# Built-in : Provided but the builtins module
