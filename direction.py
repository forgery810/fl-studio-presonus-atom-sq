import data
import device
import ui
import modes

class Directions():

	arrow_status = False
	ud_status = 0
	ud_arrow = (24, 25, 26, 27, 28, 29, 30, 31, 46, 47)

	def __init__(self, event):

		self.ud_result = self.ud_arrow.index(event.data1)
		print(self.ud_result)
		print(Directions.ud_status)
		Directions.up_down(self, event)

	def up_down(self, event):

		if event.data1 == 47 and event.data2 > 0:
			ui.down()
			Directions.ud_status = self.ud_result
			print('down expeception')
			event.handled = True
		
		elif event.data1 == 46 and event.data2 >0:
			ui.up()
			Directions.ud_status = self.ud_result
			print('up_exception')
			event.handled = True

		elif event.data1 == 31 and self.ud_status == 8:
			Directions.ud_status = self.ud_result
			print('skip 31')
			event.handled = True 

		elif event.data1 == 24 and self.ud_status == 9:
			Directions.ud_status = self.ud_result
			print('skip 24')
			event.handled = True 

		elif self.ud_result < Directions.ud_status:
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


