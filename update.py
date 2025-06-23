from datetime import datetime

readme_path = "README.md"

try:
    with open(readme_path, "r") as f:
        content = f.read()

    timestamp = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S UTC")
    
    new_content = content.split("<!--START_SECTION:updated-->")[0] + \
        f"<!--START_SECTION:updated-->{timestamp}<!--END_SECTION:updated-->"

    with open(readme_path, "w") as f:
        f.write(new_content)

    print(f"✅ README updated with timestamp: {timestamp}")

except Exception as e:
    print(f"❌ Error: {e}")
    exit(1)
