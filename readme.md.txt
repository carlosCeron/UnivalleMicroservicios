docker run --name mysql-curso -p 3306:3306  -e MYSQL_ROOT_PASSWORD=1234 -e MYSQL_DATABASE=cursos -d mysql:5.7.30
docker run --name estudiantes-db -p 5432:5432 -e POSTGRES_PASSWORD=1234 -d postgres
docker run --name mysql-profesores -p 3307:3306  -e MYSQL_ROOT_PASSWORD=1234 -e MYSQL_DATABASE=profesores -d mysql:5.7.30