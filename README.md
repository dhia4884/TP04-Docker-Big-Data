
# TP04 - Containerization and Big Data Environment Deployment Using Docker

## 1. Project Overview

This project demonstrates how to containerize a Python data analysis application using Docker and Docker Compose.

The application analyzes a large air quality dataset containing approximately 66.9 million records and calculates statistics about temperature, air quality, and geographical districts.

## 2. Technologies Used

- Docker
- Docker Hub
- Docker Compose
- Python 3.11
- Linux
- HTML and CSS

## 3. Project Structure

```text
TP04-Docker-Big-Data/
│
├── app.py
├── Dockerfile
├── compose.yaml
├── README.md
├── TP04_Report.pdf
├── .gitignore
│
├── data/
│   └── README.md
│
├── web/
│   └── index.html
│
└── screenshots/
```

## 4. Dataset

The project uses an air quality dataset with:

- File size: approximately 5.2 GiB
- Total records: 66,937,826
- Number of columns: 12

The dataset contains measurements such as temperature, humidity, PM2.5, PM10, CO2, NO2, wind speed, traffic level, and air quality index.

**Note:** The dataset is not included in this GitHub repository because of its large size. Place the original file at:

```text
~/Desktop/air_quality_5gb.csv
```

## 5. Build and Run with Docker

Build the Docker image:

```bash
docker build -t dhia8448/tp04-air-quality:latest .
```

Run the application using Docker Compose:

```bash
docker compose up --build
```

Check the container status:

```bash
docker compose ps -a
```

Stop and remove the Compose containers and network:

```bash
docker compose down
```

## 6. Docker Hub

Docker Hub image:

[dhia8448/tp04-air-quality](https://hub.docker.com/r/dhia8448/tp04-air-quality)

Pull the image:

```bash
docker pull dhia8448/tp04-air-quality:latest
```

## 7. Container Networking

Three containers were created using the Docker image and connected to a custom bridge network named `tp04-network`.

The services were exposed through these ports:

| Container | Host Port | Container Port |
|---|---:|---:|
| tp04-container-1 | 8081 | 80 |
| tp04-container-2 | 8082 | 80 |
| tp04-container-3 | 8083 | 80 |

Open the web page using:

- http://localhost:8081
- http://localhost:8082
- http://localhost:8083

## 8. Analysis Results

The application successfully processed the complete dataset.

| Metric | Result |
|---|---:|
| Total records | 66,937,826 |
| Average temperature | 22.00 °C |
| Average air quality index | 18.22 |

### Records by District

| District | Records |
|---|---:|
| Industrial | 13,387,565 |
| Centre | 11,900,058 |
| North | 11,528,184 |
| South | 10,784,428 |
| West | 10,412,549 |
| East | 8,925,042 |

## 9. Screenshots

The `screenshots/` directory is reserved for execution screenshots.

## 10. Author

Big Data TP04 - Docker Containerization and Deployment.
