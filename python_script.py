#The .py extension is important because it lets the Python interpreter know 
#that this text file contains Python code. This code for writing code with excuting 
#It also lets you, others, and coding text editors 
# know that this text file contains Python code. However,
#  text saved in a file with the .py extension is identical to that same text saved with a .txt extension; they are both just text files that contain the exact same information.

import os

cpu_num = os.cpu_count()
print(f"My computer has {cpu_num} CPU cores")