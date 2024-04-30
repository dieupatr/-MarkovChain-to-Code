from Test1_MarkovChain import *


Matrix=LoadModell_MarkovChain_Test1()


mu=[1,0]

[States,mu]=CallMarkovChain_Test1(mu,Matrix)

print([States,mu])
