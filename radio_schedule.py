"""Manage radio show scheduling and slot reservations."""

import sqlite3


class RadioSchedule:
    """Manage radio schedule slots in an SQLite database."""

    def __init__(self):
        """Initialize the database and booking counter."""
        self.conn = sqlite3.connect(":memory:")
        self.conn.execute(
            """
            CREATE TABLE slots (
                id INTEGER PRIMARY KEY,
                show TEXT,
                host TEXT,
                start_hour INTEGER,
                minutes INTEGER
            )
            """
        )
        self.booked_minutes = 0

    def add_slot(self, show, host, start_hour, minutes):
        """Add a show to the schedule."""
        self.conn.execute(
            """
            INSERT INTO slots (show, host, start_hour, minutes)
            VALUES (?, ?, ?, ?)
            """,
            (show, host, start_hour, minutes),
        )
        self.booked_minutes += minutes

    def slot_label(self, show, host):
        """Return a formatted show label."""
        return f"{show} hosted by {host}"

    def overlap_free(self, start_hour, minutes, next_start_hour):
        """Check whether a show finishes before the next show."""
        return start_hour + minutes / 60 <= next_start_hour

    def morning_shows(self):
        """Return shows scheduled before noon."""
        if self.booked_minutes > 0:
            return [
                row[0]
                for row in self.conn.execute(
                    "SELECT show FROM slots WHERE start_hour < 12"
                )
            ]
        return []

    def remove_slot(self, slot_id):
        """Remove a scheduled show by its ID."""
        self.conn.execute("DELETE FROM slots WHERE id = ?", (slot_id,))

    def close(self):
        """Close the database connection."""
        self.conn.close()


def main():
    """Run a sample radio scheduling session."""
    schedule = RadioSchedule()
    schedule.add_slot("Sunrise Beats", "Vik", 7, 60)
    schedule.add_slot("Midday Talk", "Anu", 13, 45)
    print(schedule.slot_label("Sunrise Beats", "Vik"))
    print(schedule.overlap_free(7, 60, 13), schedule.morning_shows())
    schedule.remove_slot(2)
    schedule.close()


if __name__ == "__main__":
    main()
