from pymongo import MongoClient
from bson import ObjectId
from dotenv import load_dotenv
import os

load_dotenv()

client = MongoClient(f"mongodb+srv://{os.getenv("MONGO_USER")}:{os.getenv("MONGO_PASS")}@youtubemanagerpy.35pcg.mongodb.net/")

db = client['ytmanager']
video_collection = db["videos"]

def list_videos():
    for video in video_collection.find():
        print(f"\nID: {video['_id']} \nName: {video['name']} \nTime: {video['time']} \n")

def add_video(name, time):
    video_collection.insert_one({"name":name, "time":time})

def update_video(video_id, newName, newTime):
    video_collection.update_one({'_id': ObjectId(video_id)}, {"$set": {"name": newName, "time": newTime}})

def delete_video(video_id):
    video_collection.delete_one({"_id": ObjectId(video_id)})

def main():
    while True:
        print("\n Youtube Manager")
        print("1. List Videos")
        print("2. Add a video")
        print("3. Update a video")
        print("4. Delete a video")
        print("5. Exit")
        choice = input("Enter your choice : ")
        
        match choice:
            case '1':
                list_videos()
            case '2':
                name = input("Enter video name: ")
                time = input("Enter video duration: ")
                add_video(name, time)
            case '3':
                video_id = input("Enter video ID to update: ")
                name = input("Enter new name: ")
                time = input("Enter new duration: ")
                update_video(video_id, name, time)
            case '4':
                video_id = input("Enter ID to delete: ")
                delete_video(video_id)
            case '5':
                print("Thank You!")
                break
            case _:
                print("Invalid Choice!!")
                
if __name__ == "__main__":
    main()