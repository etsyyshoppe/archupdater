#!/usr/bin/python3
import subprocess
import os
import platform
import time
import threading

# functions
def arch_update():
    if os.path.exists("/usr/bin/yay"):  # Adjust path if yay is installed elsewhere
        arch_update = ['/usr/bin/yay', '--noconfirm']
        subprocess.run(arch_update)
    else:
        arch_update = ['/usr/bin/pacman', '-Syu', '--noconfirm']
        subprocess.run(arch_update)
    # if update.ets_platform == 'arch':
    #     subprocess.run([update.arch_update])
def flatpak_update():
    flatpak_update = ['/usr/bin/flatpak', 'update', '-y']
    subprocess.run(flatpak_update)
    # subprocess.run([update.flatpak_update])
def main():
    threads = [
        threading.Thread(target=arch_update),
        threading.Thread(target=flatpak_update)
    ]
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()

while True:
    main()
    time.sleep(43200)
