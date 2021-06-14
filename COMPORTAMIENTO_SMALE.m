clear; clc;

%% CONDICIONES INICIALES
Robots = 25;
Vpos = 2*rand(Robots,2)-1;         % PARA QUE APAREZCA ENTRE -1 Y 1 TANTO 
Vvel = 2*rand(Robots,2)-1;         % LA VELOCIDAD COMO LA POSICIÓN 
gamma = 0.0001;


%% VECTOR DE PROCESO
tiempo = 10;                       % VECTOR PARA DAR MAS INFORMACIÓN EN 
pasos = 20;                        % LA GRAFICA Y AJUSTAR LAS ITERACCIONES 
T = linspace(0,tiempo,pasos+1);    % QUE VAN A REALIZAR


%% PLOTEAMOS EL INICIO
figure('Name','Cucker-Smale')
plot(Vpos(:,1),Vpos(:,2),'ro')    
%title('INICIO');
%xlabel({'Robots: ' + string(Robots) + '  ||  gamma: ' + string(gamma);
%        'Dirección: ' + string(mean(Vvel(:,1))) + ' + (' +  ...
%            string(mean(Vvel(:,2))) + 'j)'})
hold on
quiver(Vpos(:,1),Vpos(:,2),Vvel(:,1),Vvel(:,2))
hold off
saveas(gcf,'INICIO_COMPORTAMIENTO_SMALE_CERO.png')
pause(0.5)

%% PLOTEAMOS LAS VARIACIONES
for i = 1:length(T)
    CS = smale(Vpos, Vvel, gamma, Robots); % CUCKER SMALE
    for j = 1:Robots
        Vpos(j,1) = Vpos(j,1) + Vvel(j,1);   % APLICAMOS CAMBIO DE POSICIÓN 
        Vpos(j,2) = Vpos(j,2) + Vvel(j,2);   % SEGUN LA NUEVA VELOCIDAD 
    
        Vvel(j,1) = Vvel(j,1) + CS(j,1);     % APLICAMOS LA VARIACIÓN 
        Vvel(j,2) = Vvel(j,2) + CS(j,2);     % A TOLAS LAS VELOCIDADES
    end
    plot(Vpos(:,1),Vpos(:,2),'ro')         % PLOTEAMOS EL CAMBIO REALIZADO
    title('Tiempo: ' + string(T(i)));
    xlabel({'Robots: ' + string(Robots) + '  ||  gamma: ' + string(gamma);
        'Dirección: ' + string(mean(Vvel(:,1))) + ' + (' +  ...
            string(mean(Vvel(:,2))) + 'j)'})
    hold on
    quiver(Vpos(:,1),Vpos(:,2),Vvel(:,1),Vvel(:,2))
    hold off
    pause(0.5)
end

%%  PLOTEAMOS EL FINAL
plot(Vpos(:,1),Vpos(:,2),'ro')             
%title('FINAL');
%xlabel({'Robots: ' + string(Robots) + '  ||  gamma: ' + string(gamma);
%        'Dirección: ' + string(mean(Vvel(:,1))) + ' + (' +  ...
%            string(mean(Vvel(:,2))) + 'j)'})
hold on
quiver(Vpos(:,1),Vpos(:,2),Vvel(:,1),Vvel(:,2))
hold off
saveas(gcf,'FINAL_COMPORTAMIENTO_SMALE_CERO.png')