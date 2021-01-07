import os, subprocess

pmlist = []
#Preparing portage
print("Testing to see if Portage exists on your system...")
portagepath='/etc/portage'
portagetest = os.path.isdir(portagepath)
if portagetest == True:
    print("This system uses Portage!")
    pmlist.append("emerge -auDN @world")
else:
    print("Portage is not installed on this system...")

#Testing for Rust Cargo PM
print("Checking for Cargo..")
subprocess.run(["cargo"])
stderr=subprocess.STDOUT
if stderr != None:
    rustexists="True"
    print("Cargo is installed on this system!")
    pmlist.append("cargo update")
else:
    rustexists="False"
    print("Cargo is not installed on your system...")

#Testing for pip
print("Cheking for Pip...")
subprocess.run(["pip"])
stderr=subprocess.STDOUT
if stderr != None:
    pipexists="True"
    print("Pip is installed on your system!")
    pmlist.append("pip update")
else:
    pipexists="False"
    print("Pip is not present on your system...")