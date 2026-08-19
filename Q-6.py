with open("log.txt") as f:
     content = f.read()
 
    
if("python" in content):
     print("python is present in log file")

else:
     print("python is not present in log file")
