from impo import *
p1=score(0,0,0)
p2=score(0,0,0)
def output(count,a,s,d,e,f,g,h,j):
	print "Iteration : ",count
	print "Player%d   :  %s"% (a,s)
	print "P1 Score:",d
	print "P2 Score:",e
	print "P1 Game Win Count:",f
	print "P2 Game Win count:",g
	print "P1 Set Win Count:",h
	print "P2 Set Win count:",j
y=0
count=0
import sys
csv=open(sys.argv[-1],"r")
for line in (raw.strip().split() for raw in csv):
	count+=1
	s=line[1]
	k=p1._game+p2._game
	if s == 'Serve':
		#print "*"
		y=1
		output(count,k%2+1,s,p1._point,p2._point,p1._game,p2._game,p1._sets,p2._sets)
	elif s == 'Ace':
		y=0
		#print "**"
		if(k%2+1==1):
			if(p1._point==0)or(p1._point==15):
				p1._point+=15
			elif(p1._point==30):
				p1._point+=10
			elif(p1._point==40)and(p2._point<40):
				p1._point=0
				p2._point=0
				p1._game+=1
				if((p1._game>=6)and(p1._game-p2._game>=2))or(p1._game==7):
					p1._sets+=1
					p1._game=0
					p2._game=0
			elif(p1._point==40)and(p2._point==40):
			  	p1._point='Advantage'
			elif(p1._point==40)and(p2._point=='Advantage'):
				p2._point=40
			else:
				p1._point=0
				p2._point=0
				p1._game+=1
				if((p1._game>6)and(p1._game-p2._game>=2))or(p1._game==7):
					p1._sets+=1
					p1._game=0
					p2._game=0
			if(p1._point==40)and(p2._point==40):
				output(count,1,s,'Duece','Duece',p1._game,p2._game,p1._sets,p2._sets)
			elif(p1._point=='Advantage'):
				output(count,1,s,p1._point," ",p1._game,p2._game,p1._sets,p2._sets)
			else:
				output(count,1,s,p1._point,p2._point,p1._game,p2._game,p1._sets,p2._sets)
		else:
			if(p2._point==0)or(p2._point==15):
				p2._point+=15
			elif(p2._point==30):
				p2._point+=10
			elif(p2._point==40)and(p1._point<40):
				p1._point=0
				p2._point=0
				p2._game+=1
				if((p2._game>=6)and(p2._game-p2._game>=2))or(p2._game==7):
					p2._sets+=1
					p2._game=0
					p1._game=0
			elif(p1._point==40)and(p2._point==40):
			  	p2._point='Advantage'
			elif(p2._point==40)and(p1._point=='Advantage'):
				p1._point=40
			else:
				p1._point=0
				p2._point=0
				p2._game+=1
				if((p2._game>=6)and(p2._game-p2._game>=2))or(p2._game==7):
					p2._sets+=1
					p1._game=0
					p2._game=0
			if(p1._point==40)and(p2._point==40):
				output(count,2,s,'Duece','Duece',p1._game,p2._game,p1._sets,p2._sets)
			elif(p2._point=='Advantage'):
				output(count,2,s," ",p2._point,p1._game,p2._game,p1._sets,p2._sets)
			else:
				output(count,2,s,p1._point,p2._point,p1._game,p2._game,p1._sets,p2._sets)
	elif (s == 'Backhand')or(s=='Forehand'):
		#print "***"
		o=k+y
		output(count,(o%2)+1,s,p1._point,p2._point,p1._game,p2._game,p1._sets,p2._sets)
		y+=1
	elif (s=='Fault')or(s=='Nets'):
		y=0
		#print "****"
		if(k%2+1==2):
			if(p1._point==0)or(p1._point==15):
				p1._point+=15
			elif(p1._point==30):
				p1._point+=10
			elif(p1._point==40)and(p2._point<40):
				p1._point=0
				p2._point=0
				p1._game+=1
				if((p1._game>=6)and(p1._game-p2._game>=2))or(p1._game==7):
					p1._sets+=1
					p1._game=0
					p2._game=0
			elif(p1._point==40)and(p2._point==40):
			  	p1._point='Advantage'
			elif(p1._point==40)and(p2._point=='Advantage'):
				p2._point=40
			else:
				p1._point=0
				p2._point=0
				p1._game+=1
				if((p1._game>=6)and(p1._game-p2._game>=2))or(p1._game==7):
					p1._sets+=1
					p1._game=0
					p2._game=0
			if(p1._point==40)and(p2._point==40):
				output(count,2,s,'Duece','Duece',p1._game,p2._game,p1._sets,p2._sets)
			elif(p1._point=='Advantage'):
				output(count,2,s,p1._point," ",p1._game,p2._game,p1._sets,p2._sets)
			else:
				output(count,2,s,p1._point,p2._point,p1._game,p2._game,p1._sets,p2._sets)
		else:
			if(p2._point==0)or(p2._point==15):
				p2._point+=15
			elif(p2._point==30):
				p2._point+=10
			elif(p2._point==40)and(p1._point<40):
				p1._point=0
				p2._point=0
				p2._game+=1
				if((p2._game>=6)and(p2._game-p2._game>=2))or(p2._game==7):
					p2._sets+=1
					p2._game=0
					p1._game=0
			elif(p1._point==40)and(p2._point==40):
			  	p2._point='Advantage'
			elif(p2._point==40)and(p1._point=='Advantage'):
				p1._point=40
			else:
				p1._point=0
				p2._point=0
				p2._game+=1
				if((p2._game>=6)and(p2._game-p2._game>=2))or(p2._game==7):
					p2._sets+=1
					p1._game=0
					p2._game=0
			if(p1._point==40)and(p2._point==40):
				output(count,1,s,'Duece','Duece',p1._game,p2._game,p1._sets,p2._sets)
			elif(p2._point=='Advantage'):
				output(count,1,s," ",p2._point,p1._game,p2._game,p1._sets,p2._sets)
			else:
				output(count,1,s,p1._point,p2._point,p1._game,p2._game,p1._sets,p2._sets)
			y=0
	elif((s =='PointLost-SameSide')or(s == 'PointLost-Out'))or(s == 'PointLost-CouldNotReach'):
		l=k
		y+=1
		l+=y
		temp=0
		#print l,y
		#print "*****"
		if (s=='PointLost-CouldNotReach'):
			temp=1
		if((l%2==1)and(temp==0))or((l%2==0)and(temp==1)):
			#print "#"
			if(p1._point==0)or(p1._point==15):
				p1._point+=15
			elif(p1._point==30):
				p1._point+=10
			elif(p1._point==40)and(p2._point<40):
				p1._point=0
				p2._point=0
				p1._game+=1
				if((p1._game>=6)and(p1._game-p2._game>=2))or(p1._game==7):
					p1._sets+=1
					p1._game=0
					p2._game=0
			elif(p1._point==40)and(p2._point==40):
			  	p1._point='Advantage'
			elif(p1._point==40)and(p2._point=='Advantage'):
				p2._point=40
			else:
				p1._point=0
				p2._point=0
				p1._game+=1
				if((p1._game>=6)and(p1._game-p2._game>=2))or(p1._game==7):
					p1._sets+=1
					p1._game=0
					p2._game=0
			if(p1._point==40)and(p2._point==40):
				output(count,2,s,'Duece','Duece',p1._game,p2._game,p1._sets,p2._sets)
			elif(p1._point=='Advantage'):
				output(count,2,s,p1._point," ",p1._game,p2._game,p1._sets,p2._sets)
			else:
				output(count,2,s,p1._point,p2._point,p1._game,p2._game,p1._sets,p2._sets)
		elif((l%2==1)and(temp==1))or((l%2==0)and(temp==0)):
			#print "##"			
			if(p2._point==0)or(p2._point==15):
				p2._point+=15
			elif(p2._point==30):
				p2._point+=10
			elif(p2._point==40)and(p1._point<40):
				p1._point=0
				p2._point=0
				p2._game+=1
				if((p2._game>=6)and(p2._game-p2._game>=2))or(p2._game==7):
					p2._sets+=1
					p2._game=0
					p1._game=0
			elif(p1._point==40)and(p2._point==40):
			  	p2._point='Advantage'
			elif(p2._point==40)and(p1._point=='Advantage'):
				p1._point=40
			else:
				p1._point=0
				p2._point=0
				p2._game+=1
				if((p2._game>=6)and(p2._game-p2._game>=2))or(p2._game==7):
					p2._sets+=1
					p1._game=0
					p2._game=0
			if(p1._point==40)and(p2._point==40):
				output(count,1,s,'Duece','Duece',p1._game,p2._game,p1._sets,p2._sets)
			elif(p2._point=='Advantage'):
				output(count,1,s," ",p2._point,p1._game,p2._game,p1._sets,p2._sets)
			else:
				output(count,1,s,p1._point,p2._point,p1._game,p2._game,p1._sets,p2._sets)
		l=0
		y=0		   
