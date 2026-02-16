// Função para calcular fatorial
function f = fatorial(n)
    f = 1;
    for i = 2:n
        f = f * i;
    end
endfunction

// Função para calcular seno via série de Taylor
function y = seno_aproximado(x)
    n_termos = 10; // Quantidade de termos da série de Taylor
    y = 0;

    for n = 0:(n_termos - 1)
        termo = ((-1)^n) * (x^(2*n + 1)) / fatorial(2*n + 1);
        y = y + termo;
    end
endfunction

// Criar vetor de pontos entre 0 e 2π
x = linspace(0, 2*%pi, 100);

// Calcular seno para cada ponto (usando nossa função)
y = zeros(x);
for i = 1:length(x)
    y(i) = seno_aproximado(x(i));
end

// Plotar o resultado
plot(x, y)
xlabel("x (rad)")
ylabel("seno aproximado")
title("Aproximação da Função Seno com Série de Taylor")
xtitle("y ≈ x - x^3/3! + x^5/5! - ...")
