# Coaching Bot (Demo)

## Installation

### Development (Using docker)

#### Prerequisites

- [Docker](https://www.docker.com/products/docker-desktop) running on Mac, Windows or Linux
- Docker Know-How (recommended)
    - [Official Docker Cheatsheet](https://www.docker.com/sites/default/files/d8/2019-09/docker-cheat-sheet.pdf)

#### Step-by-step

1. Check out the repository

    ```bash
    git clone git@github.com:/path/to/this/repo.git /path/to/project
    ```

2. Copy the config file - Adjust according to your requirements

    ```bash
    cd /path/to/project
    cp bot/default.config.txt.dist bot/default.config.txt
    ```

3. Build & run the container

    ```bash
    docker-compose up --build -d --force-recreate
    ```

4. Switch into a shell on the running container

    ```bash
    docker exec -it coaching_bot_demo_bot_1 bash
   ```

5. Start Bot

    ```bash
   python start_bot.py
   ```
   
6. Start UI

    ```bash
   python start_ui.py
   ```
   
   Open [http://localhost:11500](http://localhost:11500) in your browser. You should see a the flask ui to configure the bot.
   
    