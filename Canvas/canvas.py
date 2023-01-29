# home.py


import flet as ft
import os


#	app ################################################################
PATH_TO_CANVAS_BG = "modules/Canvas/assets/"


class canvas_app(ft.UserControl):
	def __init__(self):
		super().__init__()
		self.canvas_bg = "albedo_grid.png"

	def build(self):
		readme = fetch_canvas_bg()
		return ft.Container(
				bgcolor = 'transparent',
				content = ft.Stack(
						controls = [
						],
						expand = True,
						scroll = 'auto',
				),
				margin = 4,
				padding = 4,
		)

	def fetch_canvas_bg():
		path = os.path.abspath(PATH_TO_CANVAS_BG)
		full_path = os.path.join(path, self.canvas_bg)




class canvas_settings(ft.UserControl):
	pass


class canvas_management_settings(ft.UserControl):
	pass

