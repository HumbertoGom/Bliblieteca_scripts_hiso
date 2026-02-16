clear;clc;close
/*
function f=sistema(PQ)
    P = PQ(1:3); // dividir entrada unica em P   //P(1)=p2  P(2)=p3 , P(3)=p4
    Q = PQ(4:6); // dividir entrada unica em Q   //Q(1)=C, Q(2)=D ,Q(3)=E
    p1 =14.6569; p5 =14.6569 //converti para psi, consistencia dimensional
    Fm= 0.02792 
    z5z4 = 70 //ft
    AlfaA = 156.6 ; AlfaB= 117.1
    BetaA=0.00752 ; BetaB= 0.0027
    rho= 62.43 ; pi=3.14149              //definindo constantes
    L= zeros(1,5) ;L(3)=125 ; L(4)=125 ; L(5)=145 // comprimentos em ft 3=C , 4=D e 5=E
    D=zeros(1,5) ; D(3)=0.1065; D(4)= 0.1722 ; D(5)= 0.2017 //vetor comprimentos
    
    f(1) = Q(2)+Q(1)-Q(3)
    f(2) = AlfaA - BetaA*Q(1)^2 - p(1) + p1
    f(3) =AlfaB - BetaB*Q(2)^2-p(2) + p1
    for i=3:4
        f(i+1) = (8*Fm*rho*L(i)*Q(i-2)^2)/(pi^2 *D(i)^5) -p(i-2)+p(i-1)
    end
    f(6)=(8*Fm*rho*L(5)*Q(3)^2)/(pi^2 *D(5)^5) -p(2)+p5 - rho*z5z4* 32.2 //32,2 é g em unidades imperiais
    f=f';
endfunction

//Q=ones(1,3) ; //Q(1)=C, Q(2)=D ,Q(3)=E
//P=ones(1,3) ; //P(1)=p2  P(2)=p3 , P(3)=p4
disp("ss") 

x = ones(6,1)
u=fsolve(sistema,x)
disp(u)

*/
clear; clc; close;

function f = sistema(x)
    // Separar P e Q do vetor de entrada
    P = x(1:3); // p2, p3, p4
    Q = x(4:6); // Q1 = C, Q2 = D, Q3 = E

    // Constantes
    p1 = 14.6569; p5 = 14.6569;
    Fm = 0.02792;
    z5z4 = 70;
    AlfaA = 156.6; AlfaB = 117.1;
    BetaA = 0.00752; BetaB = 0.0027;
    rho = 62.43; pi = 3.14159;
    g = 32.2;

    L = zeros(1,5); L(3) = 125; L(4) = 125; L(5) = 145;
    D = zeros(1,5); D(3) = 0.1065; D(4) = 0.1722; D(5) = 0.2017;

    // Sistema
    f(1) = Q(2) + Q(1) - Q(3);
    f(2) = AlfaA - BetaA * Q(1)^2 - P(1) + p1;
    f(3) = AlfaB - BetaB * Q(2)^2 - P(2) + p1;
    f(4) = (8 * Fm * rho * L(3) * Q(1)^2) / (pi^2 * D(3)^5) - P(1) + P(3);
    f(5) = (8 * Fm * rho * L(4) * Q(2)^2) / (pi^2 * D(4)^5) - P(2) + P(3);
    f(6) = (8 * Fm * rho * L(5) * Q(3)^2) / (pi^2 * D(5)^5) - P(2) + p5 - rho * z5z4 * g/144;// 144 converte para ps1

    
    f= matrix(f,-1,1)
endfunction

x0 = ones(6,1); // vetor coluna real

sol = fsolve(x0, sistema);

disp("Solução (P2, P3, P4, Q1, Q2, Q3):");
disp(sol);

//Q1 deu negativo sei que esta errado
