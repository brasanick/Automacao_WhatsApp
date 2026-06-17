-- Execute este SQL no Supabase → SQL Editor
-- Cria a tabela de contatos e insere 3 exemplos

create table if not exists contacts (
  id    bigint generated always as identity primary key,
  name  text   not null,
  phone text   not null        -- formato: 5511999999999
);

-- Insira seus contatos reais aqui
insert into contacts (name, phone) values
  ('Maria',  '5511900000001'),
  ('João',   '5511900000002'),
  ('Carlos', '5511900000003');
