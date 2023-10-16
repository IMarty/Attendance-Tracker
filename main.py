# Import du framework
from fastapi import FastAPI

# Documentation
from documentations.description import api_description
from documentations.tags import tags_metadata

#Routers
import routers.router_students, routers.router_attendances, routers.router_sessions





# Initialisation de l'API
app = FastAPI(
    title="Attendance Tracker",
    description=api_description,
    openapi_tags= tags_metadata
)

# Mise en place de l'authentification par Firebase

# Router dédié aux Students
app.include_router(routers.router_students.router)
app.include_router(routers.router_sessions.router)
app.include_router(routers.router_attendances.router)
