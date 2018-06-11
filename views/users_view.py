# -*- coding: utf-8 -*-
import sys
from PyQt4 import QtGui

class  users_view(QtGui.QWidget):

   def __init__(self):
      super(users_view, self).__init__()
      self.init_full_ui()


   def init_full_ui(self):
      self.init_main_windows_properties()
      self.init_labels()
      self.init_list()
      self.init_form()
      self.init_buttons()
      self.show()


   def init_main_windows_properties(self):
      self.setGeometry(100,100,500,250)
      self.setFixedSize(500,250)
      self.setWindowTitle("Animals Management Example With MVC")


   def init_labels(self):
      self.animals_code_label = QtGui.QLabel(self)
      self.animals_code_label.setText("List of Animal Codes")
      self.animals_code_label.move(10, 25)


   def init_list(self):
      self.animals_list = QtGui.QListWidget(self)
      self.animals_list.resize(250,110)
      self.animals_list.addItem("An-01"); 
      self.animals_list.addItem("An-02");
      self.animals_list.addItem("An-03"); 
      self.animals_list.addItem("An-04");
      self.animals_list.addItem("An-05"); 
      self.animals_list.addItem("An-06");
      self.animals_list.addItem("An-07"); 
      self.animals_list.addItem("An-08");
      self.animals_list.addItem("An-09"); 
      self.animals_list.addItem("An-10");
      self.animals_list.addItem("An-11"); 
      self.animals_list.addItem("An-12");
      self.animals_list.move(10, 40)
      self.animals_list.itemClicked.connect(self.display_selected_item)


   def init_form(self):
      #Code
      self.animal_code_lbl = QtGui.QLabel(self)
      self.animal_code_lbl.setText("Code")
      self.animal_code_lbl.move(300, 25)
      self.animal_code_txt = QtGui.QLineEdit(self)
      self.animal_code_txt.move(300, 40)
      #name
      self.animal_name_lbl = QtGui.QLabel(self)
      self.animal_name_lbl.setText("Name")
      self.animal_name_lbl.move(300, 70)
      self.animal_name_txt = QtGui.QLineEdit(self)
      self.animal_name_txt.move(300, 85)
      #amount
      self.animal_amount_lbl = QtGui.QLabel(self)
      self.animal_amount_lbl.setText("Amount")
      self.animal_amount_lbl.move(300, 115)
      self.animal_amount_txt = QtGui.QLineEdit(self)
      self.animal_amount_txt.move(300, 130)


   def init_buttons(self):
      #add
      self.add_animal_btn = QtGui.QPushButton(self)
      self.add_animal_btn.setText("Add")
      self.add_animal_btn.move(10, 170)
      self.add_animal_btn.resize(150,50)
      self.add_animal_btn.clicked.connect(self.add_animal)
      #modify
      self.modify_animal_btn = QtGui.QPushButton(self)
      self.modify_animal_btn.setText("Modify")
      self.modify_animal_btn.move(175, 170)
      self.modify_animal_btn.resize(150,50)
      self.modify_animal_btn.clicked.connect(self.modify_animal)
      #delete
      self.delete_animal_btn = QtGui.QPushButton(self)
      self.delete_animal_btn.setText("Delete")
      self.delete_animal_btn.move(340, 170)
      self.delete_animal_btn.resize(150,50)
      self.delete_animal_btn.clicked.connect(self.delete_animal)


   def display_selected_item(self, item):
      self.animal_code_txt.setText(item.text())


   def add_animal(self, item):
      print "Adding"


   def modify_animal(self, item):
      print "Modifying"


   def delete_animal(self, item):
      print "Deleting"


app = QtGui.QApplication(sys.argv)
user_window = users_view()
sys.exit(app.exec_())