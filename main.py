import requests
import os
import math
import json

from dotenv import load_dotenv    
load_dotenv()

API_KEY = os.getenv("HEVY_API_KEY")
BASE_URL = "https://api.hevy.com/v1" 

headers = {
    "api-key": API_KEY,
    "Content-Type": "application/json",
    "accept": "application/json" 
}

def get_workouts(page=1, page_size=10):
    if page < 1:
        raise ValueError("Page number must be 1 or greater")
    if page_size > 10:
        raise ValueError("Page size cannot exceed 10")
    
    endpoint = f"{BASE_URL}/workouts"
    params = {
        "page": page,
        "pageSize": page_size
    }
    
    try:
        response = requests.get(endpoint, headers=headers, params=params)
        response.raise_for_status() 
        workouts_data = response.json()
        return workouts_data.get("workouts", [])  
    except requests.exceptions.RequestException as e:
        print(f"Error fetching workouts: {e}")
        return None

def get_workouts_count():
    endpoint = f"{BASE_URL}/workouts/count"
   
    try:
        response = requests.get(endpoint, headers=headers)
        response.raise_for_status() 
        workouts_data = response.json()
        return workouts_data.get("workout_count", 0)  
    except requests.exceptions.RequestException as e:
        print(f"Error fetching workouts: {e}")
        return 0

def get_total_workouts(page_size=10):
    total_count = get_workouts_count()
    if total_count == 0:
        print("No workouts found or error occurred.")
        return []

    total_pages = math.ceil(total_count / page_size)
    print(f"Total workouts: {total_count}, Total pages: {total_pages} (pageSize={page_size})")

    all_workouts = []
    for page in range(1, total_pages + 1):
        workouts = get_workouts(page=page, page_size=page_size)
        if workouts:
            all_workouts.extend(workouts)
        else:
            print(f"Failed to fetch page {page}")
        
    return all_workouts

def save_workouts_to_file(workouts, output_file):
    try:
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(workouts, f, indent=2)
        print(f"Saved {len(workouts)} workouts to {output_file}")
    except IOError as e:
        print(f"Error saving workouts to file: {e}")

def main():    
    if not API_KEY:
        print("Missing API key")
        return
    
    page = 1
    page_size = 10
    workouts = get_workouts(page=page, page_size=page_size)
        
    print(f"Workouts from page {page} (pageSize={page_size}):")
    for i, workout in enumerate(workouts, 1):
        print(f"{i}. {workout.get('title', 'Untitled')} - {workout.get('start_time', 'No date')}")
        print(workout)

    all_workouts = get_total_workouts()
    print(f"\nTotal workouts fetched: {len(all_workouts)}")
    print("All workouts:")
    for i, workout in enumerate(all_workouts, 1):
        print(f"{i}. {workout.get('title', 'Untitled')} - {workout.get('start_time', 'No date')}")
        
    save_workouts_to_file(all_workouts, "workouts.json")

if __name__ == "__main__":
    main()