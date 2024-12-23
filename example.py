import fabrictk as ftk

import tkinter as tk


class LoginForm(tk.Frame):
	def __init__(self, master) -> None:
		super().__init__(master)

		# configure frame
		self.configure(background=ftk.Configure.background_color)

		# configure grid
		self.columnconfigure((0, 1), weight=1, uniform='default')
		self.rowconfigure((0, 1, 2, 3, 4, 5), weight=1, uniform='default')

		self._widgets_padding = {
			'sticky': 'nwse',
			'pady': 5,
		}

		self._label_sign_up_padding = {
			'sticky': 'nw',
			'pady': 5,
		}

		self.__create_widgets()

	def __create_widgets(self) -> None:
		# title
		font = (ftk.Configure.general_font, '24')
		self._label_login = ftk.Label(self, text='Login', font=font)
		self._label_login.grid(
			column=0,
			columnspan=2,
			row=0,
			rowspan=2,
			**self._widgets_padding,
		)

		# login form
		self._entry_login = ftk.Entry(self, placeholder='Login')
		self._entry_login.grid(
			column=0,
			columnspan=2,
			row=2,
			**self._widgets_padding,
		)

		self._entry_password = ftk.Entry(self, placeholder='Password', password=True)
		self._entry_password.grid(
			column=0,
			columnspan=2,
			row=3,
			**self._widgets_padding,
		)

		self._button_sign_in = ftk.Button(self, text='Sign in')
		self._button_sign_in.grid(
			column=0,
			columnspan=2,
			row=4,
			**self._widgets_padding,
		)

		# sign up
		self._label_sign_up_frame = tk.Frame(self, background=ftk.Configure.background_color)
		self._label_sign_up_frame.grid(
			column=0,
			columnspan=2,
			row=5,
			**self._widgets_padding,
		)

		self._label_sign_up = ftk.Label(
			self._label_sign_up_frame,
			secondary=True,
			text="Don't have and account? "
		)
		self._label_sign_up.pack(
			anchor='nw',
			side='left',
		)

		self._hyperlink_sign_up = ftk.Hyperlink(self._label_sign_up_frame, text='Sign up')
		self._hyperlink_sign_up.pack(
			anchor='nw',
			side='left',
		)


class Body(tk.Frame):
	def __init__(self, master) -> None:
		super().__init__(master)

		# configure frame
		self.configure(background=ftk.Configure.background_color)

		# configure grid
		self.columnconfigure((0), weight=1, uniform='default')
		self.rowconfigure((0), weight=1, uniform='default')


class Application(tk.Tk):
	def __init__(self) -> None:
		super().__init__()

		# configure the window
		self.title('FabricTk example')
		self.geometry('400x400')
		self.resizable(False, False)
		self.configure(background=ftk.Configure.background_color)

		# configure grid
		self.columnconfigure((0), weight=1, uniform='default')
		self.rowconfigure((0), weight=1, uniform='default')

		self._size = ftk.Configure.get_root_win_size(master=self)

		self.__create_widgets()

	def __create_widgets(self) -> None:
		self._title_bar = ftk.TitleBar(self)

		self._body = Body(self)
		self._body.place(
			height=self._size[1],
			relwidth=1,
			y=32,
		)

		self._login_form = LoginForm(self._body)
		self._login_form.grid(
			column=0,
			row=0,
			sticky='nwse',
			padx=20,
			pady=50,
		)


if __name__ == '__main__':
	application = Application()
	application.mainloop()