clear;clc;close 

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

u1= [1,0,2]
u2 =[0,1,1]


function f=paraguaioR2(u1,u2)
    f= zeros(2,length(u1))// matriz 2x3 
    f(1,:)= u1
    f(2,:)= u2 - ((prodint(u2,u1)/prodint(u1,u1))*u1)
endfunction

disp('')
y= paraguaioR2(u1,u2)
disp(y)



function f=paraguaioR3(u1,u2,u3)
    f= zeros(3,length(u1))// matriz 2x3 
    f(1,:)= u1
    f(2,:)= u2 - ((prodint(u2,u1)/prodint(u1,u1))*u1)
    f(3,:)= u3 -((prodint(u3,u1)/prodint(u1,u1))*u1)- ((prodint(u3,u2)/prodint(u2,u2))*u2)
endfunction

//base r3
x1=[1,1,2]
x2=[1,2,0]
x3=[0,-1,1]

disp('problema r3')
y2= paraguaioR3(x1,x2,x3)
disp(y2)

disp(paraguaioR3([1,0,0],[3,7,-2],[0,4,1]))

