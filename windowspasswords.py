import subprocess 
import os
print('''
┓ ┏┳┳┓  ┓ ┏┳┏┓┳    
┃┃┃┃┃┃━━┃┃┃┃┣ ┃    
┗┻┛┻┛┗  ┗┻┛┻┻ ┻    
┏┓┏┓┏┓┏┓┓ ┏┏┓┳┓┳┓┏┓
┃┃┣┫┗┓┗┓┃┃┃┃┃┣┫┃┃┗┓
┣┛┛┗┗┛┗┛┗┻┛┗┛┛┗┻┛┗┛
                   
''')
print("Produced By MulderCW")
command_output = subprocess.check_output(["netsh", "wlan", "show", "profile"], universal_newlines=True)
output_lines = command_output.split('\n')
wifi_info = {}
for line in output_lines:
    if "All User Profile" in line:
        profile_name = line.split(":")[1].strip()
        try:
            password_output = subprocess.check_output(["netsh", "wlan", "show", "profile", f"name=\"{profile_name}\"", "key=clear"], universal_newlines=True)

            # Extract the password from the output
            password_lines = password_output.split('\n')
            password = None
            for p_line in password_lines:
                if "Key Content" in p_line:
                    password = p_line.split(":")[1].strip()
                    break

            wifi_info[profile_name] = password if password is not None else "Password not available"
        except subprocess.CalledProcessError:
            wifi_info[profile_name] = "Password not available"
os.system('cls')
# Print the Wi-Fi names and passwords
print("Here is what we found...")
for name, password in wifi_info.items():
    print(f"Wi-Fi Name: {name} | Password: {password}")

# Add a wait for a key press before exiting
input("Press Enter to exit...")
