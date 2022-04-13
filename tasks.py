from sqlite3 import connect
from tokenize import group
from todoist.api import TodoistAPI
#from todoist_api_python.api import TodoistAPI
from collections import namedtuple

import datetime as dt
from datetime import datetime, timedelta

from tomlkit import value

import config
import date_methods
from weeks import Weeks


project_values = namedtuple('project_values', 'name parent_id count')

    
def connect_API():
    api = TodoistAPI(config.token)
    api.sync()
    return api

def get_username(api):
    return api.state['user']['full_name']

def get_all_completed(api, start_date, end_date):
    completed = api.completed.get_all(limit = 100, since = start_date, until = end_date)
    return len(completed['items'])
    
def get_projects_statistic(api, start_date, end_date):
    projects = {}
    groups = {}
    for todoist_project in api.state['projects']:
        completed = api.completed.get_all(limit = 100, since = start_date, until = end_date, project_id=todoist_project['id'])
        values = project_values(todoist_project['name'], todoist_project['parent_id'], len(completed['items']))
        projects[todoist_project['id']] = values 
        if not todoist_project['parent_id']:
            groups[todoist_project['name']] = 0
    return projects, groups 
 
def get_groups_statistic(projects, groups):

    for values in projects.values():
        if values.parent_id == None:
            groups[values.name] = groups[values.name] + values.count
        else:
            parent_name = projects[values.parent_id].name
            groups[parent_name] = groups[parent_name] + values.count

    return groups


if __name__ == "__main__":

    start_date = date_methods.last_monday()
    end_date = date_methods.current_monday()

    api = connect_API()
    print ("Hello", get_username(api))
    print ("Last week you have completed", get_all_completed(api, start_date, end_date), "tasks")
    
    print ("Detailed statistic: ")

    output = get_projects_statistic(api, start_date, end_date)
    groups = get_groups_statistic(output[0], output[1])
    for key, value in groups.items():
        print (key, "=", value)

    input("press close to exit") 