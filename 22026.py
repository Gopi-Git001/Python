work_hours = [("Abby",100),('Gopi',400),('Ram',2000)]


def employee_check(work_hours):
    
    max_hours = 0
    employee_of_month = ''
    
    for employee,hours in work_hours:
        
        if hours > max_hours :
            
            max_hours = hours
            
            employee_of_month = employee
            
        else :
            pass
        
    return employee_of_month,max_hours

print(employee_check(work_hours))

