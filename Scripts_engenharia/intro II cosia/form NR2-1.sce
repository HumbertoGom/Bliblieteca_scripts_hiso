function f=func(u)
    f=zeros(12,1)
    f(1) = u(1) -0.5
    for i=1:10
        f(i+1)= u(i+2)  +  4*i*u(i+1)  +     u(i)^2 -(i-1)*(10-i)
    end
    f(12)=u(12)+2
endfunction
u= 0.5*ones(12,1)
disp(func(u))
disp('trem')
disp(fsolve(u,func))
