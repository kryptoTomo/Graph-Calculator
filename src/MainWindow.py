from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt 
from PyQt5.QtWidgets import (QApplication, QComboBox,
        QDialog, QGridLayout, QGroupBox, QHBoxLayout, QLabel, 
        QPushButton, QSpinBox, QTextEdit,QVBoxLayout,QDoubleSpinBox)
import ast

from Generator import *
from Representation import AdjacencyMatrix, IncidentMatrix
from Utils import components, valid_graph, cons_graph, random_k_regular, find_Hamiltion_cycle, randomizeGraph
from EulerGraph import EulerGraph

graph_representation_list = ['Select Graph Representation','AdjacencyList','AdjacencyMatrix','IncidentMatrix']

data={'name': 'Representation.png','size': (3, 3),'directed_all': False,'node_size': 500,'graph': None,'nodes_description':{},'edges_description':{}}

class MainWindow(QDialog):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        #create user interface
        self.initUI()
        self.layout0=None
        self.layout1=None
        self.layout2=None
        self.layout3=None
        self.layout4=None
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
        self.project2Button.clicked.connect(self.initProject2)
        # self.project3Button.clicked.connect(self.initProject3)
        # self.project4Button.clicked.connect(self.initProject4)
        # self.project5Button.clicked.connect(self.initProject5)
        # self.project6Button.clicked.connect(self.initProject6)

    def clear_right_layout(self):
        if self.layout3:
            for i in reversed(range(self.layout3.count())):
                try:
                    self.layout3.itemAt(i).widget().setParent(None)
                except:pass
        if self.layout4:
            for i in reversed(range(self.layout4.count())):
                try:
                    self.layout4.itemAt(i).widget().setParent(None)
                except:pass
        for i in reversed(range(self.layoutRightGroupBox.count())):
            try:
                self.layoutRightGroupBox.itemAt(i).widget().setParent(None)
            except: pass    

    def clear_left_layout(self):
        if self.layout0:
            for i in reversed(range(self.layout0.count())):
                try:
                    self.layout0.itemAt(i).widget().setParent(None)
                except:pass
        if self.layout1:
            for i in reversed(range(self.layout1.count())):
                try:
                    self.layout1.itemAt(i).widget().setParent(None)
                except:pass
        if self.layout2:
            for i in reversed(range(self.layout2.count())):
                try:
                    self.layout2.itemAt(i).widget().setParent(None)
                except:pass
        for i in reversed(range(self.layoutRightGroupBox.count())):
            try:
                self.layoutLeftGroupBox.itemAt(i).widget().setParent(None)
            except: pass
        for i in reversed(range(self.layoutRightGroupBox.count())):
            try:
                self.layoutLeftGroupBox.itemAt(i).widget().setParent(None)
            except: pass

    def enable_all(self):
        self.project1Button.setEnabled(True)
        self.project2Button.setEnabled(True)
        # self.project3Button.setEnabled(True)
        # self.project4Button.setEnabled(True)
        # self.project5Button.setEnabled(True)
        # self.project6Button.setEnabled(True)
#+-----------------------------------------------------------------------------------------------------------------
#
# PROJECT 1
#
#------------------------------------------------------------------------------------------------------------------

    def initProject1(self):
        self.enable_all()
        self.project1Button.setDisabled(True)
        self.clear_right_layout()
        self.clear_left_layout()
        #-------------------------
        self.layout0 = QVBoxLayout()
        self.graph_representation_combo = QComboBox()
        self.graph_representation_combo.addItems(graph_representation_list)
        self.layout0.addWidget(self.graph_representation_combo)

        self.rand_graph_edge_number_button = QPushButton('Generate Model G(n,l)',self)
        self.rand_graph_edge_number_spin1_n = QSpinBox()
        self.rand_graph_edge_number_spin1_n.setValue(10)
        self.rand_graph_edge_number_spin1_l = QSpinBox()
        self.rand_graph_edge_number_spin1_l.setValue(5)

        self.layout1 = QHBoxLayout()
        self.layout1.addWidget(self.rand_graph_edge_number_button)
        self.layout1.addWidget(self.rand_graph_edge_number_spin1_n)
        self.layout1.addWidget(self.rand_graph_edge_number_spin1_l)

        self.rand_graph_edge_probability_button = QPushButton('Generate Model G(n,p)',self)
        self.rand_graph_edge_number_spin2_n = QSpinBox()
        self.rand_graph_edge_number_spin2_n.setValue(10)
        self.rand_graph_edge_number_spin2_p = QDoubleSpinBox()
        self.rand_graph_edge_number_spin2_p.setSingleStep(0.1)
        self.rand_graph_edge_number_spin2_p.setValue(0.5)

        self.layout2 = QHBoxLayout()
        self.layout2.addWidget(self.rand_graph_edge_probability_button)
        self.layout2.addWidget(self.rand_graph_edge_number_spin2_n)
        self.layout2.addWidget(self.rand_graph_edge_number_spin2_p)

        self.layout0.addLayout(self.layout1)
        self.layout0.addLayout(self.layout2)
        self.layoutLeftGroupBox.addLayout(self.layout0)
        # self.layoutLeftGroupBox.addStretch(0)

        #setup connection
        self.rand_graph_edge_number_button.clicked.connect(self.on_rand_graph_edge_number)
        self.rand_graph_edge_probability_button.clicked.connect(self.on_rand_graph_edge_probability)
        self.graph_representation_combo.currentTextChanged.connect(self.on_graph_representation_combo)


    def on_rand_graph_edge_number(self):
        self.clear_right_layout()
        Generator.rand_graph_edge_number(self.rand_graph_edge_number_spin1_n.value(), self.rand_graph_edge_number_spin1_l.value()).graphVisualization()
        label = QLabel(self)
        pixmap = QPixmap('src/__imgcache__/randomGraphEdgeNumber.png')
        label.setPixmap(pixmap)
        self.layoutRightGroupBox.addWidget(label)

    def on_rand_graph_edge_probability(self):
        self.clear_right_layout()
        Generator.rand_graph_edge_probability(self.rand_graph_edge_number_spin2_n.value(), self.rand_graph_edge_number_spin2_p.value()).graphVisualization()
        label = QLabel(self)
        pixmap = QPixmap('src/__imgcache__/randGraphEdgeProbability.png')
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

        self.layout3 = QHBoxLayout()
        self.returnTextEdit = QTextEdit()
        self.returnTextEdit.setReadOnly(True)
        self.returnTextEdit.setMaximumWidth(250)
        self.labelImage = QLabel()

        self.layout3.addWidget(self.returnTextEdit)
        self.layout3.addWidget(self.labelImage)

        self.layoutRightGroupBox.addWidget(self.inputTextEdit)
        self.layoutRightGroupBox.addWidget(label)
        self.layoutRightGroupBox.addWidget(self.representationBox)
        self.layoutRightGroupBox.addLayout(self.layout3)
        self.representationBox.currentTextChanged.connect(self.on_graph_representation)

    def on_graph_representation(self):
        data['graph']=ast.literal_eval(self.inputTextEdit.toPlainText())
        tmp = None
        if self.graph_representation_combo.currentText() == graph_representation_list[1]: tmp = AdjacencyList(data)
        if self.graph_representation_combo.currentText() == graph_representation_list[2]: tmp = AdjacencyMatrix(data)
        if self.graph_representation_combo.currentText() == graph_representation_list[3]: 
            tmp = IncidentMatrix(data)
        self.graph_representation_helper(tmp)

    def graph_representation_helper(self,tmp):
        if self.representationBox.currentText() == graph_representation_list[1]: 
            self.returnTextEdit.setText(tmp.toAdjacencyList().printGraph())
            tmp.toAdjacencyList().graphVisualization()
        if self.representationBox.currentText() == graph_representation_list[2]: 
            self.returnTextEdit.setText(tmp.toAdjacencyMatrix().printGraph())
            tmp.toAdjacencyMatrix().graphVisualization()
        if self.representationBox.currentText() == graph_representation_list[3]: 
            self.returnTextEdit.setText(tmp.toIncidentMatrix().printGraph())
            tmp.toIncidentMatrix().graphVisualization()

        pixmap = QPixmap('src/__imgcache__/Representation.png')
        self.labelImage.setPixmap(pixmap)

#+-----------------------------------------------------------------------------------------------------------------
#
# PROJECT 2
#
#------------------------------------------------------------------------------------------------------------------
    def initProject2(self):
        self.enable_all()
        self.project2Button.setDisabled(True)
        self.clear_right_layout()
        self.clear_left_layout()
        #-------------------------
        self.layout0 = QVBoxLayout()
        self.validGraphButton = QPushButton('Valid Graph',self)
        self.edgeRandomizationButton = QPushButton('Edge Randomize',self)
        self.findEulerCycleButton = QPushButton('Euler Cycle',self)
        self.findHamiltionCycleButton = QPushButton('Find Hamiltion Cycle',self)

        self.kRegularGraphsButton = QPushButton('K-Regular Graphs',self)
        self.layout0.addWidget(self.validGraphButton)
        self.layout0.addWidget(self.edgeRandomizationButton)
        self.layout0.addWidget(self.findEulerCycleButton)
        self.layout0.addWidget(self.kRegularGraphsButton)
        self.layout0.addWidget(self.findHamiltionCycleButton)
        self.validGraphButton.clicked.connect(self.on_valid_graph)
        self.edgeRandomizationButton.clicked.connect(self.on_edge_randomize)
        self.findEulerCycleButton.clicked.connect(self.on_find_euler_cycle)
        self.findHamiltionCycleButton.clicked.connect(self.on_find_hamiltion_cycle)
        self.kRegularGraphsButton.clicked.connect(self.on_k_regular_graphs)
        self.layoutLeftGroupBox.addLayout(self.layout0)

    def on_valid_graph(self):
        self.clear_right_layout()

        self.inputTextEdit = QTextEdit()
        self.inputTextEdit.setText("""[4, 2, 2, 3, 2, 1, 4, 2, 2, 2, 2]""")
        self.inputTextEdit.setMaximumHeight(250)
        valid = QPushButton('Valid Graph',self)
        self.labelImage1 = QLabel()
        labelImage2 = QLabel('------------------------------------------>')
        self.labelImage3 = QLabel()
        self.labelImage2 = QLabel()
        self.layout4=QVBoxLayout()
        self.labelImage4 = QLabel()
        self.layout4.addWidget(valid)
        self.layout4.addWidget(self.labelImage4)
        self.layout3=QHBoxLayout()
        self.layout3.addWidget(self.labelImage1)
        self.layout3.addWidget(labelImage2)
        self.layout3.addWidget(self.labelImage3)

        self.layoutRightGroupBox.addWidget(self.inputTextEdit)
        self.layoutRightGroupBox.addLayout(self.layout4)
        self.layoutRightGroupBox.addLayout(self.layout3)
        valid.clicked.connect(self.on_click_valid)

    def on_click_valid(self):
        if valid_graph(ast.literal_eval(self.inputTextEdit.toPlainText())):
            self.labelImage4.setText("The graph is graphical")
            cons_graph(ast.literal_eval(self.inputTextEdit.toPlainText())).graphVisualization()  #ex1
            pixmap = QPixmap('src/__imgcache__/CoherentComponent.png')
            self.labelImage1.setPixmap(pixmap)
            tmpStr = components(cons_graph(ast.literal_eval(self.inputTextEdit.toPlainText())).graph)     #ex3
            self.labelImage3.setText(tmpStr)
        else:
            self.labelImage4.setText("The graph is not graphical")

    def on_edge_randomize(self):
        self.clear_right_layout()

        self.inputTextEdit = QTextEdit()
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
        self.inputTextEdit.setMaximumHeight(250)
        randomize = QPushButton('Randomize',self)
        self.labelImage1 = QLabel()
        labelImage2 = QLabel('------------------------------------------>')
        self.labelImage3 = QLabel()
        self.labelImage2 = QLabel()
        self.layout4=QHBoxLayout()
        self.spin = QSpinBox()
        self.spin.setValue(10)
        self.layout4.addWidget(randomize)
        self.layout4.addWidget(self.spin)
        self.layout3=QHBoxLayout()
        self.layout3.addWidget(self.labelImage1)
        self.layout3.addWidget(labelImage2)
        self.layout3.addWidget(self.labelImage3)

        self.layoutRightGroupBox.addWidget(self.inputTextEdit)
        self.layoutRightGroupBox.addLayout(self.layout4)
        self.layoutRightGroupBox.addLayout(self.layout3)
        randomize.clicked.connect(self.on_click_randomize)

    def on_click_randomize(self):
        data['graph']=ast.literal_eval(self.inputTextEdit.toPlainText())
        tmp = AdjacencyList(data)
        tmp.graphVisualization()
        pixmap = QPixmap('src/__imgcache__/Representation.png')
        self.labelImage1.setPixmap(pixmap)
        randomizeGraph(tmp,self.spin.value()).graphVisualization()
        pixmap = QPixmap('src/__imgcache__/RandomizeGraph.png')
        self.labelImage3.setPixmap(pixmap)

    def on_find_euler_cycle(self):
        self.clear_right_layout()
        self.layout3=QVBoxLayout()
        self.layout4=QHBoxLayout()
        cycle = QPushButton('Find Euler Cycle(n)',self)
        self.spin = QSpinBox()
        self.spin.setValue(5)
        self.layout4.addWidget(cycle)
        self.layout4.addWidget(self.spin)
        self.labelImage1 = QLabel()
        self.labelImage2 = QLabel()
        self.labelImage3 = QLabel()
        self.layout3.addWidget(self.labelImage1)
        self.layout3.addWidget(self.labelImage2)
        self.layout3.addWidget(self.labelImage3)
        self.layoutRightGroupBox.addLayout(self.layout4)
        self.layoutRightGroupBox.addLayout(self.layout3)
        cycle.clicked.connect(self.on_click_cycle)

    def on_click_cycle(self):
        val = str(EulerGraph(self.spin.value()))
        pixmap = QPixmap('src/__imgcache__/CoherentComponent.png')
        self.labelImage1.setPixmap(pixmap)
        self.labelImage2.setText("The euler cycle found is:")
        print(val)
        self.labelImage3.setText(val)

    def on_k_regular_graphs(self):
        self.clear_right_layout()
        self.layout4=QHBoxLayout()
        random_k_regular_button = QPushButton('Random k-Regular Graphs',self)
        self.spin = QSpinBox()
        self.spin.setValue(2)
        self.spin1 = QSpinBox()
        self.spin1.setValue(8)
        self.layout4.addWidget(random_k_regular_button)
        self.layout4.addWidget(self.spin)
        self.layout4.addWidget(self.spin1)
        self.layout3=QHBoxLayout()
        self.labelImage1 = QLabel()
        self.layout3.addWidget(self.labelImage1)
        self.layoutRightGroupBox.addLayout(self.layout4)
        self.layoutRightGroupBox.addLayout(self.layout3)
        random_k_regular_button.clicked.connect(self.on_click_random_k)

    def on_click_random_k(self):
        random_k_regular(self.spin.value(),self.spin1.value())
        pixmap = QPixmap('src/__imgcache__/RandomizeGraph.png')
        self.labelImage1.setPixmap(pixmap)

    def on_find_hamiltion_cycle(self):
        self.clear_right_layout()

        self.inputTextEdit = QTextEdit()
        self.inputTextEdit.setText("""{1: [2,4,5],
2:  [1,3,5,6],
3:  [2,4,7],
4:  [1,3,6,7],
5:  [1,2,8],
6:  [2,4,8],
7:  [3,4,8],
8:  [5,6,7]}""")
        self.inputTextEdit.setMaximumHeight(250)
        self.layout4=QVBoxLayout()
        find_cycle = QPushButton('Find Hamiltion Cycle',self)
        self.layout4.addWidget(self.inputTextEdit)
        self.layout4.addWidget(find_cycle)
        self.labelImage1 = QLabel()
        self.labelImage3 = QLabel()

        labelImage2 = QLabel('------------------------------------------>')
        self.layout3=QHBoxLayout()
        self.layout3.addWidget(self.labelImage1)
        self.layout3.addWidget(labelImage2)
        self.layout3.addWidget(self.labelImage3)

        self.layoutRightGroupBox.addLayout(self.layout4)
        self.layoutRightGroupBox.addLayout(self.layout3)
        find_cycle.clicked.connect(self.on_click_find_cycle)

    def on_click_find_cycle(self):
        # find_Hamiltion_cycle
        data['graph']=ast.literal_eval(self.inputTextEdit.toPlainText())
        AdjacencyList(data).graphVisualization()
        pixmap = QPixmap('src/__imgcache__/Representation.png')
        self.labelImage1.setPixmap(pixmap)
        self.labelImage3.setText(str(find_Hamiltion_cycle(AdjacencyList(data).graph,1,[])))