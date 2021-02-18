#---------------------------------------------------------------q1
# accepts integers between 1 and 31 (inclusive)
def q1(num):
  if(num >= 1 and num <= 31):
    return "good"
  return "bad"

#---------------------------------------------------------------q2
# accepts username of length 7-10 (inclusive)
def q2(name):
  if(len(name) >= 7 and len(name) <= 10):
    return "good"
  return "bad"

#---------------------------------------------------------------q3
# accepts age between 16-70 (except 60-65)
def q3(num):
  if((num >= 16 and num < 60) or (num > 65 and num <= 70)):
    return "good"
  return "bad"