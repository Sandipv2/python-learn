import json
import os

file_name = 'youtube.txt'

def load_videos():
    try:
        with open(file_name, 'r') as file:
            videos = json.load(file)
            return videos
    except FileNotFoundError:
        return []
    
def save_data_helper(vidoes):
    with open(file_name, 'w') as file:
        json.dump(vidoes, file)
    
def show_all_videos(vidoes):
    print(f"\n{'*' * 40}")
    
    for index, video in enumerate(vidoes, start=1):
        print(f"{index}. {video['name']}, Duration: {video['time']}")
        
    print(f"\n{'*' * 40}")

def add_video(vidoes):
    name = input("Enter video title: ")
    time = input("Enter duraiton: ")
    vid = {"name": name, "time": time}
    vidoes.append(vid)
    save_data_helper(vidoes)
    print("Added!!")
    

def update_video(vidoes):
    show_all_videos(vidoes)
    index = int(input("Enter video number to update: "))
    
    if 1 <= index <= len(vidoes):
        name = input("Enter new video title: ")
        time = input("Enter new duraiton: ")
    
        vidoes[index-1]["name"] = name
        vidoes[index-1]["time"] = time    
        save_data_helper(vidoes)
        print("Updated!!")
    else:
        print("Invalid Number!!")

def delete_video(vidoes):
    show_all_videos(vidoes)
    index = int(input("Enter video number to delete: "))
    
    if 1 <= index <= len(vidoes):
        del vidoes[index - 1]
        save_data_helper(vidoes)
        print("Deleted!!")
    else:
        print("Invalid Number!!")

def main():
    videos = load_videos()
    
    while True:
        print("\n******* YouTube Manager *******")
        print("1. See all videos")
        print("2. Add video")
        print("3. Update video")
        print("4. Delete video")
        print("5. Exit")
        choice = input("Enter your choice: ")
        
        os.system('cls')
        match choice:
            case '1':
                show_all_videos(videos)
            case '2':
                add_video(videos)
            case '3':
                update_video(videos)
            case '4':
                delete_video(videos)
            case '5':
                print("\nThank You :)")
                break
            case _:
                print("Invalid choice!!")
                
if __name__ == "__main__":
    main()