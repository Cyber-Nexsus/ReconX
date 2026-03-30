# ReconX
# ReconX - Simple Recon Tool

## Features
- IP Resolve
- HTTP Status Check
- Port Scan
- Subdomain Discovery

## Usage

```bash
python reconx.py

In Kali Linux, if you attempt to run the command python reconx.py and Python is not installed, the terminal will return an error stating: "command not found: python"
However, since you are using Kali Linux (which is a Debian-based distribution), it is highly likely that Python 3 is already installed by default, but the system might not recognize the shortened command python. 
1. Check for Python 3
Modern Kali Linux versions (since 2020) have phased out Python 2. Try running the script using the explicit python3 command: 

python3 reconx.py

2. Verify the Installation
To confirm if Python is truly missing or just named differently, run these version checks:

* Check Python 3: python3 --version
* Check Python 2: python --version (usually fails on newer Kali) 

3. How to Install Python
If both commands fail and you have confirmed it is not installed, you can install it using the [APT package manager](https://www.kali.org/docs/general-use/python3-external-packages/):

sudo apt update
sudo apt install python3

4. Professional Tip for CEH (Executable Scripts) 
In a pentesting environment, you often want to run scripts directly like a tool. You can do this by adding a "shebang" line and changing permissions: 

   1. Add the shebang: Open reconx.py in an editor (like nano) and ensure the first line is:
   #!/usr/bin/env python3
   2. Make it executable:
   chmod +x reconx.py
   3. Run it directly:
   ./reconx.py 

Are you getting a specific error message like "externally-managed-environment" when trying to install related libraries for your recon script?

[1] [https://www.geeksforgeeks.org](https://www.geeksforgeeks.org/linux-unix/how-to-resolve-python-command-not-found-error-in-linux/)
[2] [https://www.youtube.com](https://www.youtube.com/watch?v=LMmtwTV6gTY&t=549)
[3] [https://www.scaler.com](https://www.scaler.com/topics/how-to-run-python-script-in-linux/)
[4] [https://stackoverflow.com](https://stackoverflow.com/questions/71427901/how-to-run-a-python-script-on-linux)
[5] [https://www.geeksforgeeks.org](https://www.geeksforgeeks.org/linux-unix/how-to-install-python-3-on-kali-linux/)
[6] [https://www.kali.org](https://www.kali.org/blog/python-externally-managed/)
[7] [https://www.webasha.com](https://www.webasha.com/blog/how-to-use-shell-scripting-in-kali-linux-for-automation-the-complete-guide)
[8] [https://superuser.com](https://superuser.com/questions/828737/run-python-scripts-without-explicitly-invoking-python)
[9] [https://www.kali.org](https://www.kali.org/docs/general-use/python3-transition/)
