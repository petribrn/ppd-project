#!/bin/bash

docker compose down

docker compose --env-file .env --compatibility up
