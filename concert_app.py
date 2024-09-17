import sqlite3

# add a new band
def add_new_band():
    conn = sqlite3.connect('concerts.db')
    cursor = conn.cursor()

    # prompt
    name = input("Enter band name: ")
    hometown = input("Enter band hometown: ")

    # new band into database
    cursor.execute("INSERT INTO bands (name, hometown) VALUES (?, ?)", (name, hometown))
    conn.commit()
    
    print(f"Successfully added band: {name} from {hometown}")

    conn.close()


def add_new_venue():
    conn = sqlite3.connect('concerts.db')
    cursor = conn.cursor()


    title = input("Enter venue title: ")
    city = input("Enter venue city: ")

    
    cursor.execute("INSERT INTO venues (title, city) VALUES (?, ?)", (title, city))
    conn.commit()
    
    print(f"Successfully added venue: {title} in {city}")

    conn.close()


def add_new_concert():
    conn = sqlite3.connect('concerts.db')
    cursor = conn.cursor()

    
    band_id = input("Enter band ID: ")
    venue_id = input("Enter venue ID: ")
    date = input("Enter concert date (YYYY-MM-DD): ")

    
    cursor.execute("INSERT INTO concerts (band_id, venue_id, date) VALUES (?, ?, ?)", (band_id, venue_id, date))
    conn.commit()
    
    print(f"Successfully added concert for Band ID {band_id} at Venue ID {venue_id} on {date}")

    conn.close()



if __name__ == "__main__":
    
    add_new_band()
    add_new_venue()
    add_new_concert()