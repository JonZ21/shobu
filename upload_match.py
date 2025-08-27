from supabase import create_client
from datetime import datetime
import os

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

def upload_match(player1, player2, p1_character, p2_character, winner):
    data = {
        "p1_name": player1,
        "p2_name": player2,
        "winner": winner,
        "created_at": datetime.now().isoformat(),
        "p1_character": p1_character,
        "p2_character": p2_character
    }
    res = supabase.table("results").insert(data).execute()
    print(res)

# Test upload
# upload_match("Jon", "Justin", "Donkey Kong", "Kazuya","Jon")


