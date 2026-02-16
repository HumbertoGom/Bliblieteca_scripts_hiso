clear; clc; close

function f = escoamento(x)
    // Constantes
    patm = 101325; // em Pa
    g = 9.8;
    fat = 0.03;
    pi = %pi;
    rho = 997.1;
    L = 500;
    D = 0.0508; // metros
    a = 11 * 101325;
    b = 1.5 * 101325;
    h = 30;

    f(1) = a - b * x(2)^(1.5) - (x(1) - patm);
    f(2) = x(1) - patm + rho * g * h - (8 * fat * rho * L * x(2)^2) / (pi^2 * D^5);
endfunction

function [x, f, IT] = NossoNR(x0, func)
    tol = 1e-6;
    ITMAX = 100;
    f0 = func(x0);
    df0 = numderivative(func, x0);
    passo = -inv(df0) * f0;
    IT = 0;

    while norm(f0) > tol & IT < ITMAX
        x1 = x0 + passo;
        f1 = func(x1);

        if norm(f1) < norm(f0) then
            x0 = x1;
            f0 = f1;
            df0 = numderivative(func, x0);
            passo = -inv(df0) * f0;
        else
            passo = passo / 2;
        end
        IT = IT + 1;
    end

    if norm(f0) < tol then
        x = x0;
        f = f0;
    else
        x = [];
        f = [];
    end
endfunction

// Chute inicial: p2 = patm, Q = 0.01 m^3/s
x0 = [101325; 0.01];

[x, f, IT] = NossoNR(x0, escoamento);

disp("Resultado final:")
disp("p2 = " + string(x(1)) + " Pa");
disp("Q  = " + string(x(2)) + " m^3/s");
disp("Iterações = " + string(IT));
