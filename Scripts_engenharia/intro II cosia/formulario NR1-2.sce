// Para o escoamento turbulento de um fluido em um tubo liso, a expressão abaixo
//pode ser usada para determinar o fator de atrito, f , em função do número de Reynolds, Re.

function f=func(fat)
    Re=5000
    f= (fat*(1.74*log(Re*sqrt(fat))-0.4)) - sqrt(fat)
endfunction


function [x,f,IT]=NRUni(x0,func)
    IT= 0;ITMAX=100
    tol=10e-6
    f0 = func(x0)
    
    while abs(f0)>tol & IT< ITMAX
        df0=numderivative(func,x0)
        passo=-f0/df0
        x1=x0+passo
        f1=func(x1)
       
        
        if abs(f1) > abs(f0) then// se o resultado piorar pelo passo
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



fat0= 0.316*(5000**-0.25)

[fat,Fzero,IT] = NRUni(fat0,func)

disp(fat,Fzero,IT)
//com 4 iterações chegamos em um resultado muito proximo a 0
//fat é aproximadamente 0,0093296
