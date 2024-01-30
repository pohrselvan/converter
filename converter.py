import argparse         #To import the module which is used for parsing command-line arguments.
import markdown         #To import the module which is used for converting markdown to html
import markdownify      #To import the module which is used for converting html to markdown  

parser=argparse.ArgumentParser()            #creating a parser
parser.add_argument("--operation",help="Operation",choices=("h2m","m2h"))    #Adding operation argument to the parser by using "add_argument" with choice
parser.add_argument("--input",help="Enter the input file name")              #Adding input arugment to the parser by using "add_argument"
parser.add_argument("--output",help="Enter the output file name")            #Adding output arugment to the parser using "add_argument"
args=parser.parse_args()                    #parse_args method is used to parse the command line argument
a=args.operation                            #After parsing the command line args will be an object with attributes corresponding to the argument


if(a=="m2h"):                               #Converting markdown to html                       
        v=open(args.input+".txt",'r')
        f=v.read()
        temphtml=markdown.markdown(f)       
        b=open(args.output+".txt","w")
        b.write(temphtml)
        b.close()
        y=open(args.output+".html","w")
        y.write(temphtml)
        y.close()

        
elif(a=="h2m"):                             #Converting html to markdown
       v=open(args.input+".txt",'r')
       file=v.read()
       tempmd=markdownify.markdownify(file,heading_style='ATX')
       f=open(args.output+".txt",'w')
       f.write(tempmd)
       f.close()
else:
         print("Enter the correct operation")
    

    
