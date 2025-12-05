work_hours = [('Abby',400),('Billey',2000),('Cassie',300)]


def employee_check(work_hours):
    
    current_max = 0
    
    employee_of_month = ''
    
    for employee,hours in work_hours:
        
        if hours > current_max :
            
            current_max = hours
            
            employee_of_month = employee
            
        else:
            
            pass
    return (employee_of_month,current_max)


print(employee_check(work_hours))

