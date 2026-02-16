clear;clc;close

function f=escoamento(x)
    patm=101325 ;g=9.8; fat=0.03 ; pi =3.141592
     rho=997.1; L=500; D=0.0508
    a=11* 101325; b =1.5*101325; h=30
    f(1) = a-b*x(2)**1.5 - x(1) - patm
    f(2) = 8*((fat*rho*L*x(2)**2)/(pi**2*D**5)) - rho*g*h + patm-x (1)
endfunction

function [x,f,IT]=NossoNR(x0,func)
    tol = 1e-6
    ITMAX = 100 // nº max de iterações
    f0 = func(x0)
    df0 = numderivative(func,x0)
    passo = -inv(df0)*f0
    IT = 0 //contador de iterações
    while norm(f0)>tol & IT<ITMAX
    	x1 = x0+passo
    	f1 = func(x1)
    	if norm(f1)<norm(f0) then
    		x0 = x1
    		f0 = f1
    		df0 = numderivative(func,x0)
    		passo = -inv(df0)*f0
    	else
    		passo = passo/2
    	end
    IT = IT+1
end
if norm(f0)<tol then
    x=x0; f=f0
else
    x = []; f = []
end
endfunction

x0 = [0.5;10]//chutei p2 como 1,o que o problema sugere, e Q como 10, 

[x,f,IT]=NossoNR(x0,escoamento)

disp("x = "), disp(x)
disp("f = "), disp(f)
disp("Iterações = "), disp(IT)


//p2 é cerca de 10 MPa e aproximadamente 0,00580 m3/s
