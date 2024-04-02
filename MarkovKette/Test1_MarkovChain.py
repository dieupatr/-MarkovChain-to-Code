

def MarkovChain_Test1(mu):
       
       Matrix=[[0.3, 0.7], [0.4, 0.6]]
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

       PrintState(mu,States)

       return [States, mu]


#######################


CallMarkovChain_Test1([1,0])





       
