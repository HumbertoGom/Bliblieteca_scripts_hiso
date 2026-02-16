//Na = 10 
//mistura: Na2 = Na1 + Na6
//purga: Na5 = delta * Na4
//purga:Na6 = Na4(1-delta)
//reação:Na3 = Na2(1-Xa)
//separador:Na4 = Na3 * RECa4 
//Na7= Na3 *(1-RECa4)

//equações
//0= Na1 +Na6 - Na2
//0=Na2(1-Xa) - Na3
//0=delta*Na4 - Na5
//0=Na4(1-delta) * Na6
//0= Na3 *RECa4 - Na4
//0 = Na3(1-RECa4) - Na7
//100 = Na1

//7 variaveis e 7 equações.
// 1 2 3 4 5 6 7
Xa= 0.75
RECa4 = 0.98
delta = 0.05

S=[1,-1,0,0,0,1,0;
0,(1-Xa),-1,0,0,0,0;
0,0,0,delta,-1,0,0;
0,0,0,(1-delta),0,-1,0;
0,0,RECa4,-1,0,0,0;
0,0,(1-RECa4),0,0,0,-1;
1,0,0,0,0,0,0]

y=[0;0;0;0;0;0;100]

disp(S,y)
disp('resolução por rref()',rref([S,y]))

disp('por inversa',inv(S)*y)
disp('Resolução por linsolve', linsolve(S,-y))
