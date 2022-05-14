from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import (QApplication, QComboBox,
        QDialog, QGridLayout, QGroupBox, QHBoxLayout, QLabel, 
        QPushButton, QSpinBox, QTextEdit,QVBoxLayout,QDoubleSpinBox)
import ast

from Project1.Generator import *
from Project1.Representation import AdjacencyMatrix, IncidentMatrix

graph_representation_list = ['Select Graph Representation','AdjacencyList','AdjacencyMatrix','IncidentMatrix']
data={'name': 'tmpImg.png',
       'directed': True,
       'colors': [],
       'graph': None
}
class MainWindow(QDialog):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        #create user interface
        self.initUI()
        self.layouH=None
        self.layout2=None
        #connect functionality with methods
        self.setupQtConnections()
        #set geometry
        self.setGeometry(50, 50, 900, 600)
        #set window title
        self.setWindowTitle('Graphs Presentation')

    def initUI(self):
        #Tool Bar & EDI
        #basic
        self.originalPalette = QApplication.palette()

        self.LeftGroupBox = QGroupBox("Option")
        self.layoutLeftGroupBox = QVBoxLayout()
        self.LeftGroupBox.setLayout(self.layoutLeftGroupBox)

        self.RightGroupBox = QGroupBox("Display")
        self.layoutRightGroupBox = QVBoxLayout()
        self.RightGroupBox.setLayout(self.layoutRightGroupBox)

        topLayout = QHBoxLayout()
        topLayout = QHBoxLayout()
        self.project1Button = QPushButton('Project1', self)
        self.project2Button = QPushButton('Project2', self)
        self.project3Button = QPushButton('Project3', self)
        self.project4Button = QPushButton('Project4', self)
        self.project5Button = QPushButton('Project5', self)
        self.project6Button = QPushButton('Project6', self)
        topLayout.addWidget(self.project1Button)
        topLayout.addWidget(self.project2Button)
        topLayout.addWidget(self.project3Button)
        topLayout.addWidget(self.project4Button)
        topLayout.addWidget(self.project5Button)
        topLayout.addWidget(self.project6Button)
        topLayout.addStretch(1)

        #delete if project is added
        self.project2Button.setDisabled(True)
        self.project3Button.setDisabled(True)
        self.project4Button.setDisabled(True)
        self.project5Button.setDisabled(True)
        self.project6Button.setDisabled(True)
        #init main Layout
        mainLayout = QGridLayout()
        mainLayout.addLayout(topLayout, 0, 0,1,2)
        mainLayout.addWidget(self.LeftGroupBox, 1, 0)
        mainLayout.addWidget(self.RightGroupBox, 1, 1)

        mainLayout.setColumnStretch(1, 1)
        self.setLayout(mainLayout)

    def setupQtConnections(self):
        """
        A method that combines events with appropriate methods
        """
        self.project1Button.clicked.connect(self.initProject1)
        # self.project2Button.clicked.connect(self.initProject2)
        # self.project2Button.clicked.connect(self.initProject2)
        # self.project3Button.clicked.connect(self.initProject3)
        # self.project4Button.clicked.connect(self.initProject4)
        # self.project5Button.clicked.connect(self.initProject5)
        # self.project6Button.clicked.connect(self.initProject6)

    def clear_right_layout(self):
        if self.layouH:
            for i in reversed(range(self.layouH.count())):
                try:
                    self.layouH.itemAt(i).widget().setParent(None)
                except:pass
        for i in reversed(range(self.layoutRightGroupBox.count())):
            try:
                self.layoutRightGroupBox.itemAt(i).widget().setParent(None)
            except: pass    

    def clear_left_layout(self):
        for i in reversed(range(self.layoutLeftGroupBox.count())):
                self.layoutLeftGroupBox.itemAt(i).widget().setParent(None)
        # except: self.restart()


    def initProject1(self):
        self.project1Button.setDisabled(True)
        #option
        self.graph_representation_combo = QComboBox()
        self.graph_representation_combo.addItems(graph_representation_list)

        self.rand_graph_edge_number_button = QPushButton('Generate Model G(n,l)',self)
        self.rand_graph_edge_number_spin1_n = QSpinBox()
        self.rand_graph_edge_number_spin1_n.setValue(10)
        self.rand_graph_edge_number_spin1_l = QSpinBox()
        self.rand_graph_edge_number_spin1_l.setValue(5)

        layout1 = QHBoxLayout()
        layout1.addWidget(self.rand_graph_edge_number_button)
        layout1.addWidget(self.rand_graph_edge_number_spin1_n)
        layout1.addWidget(self.rand_graph_edge_number_spin1_l)

        self.rand_graph_edge_probability_button = QPushButton('Generate Model G(n,p)',self)
        self.rand_graph_edge_number_spin2_n = QSpinBox()
        self.rand_graph_edge_number_spin2_n.setValue(10)
        self.rand_graph_edge_number_spin2_p = QDoubleSpinBox()
        self.rand_graph_edge_number_spin2_p.setSingleStep(0.1)
        self.rand_graph_edge_number_spin2_p.setValue(0.5)

        layout2 = QHBoxLayout()
        layout2.addWidget(self.rand_graph_edge_probability_button)
        layout2.addWidget(self.rand_graph_edge_number_spin2_n)
        layout2.addWidget(self.rand_graph_edge_number_spin2_p)

        self.layoutLeftGroupBox.addWidget(self.graph_representation_combo)
        self.layoutLeftGroupBox.addLayout(layout1)
        self.layoutLeftGroupBox.addLayout(layout2)
        self.layoutLeftGroupBox.addStretch(1)

        #setup connection
        self.rand_graph_edge_number_button.clicked.connect(self.on_rand_graph_edge_number)
        self.rand_graph_edge_probability_button.clicked.connect(self.on_rand_graph_edge_probability)
        self.graph_representation_combo.currentTextChanged.connect(self.on_graph_representation_combo)

    def initProject2(self):
        self.clear_right_layout()
        self.clear_left_layout()

    def on_rand_graph_edge_number(self):
        self.clear_right_layout()
        Generator.rand_graph_edge_number(self.rand_graph_edge_number_spin1_n.value(), self.rand_graph_edge_number_spin1_l.value()).graphVisualization()
        label = QLabel(self)
        pixmap = QPixmap('src/__imgcache__/Ad3 (1).png')
        label.setPixmap(pixmap)
        self.layoutRightGroupBox.addWidget(label)

    def on_rand_graph_edge_probability(self):
        self.clear_right_layout()
        Generator.rand_graph_edge_probability(self.rand_graph_edge_number_spin2_n.value(), self.rand_graph_edge_number_spin2_p.value()).graphVisualization()
        label = QLabel(self)
        pixmap = QPixmap('src/__imgcache__/Ad3 (2).png')
        label.setPixmap(pixmap)
        self.layoutRightGroupBox.addWidget(label)

    def on_graph_representation_combo(self):
        self.clear_right_layout()

        self.inputTextEdit = QTextEdit()
        if self.graph_representation_combo.currentText() == graph_representation_list[1]:
            self.inputTextEdit.setText("""{ 1:  [2,5,6],
2:  [1,3,6],
3:  [2,4,5,12],
4:  [3,8,9,11],
5:  [1,3,7,9],
6:  [1,2,7],
7:  [5,6,8],
8:  [4,7,9,12],
9:  [4,5,8,10],
10: [9],
11: [4],
12: [3,8]}""")
        if self.graph_representation_combo.currentText() == graph_representation_list[2]:
            self.inputTextEdit.setText("""[[0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0],
[1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0],
[0, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1],
[0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 1, 0],
[1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0],
[1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0],
[0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1],
[0, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
[0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0]]""")
        if self.graph_representation_combo.currentText() == graph_representation_list[3]:
            self.inputTextEdit.setText("""[[1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 1, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0],
[0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0],
[0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 1, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 1],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0]]""")
        label = QLabel("Select the representation you want to convert to!")
        self.representationBox = QComboBox()
        self.representationBox.addItems(graph_representation_list)

        self.layouH = QHBoxLayout()
        self.returnTextEdit = QTextEdit()
        self.returnTextEdit.setReadOnly(True)
        self.returnTextEdit.setMaximumWidth(250)
        self.labelImage = QLabel()

        self.layouH.addWidget(self.returnTextEdit)
        self.layouH.addWidget(self.labelImage)

        self.layoutRightGroupBox.addWidget(self.inputTextEdit)
        self.layoutRightGroupBox.addWidget(label)
        self.layoutRightGroupBox.addWidget(self.representationBox)
        self.layoutRightGroupBox.addLayout(self.layouH)
        self.representationBox.currentTextChanged.connect(self.on_graph_representation)

    def on_graph_representation(self):
        data['graph']=ast.literal_eval(self.inputTextEdit.toPlainText())
        tmp = None
        if self.graph_representation_combo.currentText() == graph_representation_list[1]: tmp = AdjacencyList(data)
        if self.graph_representation_combo.currentText() == graph_representation_list[2]: tmp = AdjacencyMatrix(data)
        if self.graph_representation_combo.currentText() == graph_representation_list[3]: 
            tmp = IncidentMatrix(data)
            print("incyden1t")
        self.graph_representation_helper(tmp)

    def graph_representation_helper(self,tmp):
        if self.representationBox.currentText() == graph_representation_list[1]: 
            self.returnTextEdit.setText(tmp.toAdjacencyList().printGraph())
            tmp.toAdjacencyList().graphVisualization()
        if self.representationBox.currentText() == graph_representation_list[2]: 
            self.returnTextEdit.setText(tmp.toAdjacencyMatrix().printGraph())
            tmp.toAdjacencyMatrix().graphVisualization()
        if self.representationBox.currentText() == graph_representation_list[3]: 
            print("incydent")
            self.returnTextEdit.setText(tmp.toIncidentMatrix().printGraph())
            tmp.toIncidentMatrix().graphVisualization()

        pixmap = QPixmap('src/__imgcache__/tmpImg.png')
        self.labelImage.setPixmap(pixmap)

