# test cases:
# let candidate1 = { minSalary: 120000 },
# job1 = { maxSalary: 130000 },
# job2 = { maxSalary: 80000 };
    
# match(candidate1, job1) --> true
# match(candidate1, job2) --> false

def match(candidate, job):
    try:
        return job['max_salary'] >= candidate['min_salary'] * 0.9
    except:
        return False
