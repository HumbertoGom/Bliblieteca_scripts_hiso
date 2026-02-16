// Parâmetros conhecidos
Nao = 50;     // mol/s
k = 0.1;      // s^-1
Cao = 0.3;    // mol/L
K = 0.06;     // L/mol
V = 5;        // L

// Definir a função f(X)
function y = f(X)
    numerador = V * k * Cao * (1 - X);
    denominador = (1 + K * Cao * (1 - X))^2;
    y = Nao * X - numerador / denominador;
endfunction

// Implementar método da bisseção
function Xroot = bissecao(f, a, b, tol, max_iter)
    if f(a) * f(b) > 0 then
        error("Não há mudança de sinal no intervalo dado.");
    end

    for i = 1:max_iter
        c = (a + b) / 2;
        fc = f(c);

        if abs(fc) < tol then
            Xroot = c;
            return;
        end

        if f(a) * fc < 0 then
            b = c;
        else
            a = c;
        end
    end

    Xroot = (a + b) / 2; // Aproximação final
endfunction

// Parâmetros do método da bisseção 
a = 0.0;           // limite inferior
b = 0.99;          // limite superior (X < 1)
tol = 1e-6;        // tolerância
max_iter = 100;    // número máximo de iterações

// Chamada da função
X_sol = bissecao(f, a, b, tol, max_iter);

// Exibir resultado
disp("Conversão X encontrada: " + string(X_sol));
