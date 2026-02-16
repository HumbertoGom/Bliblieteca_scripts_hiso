/*
clc;
clear;

// Dados constantes
alphaA = 136; betaA = 0.000752;
alphaB = 135; betaB = 0.000727;
f = 0.02792;
L = 2000; D = 2.067;
p1 = 1; p5 = 1;

// Função do sistema com 8 incógnitas
function F = sistema(x)
    p2 = x(1); p3 = x(2); p4 = x(3);
    QA = x(4); QB = x(5); QC = x(6); QD = x(7); QE = x(8);

    hC = (f * L * QC^2) / (D^5);
    hD = (f * L * QD^2) / (D^5);
    hE = (f * L * QE^2) / (D^5);

    F = [
        QE - QA - QC;                              // Eq. 1: conservação de vazão
        p1 - p2 - (alphaA - betaA*QA^2);           // Eq. 2: bomba A
        p1 - p3 - (alphaB - betaB*QB^2);           // Eq. 3: bomba B
        p2 - p4 - hC;                              // Eq. 4: perda tubo C
        p3 - p4 - hD;                              // Eq. 5: perda tubo D
        p4 - p5 - hE;                              // Eq. 6: perda tubo E
        p1 - 1;                                    // Eq. 7: p1 fixo
        p5 - 1                                     // Eq. 8: p5 fixo
    ];
endfunction

// Chute inicial: [p2, p3, p4, QA, QB, QC, QD, QE]
x = [0.5; 0.5; 0.5; 3; 3; 3; 3; 6];
tol = 1e-6;
max_iter = 100;

for k = 1:max_iter
    F = sistema(x);
    J = numderivative(sistema, x); // derivada numérica do sistema
    delta = -linsolve(J, F);       // melhor que usar inv(J)
    x = x + delta;
    if norm(delta) < tol then
        break;
    end
end

// Resultados
p2 = x(1); p3 = x(2); p4 = x(3);
QA = x(4); QB = x(5); QC = x(6); QD = x(7); QE = x(8);

printf("Pressões (atm):\n");
printf("p2 = %.4f\np3 = %.4f\np4 = %.4f\n\n", p2, p3, p4);

printf("Vazões (ft³/s):\n");
printf("QA = %.4f\nQB = %.4f\nQC = %.4f\nQD = %.4f\nQE = %.4f\n", QA, QB, QC, QD, QE);
*/

clc;
clear;

// Dados constantes
alphaA = 136; betaA = 0.000752;
alphaB = 135; betaB = 0.000727;
f = 0.02792;
L = 2000; D = 2.067;
p1 = 1; p5 = 1;

// Sistema com 6 equações e 6 variáveis:
// Variáveis: p2, p3, p4, QA, QB, QC

function F = sistema(x)
    p2 = x(1); p3 = x(2); p4 = x(3);
    QA = x(4); QB = x(5); QC = x(6);

    QE = QA + QC;
    hC = (f * L * QC^2) / (D^5);
    hD = (f * L * QB^2) / (D^5);  // usa QB para simplificar
    hE = (f * L * QE^2) / (D^5);

    F = [
        QE - QA - QC;                              // Eq. 1: definição QE
        p1 - p2 - (alphaA - betaA*QA^2);           // Eq. 2: bomba A
        p1 - p3 - (alphaB - betaB*QB^2);           // Eq. 3: bomba B
        p2 - p4 - hC;                              // Eq. 4: tubo C
        p3 - p4 - hD;                              // Eq. 5: tubo D
        p4 - p5 - hE                               // Eq. 6: tubo E
    ];
endfunction

function J = jacobiano(x)
    p2 = x(1); p3 = x(2); p4 = x(3);
    QA = x(4); QB = x(5); QC = x(6);

    QE = QA + QC;
    dhC_dQC = (2 * f * L * QC) / (D^5);
    dhD_dQB = (2 * f * L * QB) / (D^5);
    dhE_dQE = (2 * f * L * QE) / (D^5);

    J = zeros(6,6);
    
    // Eq1: QE - QA - QC = 0
    J(1,4) = -1; // d/dQA
    J(1,6) = -1; // d/dQC
    J(1,4) = J(1,4) + 1; // QE depende de QA
    J(1,6) = J(1,6) + 1; // QE depende de QC

    // Eq2: bomba A
    J(2,1) = -1; // d/dp2
    J(2,4) = 2*betaA*QA; // d/dQA

    // Eq3: bomba B
    J(3,2) = -1; // d/dp3
    J(3,5) = 2*betaB*QB; // d/dQB

    // Eq4: tubo C
    J(4,1) = 1; // d/dp2
    J(4,3) = -1; // d/dp4
    J(4,6) = -dhC_dQC; // d/dQC

    // Eq5: tubo D
    J(5,2) = 1; // d/dp3
    J(5,3) = -1; // d/dp4
    J(5,5) = -dhD_dQB; // d/dQB

    // Eq6: tubo E
    J(6,3) = 1; // d/dp4
    J(6,4) = -dhE_dQE; // d/dQA
    J(6,6) = -dhE_dQE; // d/dQC
endfunction

// Chute inicial: [p2, p3, p4, QA, QB, QC]
x = [0.5; 0.5; 0.5; 3; 3; 3];
tol = 1e-6;
max_iter = 100;

for k = 1:max_iter
    F = sistema(x);
    J = jacobiano(x);
    delta = -linsolve(J, F);
    x = x + delta;
    if norm(delta) < tol then
        break;
    end
end

p2 = x(1); p3 = x(2); p4 = x(3);
QA = x(4); QB = x(5); QC = x(6);
QE = QA + QC;

mprintf("Pressões (atm):\n");
mprintf("p2 = %.4f\np3 = %.4f\np4 = %.4f\n\n", p2, p3, p4);

mprintf("Vazões (ft³/s):\n");
mprintf("QA = %.4f\nQB = %.4f\nQC = %.4f\nQE = %.4f\n", QA, QB, QC, QE);
B = %.4f\nQC = %.4f\nQD = %.4f\nQE = %.4f\n", QA, QB, QC, QD, QE);
