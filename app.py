from src import app
import os
from dotenv import load_dotenv

load_dotenv()


if __name__ == '__main__':
    app.run(host=os.getenv("HOST"), port=os.getenv("PORT", 5000), debug=os.getenv("DEBUG"))