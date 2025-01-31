"""
Inside conditions.json, you will see a subset of UNSW courses mapped to their 
corresponding text conditions. We have slightly modified the text conditions
to make them simpler compared to their original versions.

Your task is to complete the is_unlocked function which helps students determine 
if their course can be taken or not. 

We will run our hidden tests on your submission and look at your success rate.
We will only test for courses inside conditions.json. We will also look over the 
code by eye.

NOTE: This challenge is EXTREMELY hard and we are not expecting anyone to pass all
our tests. In fact, we are not expecting many people to even attempt this.
For complete transparency, this is worth more than the easy challenge. 
A good solution is favourable but does not guarantee a spot in Projects because
we will also consider many other criteria.
"""
import json
import re

# NOTE: DO NOT EDIT conditions.json
with open("./conditions.json") as f:
    CONDITIONS = json.load(f)
    f.close()


def and_cond()


def is_unlocked(courses_list, target_course):
    """Given a list of course codes a student has taken, return true if the target_course 
    can be unlocked by them.
    
    You do not have to do any error checking on the inputs and can assume that
    the target_course always exists inside conditions.json

    You can assume all courses are worth 6 units of credit
    """
    
    # TODO: COMPLETE THIS FUNCTION!!!
    
    #case 1 -> simple or
    if ('')


    #special conditions

    #brackets
    if ("(" in CONDITIONS[target_course] or ")" in CONDITIONS[target_course]):
        bracket_cond = filter(None, re.split("[()]" , CONDITIONS[target_course]))

    #AND
    if ("AND" in CONDITIONS[target_course] or "and" in CONDITIONS[target_course]):
        and_cond = filter(None, re.split("[and, AND]" , CONDITIONS[target_course]))
    
        and_val = True
        for (course in and_cond):
            if course not in courses_list:
                and_val = False
                break
    
    #OR
    if ("or" in CONDITIONS[target_course] or "OR" in CONDITIONS[target_course]):
        or_cond = filter(None, re.split("[or, OR]" , CONDITIONS[target_course]))

        or_val = False
        for (course in or_cond):
            if course in courses_list:
                or_val = True
                break
            


    cond = CONDITIONS[target_course].split()
    
    return True





    