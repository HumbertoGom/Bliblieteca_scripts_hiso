function f=reator(x)//x(1)= V, x(2) é C1
    k=0.075; n=2; q=30 ; C0=1.6; C2= 1.6 *0.8// considerando conversão como 80% C2 é 80%da entrada de c1
    f(1)= q/x(1)*(C0-x(2)) -k* x(2)
    f(2) = q/x(1)*(x(2)-C2) -k* C2
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

x0=[1; 1.2]//1 para volume e 1,2 para C1
[x,f,IT] = NossoNR(x0,reator)

disp('volume e C1',x)
disp('convergencia',f)
disp('IT:', IT)
