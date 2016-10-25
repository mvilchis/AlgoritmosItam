import profile
import sys
import getopt
def n_part(m,n):
    if (m == 1 or n == 1):
        return 1
    else:
        if (m < n ):
            return n_part(m,m)
        else:
            if (m == n):
                return 1+ n_part(m,m-1)
            else:
                return n_part(m,n-1) + n_part(m-n, n)


def n_part_mem(m,n, Matrix):
    if (m == 1 or n == 1):
        return 1
    else:
        if (m < n ):
            if (Matrix[m][n] == -1):
                tmp = Matrix[m][m]  if Matrix[m][m]  != -1 else n_part_mem(m,m,Matrix)
                Matrix [m][n]= tmp
            return Matrix[m][n]
        else:
            if (m == n):
                if (Matrix[m][n] == -1):
                    tmp = Matrix[m][m-1] if Matrix[m][m-1] != -1 else  n_part_mem(m,m-1,Matrix)
                    Matrix[m][n] = 1 + tmp
                return Matrix[m][n]

            else:
                if (Matrix[m][n] == -1):
                    tmp1 =Matrix[m][n-1] if Matrix[m][n-1] != -1 else  n_part_mem(m,n-1,Matrix)
                    tmp2 =Matrix[m-n][n] if Matrix[m-n][n] != -1 else  n_part_mem(m-n,n,Matrix)
                    Matrix[m][n] = tmp1 + tmp2
                return Matrix[m][n]
def main(recursivo = False):
    n_lim = 100
    m_lim = 100
    if recursivo:
        """ Medimos el tiempo para recursivo """
        for m in range (1,m_lim):
            for n in range (1,n_lim):
                Matrix = [[-1 for x in range(n+1)] for y in range(m+1)]
                print "*"*10
                print "%d %d" %(m,n)
                profile.run('n_part(%d,%d)' %(m,n))
    else:

        """ Medimos el tiempo para el caso pd """
        for m in range (1,m_lim):
            for n in range (1,n_lim):
                Matrix = [[-1 for x in range(n+1)] for y in range(m+1)]
                print "*"*10
                print "%d %d" %(m,n)
                profile.runctx('print n_part_mem(m,n,Matrix); print', globals(), {'m':m, 'n':n, 'Matrix':Matrix})
                #profile.run('n_part_mem(%d,%d,%s)' %(m,n, Matrix))

if __name__ == '__main__':
    argv = sys.argv[1:]
    opts, args = getopt.getopt(argv, "r", ["local="])
    if opts: #Si el usuario mando alguna bandera
        main(True)
    else:
        main(False)
