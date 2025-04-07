from config.config import BOUNDING_BOX, DATABASE_URL, OPENSKY_API_BASE_URL

print(f"Database URL: {DATABASE_URL}")
print(f"OpenSky API Base URL: {OPENSKY_API_BASE_URL}")
if BOUNDING_BOX:
    print(f"Bounding Box: {BOUNDING_BOX}")
else:
    print("Bounding Box is not set or invalid.")
