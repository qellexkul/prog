from typing import Union, List

from vkbottle.dispatch.rules import ABCRule
from vkbottle.bot import Message


class teacher(ABCRule[Message]):

	def __init__(self, user_ids: Union[List[int], int]):
		if not isinstance(user_ids, list):
			user_ids = [user_ids]
		self.uids = user_ids

	async def che(self, event: Message) -> bool: 
		return event.from_id in self.uids