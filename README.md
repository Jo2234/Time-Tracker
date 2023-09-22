# Task Time Tracker

This script allows users to track the time spent on a specific task and then automatically adds the tracked time as an event to the local macOS Calendar.

## Features

- Prompt the user to input the task name.
- Start and stop a timer to track the duration of the task.
- Automatically add the tracked time as an event to the local macOS Calendar.

## Usage

1. Run the script.
2. Enter the name of the task you want to track.
3. Press Enter to start the timer.
4. Once done with the task, press Enter again to stop the timer.
5. The script will then add the task with its duration to the macOS Calendar under the "Work" calendar. (You can change the calendar name in the script if needed.)

## Requirements

- Python 3
- macOS with the Calendar app
- Necessary permissions for the terminal application to control the Calendar app.

## Customization

- To change the calendar where the event is added, modify the `"Work"` string in the `add_to_calendar_local` function to the name of your preferred calendar.

## Troubleshooting

If you encounter an error related to adding the event to the calendar, ensure that:

- Your terminal application has the necessary permissions to control the Calendar app. This can be set in `System Preferences` > `Security & Privacy` > `Privacy` > `Automation`.
- The specified calendar name exists in your Calendar app.# Time-Tracker
