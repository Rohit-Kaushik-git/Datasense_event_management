import psycopg2
from urllib.parse import quote
PG_PORT='5432'
PG_HOST='localhost'
PG_DB = 'event_management'
PG_USER='rohit'
PG_PASSWORD_RAW='qwerty@123'

PG_PASSWORD = quote(PG_PASSWORD_RAW)

POSTGRES_URL=f"postgresql://{PG_USER}:{PG_PASSWORD}@{PG_HOST}:{PG_PORT}/{PG_DB}"

conn = psycopg2.connect(POSTGRES_URL)
cursor = conn.cursor()

create_table_query = """
CREATE TABLE events (
    event_id SERIAL PRIMARY KEY,
    event_name VARCHAR(100),
    event_date DATE,
    location VARCHAR(100)
);

CREATE TABLE guests (
    guest_id SERIAL PRIMARY KEY,
    event_id INT REFERENCES events(event_id),
    name VARCHAR(100),
    email VARCHAR(100),
    rsvp_status VARCHAR(10),
    UNIQUE (event_id,name, email));
"""

try:
    cursor.execute(create_table_query)
    conn.commit()
except Exception as e:
    conn.rollback()