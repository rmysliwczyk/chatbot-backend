from typing import Annotated, Sequence

from fastapi import APIRouter, Depends, HTTPException, Query
from ollama import ChatResponse, Message, chat, create
from sqlmodel import select

from app.dependencies import SessionDep, get_current_active_user
from app.models import User

router = APIRouter(prefix="/chat", tags=["chat"])


@router.post(
    "/",
    dependencies=[Depends(get_current_active_user)],
)
def send_message(
    session: SessionDep,
    messages: Sequence[Message],
    current_user: Annotated[User, Depends(get_current_active_user)],
) -> ChatResponse:
    user = session.get(User, current_user.id)
    if user is None:
        raise HTTPException(404, "User not found")
    if user.subscription_active == False:
        raise HTTPException(401, "User doesn't have valid subscription for chat!")

    create(model="t530_model", from_="gemma3:1b", system="You're a homelab server. Your name is t530. Your owner is Rafal Mysliwczyk, and you are used for experimenting with serving different services")

    response = chat(model="t530_model", messages=messages)

    user.number_of_messages = user.number_of_messages + 1
    session.add(user)
    session.commit()
    session.refresh(user)

    return response
