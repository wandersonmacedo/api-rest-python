# api-rest-python

## python + docker + postgres

 - Padrão dominante: service repository
 - Paradigma: OOP
 - As variaves de ambiente estão no arquivo .env
 - Será necessário adicionar uma credencial Git com permissionamento de leitura de repos e users no .env


## Instruções 

1. Git pull na url https://github.com/wandersonmacedo/api-rest-python.git

2. Rodar docker-compose up --build
     - rodar: "docker exec -it app-rest-api bash"
     - rodar: "alembic upgrade head"

3. Acessar o endereço http://127.0.0.1/docs para ver os endpoints

4. O endpoint pode ser acessado direto pelo swagger ou via postman

5. Testes unitarios estão em app/test e para rodar precisa acessar o container e rodar python -m unittest app/test/* 


