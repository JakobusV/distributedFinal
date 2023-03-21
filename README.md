## Final Project for CSC380 "Distributed Systems"

### About this project

In the last two weeks of class CSC380 at <a href="https://neumont.edu/">Neumont</a>. All students are required to build a project that includes:

An API (RMM level 3 compliant), Database (minimum of 2 resources), Event Stream (Producer and Consumer), Data scraper, Data visualization, and Load balancer

This project is the final result of that assignment! For the topic of my resources and API I came up with the idea of a music manager. For the sake of simplicity, the project consists of creating playlists. CRUD can be preformed on music and playlist objects.

### Technologies
- Python (Main language)
    - <a href="https://docs.pydantic.dev/">Pydantic</a>
    - <a href="https://www.sqlalchemy.org/">SQLAlchemy</a>
    - <a href="https://fastapi.tiangolo.com/">FastAPI</a>
- PostgreSQL (SQL database)
- Kafka (Event stream)
- Prometheus (Data scrape and visualization)
- Nginx (Load balancer)
