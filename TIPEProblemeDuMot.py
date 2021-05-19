# Générateurs représentés par 1, 2, 3 et 4 et leur inverse avec un "-" devant
##
def reduire_help(L):# supprime la première occurrence d'un générétateur et de son inverse à la suite
    for i in range(len(L)-1):
        for j in range(1,5):
            if (L[i]==j and L[i+1]==-j) or (L[i]==-j and L[i+1]==j):
                L[i]=0
                L[i+1]=0
    k=L.count(0)
    for i in range(k):
        L.remove(0)
    return L
##
def reduire(L):# supprime toutes les occurrences d'un générétateur et de son inverse à la suite, ie réduit les mots dans le groupe libre
    k=0
    n=len(L)
    M=[]
    while k<n/2:
        M=reduire_help(L)
        k=k+1
        L=M
    return L
##
B=[1,-1,4,2,-2,-4,1,-1,3,4,-3,3,3,2,-4]
reduire(B)
##
def de_tresse_a_libre_help(gen,libre):# donne l'action d'un générateur du groupe des tresses sur un mot du groupe libre
    if libre==[]:
        return []
    else:
        return action(gen,libre[0]) + de_tresse_a_libre_help(gen,libre[1:])
##
print(reduire(de_tresse_a_libre([1,1],[1,1])))
##
def de_tresse_a_libre(t,libre):# donne l'action d'une tresse sur un mot du groupe libre
    if t==[]:
        return libre
    else:
        return de_tresse_a_libre(t[1:],de_tresse_a_libre_help(t[0],libre))
##
def action(i,j):# donne l'action d'un générateur du groupe des tresses sur un générateur du groupe libre
    if j > 0:
        if i > 0:
            if j==i:
                return [-j,j+1,j]
            elif j==i+1:
                return [j-1]
            else:
                return [j]
        else:
            if j==-i:
                return [j+1]
            elif j==-i+1:
                return [j,j-1,-j]
            else:
                return [j]
    else:
        l=action(i,-j)
        for k in range(len(l)):
            l[k]=-l[k]
        l.reverse()
        return l
##
def triviale(B):# dit si une tresse est triviale ou non
    print("La tresse :",B)
    test=True
    for i in range(1,5):
        if len(de_tresse_a_libre(B,[i]))<50:
            print("L'action sur le", i, "e générateur du groupe libre :",de_tresse_a_libre(B,[i]))
        else:
            print("L'action sur le", i, "e générateur du groupe libre : trop long !!, de longueur",len(de_tresse_a_libre(B,[i])))
        print("Le mot réduit :", reduire(de_tresse_a_libre(B,[i])))
        test=(reduire(de_tresse_a_libre(B,[i]))==[i] and test)
        if test==False:
            break
    if test:
        return "La tresse est triviale"
    else:
        return "La tresse n'est pas triviale"
##
print(triviale([1,-1]))
print(triviale([1,2,-1,-2]))
print(triviale([1,1,1,2,2,-1,-1,-2,-2,-1]))
print(triviale([2,2,2,3,3,-2,-2,-3,-3,-2]))