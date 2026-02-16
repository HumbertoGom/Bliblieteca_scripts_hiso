clc;clear;close

//Linha = [entrada da unidade referente, saída da unidade referente, se ocorre reação com A nessa unidade]

processo = [ 
1, 2, 0; //Mix
2, 3, 1; //R1
3, 4, 0; //S1
3, 7, 0; //S1
7, 8, 1; //R2
8, 9, 0; //S2
8, 10, 0 //S2
]

sensores = []

for i = 1:size(processo,1)
    entrada = processo(i,1)
    saída = processo(i,2)
    reação_A = processo(i,3)
    
    if reação_A == 1 then
        sensores = [sensores, entrada] 
        sensores = [sensores, saída]
    end
end

sensores = unique(sensores)
sensores = gsort(sensores,"g","i")

disp("Os sensores devem ser inseridos nas posições: ", sensores)
