# MySQL-Docker

## Docker Desktop Setup
1. Download Docker Desktop 
2. Sign up for a Docker account 
3. Start Docker Desktop
## Build Docker Image
4. Open terminal/command line on your computer
5. Build Docker image by entering this line into your terminal/command line
 <br />`docker build -t local-mysql .` 
## Run the Docker Container
6. Run Docker container by entering this line into your terminal/command line
<br /> `docker run -dp 3306:3306 local-mysql`
<br />After you ran this line, go to *Containers* in Docker Desktop. You should be able to see a running container
## Python Program with MySQL
7. Install mysql-connector-python by entering this line into your terminal/command line
<br /> `pip install -r requirements.txt`
<br /> or
<br /> `pip install mysql-connector-python`
