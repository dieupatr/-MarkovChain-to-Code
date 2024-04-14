from LexDrawio import *

import os

import pickle

import sys


def create_folder(folder_name):
    try:
        os.makedirs(folder_name)
        
    except :
        pass

def pickle_data(data, filename):
    """
    Pickle a dictionary to a file.

    Parameters:
        dictionary (dict): The dictionary to pickle.
        filename (str): The name of the file to pickle to.
    """
    with open(filename, 'wb') as file:
        pickle.dump(data, file)


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

def LoadModell_MarkovChain_{TabName}():
       

       with open('Model_MarkovChain_{TabName}'+'/PMatrix_{TabName}.pkl', 'rb') as file:   Matrix = pickle.load(file)

       return Matrix



def MarkovChain_{TabName}(mu, Matrix):

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
              
                  RootFolder="Modell_MarkovChain_"+TabName

                  create_folder(RootFolder)

                  pickle_data(Matrix, RootFolder+"/"+"PMatrix_"+TabName+".pkl")

                  File=open(RootFolder+"/"+TabName+"_MarkovChain.py",'w')

                  File.write(
                     GenerateCode(Matrix , DescribeState,TabName)

                     )

                  File.close()
              

       

       



         

              
     
###############################
       

file_path=sys.argv[1]

#"MarkovStateDia.drawio"
TabName=sys.argv[2]
#"Test1"

BuildMarkovChainModell(file_path, TabName)







