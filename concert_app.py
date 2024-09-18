import sqlite3

class Band:
    def __init__(self, name, hometown):
        self.name = name
        self.hometown = hometown

    def add_new_band(self):
        conn = sqlite3.connect('concerts.db')
        cursor = conn.cursor()

        cursor.execute("INSERT INTO bands (name, hometown) VALUES (?, ?)", (self.name, self.hometown))
        conn.commit()

        print(f"Successfully added band: {self.name} from {self.hometown}")
        conn.close()


class Venue:
    def __init__(self, title, city):
        self.title = title
        self.city = city

    def add_new_venue(self):
        conn = sqlite3.connect('concerts.db')
        cursor = conn.cursor()

        cursor.execute("INSERT INTO venues (title, city) VALUES (?, ?)", (self.title, self.city))
        conn.commit()

        print(f"Successfully added venue: {self.title} in {self.city}")
        conn.close()


class Concert:
    def __init__(self, band_id, venue_id, date):
        self.band_id = band_id
        self.venue_id = venue_id
        self.date = date

    def add_new_concert(self):
        conn = sqlite3.connect('concerts.db')
        cursor = conn.cursor()

        cursor.execute("INSERT INTO concerts (band_id, venue_id, date) VALUES (?, ?, ?)", (self.band_id, self.venue_id, self.date))
        conn.commit()

        print(f"Successfully added concert for Band ID {self.band_id} at Venue ID {self.venue_id} on {self.date}")
        conn.close()


if __name__ == "__main__":
    
    name = input("Enter band name: ")
    hometown = input("Enter band hometown: ")
    band = Band(name, hometown)
    band.add_new_band()

    title = input("Enter venue title: ")
    city = input("Enter venue city: ")
    venue = Venue(title, city)
    venue.add_new_venue()

    band_id = input("Enter band ID: ")
    venue_id = input("Enter venue ID: ")
    date = input("Enter concert date (YYYY-MM-DD): ")
    concert = Concert(band_id, venue_id, date)
    concert.add_new_concert()
