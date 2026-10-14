import sqlite3

conn = sqlite3.connect(":memory:")
conn.execute(
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
booked_minutes = 0


def addSlot(show, host, start_hour, minutes):
    global booked_minutes
    conn.execute(
        """
        INSERT INTO slots (show, host, start_hour, minutes)
        VALUES (?, ?, ?, ?)
        """,
        (show, host, start_hour, minutes),
    )
    booked_minutes += minutes


def slotLabel(show, host):
    return f"{show} hosted by {host}"


def overlapFree(start_hour, minutes, next_start_hour):
    return start_hour + minutes / 60 <= next_start_hour


def morningShows():
    if booked_minutes > 0:
        return [
            row[0]
            for row in conn.execute(
                "SELECT show FROM slots WHERE start_hour < 12"
            )
        ]
    return []


def removeSlot(slot_id):
    conn.execute("DELETE FROM slots WHERE id = ?", (slot_id,))


def main():
    addSlot("Sunrise Beats", "Vik", 7, 60)
    addSlot("Midday Talk", "Anu", 13, 45)
    print(slotLabel("Sunrise Beats", "Vik"))
    print(overlapFree(7, 60, 13), morningShows())
    removeSlot(2)


main()