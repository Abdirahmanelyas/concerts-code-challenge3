import sqlite3

class Band:
    @staticmethod
    def add_new_band():
        conn = sqlite3.connect('concerts.db')
        cursor = conn.cursor()

        name = input("Enter band name: ")
        hometown = input("Enter band hometown: ")

        cursor.execute("INSERT INTO bands (name, hometown) VALUES (?, ?)", (name, hometown))
        conn.commit()

        print(f"Successfully added band: {name} from {hometown}")
        conn.close()

class Venue:
    @staticmethod
    def add_new_venue():
        conn = sqlite3.connect('concerts.db')
        cursor = conn.cursor()

        title = input("Enter venue title: ")
        city = input("Enter venue city: ")

        cursor.execute("INSERT INTO venues (title, city) VALUES (?, ?)", (title, city))
        conn.commit()

        print(f"Successfully added venue: {title} in {city}")
        conn.close()

class Concert:
    @staticmethod
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
    
    Band.add_new_band()
    Venue.add_new_venue()
    Concert.add_new_concert()
