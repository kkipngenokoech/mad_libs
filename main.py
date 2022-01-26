#MAD LIBS GENERATOR
from IPython.display import clear_output
loop=1
while(loop<10):
    noun_1=input("please enter a noun:")
    pronoun=input("please enter a pronoun:")
    noun_2=input("please enter a second noun:")
    place=input("please enter a place:")
    adjective=input("choose an adjective(describing word):")
    noun_3=input("choose a noun:")
    clear_output()
    print("="*50)
    print(f"be kind to your {noun_1} -footed {pronoun}")
    print(f"for a duck maybe somebody's {noun_2},")
    print(f"be kind to your {pronoun} in {place}")
    print(f"where the weather is always {adjective}")
    print()
    print(f"you may think it is the{noun_3}")
    print("well it is!^")
    loop=loop+1
