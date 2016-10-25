import profile
import sys
import getopt

def num_catalan(n):
    if n == 1:
        return 1
    else:
        counter = 0
        for i in range(1,n-1):
            counter += num_catalan(i)* num_catalan(n-1)
        return counter



def num_catalan_mem(n, Matrix):
    if n == 1:
        return 1
    else:
        counter = 0
        for i in range(1,n-1):
            cat_i = Matrix[i] if Matrix[i] != -1 else num_catalan_mem(i, Matrix)
            cat_n_1 = Matrix[n-1] if Matrix[n-1] != -1 else num_catalan_mem(n-1, Matrix)
            counter += cat_i *cat_n_1

        return counter

def main(recursivo = False):
    n_max = 100
    if recursivo:
        for n in range(1, n_max):
            print "*"*10
            print "%d" %(n)
            profile.run('num_catalan(%d)' %(n))
    else:
        for n in range(1, n_max):
            Matrix = [-1 for x in range(n+1)]
            print "*"*10
            print "%d" %(n)
            profile.runctx('print num_catalan_mem(n,Matrix); print', globals(), {'n':n, 'Matrix':Matrix})

if __name__ == '__main__':
    argv = sys.argv[1:]
    opts, args = getopt.getopt(argv, "r", ["local="])
    if opts: #Si el usuario mando alguna bandera
        main(True)
    else:
        main(False)
