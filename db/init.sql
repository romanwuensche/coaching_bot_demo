/* Create database */
CREATE DATABASE bot ENCODING 'UTF8';

/* Switch to database */
\connect bot

/* Create tables */
CREATE TABLE IF NOT EXISTS public.users
(
    id           int          NOT NULL,
    username     varchar(50)  NOT NULL,
    created      timestamp(0) NOT NULL,
    CONSTRAINT user_pkey PRIMARY KEY (id)
);