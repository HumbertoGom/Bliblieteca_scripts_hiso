
function f=func(x)
    f=zeros(11,1)
    L=40; V=65
    y=zeros(length(x),1)
    y(1)=0.25
    for i=2:11 //definindo y.
        y(i)=0.75*x(i) / (1+exp(-0.2*x(i)*y(i)))    
    end
    for i=2:10
        f(i+1)= L*x(i+1)+ V*y(i-1) - L*x(i)- V*y(i)
    end
    
endfunction

//x0 =x(1)
//y0 = y(1) 
//por isso que tem 11 linhas
x=ones(11,1)//não preciso definir x1 como 1.pq todos ja são 1.
x(1) = 0 


disp('trem')
disp(fsolve(x,func))
