def power  (N,P) :
    #if power is zero then the return value is 1
    if P== 0:
        return 1

    #if power is 1 then the return value is N
    elif P== 1:
        return N

    else:
            return(N*power(N, P-1))

            N=5
            P=2
