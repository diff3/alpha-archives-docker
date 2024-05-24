# Alpha Project Archive Docker



Check https://github.com/geo-tp/Alpha-archives-website to see how it's installed manually. 



## Basic



- Edit config files in configs folder, the default settings is localhost only, with MariaDB in a container.

- Clone or download https://github.com/The-Alpha-Project/Alpha-Project-Archive to media/Alpha-Project-Archive. 

  - cd media && git clone https://github.com/The-Alpha-Project/Alpha-Project-Archive

  - It's important it's to media/Alpha-Project-Archive, otherwise you need to change in the config before building.

- start with docker compose up -d

- backend will loop until DB is created

- on first run backend will create image database from media/Alpha-Project-Archive, it will run for a while.

  - you can use docker compose logs -f to follow progress. ctrl-c to exit.

  - Image database is not auto upteded, but you can do i manually by login into backend container. 

- log into localhost:3000/login and change superuser password. it's admin:admin

  

## Config files. 



- Config.py is settings for building image database from media/Alpha-Project-Archive
- Settings.py is backend server settings
- api.tsx is frontend settings.
