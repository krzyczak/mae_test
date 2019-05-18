
if __name__ == "__main__":
  from config import *


  print(f"automatise: your_path is: {your_path}")
  print(f"automatise:       DIR_RAW is: {DIR_RAW}")

  print(DIR_RAW)

  import zxc

  zxc.start()

  print(DIR_RAW)



  import mae

  result_of_modeling = mae.start()
  print("\n\n---------------------------")
  print("Result of modelling and evaluation:")
  print(result_of_modeling)
  print(" DONE ---------------------------\n\n")
