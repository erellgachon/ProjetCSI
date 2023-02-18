####################################
###################################

##  ADDITION ET PRODUIT DANS LE TORE ##

# a,b in Tp
def AddInTore(p,a,b) :
    return (a+b)%p

# x in Tp
# n in Z
def MultExtTore(p,n,x):
    if(n>=0):
        cpt = 0
        for i in range(n):
            cpt = AddInTore(p,cpt,x)
        return cpt
    return MultExtTore(p,-n,-x)




#################################
#################################

## TORE ET MATRICES


#Addition de deux matrices à coefficients dans Tq
def AddInMatr(q,M1,M2):
    return [[AddInTore(q,M1[i][j],M2[i][j]) for j in range(len(M1[0]))] for i in range(len(M1))]


#Multiplication de chaque élément de la matrice par une constante
#K une constante de Z
#M matrice de Tq
def MultExtMatr(q,K,M):
    return [[MultExtTore(q,K,M[i][j]) for j in range(len(M[0]))] for i in range(len(M))]


#Multiplication de deux matrices
#M1 matrice de Z
#M2 matrice dans Tq
def MultInMatr(q,M1,M2) :
    M = [[0 for _ in range(len(M2[0]))] for _ in range(len(M1))]
    for i in range(len(M1)) :
        for j in range(len(M2[0])) :
            for k in range(len(M2)) :
                M[i][j] = AddInTore(q,M[i][j],MultExtTore(q,M1[i][k],M2[k][j]))
    return M




################################
################################

## POLYNOMES DANS LE TORE ET MATRICES


# Addition de deux polynômes de Tq / (X^N+1)
# P1,P2 in Tp[X] / (X^N+1)
def AddPolyInTore(q,N,P1,P2) :
    P = [0]*N
    for i in range(N) :
        P[i] = AddInTore(q,P1[i],P2[i])
    return P

# P1 in Z[X] / X^N+1
# P2 in TP[X] / X^N+1
def MultPolyExt(q,N,P1,P2) :
    P = [0]*2*N
    for i in range(N) :
        for j in range(N) :
            tmp = MultExtTore(q,P1[i],P2[j])
            P[i+j] = AddInTore(q,P[i+j],tmp)
    for i in range(N) :
        P[i] = AddInTore(q,P[i],-P[i+N])
        if P[i]==0 :
            P[i]=1
    return P[:N]

# Addition de deux matrices de polynômes de Tq[X] / (X^N+1)
def AddInMatrPoly(q,N,M1,M2):
    return [[AddPolyInTore(q,N,M1[i][j],M2[i][j]) for j in range(len(M1[0]))] for i in range(len(M1))]


#Multiplication de chaque coeff d'une matrice de polynômes de Tq[X] / (X^N+1) par un polynôme de Z/pZ[X]
#M in Tq[X] / (X^N+1)
#K in Z/pZ[X]
def MultExtMatrPoly(q,N,K,M):
    return [[[MultExtTore(q,K[k],M[i][j]) for k in range(N)] for j in range(len(M[0]))] for i in range(len(M))]


#Multiplication de deux matrices
#M1 in Z[X] / (X^N+1)
#M2 in Tq[X] / (X^N+1)
def MultMatPoly(q,N,M1,M2) :
    M = [[[0]*N for _ in range(len(M2[0]))] for _ in range(len(M1))]
    for i in range(len(M1)) :
        for j in range(len(M2[0])) :
            for m in range(len(M2)) :
                tmp = MultPolyExt(q,N,M1[i][m],M2[m][j])
                M[i][j] = AddPolyInTore(q,N,M[i][j],tmp)
    return M
