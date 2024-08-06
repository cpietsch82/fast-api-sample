from fastapi import APIRouter, Depends, HTTPException

from ..dependencies import get_token_header

router = APIRouter(
  prefix="/todos",
  tags=["todos"],
  # dependencies=[Depends(get_token_header)],
  responses={404: {"description": "Not found"}},
)

# fake_todos_db = {"plumbus": {"name": "Plumbus"}, "gun": {"name": "Portal Gun"}}
fake_todos_db = { "0": { "todo": "Lebenslauf aktualisieren", "done": "false"  }, "1": { "todo": "Salat einkaufen", "done": "false" } }

@router.get("/")
async def read_todos():
  return fake_todos_db

@router.get("/{todo_id}")
async def read_todo(todo_id: str):
  if todo_id not in fake_todos_db:
    raise HTTPException(status_code=404, detail="Todo not found")
  return {"todo": fake_todos_db[todo_id]["todo"], "todo_id": todo_id}

@router.put(
  "/{todo_id}",
  tags=["custom"],
  responses={403: {"description": "Operation forbidden"}},
)
async def update_todo(todo_id: str):
  if todo_id != "1":
    raise HTTPException(
      status_code=403, detail="You can only update the item: 1"
    )
  return {"todo_id": todo_id, "todo": "The great Todo" }