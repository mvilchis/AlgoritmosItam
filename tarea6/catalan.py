import profile
import sys
import getopt
import time 


counter_cat = 0 
counter_cat_mem = 0
def num_catalan(n):
    global counter_cat
    counter_cat += 1
    if n == 1: 
        return 1
    if n == 2:
        return 2
    else:
        counter = 0
        for i in range(1,n-1):
            counter += num_catalan(i)* num_catalan(n-i) 
        return counter


def num_catalan_mem(n, Matrix):
    global counter_cat_mem
    counter_cat_mem += 1
    if n == 1:
        return 1
    if n == 2:
        return 2
    else:
        counter = 0
        for i in range(1,n-1):
            cat_i = Matrix[i] if Matrix[i] != -1 else num_catalan_mem(i, Matrix)
            cat_n_1 = Matrix[n-i] if Matrix[n-i] != -1 else num_catalan_mem(n-i, Matrix)
            counter += cat_i *cat_n_1 
        return counter

def main(recursivo = False):
    n_max = 200 
    if recursivo:
        global counter_cat 
        for n in range(1, n_max):
            counter_cat = 0
            start = time.time()
            num_catalan(n)
            print "%d %s %d"% (n, time.time() - start, counter_cat)
    else:
        global counter_cat_mem
        for n in range(1, n_max):
            Matrix = [-1 for x in range(n+1)]
            counter_cat_mem = 0
            start = time.time()
            num_catalan_mem(n, Matrix)
            print "%d %s %d"% (n, time.time() - start, counter_cat_mem)

if __name__ == '__main__':
    argv = sys.argv[1:]
    opts, args = getopt.getopt(argv, "r", ["local="])
    if opts: #Si el usuario mando alguna bandera
        main(True)
    else:
        main(False)
