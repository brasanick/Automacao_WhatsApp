# 📲 WhatsApp Bot — Supabase + Z-API + Python

Automações no WhatsApp têm alta escalabilidade e podem ser aplicadas em diversos contextos: 
lojas, empresas, atendimento ao cliente e bots integrados com IA.

Este projeto lê contatos cadastrados no **Supabase** e envia, via **Z-API**, a mensagem personalizada:

> _"Olá, \<nome_contato\> tudo bem com você?"_

---

## 🗂️ Estrutura

```
.
├── main.py               # Script principal
├── requirements.txt      # Dependências
├── supabase_setup.sql    # SQL para criar a tabela no Supabase
├── .env.example          # Modelo das variáveis de ambiente
└── .gitignore
```

---

## ⚙️ Pré-requisitos

| Serviço  | Plano | Link                 |
|----------|-------|----------------------|
| Supabase | Free  | https://supabase.com |
| Z-API    | Free  | https://z-api.io     |
| Python   | 3.11+ | https://python.org   |

---

## 🚀 Como rodar

### 1. Clone o repositório

```bash
git clone https://github.com/<seu-usuario>/<seu-repositorio>.git
cd <seu-repositorio>
```

### 2. Instale as dependências

```bash
pip install -r requirements.txt
```

### 3. Configure as variáveis de ambiente

Copie `.env.example` para `.env` e preencha com suas credenciais:

| Variável             | Onde encontrar                                       |
|----------------------|------------------------------------------------------|
| `SUPABASE_URL`       | Supabase → Project Settings → API → Project URL      |
| `SUPABASE_KEY`       | Supabase → Project Settings → API → anon public key  |
| `ZAPI_INSTANCE_ID`   | Z-API → sua instância → ID                           |
| `ZAPI_TOKEN`         | Z-API → sua instância → Token                        |
| `ZAPI_CLIENT_TOKEN`  | Z-API → Conta → Security → Client-Token              |

### 4. Crie a tabela no Supabase

Acesse **Supabase → SQL Editor**, cole e execute o conteúdo de `supabase_setup.sql`.
Substitua os números de exemplo pelos números reais (com código do país).

### 5. Conecte o WhatsApp na Z-API

Acesse sua instância na Z-API e escaneie o QR Code com o WhatsApp.

### 6. Execute

```bash
python main.py
```

Saída esperada:

```
🔍 Buscando contatos no Supabase...
✅ 3 contato(s) encontrado(s).

📤 Enviando mensagem para Maria (5511900000001)...
   ✅ Enviado! Resposta Z-API: {'zaapId': '...', 'messageId': '...'}

📤 Enviando mensagem para João (5511900000002)...
   ✅ Enviado! Resposta Z-API: {'zaapId': '...', 'messageId': '...'}

📤 Enviando mensagem para Carlos (5511900000003)...
   ✅ Enviado! Resposta Z-API: {'zaapId': '...', 'messageId': '...'}
```

---

## 📐 Formato do número de telefone

O campo `phone` deve conter **somente dígitos**, no formato `[código do país][DDD][número]`.

Exemplo brasileiro: `5511999998888`

---

## 🔒 Segurança

- **Nunca** comite o arquivo `.env` — ele está no `.gitignore`.
- Use a chave `anon` do Supabase (não a `service_role`) para menor privilégio.
