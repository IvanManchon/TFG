function [BE] = Bertozziode45(y,alpha,beta,CR,CA,lR,lA,N)
% Variables POS y VEl
VposX = y(1:N);
VposY = y(N + 1 : 2*N);
VvelX = y(2*N + 1 : 3*N);
VvelY = y(3*N + 1 : end);

Vpos = [VposX,  VposY];
Vvel = [VvelX,  VvelY];

BE = zeros(size(Vvel));        % MATRIZ DE ALMACENAJE PARA X & Y
U = zeros(size(Vvel));

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
BE = [Vvel(:); BE(:)];
end