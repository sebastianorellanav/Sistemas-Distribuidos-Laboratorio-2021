SELECT 'CREATE DATABASE terremotos'
WHERE NOT EXISTS (SELECT FROM pg_database WHERE datname = 'terremotos');
