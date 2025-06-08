from datetime import datetime
from db import conn,cursor

def add_event():
    event_name = input("Enter the name of the Event: ")
    event_date = datetime.strptime(input("Enter the date of the event (YYYY-MM-DD): "), "%Y-%m-%d")
    event_location = input("Enter event location: ")

    insert_query = """INSERT INTO events(event_name,event_date,location) values (%s,%s,%s);"""
    try:
        cursor.execute(insert_query,(event_name,event_date,event_location))
        conn.commit()
        print("Data Inserted")
    except Exception as e:
        print(f"Error inserting data: {e}")
        conn.rollback()

def add_guest():
    event_id = int(input("Enter the Event ID: "))
    guest_name = input("Enter your name: ")
    guest_email = input("Enter your Email: ")
    rsvp = input("Enter RSVP: ")

    insert_query = """INSERT INTO guests(event_id,name,email,rsvp_status) values (%s,%s,%s,%s);"""
    try:
        cursor.execute(insert_query,(event_id,guest_name,guest_email,rsvp))
        conn.commit()
        print("Data Inserted")
    except Exception as e:
        print(f"Error inserting data: {e}")
        conn.rollback()

def fetch_all_guest():
    event_id_fetch = int(input("Enter the Event ID: "))
    fetch_guest_query = """select * from guests where event_id=%s;"""
    
    try:
        cursor.execute(fetch_guest_query,(event_id_fetch,))
        rows = cursor.fetchall()
        if rows:
            for row in rows:
                print(row)
        else:
            print("No Guest has registered for this event")
    except Exception as e:
        print(f"Error fetching data: {e}")
        conn.rollback()

def search_guest():
    search_guest_by_email = input("Enter Email of guest: ")

    search_guest_by_email_query = "select * from guests where email = %s"

    try:
        cursor.execute(search_guest_by_email_query,(search_guest_by_email,))
        rows = cursor.fetchall()
        if rows:
            for row in rows:
                print(row)
        else:
            print("Guest with this email id doesn't exist")
    except Exception as e:
        print(f"Error while fetching data: {e}")
        conn.rollback()

def events_with_no_guests():
    events_with_no_guests_query = """select * from events where event_id not in 
                                    (select distinct event_id from guests);"""
    
    try:
        cursor.execute(events_with_no_guests_query)
        rows = cursor.fetchall()
        if rows:
            for row in rows:
                print(row)
        else:
            print("No events with 0 guests")
    except Exception as e:
        print(f"Error while fetching data {e}")
        conn.rollback()

def rsvp_counts():
    rsvp_count_query = """select rsvp_status,count(rsvp_status) from guests group by rsvp_status;"""

    try:
        cursor.execute(rsvp_count_query)
        rows = cursor.fetchall()
        if rows:
            for row in rows:
                print(row)
        else:
            print("No data in guest")
    except Exception as e:
        print(f"Error while reading data: {e}")
        conn.rollback()

print("Welcome to Rohit Event Management Private Limited")
print("--------------------------------------------------")

print("What do you want to do?")
print("1. Add an Event\n2. Add a Guest\n3. Fetch Guest list\n4. Search Guest\n5. Events with NO guests\n6. RSVP counts")
choice = int(input("Enter a choice: "))
match choice:
    case 1:
        add_event()
    case 2:
        add_guest()
    case 3:
        fetch_all_guest()
    case 4:
        search_guest()
    case 5:
        events_with_no_guests()
    case 6:
        rsvp_counts()
