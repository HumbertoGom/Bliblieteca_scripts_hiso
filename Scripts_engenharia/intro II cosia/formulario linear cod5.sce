clc;clear;close

//na coluna 3 vou especificar o procoesso
//vou usar 1 para mistura, 2 para seperação , 3 para reação

processo=[
1,2,1;//Mix: 1 adicionado a 2
9,2,1;//Mix: 9 adicionado a 2
6,2,1;//Mix: 6 adicionado 1
2,3,3;//R1: reator 1
3,4,2;//S1 3 separado em 4
3,7,2;//S1 3 sepraddo em 7
7,8,3;//R2:reator 2
8,9,2;//S2 8 separado em 9
8,10,2//S2 8 separado em 2
]

sensores = []

for i= 1:size(processo,1)
    entrada = processo(i,1)
    saida = processo(i,2)
    operacao = processo(i,3)
    if operacao == 3 then //checa se ha reação
        sensores = [sensores,entrada]
        sensores = [sensores,saida]
    end
end


sensores = unique(sensores)
disp(sensores)

//o codigo retorna as posições 2,3,7 e 8.
