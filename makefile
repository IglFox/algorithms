lr1: n1/lab1.c
	gcc n1/lab1.c -o n1/lab1.exe -lm
	./n1/lab1.exe

lr2: n2/lab2.c
	gcc n2/lab2.c -o n2/lab2.exe -lm
	./n2/lab2.exe

clean:
	rm -rfv *.exe
