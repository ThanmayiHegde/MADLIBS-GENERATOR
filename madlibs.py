from PIL import Image, ImageTk
import tkinter as tk
IMAGE_PATH = 'IMAGE.jpg'
WIDTH, HEIGTH = 1500, 800

root = tk.Tk()
root.geometry('1500x800')

canvas = tk.Canvas(root, width=1500, height=800)
canvas.pack()

img = ImageTk.PhotoImage(Image.open(IMAGE_PATH).resize((WIDTH, HEIGTH), Image.ANTIALIAS))
canvas.background = img  # Keep a reference in case this code is put in a function.
bg = canvas.create_image(0, 0, anchor=tk.NW, image=img)
ll1=tk.Label(root,text="FLOWER POT OF FUN !!!!",font="calibri")
ll1_window=canvas.create_window(1400,750,window=ll1)
# Put a tkinter widget on the canvas.
root.title('Mad Libs Generator')
label1=tk.Label(root, text= 'Mad Libs Generator \n Have Fun.......!' , font = 'arial 35 bold')
label1_window=canvas.create_window(700,50,anchor=tk.CENTER,window=label1)
label2=tk.Label(root, text= 'Click Any One:' , font = 'calibri 25 bold',bg='violet')
label2_window=canvas.create_window(120,100,window=label2)
def madlib1():
	l1=tk.Label(root,text="Enter the animal name :",font = 'calibri 10 bold',bg='sky blue')
	l1_window=canvas.create_window(400,200,window=l1)
	global e1
	e1=tk.Entry(root,width=50,bg='yellow')
	e1_window=canvas.create_window(700,200,window=e1)
	def lib10():
		l2=tk.Label(root,text="Enter the profession name :",font = 'calibri_itallic 10 bold',bg='sky blue')
		l2_window=canvas.create_window(400,250,window=l2)
		global e2
		e2=tk.Entry(root,width=50,bg='yellow')
		e2_window=canvas.create_window(700,250,window=e2)
		def lib20():
			l3=tk.Label(root,text="Enter the cloth name :",font = 'calibri 10 bold',bg='sky blue')
			l3_window=canvas.create_window(400,300,window=l3)
			global e3
			e3=tk.Entry(root,width=50,bg='yellow')
			e3_window=canvas.create_window(700,300,window=e3)
			def lib30():
				l4=tk.Label(root,text="Enter the thing name :",font = 'calibri 10 bold',bg='sky blue')
				l4_window=canvas.create_window(400,350,window=l4)
				global e4
				e4=tk.Entry(root,width=50,bg='yellow')
				e4_window=canvas.create_window(700,350,window=e4)
				def lib40():
					l5=tk.Label(root,text="Enter a name :",font = 'calibri 10 bold',bg='sky blue')
					l5_window=canvas.create_window(400,400,window=l5)
					global e5
					e5=tk.Entry(root,width=50,bg='yellow')
					e5_window=canvas.create_window(700,400,window=e5)
					def lib50():
						l6=tk.Label(root,text="Enter a place name :",font = 'calibri 10 bold',bg='sky blue')
						l6_window=canvas.create_window(400,450,window=l6)
						global e6
						e6=tk.Entry(root,width=50,bg='yellow')
						e6_window=canvas.create_window(700,450,window=e6)
						def lib60():
							l7=tk.Label(root,text="Enter a verb in ing :",font = 'calibri 10 bold',bg='sky blue')
							l7_window=canvas.create_window(400,500,window=l7)
							global e7
							e7=tk.Entry(root,width=50,bg='yellow')
							e7_window=canvas.create_window(700,500,window=e7)
							def lib70():
								l8=tk.Label(root,text="Enter a food name :",font = 'calibri 10 bold',bg='sky blue')
								l8_window=canvas.create_window(400,550,window=l8)
								global e8
								e8=tk.Entry(root,width=50,bg='yellow')
								e8_window=canvas.create_window(700,550,window=e8)
								def mycall1():
									message1='In the outskirts of '+e6.get()+' a watchman said mysteriously that he saw someone as the street lights flashed!!!!! at midnight.\n'+e5.get()+' and I were ready with '+e8.get()+' to surprise him on his birthday. The first photo we really wanted was a \n picture of pretty smile on his face with happiness . So we secretly hiered a photographer to click the snaps \n which we wanted .Just dressed as ' +e1.get()+' to add more colours for the event and pretending to be a ' +e2.get()+' \n like him .When he saw us, he bursted out with tears, with  bit of satisfaction. We both looked like '+e4.get()+ '\n wearing '+e3.get()+' and ' +e7.get()+' --exactly what we had in mind on his birthday.'
									lab1=tk.Label(root,text=message1,font = 'calibri_itallic 15 bold',fg='violet')
									lab1_window=canvas.create_window(720,690,window=lab1)
								b8=tk.Button(root,text="submit",command=lambda:mycall1(),bg='red')
								b8_window=canvas.create_window(900,550,window=b8)		
							b7=tk.Button(root,text="click next",command=lambda:lib70(),bg='light green')
							b7_window=canvas.create_window(900,500,window=b7)
						b6=tk.Button(root,text="click next",command=lambda:lib60(),bg='light green')
						b6_window=canvas.create_window(900,450,window=b6)
					b5=tk.Button(root,text="click next",command=lambda:lib50(),bg='light green')
					b5_window=canvas.create_window(900,400,window=b5)
				b4=tk.Button(root,text="click next",command=lambda:lib40(),bg='light green')
				b4_window=canvas.create_window(900,350,window=b4)
			b3=tk.Button(root,text="click next",command=lambda:lib30(),bg='light green')
			b3_window=canvas.create_window(900,300,window=b3)
		b2=tk.Button(root,text="click next",command=lambda:lib20(),bg='light green')
		b2_window=canvas.create_window(900,250,window=b2)
	b1=tk.Button(root,text="click next",command=lambda:lib10(),bg='light green')
	b1_window=canvas.create_window(900,200,window=b1)


def madlib2():
	l11=tk.Label(root,text="Enter the adjactive:",font = 'calibri_itallic 10 bold',bg='sky blue')
	l11_window=canvas.create_window(400,200,window=l11)
	global e11
	e11=tk.Entry(root,width=50,bg='yellow')
	e11_window=canvas.create_window(700,200,window=e11)
	def lib101():
		l21=tk.Label(root,text="Enter the name of a person:",font = 'calibri 10 bold',bg='sky blue')
		l21_window=canvas.create_window(400,250,window=l21)
		global e21
		e21=tk.Entry(root,width=50,bg='yellow')
		e21_window=canvas.create_window(700,250,window=e21)
		def lib201():
			l31=tk.Label(root,text="Enter a place:",font = 'calibri 10 bold',bg='sky blue')
			l31_window=canvas.create_window(400,300,window=l31)
			global e31
			e31=tk.Entry(root,width=50,bg='yellow')
			e31_window=canvas.create_window(700,300,window=e31)
			def lib301():
				l41=tk.Label(root,text="Enter the colour:",font = 'calibri 10 bold',bg='sky blue')
				l41_window=canvas.create_window(400,350,window=l41)
				global e41
				e41=tk.Entry(root,width=50,bg='yellow')
				e41_window=canvas.create_window(700,350,window=e41)
				def lib401():
					l51=tk.Label(root,text="Enter a thing :",font = 'calibri 10 bold',bg='sky blue')
					l51_window=canvas.create_window(400,400,window=l51)
					global e51
					e51=tk.Entry(root,width=50,bg='yellow')
					e51_window=canvas.create_window(700,400,window=e51)
					def lib501():
						l61=tk.Label(root,text="Enter the adjactive:",font = 'calibri 10 bold',bg='sky blue')
						l61_window=canvas.create_window(400,450,window=l61)
						global e61
						e61=tk.Entry(root,width=50,bg='yellow')
						e61_window=canvas.create_window(700,450,window=e61)
						def lib601():
							l71=tk.Label(root,text="Enter the food name:",font = 'calibri 10 bold',bg='sky blue')
							l71_window=canvas.create_window(400,500,window=l71)
							global e71
							e71=tk.Entry(root,width=50,bg='yellow')
							e71_window=canvas.create_window(700,500,window=e71)
							def lib701():
								l81=tk.Label(root,text="Enter a name of insect:",font = 'calibri 10 bold',bg='sky blue')
								l81_window=canvas.create_window(400,550,window=l81)
								global e81
								e81=tk.Entry(root,width=50,bg='yellow')
								e81_window=canvas.create_window(700,550,window=e81)
								def lib801():
									l91=tk.Label(root,text="Enter a verb:",font='calibri 10 bold',bg='sky blue')
									l91_window=canvas.create_window(400,600,window=l91)
									global e91
									e91=tk.Entry(root,width=50,bg='yellow')
									e91_window=canvas.create_window(700,600,window=e91)														
									def mycall2():
										message2='Pizza was invented by '+e11.get()+' person called '+e21.get()+' in '+e31.get()+ ' .To\n make a pizza, you need '+e41.get()+' coloured '+e51.get()+' You cover it with a \n '+e61.get()+' ,cheese and sauce. Other kids \nmay like any other food like '+e71.get() +' ,but I like Pizza and i have it\n with my '+e81.get()+' . I '+e91.get()+' and eat pizza.'
										lab2=tk.Label(root,text=message2,font = 'calibri_itallic 15 bold',fg='violet')
										lab2_window=canvas.create_window(720,690,window=lab2)
									b91=tk.Button(root,text='submit',command=lambda:mycall2(),bg='red')
									b91_window=canvas.create_window(900,600,window=b91)									
								b81=tk.Button(root,text='click next',command=lambda:lib801(),bg='light green')
								b81_window=canvas.create_window(900,550,window=b81)		
							b71=tk.Button(root,text="click next",command=lambda:lib701(),bg='light green')
							b71_window=canvas.create_window(900,500,window=b71)
						b61=tk.Button(root,text="click next",command=lambda:lib601(),bg='light green')
						b61_window=canvas.create_window(900,450,window=b61)
					b51=tk.Button(root,text="click next",command=lambda:lib501(),bg='light green')
					b51_window=canvas.create_window(900,400,window=b51)
				b41=tk.Button(root,text="click next",command=lambda:lib401(),bg='light green')
				b41_window=canvas.create_window(900,350,window=b41)
			b31=tk.Button(root,text="click next",command=lambda:lib301(),bg='light green')
			b31_window=canvas.create_window(900,300,window=b31)
		b21=tk.Button(root,text="click next",command=lambda:lib201(),bg='light green')
		b21_window=canvas.create_window(900,250,window=b21)
	b11=tk.Button(root,text="click next",command=lambda:lib101(),bg='light green')
	b11_window=canvas.create_window(900,200,window=b11)
  
def madlib3():
	l111=tk.Label(root,text="Enter person name:",font = 'calibri 10 bold',bg='sky blue')
	l111_window=canvas.create_window(400,200,window=l111)
	global e111
	e111=tk.Entry(root,width=50,bg='yellow')
	e111_window=canvas.create_window(700,200,window=e111)
	def lib300():
		l211=tk.Label(root,text="Enter mode of traveling :",font = 'calibri 10 bold',bg='sky blue')
		l211_window=canvas.create_window(400,250,window=l211)
		global e211
		e211=tk.Entry(root,width=50,bg='yellow')
		e211_window=canvas.create_window(700,250,window=e211)
		def lib400():
			l311=tk.Label(root,text="Enter number of hours :",font = 'calibri 10 bold',bg='sky blue')
			l311_window=canvas.create_window(400,300,window=l311)
			global e311
			e311=tk.Entry(root,width=50,bg='yellow')
			e311_window=canvas.create_window(700,300,window=e311)
			def lib500():
				l411=tk.Label(root,text="Enter a adjective : ",font = 'calibri 10 bold',bg='sky blue')
				l411_window=canvas.create_window(400,350,window=l411)
				global e411
				e411=tk.Entry(root,width=50,bg='yellow')
				e411_window=canvas.create_window(700,350,window=e411)
				def lib600():
					l511=tk.Label(root,text="Enter a type of dressing style:",font = 'calibri 10 bold',bg='sky blue')
					l511_window=canvas.create_window(400,400,window=l511)
					global e511
					e511=tk.Entry(root,width=50,bg='yellow')
					e511_window=canvas.create_window(700,400,window=e511)
					def lib700():
						l611=tk.Label(root,text="Enter adverb :",font = 'calibri 10 bold',bg='sky blue')
						l611_window=canvas.create_window(400,450,window=l611)
						global e611
						e611=tk.Entry(root,width=50,bg='yellow')
						e611_window=canvas.create_window(700,450,window=e611)
						def lib800():
							l711=tk.Label(root,text="Enter verb :",font = 'calibri 10 bold',bg='sky blue')
							l711_window=canvas.create_window(400,500,window=l711)
							global e711
							e711=tk.Entry(root,width=50,bg='yellow')
							e711_window=canvas.create_window(700,500,window=e711)
							def lib900():
								l811=tk.Label(root,text="Enter place name:",font = 'calibri 10 bold',bg='sky blue')
								l811_window=canvas.create_window(400,550,window=l811)
								global e811
								e811=tk.Entry(root,width=50,bg='yellow')
								e811_window=canvas.create_window(700,550,window=e811)
								def lib1000():
									l911=tk.Label(root,text="Enter a animal name :",font='calibri 10 bold',bg='sky blue')
									l911_window=canvas.create_window(400,600,window=l911)
									global e911
									e911=tk.Entry(root,width=50,bg='yellow')
									e911_window=canvas.create_window(700,600,window=e911)														
									def mycall3():
										message3='Last month,I went to Disney World with '+e111.get()+'\n.We traveled for '+e211.get()+' hours by '+e311.get()+'.Finally, we\n arrived and I was very '+e411.get()+'.There were also people \ndressed up in '+e511.get()+' costumes.Later we  went on a \nride, where '+e111.get()+' nearly fell off a ride due to which we\n '+e611.get()+' went back to the hotel and '+e711.get()+' there.Next year, I want to\n go to '+e811.get()+' , where we can find '+e911.get()+'.'
										lab3=tk.Label(root,text=message3,font = 'calibri_itallic 15 bold',fg='violet')
										lab3_window=canvas.create_window(720,710,window=lab3)
									b911=tk.Button(root,text='submit',command=lambda:mycall3(),bg='red')
									b911_window=canvas.create_window(900,600,window=b911)									
								b811=tk.Button(root,text='click next',command=lambda:lib1000(),bg='light green')
								b811_window=canvas.create_window(900,550,window=b811)		
							b711=tk.Button(root,text="click next",command=lambda:lib900(),bg='light green')
							b711_window=canvas.create_window(900,500,window=b711)
						b611=tk.Button(root,text="click next",command=lambda:lib800(),bg='light green')
						b611_window=canvas.create_window(900,450,window=b611)
					b511=tk.Button(root,text="click next",command=lambda:lib700(),bg='light green')
					b511_window=canvas.create_window(900,400,window=b511)
				b411=tk.Button(root,text="click next",command=lambda:lib600(),bg='light green')
				b411_window=canvas.create_window(900,350,window=b411)
			b311=tk.Button(root,text="click next",command=lambda:lib500(),bg='light green')
			b311_window=canvas.create_window(900,300,window=b311)
		b211=tk.Button(root,text="click next",command=lambda:lib400(),bg='light green')
		b211_window=canvas.create_window(900,250,window=b211)
	b111=tk.Button(root,text="click next",command=lambda:lib300(),bg='light green')
	b111_window=canvas.create_window(900,200,window=b111)

######buttons   
button2 = tk.Button(root, text = 'PHOTOGRAPHER', font = 'calibri_italic 15 bold',bg='pink',command=madlib1)
button2_window = canvas.create_window(100, 200, window=button2)
button3 = tk.Button(root, text = 'PIZZA LOVE', font = 'calibri_italic 15 bold',bg='pink',command=madlib2)
button3_window = canvas.create_window(100, 300, window=button3)
button4 = tk.Button(root, text = 'MY TRIP TO DISNEY WORLD', font = 'calibri_italic 15 bold',bg="pink",command=madlib3)
button4_window = canvas.create_window(150, 400, window=button4)

root.mainloop()