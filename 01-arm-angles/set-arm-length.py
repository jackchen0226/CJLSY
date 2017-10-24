import pickle
import click

@click.command()
@click.option('-l', prompt="Set length of arm", help="A command to save the length of your arm's segment as a pickle file.")
def write(l):
    pkl = open("armlengths.pkl", "wb")
    pickle.dump(float(l), pkl, protocol=pickle.HIGHEST_PROTOCOL)
    pkl.close()

if __name__ == '__main__':
    write()
    

