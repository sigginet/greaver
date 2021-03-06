#!/usr/bin/python
#
# greaver.py
# Copyright (C) Sigurdur Gudbrandsson 2012 <sigurdur@sigginet.info>
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
# 1. Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
# 2. Redistributions in binary form must reproduce the above copyright
#    notice, this list of conditions and the following disclaimer in the
#    documentation and/or other materials provided with the distribution.
# 3. Neither the name ``Sigurdur Gudbrandsson'' nor the name of any other
#    contributor may be used to endorse or promote products derived
#    from this software without specific prior written permission.
# 
# Greaver IS PROVIDED BY Sigurdur Gudbrandsson ``AS IS'' AND ANY EXPRESS
# OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED.  IN NO EVENT SHALL Sigurdur Gudbrandsson OR ANY OTHER CONTRIBUTORS
# BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
# CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
# SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR
# BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY,
# WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR
# OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF
# ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.


from gi.repository import Gtk, GdkPixbuf, Gdk, Vte
import os, sys, interfaces


#Comment the first line and uncomment the second before installing
#or making the tarball (alternatively, use project variables)
UI_FILE = "src/greaver2.ui"
#UI_FILE = "/usr/local/share/greaver/ui/greaver.ui"


class GUI:
	def __init__(self):

		self.builder = Gtk.Builder()
		self.builder.add_from_file(UI_FILE)
		self.builder.connect_signals(self)

		main_window = self.builder.get_object('main_window')

		# Create an output terminal
		terminal = Vte.Terminal()
		output_preview = self.builder.get_object('output_preview')
		output_preview.add(terminal)
		
		main_window.show_all()

	def destroy(main_window, self):
		Gtk.main_quit()

	def button_adapter_clicked(self, widget):
		adapter_window = self.builder.get_object('adapter_window')

		adapter_window.show_all()

	def button_network_clicked(self, widget):
		network_window = self.builder.get_object('network_window')
		network_window.show_all()

	def button_attack_clicked(self, widget):
		a = "12"
		#attack()

	def button_advanced_clicked(self, widget):
		advanced_window = self.builder.get_object('advanced_settings_window')
		advanced_window.show_all()

	def expander_output_activated(self, widget):
		expander_output = self.builder.get_object('expander_output')
		#a = 1
		#main_window.height = 800
		#expander_output.height = 400

def main():
	app = GUI()
	Gtk.main()
		
if __name__ == "__main__":
    sys.exit(main())
