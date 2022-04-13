import config
import datetime as dt
from datetime import datetime, timedelta

delta = timedelta(days=7)

birthday_date = datetime(config.year, config.month, config.day, 0, 0)
today = datetime.today()
my_delta = today - birthday_date

prev_year_week = int(today.strftime('%W'))
cur_year_week = prev_year_week + 1
weekday = today.weekday()


def last_monday():
    last_mon = today - delta - timedelta(days=weekday + 1)
    last_mon = last_mon.strftime("%Y-%m-%dT21:00:00")
    print ("Last Monday is", last_mon)
    return last_mon

def current_monday():
    cur_mon = today - timedelta(days=weekday + 1)
    cur_mon = cur_mon.strftime("%Y-%m-%dT21:00:00") #Temporary hack to avoid timezone issue.
    print ("Current Monday is", cur_mon)
    
    return cur_mon

def print_weeks_info():
    print("Prev year_week is", prev_year_week)
    print("Current year_week is", cur_year_week) 
    

def get_my_year_week():
    week = cur_year_week - 9
    return week

def calc_life_days():
    life_days = my_delta.days
    return life_days

def calc_life_weeks():
    life_weeks = calc_life_days()//7
    return life_weeks

def calc_life_years():
    life_years = calc_life_weeks()/52.1775
    return life_years