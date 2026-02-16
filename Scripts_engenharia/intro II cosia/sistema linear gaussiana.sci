
M=[2,5,-5;
  -1,3,1;
  0,2,-4]

pivo = M(1,1)
M(1,:) = M(1,:)/pivo

M(2,:) = M(2,:) - M(1,:)* M(2,1) 

M(3,:) = M(3,:) - M(1,:) *M(3,1) 

//essas operações ajeitam a primeira coluna para 0.


pivo = M(2,2)
M(2,:) = M(2,:)/pivo 
M(1,:) = M(1,:) - M(2,:)* M(2,2) 
M(3,:) = M(3,:) - M(2,:) *M(3,2) 


disp(M)

