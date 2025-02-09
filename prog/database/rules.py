from prog.database.models import Rules
from psycopg import AsyncConnection

class RulesRepository():
    def __init__(self, conn: AsyncConnection):
        self._conn = conn

    async def create(self,name: str, functional: str):
        async with self._conn.cursor() as cursor:
            try:
                await cursor.execute("""
                    INSERT INTO Rules (name, functional)
                    VALUES (%s, %s)
                """, (name, functional))
                await self._conn.commit()
            except Exception as e:
                await self._conn.rollback()
                raise e

    async def get_id(self, id_rule: int) -> Rules | None:
        async with self._conn.cursor() as cursor:
            await cursor.execute("""
                SELECT *
                FROM Rules
                WHERE id_rule = %s
            """, (id_rule,))
            result = await cursor.fetchone()
            if result is None:
                return None
            return Rules(
                id_rule=result[0], name=result[1], functional=result[2]
            )

    # async def get_name(self, name: str) -> Rules | None:
    #     async with self._conn.cursor() as cursor:
    #         await cursor.execute("""
    #             SELECT *
    #             FROM Rules
    #             WHERE name = %s
    #         """, (name))
    #         result = await cursor.fetchone()
    #         if result is None:
    #             return None
    #         return Rules(
    #             id_rule=result[0], name=result[1], functional=result[2]
    #         )


    async def get_list(self, limit: int, offset: int = 0) -> list[Rules]:
        async with self._conn.cursor() as cursor:
            await cursor.execute("""
                SELECT *
                FROM Rules
                LIMIT %s
                OFFSET %s
            """, (limit, offset))
            result = await cursor.fetchall()
            return [Rules(
                id_rule=row[0], name=row[1], functional=row[2]
            ) for row in result]