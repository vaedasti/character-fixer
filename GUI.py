#!/usr/bin/env python
#-*- coding: utf-8 -*-

import pygtk
pygtk.require20()
import gtk
import charsFixer

class Window(object):
	def __init__(self):
		while gtk.events_pending(): # Update
			gtk.main_iteration()	#  GUI
		self.GUI(self)

	# Methods
	def GUI (self, widget):
		# Window
		self.win = gtk.Window(gtk.WINDOW_TOPLEVEL)
		self.win.set_title("Editor")
		self.win.set_position(gtk.WIN_POS_CENTER)       # Open Window Center
		self.win.connect("delete_event", gtk.main_quit) # Close Event
		#self.win.resize(400, 700)
		self.win.set_geometry_hints(self.win, 400, 700, 400, 700)
		self.win.modify_bg(gtk.STATE_NORMAL, gtk.gdk.color_parse('#efefef'))	# Set BG Color

		# Menu
		self.menubar = gtk.MenuBar()
		self.menubar.set_size_request(800, 25)
		# Menu
		menu_file = gtk.Menu()
		menu_edit = gtk.Menu()
		menu_help = gtk.Menu()
		# Open
		item_open = gtk.MenuItem("Open")
		item_open.connect("activate", self.openFileDialog)
		menu_file.append(item_open)
		# Save
		self.item_save = gtk.MenuItem("Save")
		self.item_save.connect("activate", self.saveFileDialog)
		menu_file.append(self.item_save)
		# Quit
		item_quit = gtk.MenuItem("Quit")
		item_quit.connect("activate", gtk.main_quit)
		menu_file.append(item_quit)
		# About
		item_about = gtk.MenuItem("About")
		menu_help.append(item_about)
		#
		item_file = gtk.MenuItem("File")
		item_edit = gtk.MenuItem("Edit")
		item_help = gtk.MenuItem("Help")
		#
		item_file.set_submenu(menu_file)
		item_edit.set_submenu(menu_edit)
		item_help.set_submenu(menu_help)
		#
		self.menubar.append(item_file)
		self.menubar.append(item_edit)
		self.menubar.append(item_help)

		# Create Rich TextBox1 (Name is Before)
		self.textview1 = gtk.TextView()
		self.textview1.set_size_request(390, 595)
		# Buffer
		self.buffer1 = self.textview1.get_buffer()
		self.textview1.set_buffer(self.buffer1)
		# Scrollbars
		sw1 = gtk.ScrolledWindow()
		sw1.set_policy(gtk.POLICY_AUTOMATIC, gtk.POLICY_AUTOMATIC)
		self.textview1.set_border_window_size(gtk.TEXT_WINDOW_BOTTOM,1)
		sw1.add(self.textview1)

		# Create Rich TextBox2 (Name is After)
		self.textview2 = gtk.TextView()
		self.textview2.set_size_request(390, 595)
		# Buffer
		self.buffer2 = self.textview2.get_buffer()
		self.textview2.set_buffer(self.buffer2)
		# Scrollbars
		sw2 = gtk.ScrolledWindow()
		sw2.set_policy(gtk.POLICY_AUTOMATIC, gtk.POLICY_AUTOMATIC)
		self.textview2.set_border_window_size(gtk.TEXT_WINDOW_BOTTOM,1)
		sw2.add(self.textview2)
		# Tags
		#self.tag_orange = self.buffer1.create_tag("orange_bg", background="orange")
		#h_tag = self.textbuffer.create_tag( "h", size_points=16, weight=pango.WEIGHT_BOLD)
 		#position = self.textbuffer.get_end_iter()
 		#self.textbuffer.insert_with_tags( position, "Heading\n", h_tag)
 		## normal text
 		#position = self.textbuffer.get_end_iter()
 		#self.textbuffer.insert( position, "Several lines\nof normal text.\n")
 		## more text
 		#position = self.textbuffer.get_end_iter()
 		#i_tag = self.textbuffer.create_tag( "i", style=pango.STYLE_ITALIC)
 		#self.textbuffer.insert_with_tags( position, "italic text", i_tag)
 		#position = self.textbuffer.get_end_iter()
 		#self.textbuffer.insert_with_tags( position, " combined with heading", i_tag, h_tag)
 		#position = self.textbuffer.get_end_iter()
 		#c_tag = self.textbuffer.create_tag( "colored", foreground="#FFFF00", background="#0000FF")
 		#self.textbuffer.insert_with_tags( position, "\nand color", i_tag, h_tag, c_tag)
 		#e_tag = self.textbuffer.create_tag( "fixed", editable=False)
 		#position = self.textbuffer.get_end_iter()
 		#self.textbuffer.insert_with_tags( position, "\nnon-editable ", e_tag)
 		#position = self.textbuffer.get_end_iter()
 		#self.textbuffer.insert_with_tags_by_name( position, " and colored text", "colored", "fixed")

		# CheckBox
		self.check_Turkish = gtk.CheckButton("Turkish")
		self.check_Turkish.set_active(True)

		# OK Button
		self.ok_But = gtk.Button("OK")
		self.ok_But.set_size_request(100, 30)
		self.ok_But.connect("clicked", self.fix)

		# Save Button
		self.save_But = gtk.Button("Save")
		self.save_But.set_size_request(100, 30)
		self.save_But.connect("clicked", self.saveFileDialog)

		# ComboBox
		self.dropD = gtk.combo_box_new_text()
		self.dropD.append_text("utf-8")			# Add Option
		self.dropD.append_text("UTF-16")		# Add Option
		self.dropD.append_text("iso-8859-1")	# Add Option
		self.dropD.append_text("latin-1")		# Add Option
		self.dropD.set_active(0)				# Select First
		#dropD.connect('changed', self.changed_cb)
		#text = self.dropD.get_active_text()

		# Create Fixed
		self.fixed = gtk.Fixed()

		# Add Widgets to Table
		self.fixed.put(self.menubar, 0, 0)		# Menu (File, Edit, Help)
		self.fixed.put(self.check_Turkish, 5, 30)	# CheckBox (Latin)
		self.fixed.put(sw1, 5, 60)				# Rich TextBox1 (Before)
		self.fixed.put(sw2, 405, 60)			# Rich TextBox2 (After)
		self.fixed.put(self.dropD, 10, 660)		# Dropdown Menu
		self.fixed.put(self.ok_But, 290, 660)	# Save  Button
		self.fixed.put(self.save_But, 410, 660)	# Save  Button

		# Disable Objects
		self.disableObjects(self)

		# Fixed Add to Window & Show Window
		self.win.add(self.fixed)
		self.win.show_all()

	def openFileDialog(self, widget): # Open Dialog
		# Open Dialog
		# Create Dialog
		dialog = gtk.FileChooserDialog("Open...", None,
										gtk.FILE_CHOOSER_ACTION_OPEN,
										(gtk.STOCK_CANCEL, gtk.RESPONSE_CANCEL,
											gtk.STOCK_OPEN, gtk.RESPONSE_OK))
		dialog.set_default_response(gtk.RESPONSE_OK)
		#dialog.set_current_folder("~")

		# Create Filter
		filter = gtk.FileFilter()
		filter.set_name("Text files")
		filter.add_mime_type("text/plain")
		dialog.add_filter(filter)
		# Create Filter 2
		filter = gtk.FileFilter()
		filter.set_name("All files")
		filter.add_pattern("*")
		dialog.add_filter(filter)

		response = dialog.run()
		if response == gtk.RESPONSE_OK:
			# Go to 'read' file
			self.buffer1.set_text(charsFixer.readFile(dialog.get_filename()))
			# Clear Text Box 2
			self.buffer2.set_text("")
			# Disable Objects
			self.disableObjects(self)
		dialog.destroy()

	def saveFileDialog(self, widget): # Save Method
		print(self.dropD.get_active_text())
		# Save Dialog
		# Create Dialog
		dialog = gtk.FileChooserDialog("Save...", None,
										gtk.FILE_CHOOSER_ACTION_SAVE,
										(gtk.STOCK_CANCEL, gtk.RESPONSE_CANCEL,
											gtk.STOCK_SAVE, gtk.RESPONSE_OK))
		dialog.set_default_response(gtk.RESPONSE_OK)
		#dialog.set_current_folder("~")

		response = dialog.run()
		if response == gtk.RESPONSE_OK:
			self.save(self, dialog.get_filename())
		dialog.destroy()

	def save(self, widget, _file_):
		# Write
		wrt = open(_file_, 'w')
		wrt.write(self.buffer2.get_text(self.buffer2.get_start_iter(), self.buffer2.get_end_iter()).encode('utf-8'))
		wrt.close()

	def enableObjects(self, widget):
		# Enable Object
		self.save_But.set_sensitive(True)
		self.textview2.set_sensitive(True)
		self.item_save.set_sensitive(True)

		self.win.set_geometry_hints(self.win, 800, 700, 800, 700)	# Resize

	def disableObjects(self, widget):
		# Disable Object
		self.save_But.set_sensitive(False)
		self.textview2.set_sensitive(False)
		self.item_save.set_sensitive(False)
		self.buffer2.set_text("")									# Clear Rich-Text-Box 2
		self.win.set_geometry_hints(self.win, 400, 700, 400, 700)	# Resize

	def fix(self, widget):
		print("Turkish checkbox", self.check_Turkish.get_active())
		damagedText = self.buffer1.get_text(self.buffer1.get_start_iter(), self.buffer1.get_end_iter())
		correctedText = charsFixer.fixIt(damagedText)
		self.buffer2.set_text(correctedText)
		# Enable Object
		self.enableObjects(self)

	def main(self):
		gtk.main()

Window().main()
