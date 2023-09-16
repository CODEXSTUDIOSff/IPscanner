import subprocess
while True :
      print()
      print("ENTER AN IP OR WEBSITE NAME : ")

    
      i = input(">>>>")
      print()
      subprocess.call("ping "+ i ,shell=True)
