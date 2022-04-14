# ToDoist weeks statistic
Script uses Todoist app API to collect statistics of completed tasks in different projects on weekly basis.
It combines number of completed tasks under parent project


## How to use
- Create config.py. It should contain the following information: 

        #Todoist API token
        token = '..........................'
        # Your birthday
        day = XX
        month = XX
        year = XXXX

## Example

    'python tasks.py'

# ToDo
- Add DB support
- Add ability to select week 
- Move to new todoist API lib

