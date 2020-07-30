    import asyncio
    import aiohttp 

    class AsyncHTTP:

    	def __init__(self):
    		pass

	    async def post(self, base_uri, headers=None, params):
		    async with aiohttp.ClientSession() as session:
		        async with session.post(base_uri, 
		        headers=headers, params=params) as resp:
		            data = await resp.json()

	    	return data


	    async def get(self, base_uri, headers=None):
		    async with aiohttp.ClientSession() as session:
		        async with session.get(base_uri, 
		        headers=headers, params=params) as resp:
		            data = await resp.json()

	    	return data

