all:
    gcc -Wall -Werror -o hw1 hw1.c
    gcc -Wall -Werror -o hw2 hw2.c
    gcc -Wall -Werror -o hw3 hw3.c
    
clean:
    rm hw1 hw2 hw3
