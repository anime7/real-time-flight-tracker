# Real-Time Flight Tracker Dashboard

## Overview
This project demonstrates an end-to-end data engineering pipeline that processes live aircraft positioning data from the OpenSky Network API. The system ingests real-time flight data, enriches it with additional metrics, stores the results in a PostgreSQL database, and visualizes insights through an interactive Tableau Public dashboard.

## Features
- Real-time flight data ingestion from the OpenSky Network API
- Automated data processing and enrichment pipeline
- PostgreSQL database for structured data storage
- Interactive Tableau dashboard with flight metrics and map visualization
- CI/CD automation with GitHub Actions
- Comprehensive logging and monitoring

## Architecture
The pipeline consists of the following components:

1. **Data Source:** OpenSky Network API providing real-time aircraft positioning data
2. **Ingestion Layer:** Python-based polling mechanism orchestrated by Prefect
3. **Storage Layer:** Raw data stored as Parquet files; processed data stored in PostgreSQL
4. **Transformation Layer:** Data cleaning, transformation, and feature engineering
5. **Visualization Layer:** Tableau Public dashboard displaying flight metrics and geographic visualizations
6. **DevOps Layer:** CI/CD automation using GitHub Actions

## Tech Stack
- **Programming Language:** Python 3.9+
- **Orchestration:** Prefect 2.0
- **Data Processing:** Pandas, NumPy
- **Storage:** PostgreSQL, Parquet
- **Visualization:** Tableau Public
- **CI/CD:** GitHub Actions
- **Testing:** Pytest

## Setup

### Prerequisites
- Python 3.9+
- PostgreSQL
- OpenSky Network account
- Tableau Public account

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/anime7/real-time-flight-tracker.git
   cd real-time-flight-tracker
   ```

2. **Create and activate a virtual environment:**
   ```bash
   # Create the environment
   python -m venv venv

   # Activate the environment
   # Windows:
   venv\Scripts\activate
   # macOS/Linux:
   source venv/bin/activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure environment variables:**
   ```bash
   # Copy the example environment file
   cp .env.example .env
   ```
   Now, edit the `.env` file with your specific configurations (API keys, database credentials, etc.).

   **Note:** Ensure `.env` is listed in your `.gitignore` file to avoid committing sensitive information.

5. **Set up the database:**
   ```bash
   python -m database.setup
   ```

## Running the Pipeline

1. **Start the ingestion process:**
   ```bash
   python -m ingestion.main
   ```

2. **Run the transformation pipeline:**
   ```bash
   python -m transform.main
   ```

3. **Access the Tableau dashboard:**
   [Insert your Tableau Public Dashboard Link here when available]

## Project Structure
```
real-time-flight-tracker/
├── ingestion/        # Data ingestion from OpenSky API
├── transform/        # Data cleaning and feature engineering
├── database/         # Database models and operations
├── dashboard/        # Dashboard configuration and queries
├── config/           # Configuration files and environment handling
├── utils/            # Utility functions and logging
├── tests/            # Unit and integration tests
└── .github/          # GitHub Actions workflows
```

## Contributing
Contributions are welcome! Feel free to submit a Pull Request or open an issue.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments
- OpenSky Network for providing the API
- [List any additional acknowledgments here]
