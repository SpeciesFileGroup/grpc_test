from backend import ConnectDB
from visualization import Visualization

def main():
	connection = ConnectDB(number_of_pages = 10000)
	data = connection.get_data()
	print(len(data))

	viz = Visualization(tile_number = 1, tile_width = 100, tile_height = 100, data_list = data)
	viz.visualize_data()

if __name__ == '__main__':
	main()