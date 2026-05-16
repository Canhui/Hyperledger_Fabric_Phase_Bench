% clean the environment
clear;
clc;

% setting
lambda = 670;
mu = 470;
c = 4;
rho = lambda/(c*mu);

% main
% this is wrong: exact_mdc(lambda, mu, c) % exact mdc
appro_mdc(lambda, mu, c) % approximation mdc
%res_mmc(lambda, mu, c) % mmc
%mmcfindewq(lambda, mu, c)+1/mu
%mmcfindewq(lambda, mu, c)
