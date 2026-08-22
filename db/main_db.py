import aiosqlite
from db import queries

path_db = 'db/bot.db'


async def init_db():
    async with aiosqlite.connect(path_db) as conn:
        await conn.execute(queries.create_products_table)
        await conn.execute(queries.create_table_products_detail)
        await conn.commit()
    print('БД подключена!')


async def add_product_db(name_product, price, product_id, photo_id):
    async with aiosqlite.connect(path_db) as conn:
        await conn.execute(queries.insert_product, (name_product, price, product_id, photo_id))
        await conn.commit()


async def add_product_detail_db(product_id, category, description):
    async with aiosqlite.connect(path_db) as conn:
        await conn.execute(queries.insert_product_detail, (description, product_id, category))
        await conn.commit()


async def get_product_db():
    async with aiosqlite.connect(path_db) as conn:
        cursor = await conn.execute(queries.select_product)
        products = await cursor.fetchall()
    return products


async def update_product_db(field, value, product_id):
    if field in ('name_product', "price"):
        table = 'products'
    elif field in ('description', 'category'):
        table = 'products_detail'
    else: 
        return

    query = queries.update_product.format(table=table, field=field)

    async with aiosqlite.connect(path_db) as conn:
        await conn.execute(query, (value, product_id))
        await conn.commit()

async def delete_product_db(product_id):
    async with aiosqlite.connect(path_db) as conn:
        await conn.execute(queries.delete_product, (product_id, ))
        await conn.execute(queries.delete_product_detail, (product_id, ))
        await conn.commit()

import sqlite3
from db import queries 

path_db = 'db/sqlite3.db'


async def init_db():
    conn = sqlite3.connect(database=path_db)
    cursor = conn.cursor()
    cursor.execute(queries.create_products_table)
    cursor.execute(queries.create_table_products_detail)
    print('DB подключена!')
    conn.commit()
    conn.close()


async def add_product_db(name_product, price, product_id):
    conn = sqlite3.connect(path_db)
    cursor = conn.cursor()
    cursor.execute(queries.insert_product, (name_product, price, product_id))
    conn.commit()
    conn.close()


async def add_product_detail_db(product_id, category, description):
    conn = sqlite3.connect(path_db)
    cursor = conn.cursor()
    cursor.execute(queries.insert_product_detail, (description, product_id, category))
    conn.commit()
    conn.close()


async def get_product_db():
    conn = sqlite3.connect(path_db)
    cursor = conn.cursor()
    cursor.execute(queries.select_product)
    products = cursor.fetchall()
    conn.close()
    return products