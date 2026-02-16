function f=func(fat)
    Re=5000
    f= (fat*(1.74*log(Re*sqrt(fat))-0.4)) - sqrt(fat)
endfunction

fat0= 0.316*5000**-0.25


function [x, f, IT] = NRUni(x0, func)
    IT = 0;
    ITMAX = 100;
    tol = 1.0e-6;

    f0 = func(x0);
    
    while abs(f0) > tol & IT < ITMAX
        df0 = numderivative(func, x0);
        if df0 == 0 then
            disp("Derivada zero. Método falhou.");
            break;
        end
        
        passo = -f0 / df0;
        x1 = x0 + passo;
        f1 = func(x1);
        
        // Se a função piorar, tenta passo menor
        if abs(f1) > abs(f0) then
            passo = 0.5 * f0 / df0;
            x1 = x0 + passo;
            f1 = func(x1);
        end
        
        x0 = x1;
        f0 = f1;
        IT = IT + 1;
    end
    
    x = x0;
    f = f0;
endfunction

// Teste
[x, fval, iters] = NRUni(fat0, func);
disp("Raiz encontrada: " + string(x));
disp("Valor da função: " + string(fval));
disp("Iterações: " + string(iters));
