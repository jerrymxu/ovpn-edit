# ovpn-edit
A python based tool to batch edit OpenVPN profiles including adding login credential.

## Usage
Instructions to edit .ovpn file

### Add Authentication
The program will check the exsistence of login.conf, and prompt you to add the username and password for your ovpn profiles if one does not already exsist.
```
python3 add_auth.py <PATH_TO_CONFIG_FOLDER>
```

Force overwrite the login.conf to update username and password for your ovpn profiles.
```
python3 -f add_auth.py <PATH_TO_CONFIG_FOLDER>
```
