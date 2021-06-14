clear; clc;

% CONDICIONES INICIALES
N = 25;
Vpos = 100*rand(N,2)-1;         % PARA QUE APAREZCA ENTRE -1 Y 1 TANTO 
Vvel = rand(N,2)-0.5;         % LA VELOCIDAD COMO LA POSICIÓN 

% alpha = 0.7;
% beta = 0.005;
% CR = 5000;
% lR = 2;
% CA = 2000;
% lA = 100;

%alpha1 = 0.07;
%beta1 = 0.05;
%CR1 = 50;
%lR1 = 2;
%CA1 = 20;
%lA1 = 100;

alpha1 = 0.07;
beta1 = 0.005;
CR1 = 5000;
lR1 = 1;
CA1 = 2000;
lA1 = 20;

mu = 1;
lambda = 0.01;

CR = CR1*mu*mu/(lambda*lambda);
lR = lR1*mu;
CA = CA1*mu*mu/(lambda*lambda);
lA = lA1*mu;
beta = beta1*lambda/(mu*mu);
alpha = alpha1/lambda;


% VECTOR DE PROCESO
tiempo = 100;
t1 = 0;
t2 = 0.1;
h = 0.1;

% PLOTEAMOS EL INICIO
plot(Vpos(:,1),Vpos(:,2),'ro')    
%title('INICIO');
%xlabel({'Robots: ' + string(N), ...
%        ' alpha: ' + string(alpha1) + '  ||  beta: ' + string(beta1),...
%        'CR: ' + string(CR1) + '  ||  lR: ' + string(lR1),...
%        'CA: ' + string(CA1) + '  ||  lA: ' + string(lA1)})
hold on
quiver(Vpos(:,1),Vpos(:,2),Vvel(:,1),Vvel(:,2))
hold off
saveas(gcf,'INICIO_COMPORTAMIENTO_BERTOZZI_LIMITE.png')
pause(0.5)

% PLOTEAMOS LAS VARIACIONES
%sol = ode45(@(t,y)Bertozziode45(y,alpha,beta,CR,CA,lR,lA,N), [0 tiempo], [Vpos(:);Vvel(:)])

% PLOTEAMOS LAS VARIACIONES
for i = 0:(tiempo) %Tiene que ser entero
    sol = ode45(@(t,y)Bertozziode45(y,alpha,beta,CR,CA,lR,lA,N), [t1 t2], [Vpos(:) Vvel(:)]);
    for j = 1:sol.stats.nsteps
        c = sol.y(:,j);
        VposX = c(1:N);
        VposY = c(N + 1 : 2*N);
        VvelX = c(2*N + 1 : 3*N);
        VvelY = c(3*N + 1 : end);
        
%         plot(VposX(:),VposY(:),'ro')         % PLOTEAMOS EL CAMBIO REALIZADO
%         title('Tiempo: ' + string(i*h));
%         xlabel({'Robots: ' + string(N), ...
%             ' alpha: ' + string(alpha1) + '  ||  beta: ' + string(beta1),...
%             'CR: ' + string(CR1) + '  ||  lR: ' + string(lR1),...
%             'CA: ' + string(CA1) + '  ||  lA: ' + string(lA1)})
%         hold on
%         quiver(VposX(:),VposY(:),VvelX(:),VvelY(:))
%         hold off
%         pause(0.001)
    end
    Vpos = [VposX,  VposY];
    Vvel = [VvelX,  VvelY];
    t1 = t2;
    t2 = t2 + h;
end
%  PLOTEAMOS EL FINAL
plot(VposX(:),VposY(:),'ro')             
%title('FINAL');
%xlabel({'Robots: ' + string(N), ...
%        ' alpha: ' + string(alpha1) + '  ||  beta: ' + string(beta1),...
%        'CR: ' + string(CR1) + '  ||  lR: ' + string(lR1),...
%        'CA: ' + string(CA1) + '  ||  lA: ' + string(lA1)})
hold on
quiver(VposX(:),VposY(:),VvelX(:),VvelY(:))
hold off
saveas(gcf,'FINAL_COMPORTAMIENTO_BERTOZZI_LIMITE.png')