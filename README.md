# App Capstone Backend

    This is final project for Udacity's FullStack Web Developer Nanodegree. Web app can be accessed at URL: https://udacity-fullstack-capstone-1.onrender.com/

## Installation instructions

    Run `pip install -r requirements.txt` to install project dependencies
    Change infomation in `.env`
    Type `python app.py` to run project

## Roles

    Casting Assistant
        GET /actors and /movies
    Casting Director
        GET /actors and /movies
        ADD /actors and DELETE /actors
        PATCH /actors and /movies
    Executive Producer
        GET /actors and /movies
        ADD /actors and DELETE /actors
        PATCH /actors and /movies
        ADD /movies and DELETE /movies

## JWT Token for each role

    Casting Assistant:
        eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Il96SFJDQmh2YUJNRXBweURLQlVubSJ9.eyJpc3MiOiJodHRwczovL2Rldi1reXU1YWdoemlkNTZldnIxLnVzLmF1dGgwLmNvbS8iLCJzdWIiOiJnb29nbGUtb2F1dGgyfDEwNTg3NDM4NDE4NTA3OTk1MzQ0NyIsImF1ZCI6ImNhcHN0b25lLXVkYWNpdHkiLCJpYXQiOjE3MjIwMjM3MTQsImV4cCI6MTcyMjAzMDkxNCwic2NvcGUiOiIiLCJhenAiOiI5dGtpRjZtaG95QU51TTdmb2RwVTRUQ0hnVTR5OVdjeSIsInBlcm1pc3Npb25zIjpbInZpZXc6YWN0b3JzIiwidmlldzptb3ZpZXMiXX0.gFZhgd4_8__J9F_RjnQJUB1bA3scITNPR6wA0lH31_AaUe_rfvJvyqa5c3eH1cL5VtXOSApbXrJJm3qAx2gOnP9BvdOY9Cp8pwnCoCxs63nvjyyD2ds6HrYGyrhs7fdWuHysZjf_e7jwSxN8pjdDRVALlZ0k6mVpsqe9gsNMt0RiudMhCrMKCrDFGCyFhC2DH5ofqcc7zHrCIrpXgSJ5CtVC9qV0qgSL6P4HgaW6eUlqeh1eZatKtn_rMbPCbkC9fxqw6d1LRfHuo-FPM7GJmRlOrf4K0o7U6Aj_hDtCCIB4vv2zlF-8JQ_5BoQe_tZtTyoOv7s9x4VhxzV2BuMUZA

    Casting Director:
        eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Il96SFJDQmh2YUJNRXBweURLQlVubSJ9.eyJpc3MiOiJodHRwczovL2Rldi1reXU1YWdoemlkNTZldnIxLnVzLmF1dGgwLmNvbS8iLCJzdWIiOiJnb29nbGUtb2F1dGgyfDEwMzk1NDA1MTI1NjE4MjYxNDkzNSIsImF1ZCI6ImNhcHN0b25lLXVkYWNpdHkiLCJpYXQiOjE3MjIwMjM3ODYsImV4cCI6MTcyMjAzMDk4Niwic2NvcGUiOiIiLCJhenAiOiI5dGtpRjZtaG95QU51TTdmb2RwVTRUQ0hnVTR5OVdjeSIsInBlcm1pc3Npb25zIjpbXX0.ZfjfKLDEip7Z33WzuRJPgwhROrRdfs14-3RppWm700lkc9km-sucJrVmmrp_Io3sKIYoci5xUc89enusbJ2nBYsqTOlR5VmbrRk84JGQ6dYjNjxOLn1r-TQxUHXWGRjpSJdZpOh1JFCcBaSC_xUysE-k8Gh4G0VA4yzpj8ijo2cCRa6j8RnmihgC16dabwR3J6Tq6IvBtc_c8eVtcq38Klrs0nz_A8turQ4cZuGnewNTJycKljzYTkiJg6hFT7Q7FleaxpD2hCub9tQ2pmqdUNb1zMNm1vkCDGnlOBweBNqAGTwXdnDx-VW30H65GaX-_I7fdi9msB1pz4zKIU_hZg
    Executive Producer:
        eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Il96SFJDQmh2YUJNRXBweURLQlVubSJ9.eyJpc3MiOiJodHRwczovL2Rldi1reXU1YWdoemlkNTZldnIxLnVzLmF1dGgwLmNvbS8iLCJzdWIiOiJnb29nbGUtb2F1dGgyfDEwNTM4MTAzMzQ4MDc4MzE0NjQ3MiIsImF1ZCI6ImNhcHN0b25lLXVkYWNpdHkiLCJpYXQiOjE3MjIwMjQyNzksImV4cCI6MTcyMjAzMTQ3OSwic2NvcGUiOiIiLCJhenAiOiI5dGtpRjZtaG95QU51TTdmb2RwVTRUQ0hnVTR5OVdjeSIsInBlcm1pc3Npb25zIjpbImFkZDphY3RvcnMiLCJhZGQ6bW92aWVzIiwiZGVsZXRlOmFjdG9ycyIsImRlbGV0ZTptb3ZpZXMiLCJ1cGRhdGU6YWN0b3JzIiwidXBkYXRlOm1vdmllcyIsInZpZXc6YWN0b3JzIiwidmlldzptb3ZpZXMiXX0.dTpBjqoUsn_88DOSzhL50WwWvt0wanVs1JiWVnWCI1aJ0eD_s2JkGSYkIu5l8WbBf9Jm1NUrXkHdZFU-LFZxUjlhLE1IOY3M9NeOXt476nt_VRAmgt-ublPKnV4qEek7rNQdIjKu1Dt7AmNEGRt5ANJs5MVOQkkhFXJ__BHPDhCntDTEt8lbX4QvQChgG2uM90xOYQDqYyJYLnHx9pMS8Vovd6FGMd4cvz19xqcy4GIBiy4pTxy-lg8Odvrw9Hpv5p1asfFoyDDJHFmTlSN4sUcQqg9r26p_NlxnCkecBL8EJtdSGT1OQtQQdwopyJw5_6ZuEJrC49ShO3pWMOOxZw

## API Endpoints

    ### GET Enpoints
        #### GET /movies : Displays all movies.
        Sample response:
            {
                "message": "Get movies successfully",
                "movies": [
                    {
                    "id": 1,
                    "duration": 123,
                    "title": "update movie"
                    }
                ],
                "status": true
            }

        #### GET /actors: Displays all actors.
        Sample response:
            {
                "actors": [
                    {
                        "role": "antagonist",
                        "id": 4,
                        "movie_id": 1,
                        "name": "actor name"
                    },
                ],
                "message": "Get actors successfully",
                "status": true
            }

    ### POST Enpoints
        #### POST /movies/add: Creates a new movie
        Sample response:
            {
                "message": "Add movie successfully",
                "movie": {
                    "id": 3,
                    "duration": 231,
                    "title": "add movie"
                },
                "status": true
            }

        #### POST /actors/add: Creates a new actor
        Sample response:
            {
                "actor": {
                    "role": "antagonist",
                    "id": 5,
                    "movie_id": 1,
                    "name": "actor name"
                },
                "message": "Add actor successfully",
                "status": true
            }

    ### PATCH Enpoints
        #### PATCH /movies/<movie_id>/update : Updates movie information given a movie_id and newly updated attribute info.
        Sample response:
            {
                "message": "Update movie successfully",
                "movie": {
                    "id": 1,
                    "duration": 444,
                    "title": "update movie"
                },
                "status": true
            }

        #### PATCH /actors/<actor_id>/update : Updates actor information given a actor_id and newly updated attribute info.
        Sample response:
            {
                "actor": {
                    "role": "protagonist",
                    "id": 3,
                    "movie_id": 1,
                    "name": "update actor"
                },
                "message": "Update actor successfully",
                "status": true
            }

    ### DELETE Enpoints
        #### DELETE /movies/<movie_id>/delete : Delete a movie entry from the database given the inputted movie_id.
        Sample response:
            {
                "actor_id": 3,
                "message": "Delete actor successfully",
                "status": true
            }

        #### DELETE /actors/<actor_id>/delete : Delete an actor / actress entry from the database given the inputted actor_id.
        Sample response:
            {
                "message": "Delete movie successfully",
                "movie_id": 3,
                "status": true
            }
