// Simulação da função seno

// Criar vetor de pontos entre 0 e 2*pi
x = linspace(0, 2*%pi, 100);  // 100 pontos entre 0 e 2π

// Calcular seno de cada ponto
y = sin(x);

// Plotar a função seno
plot(x, y)
xlabel("x (rad)")
ylabel("sin(x)")
title("Simulação da Função Seno")
xtitle("Função Seno: y = sin(x)")
