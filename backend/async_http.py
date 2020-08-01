    import asyncio
    import aiohttp 

    class AsyncHTTP:

    	def __init__(self):
    		pass

	    async def post(self, base_uri, headers=None, params):
	    	"""A convenience wrapper for async http POST requests.
	    	Args:
				self: an instance of the AsyncHTTP class
				base_uri: string
				headers: dict: optional
				params: dict
	    	"""
		    async with aiohttp.ClientSession() as session:
		        async with session.post(base_uri, 
		        headers=headers, params=params) as resp:
		            data = await resp.json()

	    	return data


	    async def get(self, base_uri, headers=None):
	    	"""A convenience wrapper for async http GET requests.
	    	Args:
				self: an instance of the AsyncHTTP class
				base_uri: string
				headers: dict: optional
				params: dict
	    	"""
		    async with aiohttp.ClientSession() as session:
		        async with session.get(base_uri, 
		        headers=headers, params=params) as resp:
		            data = await resp.json()

	    	return data

