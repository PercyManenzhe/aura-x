from fastapi import APIRouter

router = APIRouter()


@router.get("/")
def health_check():

    return {
        "status": "online",
        "platform": "Aura-X",
        "service": "municipal-intelligence"
    }