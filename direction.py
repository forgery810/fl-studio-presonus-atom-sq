import data
import device
import ui

class Directions():

	arrow_status = False
	ud_status = 0
	ud_arrow = (24, 25, 26, 27, 28, 29, 30, 31, 46, 47)

	def __init__(self, event):

		self.ud_result = data.ud_arrow.index(event.data1)
		print(self.ud_result)
		print(Directions.ud_status)
		Directions.up_down(self, event)


	def up_down(self, event):
		
		if self.ud_result < Directions.ud_status:
			ui.up()
			print('up')
			Directions.ud_status = self.ud_result
			event.handled = True

		elif self.ud_result > Directions.ud_status:
			ui.down()
			print('down')
			Directions.ud_status = self.ud_result
			event.handled = True

		else:
			print('else')
			event.handled = True

