# archupdater
Auto update arch systems
- Add updater.py to /usr/local/bin/
- Add updater.service to /etc/systemd/system/
- Execute:
  - `systemctl daemon-reload`
  - `systemctl enable updater.service`
