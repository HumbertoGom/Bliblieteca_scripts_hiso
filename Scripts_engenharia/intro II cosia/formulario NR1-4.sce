function f=visc(T)
    f=exp(-3.332+1039/T-0.001768*T +1.076*10^-6*T^2) - 0.1404804 
    //subtrair por V(400)/2 deveria zerar a função no u(tx)
    
endfunction



disp(visc(400)/2) //metade da visc de 400 = 0.1405~

function [x,f,IT]=NRUni(x0,func)
    IT= 0;ITMAX=100
    tol=10e-4
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

[T,Vobj,IT] = NRUni(600,visc)
disp('Temperatura Objetivo: ',T)
disp('Viscosidade Objetivo: ',Vobj+ 0.1404804) // eu tinha subtraido isso na função para chegar nesse valor
disp('Iterações até a convergência',IT)

//a temperatura onde a viscosidade é metade do valor em 400K é 520K.
