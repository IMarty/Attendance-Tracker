# Import du framework
from fastapi import FastAPI

# Documentation
from documentations.description import api_description
from documentations.tags import tags_metadata

#Routers
import routers.router_students
# Initialisation de l'API
app = FastAPI(
    title="Attendance Tracker",
    description=api_description,
    openapi_tags= tags_metadata
)

# Router dédié aux Students
app.include_router(routers.router_students.router)

# Reste à faire 
# X Sortir mon student's router dans un dossier "routers"
# X Rédiger une documentation et l'ajouter à mon app FastAPI()
# X Sortir mes pydantic models dans un dossier classes
# X Ajouter les tags 


# X et description pour chaque endpoing/methods
# -> En ajouter enpoints suivant en fonction de votre projet


