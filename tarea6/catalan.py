import profile
import sys
import getopt
import time 


counter_cat = 0 
counter_cat_mem = 0
def num_catalan(n):
    global counter_cat
    counter_cat += 1
    if n <= 1: 
        return 1
    else:
        counter = 0
        for i in range(n):
            counter += num_catalan(i)* num_catalan(n-i-1) 
        return counter


def num_catalan_mem(n, Matrix):
    global counter_cat_mem
    counter_cat_mem += 1
    if n <= 1:
        return 1
    else:
        counter = 0
        for i in range(n):
            cat_i = Matrix[i] if Matrix[i] != -1 else num_catalan_mem(i, Matrix)
            Matrix[i] = cat_i
            cat_n_1 = Matrix[n-i-1] if Matrix[n-i-1] != -1 else num_catalan_mem(n-i-1, Matrix)
            Matrix[n-i-1] = cat_n_1
            counter += cat_i *cat_n_1 
        return counter

def main(recursivo = False):
    n_max = 100 
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
            res = num_catalan_mem(n, Matrix)
            print "%d %s %d %d"% (n, time.time() - start, counter_cat_mem, res)

if __name__ == '__main__':
    argv = sys.argv[1:]
    opts, args = getopt.getopt(argv, "r", ["local="])
    if opts: #Si el usuario mando alguna bandera
        main(True)
    else:
        print "CHo"
        main(False)
