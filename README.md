# Overview

This is a stock screener app (taken from this youtube series https://www.youtube.com/watch?v=5GorMC2lPpk ) which was put together to learn about:

1.  FastAPI - https://fastapi.tiangolo.com/
2.  Docker - https://www.docker.com/
3.  Docker Compose - https://docs.docker.com/compose/

The idea was to take the API produced by following the above youtube series but to dockerize the application and the dataabse.

The use case is just a nice use case for CRUD operations but not a main part of the project - the idea is to add stock symbols to the database from a POST request, then grab some details fron yahoo finance to update the database with extra data. A GET request should list all the symbols in the database.

Next steps:

1.  Improve the business logic behind the API calls too be more inlice with clean architecture https://blog.cleancoder.com/uncle-bob/2012/08/13/the-clean-architecture.html 
2.  Implement react front end.
3.  Once front end is implemented, add service workers to allow extra long running tasks.