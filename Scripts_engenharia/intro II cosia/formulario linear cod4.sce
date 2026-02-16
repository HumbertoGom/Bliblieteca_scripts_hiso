clear;clc

//equações
//N1+N6+N9 - N2 =0
//(Nb2 + 2*(Na2 * Xa)) -Nb3=0
//Na3 - Na2(1-Xa) =0
//N2c -Na3c = 0 
//N3c - Na7c = 0
//N3b * Recb7 - N7b = 0
//N3a * Reca7 - N7a = 0
//N3a* (1-Reca7) - N4a =0
//N3b * (1-Recb7) - N4b =0
//N4c=N5c=N6c = 0
//N4 - N5 - N6 =0
//N7b - N8b = 0
//N7a * (1-Xb) - N8a = 0
//N7c + N7a * Xb - N8c =0.
//N8a * RECa9  - N9a = 0
//N8b * RECb9 - N9b = 0
//N8c * RECc9 - N9b= 0
//N8a(1-RECa9) -N10a = 0
//N8b(1-RECb9) -N10b = 0
//N8c(1-RECc9) -N10c = 0


Reca9=0.94
Recb9=0.93
Recc9=0.03

Xb=0.42

Reca7=0.92
Recb7=0.06
Recc7=1

Xa= 0.75


//n5-0.7n6=0
//Nc10 = 1200
S=zeros(22,30)
y=zeros(22,1)

y(22,1) = 1200

//linha 1

S(1,1) = 1
S(1,6) = 1
S(1,9) = 1

S(1,11) = 1
S(1,16) = 1
S(1,19) = 1

S(1,21) = 1
S(1,26) = 1
S(1,29) = 1

S(1,2) = -1

//linha 2

S(2,12) = 1
S(2,2) = 2*Xa
S(2,13) = -1

//linha 3

S(3,2) = -1*(1-Xa)
S(3,3) = 1

//linha 4 

S(4,22) = 1
S(4,23) = -1

//linha 5

S(5,23) = 1
S(5,27) = -1

//linha 6

S(6,13) = Recb7
S(6,17) = -1

//linha 7

S(7,3) = Reca7
S(7,7) = -1

//linha 8

S(8,3) = (1-Reca7)
S(8,4) = -1

//linha 9

S(9,13) = (1-Recb7)
S(9,14) = -1

//linha 10
//nao sei se isso ajuda

S(10,24) = 0
S(10,25) = 0

//linha 11

S(11,4) = 1
S(11,5) = 1
S(11,6) = 1

S(11,14) = -1
S(11,15) = -1
S(11,16) = -1

S(11,24) = -1
S(11,25) = -1
S(11,26) = -1

// linha 12

S(12,17) =1
S(12, 18) = -1

//linha 13

S(13,7) = (1-Xb) 
S(13,8) = -1

//linha 14

S(14,7) = Xb
S(14,27) = 1
S(14,28) = -1

//linha 15

S(15,8) = Reca9
S(15,9) = -1

//linha 16

S(16,18) = Recb9
S(16,19) = -1

//linha 17

S(17,28) = Recc9 
S(17,19) = -1

//linha 18

S(18,8) = (1-Reca9)
S(18,10) = -1

//linha 19

S(19,18) = (1-Recb9)
S(19,29) = -1

//linha 20

S(20,28) = (1-Recc9)
S(20,30) = -1



disp(rref([S,y]))

//o código fica muito grande
