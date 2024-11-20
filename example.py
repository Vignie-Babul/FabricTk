import fabrictk as ftk

import tkinter as tk


class LoginForm(tk.Frame):
	def __init__(self, master) -> None:
		super().__init__(master)

		# configure frame
		self.configure(background=ftk.Configure.background_color)

		# configure grid
		self.columnconfigure((0), weight=1, uniform='default')
		self.rowconfigure((0, 1, 2), weight=1, uniform='default')

		self._widgets_padding = {
			'sticky': 'nwse',
			'padx': 20,
			'pady': 5,
		}

		self.__create_widgets()

	def __create_widgets(self) -> None:
		self._entry_login = ftk.Entry(self, placeholder='Login')
		self._entry_login.grid(
			column=0,
			row=0,
			**self._widgets_padding,
		)

		self._entry_password = ftk.Entry(self, placeholder='Password')
		self._entry_password.grid(
			column=0,
			row=1,
			**self._widgets_padding,
		)

		self._button_sign_in = ftk.Button(self, text='Sign in')
		self._button_sign_in.grid(
			column=0,
			row=2,
			**self._widgets_padding,
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
		self.title('FaricTk example')
		self.geometry('400x300')
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
			height=self._size[1] - 32,
			relwidth=1,
			y=32,
		)

		self._login_form = LoginForm(self._body)
		self._login_form.grid(
			column=0,
			row=0,
			sticky='nwse',
			padx=0,
			pady=50,
		)


if __name__ == '__main__':
	application = Application()
	application.mainloop()