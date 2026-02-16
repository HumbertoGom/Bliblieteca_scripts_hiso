// exemplo 1

A = [3,2;1,-1]
y = [7;-1]
disp('inv(A)*y)',inv(A)*y)
disp('pinv(A)*y)',pinv(A)*y)
disp('linsolve(A,-y)',linsolve(A,-y))
disp('rref([A,y])',rref([A,y]))

//exemplo 2

A2 = [3,2;1,-1;4,1]
y2 = [7;-1;6]
//disp('inv(A2)*y2)',inv(A2)*y2)
disp('pinv(A2)*y2)',pinv(A2)*y2)
disp('linsolve(A2,-y2)',linsolve(A2,-y2))
disp('rref([A2,y2])',rref([A2,y2]))
