from service.user_service import register_user, get_user
from sanic.response import text
from sanic_openapi import doc
from util.generic_except import get_response_error
from sanic.exceptions import ServerError
from marshmallow.exceptions import ValidationError
from sanic import response
import json


@doc.summary("Post new User.")
@doc.consumes(doc.String(name="body"), location="body")
async def route_post_user(req):
    try:
        return response.json(await register_user(req))
    except ServerError as se:
        return get_response_error("user.post.generic.error",se)
    except ValidationError as ve:
        return get_response_error("user.post.validation.error",ve)

@doc.summary("Fetch user by ID")
async def route_get_user(req, user_id):
    try:
        user = await get_user(user_id)
        return response.json(text(user))
    except ServerError as se:
        return get_response_error("user.get.generic.error",se)