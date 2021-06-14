function [CS] = smale(Vpos,Vvel,gamma,N)
CS = zeros(N,2);        % MATRIZ DE ALMACENAJE PARA X & Y
for i = 1:N
    for j = 1:N
        if i == j       % PARA QUE NO SE COMPRUEBE AL MISMO INDIVIDUO
            continue
        else            % ECUACIÓN DE EULER
        CS(i,1) = CS(i,1) + ((Vvel(j,1) - Vvel(i,1))/(1 + ...
                            ((Vpos(j,1) - Vpos(i,1))^2) + ...
                             (Vpos(j,2) - Vpos(i,2))^2)^gamma);
                            
        CS(i,2) = CS(i,2) + ((Vvel(j,2) - Vvel(i,2))/(1 + ...
                            ((Vpos(j,1) - Vpos(i,1))^2) + ...
                             (Vpos(j,2) - Vpos(i,2))^2)^gamma);
        end
    end
end
CS = CS/N;
end

