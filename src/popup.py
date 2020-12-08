# popup.py
#
# Copyright 2020 Martin Abente Lahaye
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

from gi.repository import Gtk


@Gtk.Template(resource_path='/dev/tchx84/Portfolio/popup.ui')
class PortfolioPopup(Gtk.Revealer):
    __gtype_name__ = 'PortfolioPopup'

    description = Gtk.Template.Child()
    confirm_button = Gtk.Template.Child()
    cancel_button = Gtk.Template.Child()

    def __init__(self, description, on_confirm, on_cancel, data):
        super().__init__()

        self.description.set_text(description)
        self.confirm_button.connect('clicked', on_confirm, self, data)
        self.cancel_button.connect('clicked', on_cancel, self, data)