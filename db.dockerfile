FROM mysql/mysql-server

ENV MYSQL_ROOT_PASSWORD=root

COPY ./grant_access.sql ./docker-entrypoint-initdb.d

EXPOSE 3306