export DB_PORT=5432
export PG_USER=postgres

task_db_shell(){
    docker-compose run db psql -h db -p$DB_PORT -U $PG_USER 
}

task_db_create(){
    docker-compose run db psql -h db -p$DB_PORT -U $PG_USER -c "CREATE DATABASE $1;"
}