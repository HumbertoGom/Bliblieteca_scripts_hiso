clear;clc;close


Nao= 50// mol/s
k=0.1// s^-1
Cao= 0.3// mol/L
K=0.06 // L/mol
X=0.5 


//bisseção no scilab

function f= func(V)
    f= (k*Cao*(1-X))/(X*Nao((1+K*Cao*(1-X))^2))-1/V
endfunction

a =0.1
b =10000
tol= 1e-8 //lim de toleraçancia

IT=0 //contador de iterações

ITMAX=1000 //numero maximo de iterações


noconvergiu=%t //true
fa = func(a)
fb = func(b)

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
