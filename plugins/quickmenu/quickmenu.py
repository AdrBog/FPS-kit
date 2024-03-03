# -*- coding: utf-8 -*-
# Copyright Tom SF Haines
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from direct.gui.DirectGui import *

# Menu config is stored in config/menu.xml

class QuickMenu:
  """This creates a menu - nothing fancy - just a list of buttons and labels,
     each of which invokes a transition to another config file."""
  def __init__(self,manager,xml):
    self.items = []

    # Create the button objects...
    yPos = 0.8
    for but in xml.findall('item'):
      if but.get('type', '') == "button":
        item = DirectButton(text = but.get('text','-'),pos=(0.0,0.0,yPos),scale = .065)
        yPos -= 0.1
        item['command'] = manager.transition
        item['extraArgs'] = [but.get('target','')]
        item.hide()
      else:
        item = DirectLabel(text = but.get('text','-'),pos=(0.0,0.0,yPos),scale = .065)
        yPos -= 0.1
        item.hide()
      
      self.items.append(item)
        

  def start(self):
    for item in self.items:
      item.show()

  def stop(self):
    for item in self.items:
      item.hide()

  def destroy(self):
    for item in self.items:
      item.destroy()
