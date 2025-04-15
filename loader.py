import time
import urllib.request

print("""
██╗██████╗░██╗░░██╗  ░██████╗██╗███╗░░░███╗
██║██╔══██╗██║░██╔╝  ██╔════╝██║████╗░████║
██║██║░░██║█████═╝░  ╚█████╗░██║██╔████╔██║
██║██║░░██║██╔═██╗░  ░╚═══██╗██║██║╚██╔╝██║
██║██████╔╝██║░╚██╗  ██████╔╝██║██║░╚═╝░██║
╚═╝╚═════╝░╚═╝░░╚═╝  ╚═════╝░╚═╝╚═╝░░░░░╚═╝

""")

print("1 for Install")
print("2 for Uninstall")
print("source: https://github.com/idkshigng")
print("made by idkshi")

option = input("enter ur choice:")

if option == "1":
    print("Installing...")
    steps = [
        "installing idk1",
        "installing idk2",
        "installing idk3",
        "installing idk4",
        "installing idk5",
        "installing sim.exe"
    ]
    for step in steps:
        print(step)
        time.sleep(0.8)



    url = "https://media.istockphoto.com/id/537442618/photo/business-concept.jpg?s=612x612&w=0&k=20&c=7j3hrkdi3FbyX1xWrRIOKEXNcdTYdi5kV-PVdFZBLNM="  
    save_path = "sim.jpg"


    try:
        print("Downloading file...")
        urllib.request.urlretrieve(url, save_path)
        print(f"Download complete! File saved as {save_path}")
    except Exception as e:
        print(f"Failed to download the file: {e}")

    time.sleep(1)
    print("""
█░░█ 　 █▀▀▀ █▀▀█ ▀▀█▀▀ 　 █░░█ █▀▀█ █▀▀ █░█ █▀▀ █▀▀▄ 
█░░█ 　 █░▀█ █░░█ ░░█░░ 　 █▀▀█ █▄▄█ █░░ █▀▄ █▀▀ █░░█ 
░▀▀▀ 　 ▀▀▀▀ ▀▀▀▀ ░░▀░░ 　 ▀░░▀ ▀░░▀ ▀▀▀ ▀░▀ ▀▀▀ ▀▀▀░
    """)
elif option == "2":
    print("Uninstalling...")
else:
    print("no")
