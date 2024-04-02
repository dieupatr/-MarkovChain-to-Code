from LexDrawio import *






def BuildMatrix(States,Probabilitys):

       N=len(States)

       Matrix=[    [0 for i in range(N)]   for j in range(N)  ]

       for tupel in  Probabilitys:

              i=tupel[0]
              j=tupel[1]
              p=Probabilitys[tupel]

              Matrix[i][j]=p


       return Matrix

      # for tupel in  Probabilitys:

              


def ParseMarkovChainFromDiagram(Diagram):

       Blocks=Diagram.blocks
       Arrows=Diagram.arrows


       #Sort States and Labels

       States={   }
       DescribeState={   }
       State_Nr=0

       Labels={     }

       for block in Blocks:

              style=block.Attr["style"][0]
              Id=block.Attr["id"]
              value=block.Attr["value"]
              parent=block.Attr["parent"]

              if style=="ellipse":
                     
                     States[Id]=State_Nr
                     DescribeState[State_Nr]=value
                     State_Nr=State_Nr+1

              if style=="edgeLabel":  Labels[parent]=value


       Probabilitys= {   }

       for arrow in Arrows:

              target=arrow.Attr["target"]
              source=arrow.Attr["source"]
              Id=arrow.Attr["id"]

              try:  
                     target=States[target]
                     source=States[source]
                     value=Labels[Id]    
                     Probabilitys[(source,target)]=float(value)              
              except:
                     pass


       # Build Matrix

       Matrix=BuildMatrix(States,Probabilitys)

       return [Matrix , DescribeState]

     



def ValidProbabilityMatrix(Matrix  , DescribeState):

       for i in range(len(Matrix)):

              p=sum( Matrix[i] )

              if p==1 :
                     continue
              else:

                     value=DescribeState[i]

                     print(f"Error in {value} : the sum of the probabilitys should be one.")
                     
                     return False

       return True

def GenerateCode(Matrix , DescribeState,TabName):



       State=[ DescribeState[key]  for key in DescribeState]
       return f"""

def MarkovChain_{TabName}(mu):
       
       Matrix={Matrix}
       N=len(mu)

       mu_new=[0 for i in range(N) ]

       for j in range(N):

              mu_new[j]=sum([ mu[i]*Matrix[i][j] for i in range(N) ])


       return mu_new

def PrintState(mu,States):

       p=max(mu)
       index=mu.index(p)
       state=States[index]
       print( "The probably state is "+state+ " with p= "+str(p))


def CallMarkovChain_{TabName}(mu):
       States={State}

       N=len(States)
       mu_0=[0 for k in range(N) ]
       mu_0=mu

       mu=MarkovChain_{TabName}(mu)

       #PrintState(mu,States)

       return [States, mu]

       """

       

def BuildMarkovChainModell(file_path, TabName):

       Diagram=ParseDiagramsFromXmlFile(file_path)

       Diagram=Diagram[TabName]

       [Matrix , DescribeState]=ParseMarkovChainFromDiagram(Diagram)

       if ValidProbabilityMatrix(Matrix, DescribeState) :

              File=open(TabName+"_MarkovChain.py",'w')

              File.write(
                     GenerateCode(Matrix , DescribeState,TabName)

                     )
              File.close()
              

       

       



         

              
     
###############################
       

file_path="MarkovStateDia.drawio"
TabName="Test1"

BuildMarkovChainModell(file_path, TabName)







