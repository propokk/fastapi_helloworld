from starlette.routing import Route

async def home():
	return {"status": "Working"}

routes = [
	Route("/", endpoint=home)
]