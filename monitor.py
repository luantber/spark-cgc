import subprocess

def get_procesos():
    result = subprocess.run("jcmd".split(), stdout=subprocess.PIPE)
    sun = "sun.tools.jcmd.JCmd"
    procesos = []
    for linea in result.stdout.decode('utf-8').split("\n"):
        p = linea.split(" ")
        if linea!='' and p[1]!=sun: 
            procesos.append( p ) 
    return procesos
#print ( procesos )
    
def get_porcentajes(procesos):
    porcentajes = []
    for proceso in procesos:
        comando = "jstat -gcutil -t "+proceso[0]
        result = subprocess.run(comando.split(),stdout=subprocess.PIPE).stdout.decode('utf-8')
        #print("Res: ", result)
        parselineares = (result.split("\n")[1].split(" "))
        #4 old 
        #3 eden
    
        porcentaje =  [x  for x in parselineares if x!='' ][4]
        porcentajes.append(porcentaje)
    return porcentajes

procesos = get_procesos()
while len(procesos)!=0:
    porcentajes = get_porcentajes(procesos)
    print (porcentajes)
    gc = False
    for p in porcentajes:
        if float(p) >= 80:
            gc = gc or True
    if gc:
        print("Call GC")
        for p in procesos:    
            comando = "jcmd " +  p[0] + " GC.run"
            print (comando)
            subprocess.run(comando.split(), stdout=subprocess.PIPE)
        

    #procesos = get_procesos()
    