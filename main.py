from fastapi import FastAPI
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from typing import List, Any
import os
import re

app = FastAPI(title="VIT BFHL API", version="1.0.0")

ALPHA_RE = re.compile(r"^[A-Za-z]+$")
DIGIT_RE = re.compile(r"^[+-]?\d+$")


def build_user_id(full_name: str, dob_ddmmyyyy: str) -> str:
    name = " ".join(full_name.strip().split()).lower().replace(" ", "_")
    return f"{name}_{dob_ddmmyyyy}"


def alternating_caps_reversed(s: List[str]) -> str:
    chars: List[str] = []
    for token in s:
        if isinstance(token, str):
            for ch in token:
                if ch.isalpha():
                    chars.append(ch)
        else:
            for ch in str(token):
                if ch.isalpha():
                    chars.append(ch)
    chars.reverse()
    out_chars: List[str] = []
    for i, ch in enumerate(chars):
        if i % 2 == 0:
            out_chars.append(ch.upper())
        else:
            out_chars.append(ch.lower())
    return "".join(out_chars)


def is_int_string(token: str) -> bool:
    return bool(DIGIT_RE.match(token))


class InputModel(BaseModel):
    data: List[Any]


@app.post("/bfhl")
async def bfhl_endpoint(payload: InputModel):
    try:
        full_name = os.getenv("FULL_NAME", "Akshita Gupta")
        dob = os.getenv("DOB_DDMMYYYY", "31012004")
        email = os.getenv("EMAIL", "akshita31012004@gmail.com")
        roll = os.getenv("ROLL_NUMBER", "22BCE0248")

        user_id = build_user_id(full_name, dob)

        original_items = payload.data

        odd_numbers: List[str] = []
        even_numbers: List[str] = []
        alphabets: List[str] = []
        special_characters: List[str] = []
        total_sum = 0

        for item in original_items:
            token = str(item)
            if is_int_string(token):
                val = int(token)
                if val % 2 == 0:
                    even_numbers.append(token)
                else:
                    odd_numbers.append(token)
                total_sum += val
            elif ALPHA_RE.match(token):
                alphabets.append(token.upper())
            else:
                if any(not ch.isalnum() for ch in token):
                    special_characters.append(token)
                else:
                    special_characters.append(token)

        concat_string = alternating_caps_reversed([str(x) for x in original_items])

        resp = {
            "is_success": True,
            "user_id": user_id,
            "email": email,
            "roll_number": roll,
            "odd_numbers": odd_numbers,
            "even_numbers": even_numbers,
            "alphabets": alphabets,
            "special_characters": special_characters,
            "sum": str(total_sum),
            "concat_string": concat_string,
        }
        return JSONResponse(status_code=200, content=resp)

    except Exception as e:
        resp = {
            "is_success": False,
            "user_id": build_user_id(os.getenv("FULL_NAME", "John Doe"), os.getenv("DOB_DDMMYYYY", "17091999")),
            "email": os.getenv("EMAIL", "john@xyz.com"),
            "roll_number": os.getenv("ROLL_NUMBER", "ABCD123"),
            "odd_numbers": [],
            "even_numbers": [],
            "alphabets": [],
            "special_characters": [],
            "sum": "0",
            "concat_string": "",
            "error": str(e),
        }
        return JSONResponse(status_code=200, content=resp)


@app.get("/")
async def root():
    return {"status": "ok", "info": "Use POST /bfhl with body {\"data\": [...]}"}

