import plotly.plotly as py
import plotly.offline as py_offline
import plotly.graph_objs as go
import numpy as np

class Visualization(object):
	"""
	API for visualizing tiles
	"""

	def __init__(self, tile_number, tile_height, tile_width. data_list):
		"""
		Parameters:
			tile_number : Tile number in the overall image
			tile_height, tile_width : Tile size
			data_list: List of tuples of the form (page_id, count)
		"""

		if tile_height * tile_width > len(data_list):
			raise ValueError("Too much data to work with")

		self.tile_number = tile_number
		self.tile_height = tile_height
		self.tile_width = tile_width
		self.data_list = data_list

	def visualize_data(self):
		"""
		Creates a tile_height*tile_width heatmap of data_list
		"""

		x = np.arange(self.tile_width)
		y = np.arange(self.tile_height)
		z = np.zeros((self.tile_height, self.tile_width))
		hovertext = []

		counts_list = np.zeros(len(self.data_list))
		files_list = []

		for index, item in enumerate(self.data_list):
			counts_list[index] = item[1]
			files_list.append(item[0])

		counts_list = counts_list.reshape((self.tile_height, self.tile_height))

		for yi, yy in enumerate(y):
			hovertext.append(list())
			for xi, xx in enumerate(x):
				z[xi][yi] = counts_list[xi][yi]
				current_file = files_list[xi + self.tile_width * yi]
				hovertext[-1].append('File name : {}<br />Count: {}'.format())

		trace = go.Heatmap(z = z, x = x, y = y, hoverinfo = 'text', text = hovertext, colorscale = 'Greys')
		data = [trace]
		py_offline.iplot(data, filename = 'tile'+self.tile_number+'.html', auto_open = False)