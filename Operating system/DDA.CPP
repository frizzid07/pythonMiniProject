
#include <stdio.h>
#include <conio.h>
#include <graphics.h>
#include <dos.h>
int mutex=1,full=0,empty=3,x=0;
  int n;
    void producer();
    void consumer();
    int wait(int);
    int signal(int);
  int main() {
	int gd=DETECT,gm,err;
	initgraph(&gd,&gm,"..//bgi");
	int i, x1, y1, x2, y2, maxx, midy;


	err = graphresult();

	if (err != grOk) {
		/* error occurred */
		printf("Graphics Error: %s\n",
				grapherrormsg(err));
		return 0;
	}

	/* max position in x-axis */
	maxx = getmaxx();
	/* mid position in y-axis */
	midy = getmaxy() / 2;

	/* assign positions to draw road */
	x1 = 0, y1 = midy + 43;
	x2 = maxx, y2 = midy + 43;

	for (i = 0; i < maxx - 330;i+=10 ) {
		/* clears the graphic screen */
		cleardevice();
       /*
		/* draw the road */
		setcolor(WHITE);
		line(x1, y1, x2, y2);

		/* draw the dump bed(backside) of truck */
		setcolor(LIGHTGRAY);
		setfillstyle(SOLID_FILL, LIGHTGRAY);
		line(0 + i, midy, 80 + i, midy);
		line(80 + i, midy, 80 + i, midy + 30);
		line(80 + i, midy + 30, 47 + i, midy + 30);
		line(0 + i, midy + 30, 23 + i, midy + 30);
		line(0 + i, midy + 30, 0 + i, midy);
		arc(35 + i, midy + 30, 0, 180, 12);
	       floodfill(5 + i, midy + 5, LIGHTGRAY);


		rectangle(i+10,225-40,i+75,240-40);
		if(full>2)
			floodfill(12 + i, 227-40,LIGHTGRAY);
		rectangle(i+10,240-40,i+75,255-40);
		if(full>1)
			floodfill(12 + i, 243-40,LIGHTGRAY);

		rectangle(i+10,255-40,i+75,270-40);
		if(full>0)
			floodfill(12 + i, 257-40,LIGHTGRAY);



	       /*	 draw the cab of truck */
		setcolor(YELLOW);
		setfillstyle(SOLID_FILL, YELLOW);
		line(81 + i, midy + 30, 81 + i, midy - 40);
		line(82 + i, midy - 40,
		 111 + i, midy - 40);
		line(111 + i, midy - 40, 126 + i, midy - 10);
		line(126 + i, midy - 10, 126 + i, midy + 30);
		line(126 + i, midy + 30, 117 + i, midy + 30);
		line(93 + i, midy + 30, 81 + i, midy + 30);
		arc(105 + i, midy + 30, 0, 180, 12);

		/* window */
		line(87 + i, midy - 5, 118 + i, midy - 5);
		line(87 + i, midy - 5, 87 + i, midy - 30);
		line(87 + i, midy - 30, 106 + i, midy - 30);
		line(106 + i, midy - 30, 118 + i, midy - 5);
		floodfill(85 + i, midy + 25, YELLOW);

		setcolor(DARKGRAY);
		if (i % 2 == 0) {
			setfillstyle(SLASH_FILL, DARKGRAY);
		} else {
			setfillstyle(BKSLASH_FILL, DARKGRAY);
		}

		/* draw the tyres */
		circle(35 + i, midy + 30, 8);
		circle(105 + i, midy + 30, 8);
		floodfill(35 + i, midy + 30, DARKGRAY);
		floodfill(105 + i, midy + 30, DARKGRAY);




	scanf("%d",&n);
	switch(n)
	{
	    case 1:    if((mutex==1)&&(empty!=0))
			producer();

		    else


		      {
			printf("Producer is in blocked state.");
			i-=10;
			delay(1500);
			}
		    break;
	    case 2:    if((mutex==1)&&(full!=0))
			consumer();
		    else
		    {
			i-=10;
			printf("Consumer is in blocked state.");
			delay(1500);
			}
		    break;
	    case 3:
		    goto here;
		    break;
	}
		/* sleep for 50 milliseconds */
		delay(50);
	}
	    here:
	getch();

	/* deallocate memory allocated for graphic screen */
	closegraph();
	return 0;
  }
int wait(int s)
{
    return (--s);
}

int signal(int s)
{
    return(++s);
}

void producer()
{
    mutex=wait(mutex);
    full=signal(full);
    empty=wait(empty);
    x++;

    mutex=signal(mutex);
}

void consumer()
{
    mutex=wait(mutex);
    full=wait(full);
    empty=signal(empty);

    x--;
    mutex=signal(mutex);
}