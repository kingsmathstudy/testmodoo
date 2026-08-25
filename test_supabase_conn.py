import os
from dotenv import load_dotenv
from supabase import create_client

load_dotenv()

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")
SUPABASE_BUCKET = os.getenv("SUPABASE_BUCKET", "tutormark-files")

print(f"Connecting to: {SUPABASE_URL}")
client = create_client(SUPABASE_URL, SUPABASE_KEY)

# 1. Test database connection & students table
try:
    res = client.table("students").select("*").execute()
    print(f"[OK] Supabase 'students' table connected! Rows: {len(res.data)}")
    print(f"Students data: {res.data}")
except Exception as e:
    print(f"[NOTICE] 'students' table check: {e}")

# 2. Test submissions table
try:
    res = client.table("submissions").select("*").execute()
    print(f"[OK] Supabase 'submissions' table connected! Rows: {len(res.data)}")
except Exception as e:
    print(f"[NOTICE] 'submissions' table check: {e}")

# 3. Test storage bucket
try:
    test_file_name = "__conn_test__.txt"
    client.storage.from_(SUPABASE_BUCKET).upload(test_file_name, b"test_ok", {"content-type": "text/plain", "upsert": "true"})
    client.storage.from_(SUPABASE_BUCKET).remove([test_file_name])
    print(f"[OK] Storage bucket '{SUPABASE_BUCKET}' read/write is working perfectly!")
except Exception as e:
    print(f"[NOTICE] Storage bucket check: {e}")
