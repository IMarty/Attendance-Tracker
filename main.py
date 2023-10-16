# Import du framework
from fastapi import FastAPI

# Documentation
from documentations.description import api_description
from documentations.tags import tags_metadata

# Routers
import routers.router_students
import routers.router_attendances
import routers.router_sessions
import routers.router_auth

# Initialisation de l'API
app = FastAPI(
    title="Attendance Tracker",
    description=api_description,
    openapi_tags=tags_metadata
)

# Router dédié aux Students
app.include_router(routers.router_students.router)
app.include_router(routers.router_sessions.router)
app.include_router(routers.router_attendances.router)
app.include_router(routers.router_auth.router)
