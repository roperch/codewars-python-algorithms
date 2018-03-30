#test cases
dutyFree(12, 50, 1000) --> 166
dutyFree(17, 10, 500) --> 294
dutyFree(24, 35, 3000) --> 357

def duty_free(price, discount, holiday_cost):
  dollars_saved = price * (discount/100)
  return int(holiday_cost / dollars_saved
