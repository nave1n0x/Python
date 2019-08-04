fh = open("Example.txt","r")
kt = open("test.txt","w")

kt.write(fh.readline())

kt.close
fh.close