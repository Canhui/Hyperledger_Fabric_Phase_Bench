function res = res_mmc(lambda, mu, c)
    rho = lambda/(c*mu);
    sum_x = 0;
    for i = 0:c-1
        sum_x = sum_x + ((c*rho)^i)/factorial(i);
    end
    sum_x = sum_x + ((c*rho)^c)/((1-rho)*factorial(c));
    sum_x = 1/sum_x;
    res = 1/mu+((((lambda/mu)^c)*mu)/(factorial(c-1)*(c*mu-lambda)^2))*sum_x;
end
