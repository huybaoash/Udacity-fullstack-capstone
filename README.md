# App Capstone Backend

    This is final project for Udacity's FullStack Web Developer Nanodegree. Web app can be accessed at URL: https://udacity-fullstack-capstone-1.onrender.com/

## Installation instructions

    Run `pip install -r requirements.txt` to install project dependencies
    Change infomation in `.env`
    Type `python app.py` to run project

## Roles

    Supporter
        GET /characters and /scenes
    Manager
        GET /characters and /scenes
        ADD /characters and DELETE /characters
        PATCH /characters and /scenes
    Producer
        GET /characters and /scenes
        ADD /characters and DELETE /characters
        PATCH /characters and /scenes
        ADD /scenes and DELETE /scenes

## JWT Token for each role

    Supporter:
        eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Il96SFJDQmh2YUJNRXBweURLQlVubSJ9.eyJpc3MiOiJodHRwczovL2Rldi1reXU1YWdoemlkNTZldnIxLnVzLmF1dGgwLmNvbS8iLCJzdWIiOiJnb29nbGUtb2F1dGgyfDEwNTg3NDM4NDE4NTA3OTk1MzQ0NyIsImF1ZCI6ImNhcHN0b25lLXVkYWNpdHkiLCJpYXQiOjE3MjIwMTA1MzgsImV4cCI6MTgyMjAxNzczOCwic2NvcGUiOiIiLCJhenAiOiI5dGtpRjZtaG95QU51TTdmb2RwVTRUQ0hnVTR5OVdjeSIsInBlcm1pc3Npb25zIjpbInZpZXc6Y2hhcmFjdGVycyIsInZpZXc6c2NlbmVzIl19.eKqdAGtvzAq1-L1k_DkM3RrOJblprpkOpjiCfkZAUmynbXT2hivJb0SUJXHZpuRUIN4PXejLCajvc4zc4EwbIcTgdMpm3tiGu06SGEhnq578AL7RmFZcQC8Q2uIDVsFTqmU1mVfV8zcfjhYNJwsOPpYAmHYvo_9RPudzoId1KDBwftE0Id2iXNkBtFrR0zNviSr2WWaIA1Balsi71njZzDbYu5DuQ_nEuwmnnpTashx5QR7hFsMFSz2K3ha-pWfOagr2bXmMxx2Md_Md900acg1GCLA732f5cWV-g75ucYGmHohqNjDfC1pitXTpkMR2xubHhzl_vLXbot7E4jJA8Q

    Manager:
        eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Il96SFJDQmh2YUJNRXBweURLQlVubSJ9.eyJpc3MiOiJodHRwczovL2Rldi1reXU1YWdoemlkNTZldnIxLnVzLmF1dGgwLmNvbS8iLCJzdWIiOiJnb29nbGUtb2F1dGgyfDEwMzk1NDA1MTI1NjE4MjYxNDkzNSIsImF1ZCI6ImNhcHN0b25lLXVkYWNpdHkiLCJpYXQiOjE3MjIwMTEzNzcsImV4cCI6MTgyMjAxODU3Nywic2NvcGUiOiIiLCJhenAiOiI5dGtpRjZtaG95QU51TTdmb2RwVTRUQ0hnVTR5OVdjeSIsInBlcm1pc3Npb25zIjpbImFkZDpjaGFyYWN0ZXJzIiwiZGVsZXRlOmNoYXJhY3RlcnMiLCJ1cGRhdGU6Y2hhcmFjdGVycyIsInVwZGF0ZTpzY2VuZXMiLCJ2aWV3OmNoYXJhY3RlcnMiLCJ2aWV3OnNjZW5lcyJdfQ.QNs6TAm5sjhDZYRuzCRNVIkM1dF8gyajB7WyPW4Yvdb17d1S5Vwes29s5HWubYKmbqerTjwEI8Wqo9PLd21OS6w9Jt5onmv3l4I_SZ--D3UfGWrbgyBYL_9amrdyHQ9SrTu53rGJZUm74KGYpD-lNSRpVSFpHg5Im0uhdKn3mdQ0s0AyNgWPWjmk1DJTF7dj5Zr2KXFzBxwahMuuDTqXJR8jlzdytRSEM8H7RhU2-R69rI27IIAyTSJv2DglOHiavWhjounud-Cml8gI-m8x5deZhdxlctJs0OlylG9pDSHJJJfMlDO1nBLfem4QdZaCXZdWLVj6lsR_Yiam6Lvw7A
    Producer:
        eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Il96SFJDQmh2YUJNRXBweURLQlVubSJ9.eyJpc3MiOiJodHRwczovL2Rldi1reXU1YWdoemlkNTZldnIxLnVzLmF1dGgwLmNvbS8iLCJzdWIiOiJnb29nbGUtb2F1dGgyfDEwNTM4MTAzMzQ4MDc4MzE0NjQ3MiIsImF1ZCI6ImNhcHN0b25lLXVkYWNpdHkiLCJpYXQiOjE3MjIwMTE2MjEsImV4cCI6MTgyMjAxODgyMSwic2NvcGUiOiIiLCJhenAiOiI5dGtpRjZtaG95QU51TTdmb2RwVTRUQ0hnVTR5OVdjeSIsInBlcm1pc3Npb25zIjpbImFkZDpjaGFyYWN0ZXJzIiwiYWRkOnNjZW5lcyIsImRlbGV0ZTpjaGFyYWN0ZXJzIiwiZGVsZXRlOnNjZW5lcyIsInVwZGF0ZTpjaGFyYWN0ZXJzIiwidXBkYXRlOnNjZW5lcyIsInZpZXc6Y2hhcmFjdGVycyIsInZpZXc6c2NlbmVzIl19.m5w4iDQschRfY6xXTMXq49CYG--XcKAaUO0ERTm_2w-k8LswuIWe0WeYB9o1fLmVE31J3TDKtwv-ciT7DhMs-3tmQ5hZgUfAMtrMse9MlBScO3yIrSphcmk5VSTgFQbK1neJE9ar3JGE9SVVjwSHgfmq60eSc76hxoTGrFntv6OjyeEgpBbEpdLJxIDm9fipSQmCTImkh3d0NKA-IlYn2GcdM4mJ6ny7-Gc51lUCZ7cQP8Ow3q4I4Q5qKASBPK-2-ebYBk9ZFar-u3YB7sE7cxwQmjlEuE5fube_-lNONnYMjo445E_aRLgxUx5_cdVHWosofVx6p2Qq9akbILaQ_Q

## API Endpoints

    ### GET Enpoints
        #### GET /scenes : Displays all scenes.
        Sample response:
            {
                "message": "Get scenes successfully",
                "scenes": [
                    {
                    "id": 1,
                    "duration": 123,
                    "title": "update scene"
                    }
                ],
                "status": true
            }

        #### GET /characters: Displays all characters.
        Sample response:
            {
                "characters": [
                    {
                        "role": "antagonist",
                        "id": 4,
                        "scene_id": 1,
                        "name": "character name"
                    },
                ],
                "message": "Get characters successfully",
                "status": true
            }

    ### POST Enpoints
        #### POST /scenes/add: Creates a new scene
        Sample response:
            {
                "message": "Add scene successfully",
                "scene": {
                    "id": 3,
                    "duration": 231,
                    "title": "add scene"
                },
                "status": true
            }

        #### POST /characters/add: Creates a new character
        Sample response:
            {
                "character": {
                    "role": "antagonist",
                    "id": 5,
                    "scene_id": 1,
                    "name": "character name"
                },
                "message": "Add character successfully",
                "status": true
            }

    ### PATCH Enpoints
        #### PATCH /scenes/<scene_id>/update : Updates scene information given a scene_id and newly updated attribute info.
        Sample response:
            {
                "message": "Update scene successfully",
                "scene": {
                    "id": 1,
                    "duration": 444,
                    "title": "update scene"
                },
                "status": true
            }

        #### PATCH /characters/<character_id>/update : Updates character information given a character_id and newly updated attribute info.
        Sample response:
            {
                "character": {
                    "role": "protagonist",
                    "id": 3,
                    "scene_id": 1,
                    "name": "update character"
                },
                "message": "Update character successfully",
                "status": true
            }

    ### DELETE Enpoints
        #### DELETE /scenes/<scene_id>/delete : Delete a scene entry from the database given the inputted scene_id.
        Sample response:
            {
                "character_id": 3,
                "message": "Delete character successfully",
                "status": true
            }

        #### DELETE /characters/<character_id>/delete : Delete an character / actress entry from the database given the inputted character_id.
        Sample response:
            {
                "message": "Delete scene successfully",
                "scene_id": 3,
                "status": true
            }
