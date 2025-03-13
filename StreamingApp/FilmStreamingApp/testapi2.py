import requests
from googletrans import Translator
import asyncio
import json

async def detect_languages(text2detect):
	async with Translator() as translator:
		result = await translator.detect(text2detect)
		return result

async def translate_bulk(text2translate, langdest):
	async with Translator() as translator:
		translations = await translator.translate(text2translate, dest=langdest)
		print("+++++++++++++")
		print(translations)
		print("+++++++++++++")
		return translations

if __name__ == "__main__":
	url = "https://ai-movie-recommendations-reviews-suggestions-api.p.rapidapi.com/analyzeSimilarMovies"

	querystring = {"noqueue":"1"}

	payload = {
		"movieTitle": "Inception",
		"lang": "en"
	}
	headers = {
		"x-rapidapi-key": "168ee365b5msh4550dec97d31326p182ac1jsned0ed58cfcf0",
		"x-rapidapi-host": "ai-movie-recommendations-reviews-suggestions-api.p.rapidapi.com",
		"Content-Type": "application/json"
	}

	response = requests.post(url, json=payload, headers=headers, params=querystring).json()

	print(response)

	# Serializing json
	json_object = json.dumps(response, indent=4)

	# Writing to sample.json
	with open("sample.json", "w") as outfile:
		outfile.write(json_object)
	##########

	print(response['result']['movieAnalysis']['analysis']['style'])


	ssq = asyncio.run(detect_languages(response['result']['movieAnalysis']['analysis']['style']))
	print("******************")
	print(ssq.lang)
	print("******************")
	tt = asyncio.run(translate_bulk(response['result']['movieAnalysis']['analysis']['style'],'it'))
	print(tt.dest)
	print(ss)