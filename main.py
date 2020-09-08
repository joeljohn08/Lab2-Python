# Author: Yanling Wang yuw17@psu.edu
# Collaborator:
# Collaborator:
# Collaborator:
# Section: 1
# Breakout: 2
def assigngrade(percentage):
  if percentage >= 93.0:
    grade = "A"
  elif percentage >= 90.0:
    grade = "A-"
  elif percentage >= 87.0:
    grade = "B+"
  elif percentage >= 83.0:
    grade = "B"
  elif percentage >= 80.0:
    grade = "B-"
  elif percentage >= 77.0:
    grade = "C+"
  elif percentage >= 70.0:
    grade = "C"
  elif percentage >= 60.0:
    grade = "D"
  else:
    grade = "F"
  return grade

  
def main():
  percentage = input("Enter your CMPSC 131 grade:")
  percentage = float(percentage)
  print(f"Your letter grade for CMPSC 131 is {assigngrade(percentage)}.")

if __name__ == "__main__":
  main()  