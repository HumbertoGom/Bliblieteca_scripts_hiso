function f =reator(C)
    R1= 0.8;R2=1.2; Cbeq=3 ; Ka=0.7;Kb=0.6;Kc=0.4
    Vaz= 30; V=150
    Ca= 5; Cb = 0 ;Cc=0 
    r1= (R1*C(1))/(1+Ka*C(1)+Kb*C(2)+Kc*C(3))
    r2 = (R2*(C(2)-Cbeq))/(1+Ka*C(1)+Kb*C(2)+Kc*C(3))
    f(1) =  C(1) - Ca -r1*V/Vaz
    f(2) = C(2) - Cb -((r1-r2)*V/Vaz)
    f(3) = C(3) - r2*V/Vaz
endfunction

[C,f]= fsolve([3;1;1],reator)

disp([C,f])
