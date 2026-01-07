from website import create_app
import os.path
from dotenv import load_dotenv

# Wczytuje plik .env tylko jeśli istnieje 
if os.path.exists('.env'):
    load_dotenv()

app = create_app()

if __name__ == '__main__':
    env = os.environ.get("ENVIRONMENT")
    print(" * Environment: " + env)
    if env == "local":
        app.run(debug=True) # Debug tylko do celów testowych
    else:
        app.run(debug=False)
