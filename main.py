import os
import requests
from supabase import create_client, Client
from dotenv import load_dotenv

load_dotenv()

# ── Supabase ──────────────────────────────────────────────────────────────────
SUPABASE_URL: str = os.environ["SUPABASE_URL"]
SUPABASE_KEY: str = os.environ["SUPABASE_KEY"]

# ── Z-API ─────────────────────────────────────────────────────────────────────
ZAPI_INSTANCE_ID: str = os.environ["ZAPI_INSTANCE_ID"]
ZAPI_TOKEN:       str = os.environ["ZAPI_TOKEN"]
ZAPI_CLIENT_TOKEN: str = os.environ["ZAPI_CLIENT_TOKEN"]   # header Client-Token

ZAPI_URL = (
    f"https://api.z-api.io/instances/{ZAPI_INSTANCE_ID}"
    f"/token/{ZAPI_TOKEN}/send-text"
)

#versão alterada do fetch_contacts para mostrar o debug da resposta bruta, data e count

def fetch_contacts(supabase: Client, limit: int = 3) -> list[dict]:
    response = (
        supabase.table("contacts")
        .select("*")
        .limit(limit)
        .execute()
    )
    print("DEBUG — resposta bruta:", response)
    print("DEBUG — data:", response.data)
    print("DEBUG — count:", response.count)
    return response.data

# def fetch_contacts(supabase: Client, limit: int = 3) -> list[dict]:
#    """Busca até `limit` contatos na tabela 'contacts' do Supabase."""
#    response = (
#        supabase.table("contacts")
#        .select("name, phone")
#        .limit(limit)
#        .execute()
#    )
#    return response.data


def send_whatsapp(phone: str, name: str) -> dict:
    """Envia mensagem via Z-API para um número."""
    # Z-API exige o número no formato: código do país + DDD + número (somente dígitos)
    # Exemplo: 5511999999999
    clean_phone = "".join(filter(str.isdigit, phone))

    message = f"Olá, {name} tudo bem com você?"

    payload = {
        "phone": clean_phone,
        "message": message,
    }

    headers = {
        "Content-Type": "application/json",
        "Client-Token": ZAPI_CLIENT_TOKEN,
    }

    response = requests.post(ZAPI_URL, json=payload, headers=headers, timeout=15)
    response.raise_for_status()
    return response.json()


def main():
    supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

    print("🔍 Buscando contatos no Supabase...")
    contacts = fetch_contacts(supabase, limit=3)

    if not contacts:
        print("⚠️  Nenhum contato encontrado na tabela 'contacts'.")
        return

    print(f"✅ {len(contacts)} contato(s) encontrado(s).\n")

    for contact in contacts:
        name  = contact["name"]
        phone = contact["phone"]

        print(f"📤 Enviando mensagem para {name} ({phone})...")
        try:
            result = send_whatsapp(phone, name)
            print(f"   ✅ Enviado! Resposta Z-API: {result}\n")
        except requests.HTTPError as e:
            print(f"   ❌ Erro HTTP ao enviar para {name}: {e}\n")
        except Exception as e:
            print(f"   ❌ Erro inesperado ao enviar para {name}: {e}\n")


if __name__ == "__main__":
    main()
