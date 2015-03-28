import sys
sys.path.append(r'C:\Program Files\IronPython 2.7\Lib')
sys.path.append(r'C:\Program Files\IronPython 2.7')
import clr
clr.AddReference('IronPython')
clr.AddReference('IronPython.Modules')
clr.AddReference('System')
clr.AddReference('System.Windows.Forms')
clr.AddReference('System.Drawing')
from System.Drawing import *
from System.Windows.Forms import *
import System
from System import String
from System import Diagnostics
from System.Diagnostics import Process
from System.Runtime import InteropServices

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._label1 = System.Windows.Forms.Label()
		self._textBox1 = System.Windows.Forms.TextBox()
		self._button1 = System.Windows.Forms.Button()
		self._label2 = System.Windows.Forms.Label()
		self._textBox2 = System.Windows.Forms.TextBox()
		self._label3 = System.Windows.Forms.Label()
		self._label4 = System.Windows.Forms.Label()
		self._label5 = System.Windows.Forms.Label()
		self.SuspendLayout()
		# 
		# label1
		# 
		self._label1.Location = System.Drawing.Point(0, 250)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(309, 30)
		self._label1.TabIndex = 0
		self._label1.Text = "By IronManMark20 based on SuprVillain's program"
		self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# textBox1
		# 
		self._textBox1.Anchor = System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Bottom | System.Windows.Forms.AnchorStyles.Left | System.Windows.Forms.AnchorStyles.Right
		self._textBox1.BorderStyle = System.Windows.Forms.BorderStyle.None
		self._textBox1.Font = System.Drawing.Font("Microsoft Sans Serif", 11.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._textBox1.Location = System.Drawing.Point(98, 100)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(116, 17)
		self._textBox1.TabIndex = 1
		self._textBox1.Text = "640*480"
		self._textBox1.TextAlign = System.Windows.Forms.HorizontalAlignment.Center
		# 
		# button1
		# 
		self._button1.Font = System.Drawing.Font("Microsoft Sans Serif", 9.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button1.Location = System.Drawing.Point(119, 224)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(75, 23)
		self._button1.TabIndex = 2
		self._button1.Text = "Set Size"
		self._button1.UseVisualStyleBackColor = True
		self._button1.Enabled=True
		self._button1.Click+=self.buttonPressed
		# 
		# label2
		# 
		self._label2.Anchor = System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Bottom | System.Windows.Forms.AnchorStyles.Left | System.Windows.Forms.AnchorStyles.Right
		self._label2.Font = System.Drawing.Font("Microsoft Sans Serif", 9.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label2.Location = System.Drawing.Point(50, 9)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(230, 51)
		self._label2.TabIndex = 4
		self._label2.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		self._label2.Click += self.Label2Click
		# 
		# textBox2
		# 
		self._textBox2.Anchor = System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Bottom | System.Windows.Forms.AnchorStyles.Left | System.Windows.Forms.AnchorStyles.Right
		self._textBox2.BorderStyle = System.Windows.Forms.BorderStyle.None
		self._textBox2.Font = System.Drawing.Font("Microsoft Sans Serif", 11.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._textBox2.Location = System.Drawing.Point(98, 172)
		self._textBox2.Name = "textBox2"
		self._textBox2.Size = System.Drawing.Size(116, 17)
		self._textBox2.TabIndex = 5
		self._textBox2.Text = "0,0"
		self._textBox2.TextAlign = System.Windows.Forms.HorizontalAlignment.Center
		# 
		# label3
		# 
		self._label3.Font = System.Drawing.Font("Microsoft Sans Serif", 11.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label3.Location = System.Drawing.Point(50, 9)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(230, 51)
		self._label3.TabIndex = 6
		self._label3.Text = "Set the desired size of the Start Menu, then the desired position."
		self._label3.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		self._label3.Click += self.Label3Click
		# 
		# label4
		# 
		self._label4.Font = System.Drawing.Font("Microsoft Sans Serif", 11.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label4.Location = System.Drawing.Point(98, 60)
		self._label4.Name = "label4"
		self._label4.Size = System.Drawing.Size(116, 23)
		self._label4.TabIndex = 7
		self._label4.Text = "Size (x*y)"
		self._label4.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		self._label4.Click += self.Label4Click
		# 
		# label5
		# 
		self._label5.Font = System.Drawing.Font("Microsoft Sans Serif", 9.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label5.Location = System.Drawing.Point(98, 133)
		self._label5.Name = "label5"
		self._label5.Size = System.Drawing.Size(116, 36)
		self._label5.TabIndex = 8
		self._label5.Text = "Position Top, Left"
		self._label5.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		self._label5.Click += self.Label5Click
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.SystemColors.MenuBar
		self.ClientSize = System.Drawing.Size(312, 289)
		self.Controls.Add(self._label5)
		self.Controls.Add(self._label4)
		self.Controls.Add(self._label3)
		self.Controls.Add(self._textBox2)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._textBox1)
		self.Controls.Add(self._label1)
		from System.Drawing import Icon
		self.Icon = Icon("modernStart.ico")
		self.MaximizeBox = False
		self.Name = "MainForm"
		self.Text = "StartMenuResizer"
		self.TopMost = True
		self.ResumeLayout(False)
		self.PerformLayout()
	
		
	
	def buttonPressed(self, sender, e):
		self.sy=int(Screen.PrimaryScreen.WorkingArea.Height)
		self.sx=int(Screen.PrimaryScreen.WorkingArea.Width)
		self.sizesettings=self._textBox1.Text
		self.locus=self._textBox2.Text
		self.loci=self.locus.split(",")
		self.x=self.loci[0]
		self.y=self.loci[1]
		self.sizes=self.sizesettings.split('*')
		print self.sizes
		self.h=self.sizes[1]
		self.w=self.sizes[0]
		if self.sx>self.x:
			MessageBox("Your width is too large", "StartMenuResizer")
		elif self.sy>self.y:
			MessageBox("Your height is too large", "StartMenuResizer")
		else:
			self.ResizeStart(self.w,self.h,self.x,self.y)

	def Label2Click(self, sender, e):
		pass

	def Label3Click(self, sender, e):
		pass

	def Label4Click(self, sender, e):
		pass

	def Label5Click(self, sender, e):
		pass
	def ResizeStart(self,w,h,t,l):
		clr.AddReferenceToFileAndPath('./ResizeWindow.dll')
		print "in resize"
		import ModernStart
		from ModernStart import Resize 
		Res=Resize()
		if w==None or h==None or t==None or l==None:
			Res.ResizeStartWindow(0,610,1040,0,0)
		else:
			Res.ResizeStartWindow(0,int(w),int(h),int(t),int(l))

clr.AddReference('System.Windows.Forms')
clr.AddReference('System.Drawing')
import System
import sys
from System.Windows.Forms import Application
def ResizeStart(w,h,t,l):
	clr.AddReferenceToFileAndPath('./ResizeWindow.dll')
	import ModernStart
	from ModernStart import Resize
	Res=Resize()
	if w==None or h==None or t==None or l==None:
		Res.ResizeStartWindow(0,610,1040,0,0)
	else:
		Res.ResizeStartWindow(0,int(w),int(h),int(t),int(l))
def gui():
	Application.EnableVisualStyles()
	form = MainForm()
	Application.Run(form)
def about(args):
	print "This program allows you to resize the start menu.\n You can use the command line or the GUI\n Usage:\n Argument 1 is the desired width of the start menu\n Argument 2 is the desired height of the start menu\n Argument 3 is the desired distance from the top\n Argument 4 is the desired distance from the left"
	print ""
	arg=""
	for i in args:
		arg+="value:"+str(i)+"\n"
	print "Your args:\n"+arg
	diag='''                               @                                   
                               @                                   
                               @                                   
                               @                                   
                               @                                   
                               @  Top                                 
                               @                                   
                               @                                   
                               @                                   
                               @                                   
                               @                                   
                               @                                   
                   @@@@@@@@@@@@@@@@@@@@@@@@@@@                     
                   ...........................                     
                   ...........................                     
                   ...........................                     
                   ...........................                     
                   ...........................                     
                   ...........................                     
                   ...........................                     
                   ...........................                     
                   ...........................  Height            
                   .......Start Menu..........                     
                   ...........................                     
       Left        ...........................                     
@@@@@@@@@@@@@@@@@@@...........................                     
                   ...........................                     
                   ...........................                     
                   ...........................                     
                   ...........................                     
                   ...........................                     
                   ...........................                     
                   ...........................                     
                   @@@@@@@@@@@@@@@@@@@@@@@@@@@                     
                                                                   
                              Width                               '''
	print "Below is a diagram that illustrates the dimensions."
	print diag
if __name__=="__main__":
	args=sys.argv
	
	if len(args)!=5:
		if len(args)==1:
			gui()
		else:
			print "too many or too few args\n"
			about(args)
	else:
		try:
			args.remove(args[0])
			for i in args:
				i=int(i)
		except:
			print "Error non-int input\n"
			about()
		ResizeStart(args[0],args[1],args[2],args[3])
