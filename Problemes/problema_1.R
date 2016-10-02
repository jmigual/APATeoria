# Establim una seed per obtenir sempre el mateix valor
set.seed(7)

N = 1000
mu = 0
sigma = 2

X <- rnorm(N, mean = mu, sd = sigma)
P <- runif(N)

# Imposem condicio de que la suma sigui igual a 1
P <- P / sum(P)

a = 1/N
b = -2*sum(P*X)/N
c = sum(P*X*X)/N

xstar = sum(P*X)

fn = function(x) (a*x^2 +b*x + c)

# Dibuixem la corba
curve(fn, -10, 10)

# Li diem a R que busqui el mínim de la funció
xmin = optimize(fn, interval = c(-10, 10))
xmin = as.numeric(xmin["minimum"])
print(xmin)
print(xstar)

# Comprovem que siguin iguals (o molt propers)
print(abs(xmin - xstar) < 1e-5)
