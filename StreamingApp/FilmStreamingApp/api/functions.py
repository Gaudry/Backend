from googletrans import Translator
import asyncio

async def detect_languages(text2detect):
	async with Translator() as translator:
		result = await translator.detect(text2detect)
		return result