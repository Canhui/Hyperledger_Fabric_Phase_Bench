function res = appro_mdc(lambda, mu, c)
    rho = lambda/(c*mu);
    appendix = 1+(1-rho)*(c-1)*(sqrt(4+5*c)-2)/(16*rho*c);
    res = appendix*res_mmc(lambda, mu, c)/2; 
end
