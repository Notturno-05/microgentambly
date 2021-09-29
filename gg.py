import sys
import re
vars={}
lines=open(sys.argv[1],"r").read().split("\n")
lines=list(map(lambda el: el.lstrip(),lines))
i=0
jumps={}
def sostT(text,vars):
     matches=re.findall(r"(?<=\$)(.*)(?=\$)",text)
     for match in matches:
          if match in vars.keys():
              text=text.replace("$"+match+"$",str(vars[match]))
     return text
try:
    for i in range(len(lines)):
        ag=lines[i].split(" ")
        if len(ag[0]):
            if ag[0][0]==":":
                jumps[ag[0][1:]]=i
    i=0
    while lines[i].strip()!="END" or i > len(lines) :
        #print(lines[i])
        if lines[i][0]=="#":
            i+=1
            continue
        ag=lines[i].split(" ")
        if ag[0] == "INT":
            vars[ag[1]]=0
        elif ag[0]=="SET":
            vars[ag[1]]=ag[2]
        elif ag[0]=="DEC":
            if len(ag)==3:
                if ag[2].isnumeric():
                    n=int(ag[2])
                else:
                    n=int(vars[ag[2]])
            else:
                n = 1
            vars[ag[1]]=int(vars[ag[1]])-n
        elif ag[0]=="INC":
            if len(ag)==3:
                if ag[2].isnumeric():
                    n=int(ag[2])
                else:
                    n=int(vars[ag[2]])
            else:
                n = 1
            vars[ag[1]]=int(vars[ag[1]])+n
        elif ag[0]=="CP":
            vars[ag[1]]=vars[ag[2]]
        elif ag[0]=="MOD":
            if str(ag[1]).isnumeric():
                m=float(ag[1])
            else:
                m=float(vars[ag[1]])
            if str(ag[2]).isnumeric():
                modTerm=float(ag[2])
            else:
                modTerm=float(vars[ag[2]])
            vars[ag[3]]=m%modTerm
        elif ag[0]=="JLE":
            if str(ag[3]).isnumeric():
                athr=float(ag[3])
            else:
                athr=float(vars[ag[3]])
            if vars[ag[2]]<=athr:
                i = jumps[ag[1]]
        elif ag[0]=="JME":
            if str(ag[3]).isnumeric():
                athr=float(ag[3])
            else:
                athr=float(vars[ag[3]])
            if vars[ag[2]]>=athr:
                i = jumps[ag[1]]
        elif ag[0]=="JL":
            if str(ag[3]).isnumeric():
                athr=float(ag[3])
            else:
                athr=float(vars[ag[3]])
            if vars[ag[2]]<athr:
                i = jumps[ag[1]]
        elif ag[0]=="JM":
            if str(ag[3]).isnumeric():
                athr=float(ag[3])
            else:
                athr=vars[ag[3]]
            if vars[ag[2]]>athr:
                i = jumps[ag[1]]
        elif ag[0]=="OUT":
            print(sostT(" ".join(ag[1:]),vars).replace("\\n","\n"),end='')
        elif ag[0]=="IN":
            print(sostT(" ".join(ag[3:]),vars).replace("\\n","\n"),end='')
            vars[ag[2]]=int(input(""))
        i+=1
except Exception as e:
    print(vars)
    print(jumps)
    raise e
#print(lines)
