clear; clc;

%% CONDICIONES INICIALES
N = 25;
Vpos = 200*rand(N,2)-1;         % PARA QUE APAREZCA ENTRE -1 Y 1 TANTO 
Vvel = rand(N,2)-0.5;         % LA VELOCIDAD COMO LA POSICIÓN 

% alpha = 0.7;
% beta = 0.005;
% CR = 5000;
% lR = 2;
% CA = 2000;
% lA = 100;

alpha = 0.07;
beta = 0.05;
CR = 50;
lR = 2;
CA = 20;
lA = 100;

radio = 10;
vision = 130;

mu = 1;
lambda = 0.01;

CR = CR*mu*mu/(lambda*lambda);
lR = lR*mu;
CA = CA*mu*mu/(lambda*lambda);
lA = lA*mu;
beta = beta*lambda/(mu*mu);
alpha = alpha/lambda;


%% VECTOR DE PROCESO
tiempo = 200;
t1 = 0;
t2 = 0.1;
h = 0.1;

%% PLOTEAMOS EL INICIO
plot(Vpos(:,1),Vpos(:,2),'bo')    
%title('INICIO');
%xlabel({'Robots: ' + string(N), ...
%        ' alpha: ' + string(alpha/100) + '  ||  beta: ' + string(beta*100),...
%        'CR: ' + string(CR/1000) + '  ||  lR: ' + string(lR),...
%        'CA: ' + string(CA/1000) + '  ||  lA: ' + string(lA)})
hold on
quiver(Vpos(:,1),Vpos(:,2),Vvel(:,1),Vvel(:,2))
hold off
saveas(gcf,'INICIO_COMPORTAMIENTO_BERTOZZI_COLISIONES_2.png')
pause(0.5)

%% PLOTEAMOS LAS VARIACIONES
% sol = ode45(@(t,y)Bertozziode45(y,alpha,beta,CR,CA,lR,lA,N), [0 tiempo], [Vpos(:);Vvel(:)])

%% PLOTEAMOS LAS VARIACIONES
for i = 0:(tiempo) %Tiene que ser entero
    sol = ode45(@(t,y)MejoraBertozziode45(y,alpha,beta,CR,CA,lR,lA,radio,vision,N), [t1 t2], [Vpos(:) Vvel(:)]);
    for j = 1:sol.stats.nsteps
        c = sol.y(:,j);
        VposX = c(1:N);
        VposY = c(N + 1 : 2*N);
        VvelX = c(2*N + 1 : 3*N);
        VvelY = c(3*N + 1 : end);
        %plot(VposX(:),VposY(:),'bo','MarkerSize',radio)         % PLOTEAMOS EL CAMBIO REALIZADO
        %title('Tiempo: ' + string(i*h));
        %xlabel({'Robots: ' + string(N), ...
        %    ' alpha: ' + string(alpha) + '  ||  beta: ' + string(beta),...
        %    'CR: ' + string(CR) + '  ||  lR: ' + string(lR),...
        %    'CA: ' + string(CA) + '  ||  lA: ' + string(lA)})
        %hold on
        %plot(VposX(:),VposY(:),'ro','MarkerSize',vision)
        %quiver(VposX(:),VposY(:),VvelX(:),VvelY(:))
        %hold off
        %pause(0.001)
    end
    Vpos = [VposX,  VposY];
    Vvel = [VvelX,  VvelY];
    
    t1 = t2;
    t2 = t2 + h;
end
%%  PLOTEAMOS EL FINAL
plot(VposX(:),VposY(:),'bo','MarkerSize',radio)             
%title('FINAL');
%xlabel({'Robots: ' + string(N), ...
%        ' alpha: ' + string(alpha/100) + '  ||  beta: ' + string(beta*100),...
%        'CR: ' + string(CR/1000) + '  ||  lR: ' + string(lR),...
%        'CA: ' + string(CA/1000) + '  ||  lA: ' + string(lA)})
hold on
plot(VposX(:),VposY(:),'ro','MarkerSize',vision)
quiver(VposX(:),VposY(:),VvelX(:),VvelY(:))
hold off
axis([-100 100 -100 100])
saveas(gcf,'FINAL_COMPORTAMIENTO_BERTOZZI_COLISIONES_2.png')