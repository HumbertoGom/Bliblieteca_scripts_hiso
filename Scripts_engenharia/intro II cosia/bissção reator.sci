clear;clc;close



Nao= 50// mol/s
k=0.1// s^-1
Cao= 0.3// mol/L
K=0.06 // L/mol
V=5 // 


//bisseção no scilab

function f= func(X)
    f= (V*k*Cao*(1-X))/(Nao*(1+K*Cao*(1-X))^2) - X
endfunction

a =0
b =1
tol= 1e-8 //lim de toleraçancia

IT=0 //contador de iterações

ITMAX=100 //numero maximo de iterações


noconvergiu=%t //true
fa =func(a); fb=func(b)

while noconvergiu & IT<ITMAX
    c=(a+b)/2
    fc=func(c)
    noconvergiu = (abs(fc)>tol)
    if fa*fc>0 then 
        a=c;fa=fc
    else 
        b=c;fb=fc
    end
    IT=IT+1
end


disp('o C',c)
disp('f(c)',func(c))





