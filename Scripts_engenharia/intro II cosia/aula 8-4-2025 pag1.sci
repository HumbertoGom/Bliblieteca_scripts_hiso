Xa = 0.8
RECa4 = 0.75

A=zeros(5,5)
y=zeros(5,1)
//uwu
disp(A) 

A(1,[1,2,4]) =[1,-1,1]
A(2,[2,3]) =[1-Xa, -1]
A(3,[3,4]) =[RECa4,-1]
A(4,[3,5]) =[1-RECa4,-1]
A(5,1)=1;y(5)= 100



disp(A)
disp(y) 

awnser= inv(A)*y
disp(awnser)
