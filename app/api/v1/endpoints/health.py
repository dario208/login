from fastapi import APIRouter

router = APIRouter()


@router.get("/ping", summary="Health check")
def ping() -> dict[str, str]:
    return {"status": "ok"}
