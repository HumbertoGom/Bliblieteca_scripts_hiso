//bisseção no scilab

function f= func(X)
    ...
endfunction
a,b= [0,1]
tol= 1e-8 //lim de toleraçancia

IT=0 //contador de iterações

ITMAX=100 //numero maximo de iterações

//bulma
noconvergiu=%t
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
