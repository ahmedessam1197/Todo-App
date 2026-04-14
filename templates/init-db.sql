IF DB_ID('todo-db') IS NULL
BEGIN
    CREATE DATABASE todo-db;
END
GO

USE todo-db;
GO

IF NOT EXISTS (SELECT * FROM sysobjects WHERE name='todo-db' AND xtype='U')
BEGIN
    CREATE TABLE todo-db (
        id INT IDENTITY(1,1) PRIMARY KEY,
        title NVARCHAR(255) NOT NULL,
        description NVARCHAR(MAX),
        is_complete BIT DEFAULT 0
    );
END