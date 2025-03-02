# archupdater
Auto update arch systems
- Add updater.py to /usr/local/bin/
- Execute:
  - `chmod +x /usr/local/bin/updater.py`
- Add updater.service to /etc/systemd/system/
- Execute:
  - `systemctl daemon-reload`
  - `systemctl enable updater.service`
