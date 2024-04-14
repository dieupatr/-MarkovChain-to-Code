

def LoadModell_MarkovChain_Test1():
       

       with open('Model_MarkovChain_Test1'+'/PMatrix_Test1.pkl', 'rb') as file:   Matrix = pickle.load(file)

       return Matrix



def MarkovChain_Test1(mu, Matrix):

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


def CallMarkovChain_Test1(mu):

       
       States=['E', 'A']

       N=len(States)
       mu_0=[0 for k in range(N) ]
       mu_0=mu

       mu=MarkovChain_Test1(mu)

       #PrintState(mu,States)

       return [States, mu]

       