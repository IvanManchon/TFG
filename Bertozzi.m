function [BE] = Bertozzi(Vpos,Vvel,alpha,beta,CR,CA,lR,lA,N)
BE = zeros(N,2);        % MATRIZ DE ALMACENAJE PARA X & Y
U = zeros(N,2);

for i = 1:N
    for j = 1:N
        if i == j       % PARA QUE NO SE COMPRUEBE AL MISMO INDIVIDUO
            continue
        else            % ECUACIÓN DE EULER
            R = Vpos(i,:) - Vpos(j,:);
            r = norm(R);
            U(i,:) = U(i,:) + (-(CR/lR)*exp(-r/lR) + (CA/lA)*exp(-r/lA))*(R/r);
        end
    end
    BE(i,:) = (alpha - beta*(norm(Vvel(i,:))^2))*Vvel(i,:) - (1/N)*U(i,:);
end
end