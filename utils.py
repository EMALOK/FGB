log_explain = False

def expl(*parg):
    if log_explain:
        print(*parg)

def perr(*parg):
    print('\033[91m', *parg,'\033[0m')
    
def pwarn(*parg):
    print('\033[93m', *parg,'\033[0m')
