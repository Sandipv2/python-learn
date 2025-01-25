import sqlite3, os

conn = sqlite3.connect("youtube_data.db")
cursor = conn.cursor()

cursor.execute("""
               CREATE TABLE IF NOT EXISTS youtube (
                   id INTEGER PRIMARY KEY,
                   name TEXT NOT NULL,
                   time TEXT NOT NULL 
               )
               """)

def list_videos():
    cursor.execute("SELECT * FROM youtube")
    videos = cursor.fetchall()
    
    if not videos:
        print(f"{'*' * 30}")
        print("Nothing to show!")
        return
    
    print(f"\n{'*' * 30}")
    for vid in videos:
        print(f"{vid[0]}. {vid[1]} ---> {vid[2]}")
        
    print(f"{'*' * 30}")

def add_video(name, time):
    cursor.execute('''
                   INSERT INTO youtube (name, time) VALUES (?, ?)
                   ''', (name, time))
    conn.commit()
    print("Video added!!")

def update_video(id, new_name, new_time):
    cursor.execute('''
                   UPDATE youtube SET name = ?, time = ? WHERE id = ?
                   ''', (new_name, new_time, id))
    conn.commit()
    print("Updated!!")

def delete_video(id):
    cursor.execute('''
                   DELETE FROM youtube WHERE id = ?
                   ''', (id,))
    conn.commit()
    print("Deleted!!")

def main():
    while True:
        print("\n********** YouTube Manager **********")
        print("1. List Videos")
        print("2. Add Video")
        print("3. Update Video")
        print("4. Delete Video")
        print("5. Exit")
        choice = input("Your choice: ")
        
        os.system("cls")
        match choice:
            case '1':
                list_videos()
                
            case '2':
                print(f"{'*' * 30}")
                name = input("Enter video name: ")
                time = input("Enter vidoe time: ")
                add_video(name, time)
                
            case '3':
                print(f"{'*' * 30}")
                id = int(input("Enter video ID to update: "))
                name = input("Enter new name: ")
                time = input("Enter new time: ")
                update_video(id, name, time)
                
            case '4':
                print(f"{'*' * 30}")
                id = int(input("Enter vidoe ID to delete: "))
                delete_video(id)
                
            case '5':
                print("\n Thank You!")
                break
            case _:
                print("Invalid input!!")
        

if __name__ == '__main__':
    main()