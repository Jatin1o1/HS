import sys
import pkg_resources
import subprocess

'''
# checking all the installed packaged using pip
reqs = subprocess.check_output([sys.executable, '-m', 'pip','freeze'])
installed_packages = [r.decode().split('==')[0] for r in reqs.split()]
'''

dependent_pkg=["paho-mqtt", "pyttsx3","SpeechRecognition"]



#installed_packages = {d.project_name: d.version for d in pkg_resources.working_set}   # package with its version number
installed_packages = [d.project_name for d in pkg_resources.working_set]# package names only

#print(installed_packages)

#print ("home Security system is dependent on packages : " + str( dependent_pkg))

for pkg in dependent_pkg:
    if pkg in installed_packages:
        print(str(pkg)  + "is present")
        
    else:
        print( "installing package : " + str(pkg) )

        try:
            j=subprocess.call(['pip', 'install', pkg])

        except:
            j=subprocess.call(['pip3', 'install', pkg])
            


