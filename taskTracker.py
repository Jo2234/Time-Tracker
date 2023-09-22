import datetime
import subprocess

# Function to track the time spent on a task
def track_task_time():
    task_name = input("Enter the name of the task: ")
    input("Press Enter to start the timer...")
    start_time = datetime.datetime.now()
    print(f"Started tracking time for '{task_name}' at {start_time.strftime('%H:%M:%S')}")
    
    input("Press Enter to stop the timer...")
    end_time = datetime.datetime.now()
    print(f"Stopped tracking time for '{task_name}' at {end_time.strftime('%H:%M:%S')}")
    
    time_spent = end_time - start_time
    print(f"Total time spent on '{task_name}': {time_spent}")
    
    return task_name, start_time, end_time

# Function to add the tracked task to the local macOS Calendar
def add_to_calendar_local(task_name, start_time, end_time):
    # Format the start and end times for AppleScript
    start_str = start_time.strftime('%Y-%m-%d %H:%M:%S')
    end_str = end_time.strftime('%Y-%m-%d %H:%M:%S')
    
    # AppleScript to add an event to the default calendar
    applescript = f"""
    tell application "Calendar"
        tell calendar "Work"  -- You can change "Work" to the name of your preferred calendar
            make new event with properties {{summary:"{task_name}", start date:date "{start_str}", end date:date "{end_str}"}}
        end tell
    end tell
    """
    
    # Execute the AppleScript using osascript
    process = subprocess.Popen(['osascript', '-e', applescript], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()
    
    if process.returncode == 0:
        print(f"Added '{task_name}' to calendar from {start_time.strftime('%H:%M:%S')} to {end_time.strftime('%H:%M:%S')}")
    else:
        print(f"Error adding event to calendar: {stderr.decode('utf-8')}")

# Main execution
if __name__ == "__main__":
    task_name, start_time, end_time = track_task_time()
    add_to_calendar_local(task_name, start_time, end_time)
