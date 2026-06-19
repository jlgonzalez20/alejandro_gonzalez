# Air Quality Monitoring with DIY Sensors

## Overview

This project investigates air quality differences between two urban areas in Panama City, **Cerro Viento** and **Río Abajo**, using a low-cost DIY air quality monitoring system. The main objective was to measure and compare **PM2.5 concentrations** and evaluate how factors such as traffic density influence local air pollution levels.

A custom monitoring solution was built using an **SDS011 particulate matter sensor** connected to a computer. A **Python script** was developed to collect, validate, store, and visualize air quality measurements in real time. The collected data was then processed and analyzed using **Power BI**, where dashboards and visualizations were created to compare pollution levels between locations.

## Technologies Used

- **Python 3**
  - Data acquisition from the SDS011 sensor
  - Real-time monitoring and visualization
  - Data logging and storage
- **Power BI**
  - Data transformation and analysis
  - Interactive dashboards and reporting
  - Comparative visualization of air quality metrics
- **SDS011 Air Quality Sensor**
  - Measurement of PM2.5 and PM10 particulate matter concentrations
- **Visual Studio Code**
  - Development environment

## Features

- Real-time air quality monitoring
- PM2.5 and PM10 data collection
- Automatic timestamped data logging
- Sensor packet validation through checksum verification
- Live visualization using Matplotlib
- Power BI dashboards for analysis and reporting
- Comparison of air quality across different urban locations

## Hardware

- SDS011 Laser Dust Sensor
- Laptop or Desktop Computer

## Software Stack

- Python
- PySerial
- Matplotlib
- Power BI Desktop
- Visual Studio Code

## Methodology

1. Connect the SDS011 sensor to a computer.
2. Run the Python script to collect PM2.5 and PM10 measurements.
3. Store the collected data in text files with timestamps.
4. Process and clean the data.
5. Import the dataset into Power BI.
6. Create dashboards and visualizations to compare air quality between locations.

## Results

The project collected thousands of air quality measurements from both study sites.

| Location | Average PM2.5 (µg/m³) |
|-----------|----------------------|
| Cerro Viento | 0.82 |
| Río Abajo | 4.51 |

The analysis revealed significantly higher PM2.5 concentrations in Río Abajo, suggesting that factors such as higher traffic density and urban activity contribute to poorer air quality compared to Cerro Viento.

## Future Improvements

- Deploy multiple sensors simultaneously.
- Extend data collection periods.
- Incorporate weather variables such as temperature, humidity, and wind speed.
- Enable cloud-based data storage and real-time dashboards.
- Expand monitoring to additional neighborhoods.

## Authors

- Daniel Arosemena
- Alejandro González
- Sara Peláez
- Roberts Jesua
- Carlos Salinas

## Keywords

Air Quality Monitoring, SDS011, PM2.5, PM10, Python, Power BI, Environmental Data Analysis, Citizen Science, IoT, Urban Pollution.
