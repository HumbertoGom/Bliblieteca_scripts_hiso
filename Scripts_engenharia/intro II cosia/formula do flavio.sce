function f=norma(x)
    n=length(x)
    f=0
    for i=1:n
        f=f+x(i)^2
    end
endfunction

function f=prodint(x,y)
    nx=length(x)
    ny=length(y)
    f=0
    if nx ~= ny then
        error('differentes lengths')
    end
    for i=1:nx
        f=f+ x(i)*y(i)
    end
endfunction

function f=flavio2(u1,u2)
    g1=u1/norma(u1)
    v2= u2 - prodint(u2,g1)*g1
    g2= v2/norma(v2)
    f(1,:)= g1
    f(2,:) = g2
endfunction

u1= [1,0,2]
u2 =[0,1,1]

y=flavio2(u1,u2)
disp(y)

//conclusão, a formula paraguaio retorna base ortogonal
//a formula do flavio retorna base ortonormal.
//eu sou ruim em multiplicação,e devia ter reprovado o quarto ano.

