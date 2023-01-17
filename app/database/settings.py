from tortoise import Tortoise

from app.constants import DATABASE_URL

TORTOISE_MODELS_LIST = ['app.database.models', 'aerich.models']
TORTOISE_ORM = {
    'connections': {'default': DATABASE_URL},
    'apps': {
        'models': {
            'models': ['app.database.models', 'aerich.models'],
            'default_connection': 'default',
        },
    },
}


async def init_db(app, generate_schemas=True):
    await Tortoise.init(
        db_url=DATABASE_URL,
        modules={'models': TORTOISE_MODELS_LIST},
    )
    if generate_schemas:
        await Tortoise.generate_schemas()
