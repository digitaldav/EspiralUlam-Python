import ullam
import sys

if __name__ == "__main__":
    
    if len(sys.argv)<2:
        print("No se ha introducido tamaño de matriz\nUsando tamaño 5x5")
        N=5
        fichero = 'imagen'
    else:
        N=sys.argv[1]
        if N.isdigit() == False:
            print("No se ha introducido un numero\nUsando matriz de tamaño 5x5")
            N=5
        else:
            N = (sys.argv[1])
            print("Generación de Espiral de Ullam con matriz",N+"x"+N)
            N = int(N)

    if len(sys.argv)<3:
        print("No se ha introducido nombre de fichero\nUsando nombre: imagen")
        fichero = 'imagen'
    else:
        if sys.argv[2].isdigit()==False:
            fichero = sys.argv[2]
            print('La imagen generada se guardara en el fichero '+fichero+'.png')
        else:
            print("No se ha introducido nombre de fichero\nUsando nombre: imagen")
            fichero = 'imagen'
            
    a = ullam._InicializarMatriz(N)
    
    ullam._MatrizEspiralUlam(a)
    
    ullam._PintarMatrizPandas(a)
    
    ullam._GenerarImagen(a,fichero)