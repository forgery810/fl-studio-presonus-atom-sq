import data
import device
import ui

class Directions():
	arrow_status = False
	ud_status = 0

	def __init__(self, event):
		self.ud_index = 0
		
		self.ud_result = data.ud_arrow.index(event.data1)

		print(Directions.arrow_status)
		if event.data1 in data.ud_arrow:
			Directions.up_down(self, event)

	def up_down(self, event):
		print(f'ud_status before if statement: {Directions.ud_status}')
		if Directions.arrow_status == False:
			# print('temp false')
			Directions.arrow_status = True
		if self.ud_result < Directions.ud_status:
			ui.up()
			print('up')
			Directions.ud_status = self.ud_result
		elif self.ud_result > Directions.ud_status:
			ui.down()
			print('down')
			Directions.ud_status = self.ud_result
		print(f'ud_status after if statement: {Directions.ud_status}')
		print(f'status in updown: {Directions.arrow_status}')
		print(self.ud_result)
		event.handled = True