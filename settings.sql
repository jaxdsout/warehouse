CREATE DATABASE warehouse;
CREATE USER warehouseuser WITH PASSWORD 'gallery123';
GRANT ALL PRIVILEGES ON DATABASE warehouse TO warehouseuser;
ALTER DATABASE warehouse OWNER TO warehouseuser;
GRANT USAGE ON SCHEMA public TO warehouseuser;
GRANT CREATE ON SCHEMA public to warehouseuser;
