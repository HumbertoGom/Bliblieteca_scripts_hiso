function f=func(x)
    f= exp(x) -x
endfunction
//funcao teste


function [x,f,IT]=NR_DO_MAL(x0,func)
    IT= 0;ITMAX=100
    tol=10e+20
    f0 = func(x0)
    
    while abs(f0)<tol & IT< ITMAX
        df0=numderivative(func,x0)
        passo=f0/df0
        x1=x0+passo
        f1=func(x1)
       
        
        if abs(f1) < abs(f0) then// se o resultado piorar pelo passo
            passo = 0.5*f0/df0
            x1=x0+passo
            f1=func(x1)
        else
            ... 
        end
        x0=x1
        f0=f1
        IT= IT+1
    end
    x= x0
    f= f0
endfunction


[X,faval,ite] = NR_DO_MAL(0,func)
disp(X,faval,ite)
