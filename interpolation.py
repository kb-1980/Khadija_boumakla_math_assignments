def multiplypoly(poly1,poly2):
    result=[0]*(len(poly1)+len(poly2)-1)
    for i in range(len(poly1)):
        for j in range(len(poly2)):
            result[i+j]+=poly1[i]*poly2[j]
    return result

def computeLk(points,k):
    n=len(points)
    x_points=[p[0] for p in points]
    
    num=[1.0]
    den=1
    for j in range(n):
            if j!=k:
                num=multiplypoly(num,[-x_points[j],1])
                den*=(x_points[k]-x_points[j])
    return [c/den for c in num]


def computePL(points):
    n=len(points)
    x_points=[p[0] for p in points]
    y_points=[p[1] for p in points]
    p=[0.0]*n
    for k in range(n):
        Lk=computeLk(points,k)
        for i in range(len(Lk)):
            p[i]+=y_points[k]*Lk[i]

    return p
    



def all_Lk(points):
    n=len(points)
    
    for k in range(n):
        Lk=computeLk(points,k)

        print(f"L_{k}(x)=", end="")
        style=" ¹²³⁴⁵⁶⁷⁸⁹"
        for d in range(len(Lk)-1,-1,-1):
            if round(Lk[d], 2) == 0:
                continue
            if (d==0) :
                print(f"{Lk[d]:.2f}",end=" ")
            else:
                print(f"{Lk[d]:.2f}x{style[d]}",end=" + ")
        print()




def lagrange_interpolation(points):
   all_Lk(points)
   print()
   computePL(points)