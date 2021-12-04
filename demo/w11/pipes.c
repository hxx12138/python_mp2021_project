/*
    推荐的单工方式
    https://zhuanlan.zhihu.com/p/58489873
*/

#include <stdlib.h>
#include <stdio.h>
#include <unistd.h>
#include <string.h>
#include <sys/types.h>
#include <sys/wait.h>

int main()
{
    int pipefd[2];
    pid_t pid;
    char buf[BUFSIZ];

    if (pipe(pipefd) == -1) 
    {
        perror("pipe()");
        exit(1);
    }

    pid = fork();
    if (pid == -1) 
    {
        perror("fork()");
        exit(1);
    }

    if (pid == 0) 
    {
        /* this is child. */
        close(pipefd[1]); //只读，因此关闭写端

        printf("Child pid is: %d\n", getpid());
        if (read(pipefd[0], buf, BUFSIZ) < 0) {
            perror("write()");
            exit(1);
        }

        printf("%s\n", buf);

        close(pipefd[1]);

    } 
    else 
    {
        /* this is parent */
        close(pipefd[0]);//只写，因此关闭读端

        printf("Parent pid is: %d\n", getpid());

        snprintf(buf, BUFSIZ, "Message from parent: My pid is: %d", getpid());
        if (write(pipefd[1], buf, strlen(buf)) < 0) {
            perror("write()");
            exit(1);
        }

        wait(NULL);

        close(pipefd[1]);
    }

    exit(0);
}