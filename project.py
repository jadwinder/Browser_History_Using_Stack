import tkinter as tk
from tkinter import messagebox
import re
import webbrowser

# --- Core Logic Using Stacks ---
back_stack = []
forward_stack = []
current_page = ["Home"]  # Using list to make it mutable

# --- URL Validation Function ---
def is_valid_url(url):
    # Regular expression to match valid HTTP or HTTPS URLs
    regex = r'^(http://|https://)[a-zA-Z0-9-_.]+(?:\.[a-zA-Z0-9-_.]+)+.*$'
    return re.match(regex, url) is not None

# --- GUI Functions ---
def visit_page():
    new_url = url_entry.get().strip()
    if not new_url:
        messagebox.showwarning("Input Error", "Please enter a URL.")
        return

    if not is_valid_url(new_url):
        messagebox.showwarning("Invalid URL", "Please enter a valid URL (starting with http:// or https://).")
        return

    back_stack.append(current_page[0])
    current_page[0] = new_url
    forward_stack.clear()

    # Open the page in the browser
    webbrowser.open(new_url)

    update_display()

def go_back():
    if not back_stack:
        messagebox.showinfo("Navigation", "No pages in back history.")
        return
    forward_stack.append(current_page[0])
    current_page[0] = back_stack.pop()
    update_display()

def go_forward():
    if not forward_stack:
        messagebox.showinfo("Navigation", "No pages in forward history.")
        return
    back_stack.append(current_page[0])
    current_page[0] = forward_stack.pop()
    update_display()

def update_display():
    current_label.config(text=f"Current Page: {current_page[0]}")
    back_label.config(text=f"Back Stack: {back_stack}")
    forward_label.config(text=f"Forward Stack: {forward_stack}")

# --- GUI Setup ---
root = tk.Tk()
root.title("Browser History Navigation using Stack")
root.geometry("600x400")

title = tk.Label(root, text="Browser Navigation (Back / Forward)", font=("Arial", 16))
title.pack(pady=10)

url_entry = tk.Entry(root, width=50)
url_entry.pack(pady=5)

btn_frame = tk.Frame(root)
btn_frame.pack()

visit_btn = tk.Button(btn_frame, text="Visit Page", command=visit_page)
visit_btn.grid(row=0, column=0, padx=10)

back_btn = tk.Button(btn_frame, text="← Back", command=go_back)
back_btn.grid(row=0, column=1, padx=10)

forward_btn = tk.Button(btn_frame, text="→ Forward", command=go_forward)
forward_btn.grid(row=0, column=2, padx=10)

current_label = tk.Label(root, text="Current Page: Home", font=("Arial", 14))
current_label.pack(pady=10)

back_label = tk.Label(root, text="Back Stack: []", fg="blue")
back_label.pack()

forward_label = tk.Label(root, text="Forward Stack: []", fg="green")
forward_label.pack()

root.mainloop()


Krushkal 

#include<stdio.h>
#include<conio.h>
#include<graphics.h>
int i, j, k, a, b, u, v, n, ne=1;
int min,mincost=0,cost[9][9],parent[9];
int find(int);
int uni(int,int);
void main()
{
int ch;
int gd=DETECT,gm;
clrscr();
initgraph(&gd,&gm,"C:\\TurboC3\\Bgi");
settextstyle(TRIPLEX_FONT,HORIZ_DIR,5);
setcolor(RED);
outtextxy(170,50,"WELCOME TO");
settextstyle(TRIPLEX_FONT,HORIZ_DIR,5);
outtextxy(170,110,"OUR PROJECT");
settextstyle(TRIPLEX_FONT,HORIZ_DIR,1);
setcolor(3);
outtextxy(10,10,"***********************************************************************************************");
settextstyle(TRIPLEX_FONT,HORIZ_DIR,2);
setcolor(10);
outtextxy(50,250,"SUBMITTED TO :");
settextstyle(TRIPLEX_FONT,HORIZ_DIR,2);
setcolor(4);
outtextxy(50,300,"MISS PRIYANKA GHAI");
settextstyle(TRIPLEX_FONT,HORIZ_DIR,2);
setcolor(10);
outtextxy(400,250,"SUBMITTED BY :");
settextstyle(TRIPLEX_FONT,HORIZ_DIR,2);
setcolor(4);
outtextxy(400,300,"JADWINDER SINGH");
settextstyle(TRIPLEX_FONT,HORIZ_DIR,2);
outtextxy(10,450,"***************************************************************************************************");
getch();
cleardevice();


 //2 page
settextstyle(TRIPLEX_FONT,HORIZ_DIR,5);
setcolor(3);
outtextxy(250,100,"MENU");
setcolor(14);
settextstyle(TRIPLEX_FONT,HORIZ_DIR,2);
outtextxy(150,200," 1. NON-GRAPHICAL MODE");
settextstyle(TRIPLEX_FONT,HORIZ_DIR,2);
outtextxy(150,250," 2. GRAPHICAL MODE");
settextstyle(TRIPLEX_FONT,HORIZ_DIR,2);
outtextxy(150,300," 3. FOR EXIT");
setcolor(3);
outtextxy(10,10,"***************************************************************************************");
outtextxy(10,450,"********************************************************************************************");
settextstyle(TRIPLEX_FONT,HORIZ_DIR,1);
setcolor(15);


printf("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\t\t Enter your choice:");

scanf("%d",&ch);
clearviewport();
switch(ch)
{
case 1:
{

printf("Implementation of Kruskal's Algorithm\n");
printf("\nEnter the no. of vertices:");
scanf("%d",&n);
printf("\nEnter the cost adjacency matrix:\n");
for(i=1;i<=n;i++)
{
for(j=1;j<=n;j++)
{
scanf("%d",&cost[i][j]);
if (cost[i][j] == 0)
cost[i][j] = 999;
}
}
printf("The edges of Minimum Cost Spanning Tree are\n");
while(ne<n)
{
for(i=1,min=999;i<=n;i++)
{
for(j=1;j<=n;j++)
{
if(cost[i][j]<min)
{
min=cost[i][j];
a=u=i;
b=v=j;
}
}
}
u=find(u);
v=find(v);
if(uni(u,v))
{
printf("%d edge (%d,%d) =%d\n", ne++, a, b, min);
mincost+=min;
}
cost[a][b] = cost[b][a] = 999;
}
printf("\n\tMinimum cost = %d\n", mincost);
getch();
cleardevice();
setcolor(GREEN);
outtextxy(240,200,"THANK YOU!!!");
break;
}
case 2:
{
settextstyle(DEFAULT_FONT,HORIZ_DIR,0);
setcolor(YELLOW);
outtextxy(50,50,"ORIGINAL GRAPH");
setcolor(YELLOW);
outtextxy(305,100,"A Spanning tree is the subset of graph G,");
outtextxy(306,116,"which has all the vertices covered with ");
outtextxy(307,132,"minimum possible number of edges.Hence a");
outtextxy(308,148,"Spanning tree does not have cycle and it");
outtextxy(309,164,"cannot be disconnected.");
circle(90,90,10);  //for1
outtextxy(85,85,"1");
circle(150,120,10);  //for2
outtextxy(148,115,"2");
circle(190,170,10);  //for3
outtextxy(187,165,"3");
circle(110,170,10);  //for7
outtextxy(107,165,"7");
circle(35,170,10);  //for6
outtextxy(33,165,"6");
circle(80,220,10);  //for5
outtextxy(79,215,"5");
circle(150,250,10);  //for4
outtextxy(148,245,"4");
line(152,129,189,160); //for2-3
outtextxy(177,135,"16");
line(81,97,35,160); //for1-6
outtextxy(40,115,"10");
line(139,246,90,224); //for5-4
outtextxy(100,240,"22");
line(140,120,95,100); //for1-2
outtextxy(118,95,"28");
line(145,240,107,180); //for7-4
outtextxy(130,200,"18");
line(157,245,190,180); //for3-4
outtextxy(185,210,"12");
line(150,130,110,160); //for2-7
outtextxy(110,134,"14");
line(80,210,110,180); //for5-7
outtextxy(75,180,"24");
line(45,175,75,213); //for6-5
outtextxy(40,200,"25");
setcolor(YELLOW);
setlinestyle(0,1,0);
line(90,400,420,400); //for lower line
outtextxy(95,350,"Edge");
line(90,330,420,330); // for upper line
outtextxy(93,388,"Weight");
line(352,330,352,400);
outtextxy(145,350,"1-6");
outtextxy(145,388,"10");
outtextxy(175,350,"3-4");
outtextxy(175,388,"12");
outtextxy(205,350,"2-7");
outtextxy(205,388,"14");
outtextxy(235,350,"2-3");
outtextxy(235,388,"16");
outtextxy(265,350,"7-4");
outtextxy(265,388,"18");
outtextxy(295,350,"5-4");
outtextxy(295,388,"22");
outtextxy(325,350,"7-5");
outtextxy(325,388,"24");
outtextxy(355,350,"6-5");
outtextxy(355,388,"25");
outtextxy(389,350,"1-2");
outtextxy(389,388,"28");
line(90,330,90,400);
line(140,330,140,400);
line(90,365,420,365);   //for middle line
line(170,330,170,400);
line(200,330,200,400);
line(230,330,230,400);
line(260,330,260,400);
line(290,330,290,400);
line(320,330,320,400);
line(385,330,385,400);
line(420,330,420,400);
getch();
cleardevice();
//step 1
setcolor(YELLOW);
outtextxy(50,50,"ORIGINAL GRAPH");
circle(90,90,10);  //for1
outtextxy(87,85,"1");
circle(150,120,10);  //for2
outtextxy(149,115,"2");
circle(190,170,10);  //for3
outtextxy(187,165,"3");
circle(110,170,10);  //for7
outtextxy(107,165,"7");
circle(35,170,10);  //for6
outtextxy(33,165,"6");
circle(80,220,10);  //for5
outtextxy(79,215,"5");
circle(150,250,10);  //for4
outtextxy(530,245,"4");
line(152,129,189,160); //for2-3
outtextxy(177,135,"16");
line(81,97,35,160); //for1-6
outtextxy(40,115,"10");
line(139,246,90,224); //for5-4
outtextxy(100,240,"22");
line(140,120,95,100); //for1-2
outtextxy(118,95,"28");
line(145,240,107,180); //for7-4
outtextxy(130,200,"18");
line(157,245,190,180); //for3-4
outtextxy(185,210,"12");
line(150,130,110,160); //for2-7
outtextxy(110,134,"14");
line(80,210,110,180); //for5-7
outtextxy(75,180,"24");
line(45,175,75,213); //for6-5
outtextxy(40,200,"25");
outtextxy(450,50,"STEP 1");
circle(450,90,10);  //for1
outtextxy(448,85,"1");
circle(520,120,10);  //for2
outtextxy(518,115,"2");
circle(400,170,10);  //for6
outtextxy(398,165,"6");
circle(480,170,10);  //for7
outtextxy(479,165,"7");
circle(560,170,10);  //for3
outtextxy(556,165,"3");
circle(450,220,10);  //for5
outtextxy(449,215,"5");
circle(535,250,10);  //for4
outtextxy(148,245,"4");
setlinestyle(2,0,1);
setcolor(RED);
line(445,100,400,161); //for1-6
outtextxy(400,120,"10");
setcolor(RED);
setlinestyle(0,0,3);
ellipse(155,365,0,360,16,36);    //1 ellipse
setcolor(YELLOW);
setlinestyle(0,1,0);
line(90,400,420,400); //for lower line
outtextxy(95,350,"Edge");
line(90,330,420,330); // for upper line
outtextxy(93,388,"Weight");
line(352,330,352,400);
outtextxy(145,350,"1-6");
outtextxy(145,388,"10");
outtextxy(175,350,"3-4");
outtextxy(175,388,"12");
outtextxy(205,350,"2-7");
outtextxy(205,388,"14");
outtextxy(235,350,"2-3");
outtextxy(235,388,"16");
outtextxy(265,350,"7-4");
outtextxy(265,388,"18");
outtextxy(295,350,"5-4");
outtextxy(295,388,"22");
outtextxy(325,350,"7-5");
outtextxy(325,388,"24");
outtextxy(355,350,"6-5");
outtextxy(355,388,"25");
outtextxy(389,350,"1-2");
outtextxy(389,388,"28");
line(90,330,90,400);
line(140,330,140,400);
line(90,365,420,365);   //for middle line
line(170,330,170,400);
line(200,330,200,400);
line(230,330,230,400);
line(260,330,260,400);
line(290,330,290,400);
line(320,330,320,400);
line(385,330,385,400);
line(420,330,420,400);
delay(4000);
clearviewport();
//step 2
setcolor(YELLOW);
outtextxy(50,50,"ORIGINAL GRAPH");
circle(90,90,10);  //for1
outtextxy(87,85,"1");
circle(150,120,10);  //for2
outtextxy(149,115,"2");
circle(190,170,10);  //for3
outtextxy(187,165,"3");
circle(110,170,10);  //for7
outtextxy(107,165,"7");
circle(35,170,10);  //for6
outtextxy(33,165,"6");
circle(80,220,10);  //for5
outtextxy(79,215,"5");
circle(150,250,10);  //for4
outtextxy(148,245,"4");
line(152,129,189,160); //for2-3
outtextxy(177,135,"16");
line(81,97,35,160); //for1-6
outtextxy(40,115,"10");
line(139,246,90,224); //for5-4
outtextxy(100,240,"22");
line(140,120,95,100); //for1-2
outtextxy(118,95,"28");
line(145,240,107,180); //for7-4
outtextxy(130,200,"18");
line(157,245,190,180); //for3-4
outtextxy(185,210,"12");
line(150,130,110,160); //for2-7
outtextxy(110,134,"14");
line(80,210,110,180); //for5-7
outtextxy(75,180,"24");
line(45,175,75,213); //for6-5
outtextxy(40,200,"25");
outtextxy(450,50,"STEP 2");
circle(450,90,10);  //for1
outtextxy(448,85,"1");
circle(520,120,10);  //for2
outtextxy(518,115,"2");
circle(400,170,10);  //for6
outtextxy(398,165,"6");
circle(480,170,10);  //for7
outtextxy(479,165,"7");
circle(560,170,10);  //for3
outtextxy(556,165,"3");
circle(450,220,10);  //for5
outtextxy(449,215,"5");
circle(535,250,10);  //for4
outtextxy(530,245,"4");
setlinestyle(2,0,1);
setcolor(RED);
line(445,100,400,161); //for1-6
outtextxy(400,120,"10");
line(560,177,535,242); //for3-4
outtextxy(550,210,"12");
setcolor(RED);
setlinestyle(0,0,3);
ellipse(185,365,0,360,16,36);
setcolor(YELLOW);
setlinestyle(0,1,0);
line(90,400,420,400); //for lower line
outtextxy(95,350,"Edge");
line(90,330,420,330); // for upper line
outtextxy(93,388,"Weight");
line(352,330,352,400);
outtextxy(145,350,"1-6");
outtextxy(145,388,"10");
outtextxy(175,350,"3-4");
outtextxy(175,388,"12");
outtextxy(205,350,"2-7");
outtextxy(205,388,"14");
outtextxy(235,350,"2-3");
outtextxy(235,388,"16");
outtextxy(265,350,"7-4");
outtextxy(265,388,"18");
outtextxy(295,350,"5-4");
outtextxy(295,388,"22");
outtextxy(325,350,"7-5");
outtextxy(325,388,"24");
outtextxy(355,350,"6-5");
outtextxy(355,388,"25");
outtextxy(389,350,"1-2");
outtextxy(389,388,"28");
line(90,330,90,400);
line(140,330,140,400);
line(90,365,420,365);   //for middle line
line(170,330,170,400);
line(200,330,200,400);
line(230,330,230,400);
line(260,330,260,400);
line(290,330,290,400);
line(320,330,320,400);
line(385,330,385,400);
line(420,330,420,400);
delay(4000);
clearviewport();
//step 3
setcolor(YELLOW);
outtextxy(50,50,"ORIGINAL GRAPH");
circle(90,90,10);  //for1
outtextxy(87,85,"1");
circle(150,120,10);  //for2
outtextxy(149,115,"2");
circle(190,170,10);  //for3
outtextxy(187,165,"3");
circle(110,170,10);  //for7
outtextxy(107,165,"7");
circle(35,170,10);  //for6
outtextxy(33,165,"6");
circle(80,220,10);  //for5
outtextxy(79,215,"5");
circle(150,250,10);  //for4
outtextxy(148,245,"4");
line(152,129,189,160); //for2-3
outtextxy(177,135,"16");
line(81,97,35,160); //for1-6
outtextxy(40,115,"10");
line(139,246,90,224); //for5-4
outtextxy(100,240,"22");
line(140,120,95,100); //for1-2
outtextxy(118,95,"28");
line(145,240,107,180); //for7-4
outtextxy(130,200,"18");
line(157,245,190,180); //for3-4
outtextxy(185,210,"12");
line(150,130,110,160); //for2-7
outtextxy(110,134,"14");
line(80,210,110,180); //for5-7
outtextxy(75,180,"24");
line(45,175,75,213); //for6-5
outtextxy(40,200,"25");
outtextxy(450,50,"STEP 3");
circle(450,90,10);  //for1
outtextxy(448,85,"1");
circle(520,120,10);  //for2
outtextxy(518,115,"2");
circle(400,170,10);  //for6
outtextxy(398,165,"6");
circle(480,170,10);  //for7
outtextxy(479,165,"7");
circle(560,170,10);  //for3
outtextxy(556,165,"3");
circle(450,220,10);  //for5
outtextxy(449,215,"5");
circle(535,250,10);  //for4
outtextxy(530,245,"4");
setlinestyle(2,0,1);
setcolor(RED);
line(445,100,400,161); //for1-6
outtextxy(400,120,"10");
line(560,177,535,242); //for3-4
outtextxy(550,210,"12");
line(515,130,485,165); //for2-7
outtextxy(470,130,"14");
setcolor(RED);
setlinestyle(0,0,3);
ellipse(215,365,0,360,16,36);
setcolor(YELLOW);
setlinestyle(0,1,0);
line(90,400,420,400); //for lower line
outtextxy(95,350,"Edge");
line(90,330,420,330); // for upper line
outtextxy(93,388,"Weight");
line(352,330,352,400);
outtextxy(145,350,"1-6");
outtextxy(145,388,"10");
outtextxy(175,350,"3-4");
outtextxy(175,388,"12");
outtextxy(205,350,"2-7");
outtextxy(205,388,"14");
outtextxy(235,350,"2-3");
outtextxy(235,388,"16");
outtextxy(265,350,"7-4");
outtextxy(265,388,"18");
outtextxy(295,350,"5-4");
outtextxy(295,388,"22");
outtextxy(325,350,"7-5");
outtextxy(325,388,"24");
outtextxy(355,350,"6-5");
outtextxy(355,388,"25");
outtextxy(389,350,"1-2");
outtextxy(389,388,"28");
line(90,330,90,400);
line(140,330,140,400);
line(90,365,420,365);   //for middle line
line(170,330,170,400);
line(200,330,200,400);
line(230,330,230,400);
line(260,330,260,400);
line(290,330,290,400);
line(320,330,320,400);
line(385,330,385,400);
line(420,330,420,400);
delay(4000);
clearviewport();
// step 4
setcolor(YELLOW);
outtextxy(50,50,"ORIGINAL GRAPH");
circle(90,90,10);  //for1
outtextxy(87,85,"1");
circle(150,120,10);  //for2
outtextxy(149,115,"2");
circle(190,170,10);  //for3
outtextxy(187,165,"3");
circle(110,170,10);  //for7
outtextxy(107,165,"7");
circle(35,170,10);  //for6
outtextxy(33,165,"6");
circle(80,220,10);  //for5
outtextxy(79,215,"5");
circle(150,250,10);  //for4
outtextxy(148,245,"4");
line(152,129,189,160); //for2-3
outtextxy(177,135,"16");
line(81,97,35,160); //for1-6
outtextxy(40,115,"10");
line(139,246,90,224); //for5-4
outtextxy(100,240,"22");
line(140,120,95,100); //for1-2
outtextxy(118,95,"28");
line(145,240,107,180); //for7-4
outtextxy(130,200,"18");
line(157,245,190,180); //for3-4
outtextxy(185,210,"12");
line(150,130,110,160); //for2-7
outtextxy(110,134,"14");
line(80,210,110,180); //for5-7
outtextxy(75,180,"24");
line(45,175,75,213); //for6-5
outtextxy(40,200,"25");
outtextxy(450,50,"STEP 4");
circle(450,90,10);  //for1
outtextxy(448,85,"1");
circle(520,120,10);  //for2
outtextxy(518,115,"2");
circle(400,170,10);  //for6
outtextxy(398,165,"6");
circle(480,170,10);  //for7
outtextxy(479,165,"7");
circle(560,170,10);  //for3
outtextxy(556,165,"3");
circle(450,220,10);  //for5
outtextxy(449,215,"5");
circle(535,250,10);  //for4
outtextxy(530,245,"4");
setlinestyle(2,0,1);
setcolor(RED);
line(445,100,400,161); //for1-6
outtextxy(400,120,"10");
line(560,177,535,242); //for3-4
outtextxy(550,210,"12");
line(515,130,485,165); //for2-7
outtextxy(470,130,"14");
line(520,130,550,160); //for2-3
outtextxy(540,135,"16");
setcolor(RED);
setlinestyle(0,0,3);
ellipse(245,365,0,360,16,36);
setcolor(YELLOW);
setlinestyle(0,1,0);
line(90,400,420,400); //for lower line
outtextxy(95,350,"Edge");
line(90,330,420,330); // for upper line
outtextxy(93,388,"Weight");
line(352,330,352,400);
outtextxy(145,350,"1-6");
outtextxy(145,388,"10");
outtextxy(175,350,"3-4");
outtextxy(175,388,"12");
outtextxy(205,350,"2-7");
outtextxy(205,388,"14");
outtextxy(235,350,"2-3");
outtextxy(235,388,"16");
outtextxy(265,350,"7-4");
outtextxy(265,388,"18");
outtextxy(295,350,"5-4");
outtextxy(295,388,"22");
outtextxy(325,350,"7-5");
outtextxy(325,388,"24");
outtextxy(355,350,"6-5");
outtextxy(355,388,"25");
outtextxy(389,350,"1-2");
outtextxy(389,388,"28");
line(90,330,90,400);
line(140,330,140,400);
line(90,365,420,365);   //for middle line
line(170,330,170,400);
line(200,330,200,400);
line(230,330,230,400);
line(260,330,260,400);
line(290,330,290,400);
line(320,330,320,400);
line(385,330,385,400);
line(420,330,420,400);
delay(4000);
clearviewport();
//step 5
setcolor(YELLOW);
outtextxy(50,50,"ORIGINAL GRAPH");
circle(90,90,10);  //for1
outtextxy(87,85,"1");
circle(150,120,10);  //for2
outtextxy(149,115,"2");
circle(190,170,10);  //for3
outtextxy(187,165,"3");
circle(110,170,10);  //for7
outtextxy(107,165,"7");
circle(35,170,10);  //for6
outtextxy(33,165,"6");
circle(80,220,10);  //for5
outtextxy(79,215,"5");
circle(150,250,10);  //for4
outtextxy(148,245,"4");
line(152,129,189,160); //for2-3
outtextxy(177,135,"16");
line(81,97,35,160); //for1-6
outtextxy(40,115,"10");
line(139,246,90,224); //for5-4
outtextxy(100,240,"22");
line(140,120,95,100); //for1-2
outtextxy(118,95,"28");
line(145,240,107,180); //for7-4
outtextxy(130,200,"18");
line(157,245,190,180); //for3-4
outtextxy(185,210,"12");
line(150,130,110,160); //for2-7
outtextxy(110,134,"14");
line(80,210,110,180); //for5-7
outtextxy(75,180,"24");
line(45,175,75,213); //for6-5
outtextxy(40,200,"25");
outtextxy(450,50,"STEP 5");
circle(450,90,10);  //for1
outtextxy(448,85,"1");
circle(520,120,10);  //for2
outtextxy(518,115,"2");
circle(400,170,10);  //for6
outtextxy(398,165,"6");
circle(480,170,10);  //for7
outtextxy(479,165,"7");
circle(560,170,10);  //for3
outtextxy(556,165,"3");
circle(450,220,10);  //for5
outtextxy(449,215,"5");
circle(535,250,10);  //for4
outtextxy(530,245,"4");
setlinestyle(2,0,1);
setcolor(RED);
line(445,100,400,161); //for1-6
outtextxy(400,120,"10");
line(560,177,535,242); //for3-4
outtextxy(550,210,"12");
line(515,130,485,165); //for2-7
outtextxy(470,130,"14");
line(520,130,550,160); //for2-3
outtextxy(540,135,"16");
setcolor(RED);
setlinestyle(0,0,3);     // for bold ellipse
ellipse(275,365,0,360,16,36);
setlinestyle(0,0,2); //for thin line
line(480,180,525,245);
outtextxy(515,200,"18");
setcolor(GREEN);
settextstyle(TRIPLEX_FONT,HORIZ_DIR,3);
outtextxy(500,195,"x");
setlinestyle(0,0,2);
settextstyle(DEFAULT_FONT,HORIZ_DIR,0);
setcolor(YELLOW);
setlinestyle(0,1,0);
line(90,400,420,400); //for lower line
outtextxy(95,350,"Edge");
line(90,330,420,330); // for upper line
outtextxy(93,388,"Weight");
line(352,330,352,400);
outtextxy(145,350,"1-6");
outtextxy(145,388,"10");
outtextxy(175,350,"3-4");
outtextxy(175,388,"12");
outtextxy(205,350,"2-7");
outtextxy(205,388,"14");
outtextxy(235,350,"2-3");
outtextxy(235,388,"16");
outtextxy(265,350,"7-4");
outtextxy(265,388,"18");
outtextxy(295,350,"5-4");
outtextxy(295,388,"22");
outtextxy(325,350,"7-5");
outtextxy(325,388,"24");
outtextxy(355,350,"6-5");
outtextxy(355,388,"25");
outtextxy(389,350,"1-2");
outtextxy(389,388,"28");
line(90,330,90,400);
line(140,330,140,400);
line(90,365,420,365);   //for middle line
line(170,330,170,400);
line(200,330,200,400);
line(230,330,230,400);
line(260,330,260,400);
line(290,330,290,400);
line(320,330,320,400);
line(385,330,385,400);
line(420,330,420,400);
delay(4000);
clearviewport();
// step 6
setcolor(YELLOW);
outtextxy(50,50,"ORIGINAL GRAPH");
circle(90,90,10);  //for1
outtextxy(87,85,"1");
circle(150,120,10);  //for2
outtextxy(149,115,"2");
circle(190,170,10);  //for3
outtextxy(187,165,"3");
circle(110,170,10);  //for7
outtextxy(107,165,"7");
circle(35,170,10);  //for6
outtextxy(33,165,"6");
circle(80,220,10);  //for5
outtextxy(79,215,"5");
circle(150,250,10);  //for4
outtextxy(148,245,"4");
line(152,129,189,160); //for2-3
outtextxy(177,135,"16");
line(81,97,35,160); //for1-6
outtextxy(40,115,"10");
line(139,246,90,224); //for5-4
outtextxy(100,240,"22");
line(140,120,95,100); //for1-2
outtextxy(118,95,"28");
line(145,240,107,180); //for7-4
outtextxy(130,200,"18");
line(157,245,190,180); //for3-4
outtextxy(185,210,"12");
line(150,130,110,160); //for2-7
outtextxy(110,134,"14");
line(80,210,110,180); //for5-7
outtextxy(75,180,"24");
line(45,175,75,213); //for6-5
outtextxy(40,200,"25");
outtextxy(450,50,"STEP 6");
circle(450,90,10);  //for1
outtextxy(448,85,"1");
circle(520,120,10);  //for2
outtextxy(518,115,"2");
circle(400,170,10);  //for6
outtextxy(398,165,"6");
circle(480,170,10);  //for7
outtextxy(479,165,"7");
circle(560,170,10);  //for3
outtextxy(556,165,"3");
circle(450,220,10);  //for5
outtextxy(449,215,"5");
circle(535,250,10);  //for4
outtextxy(530,245,"4");
setlinestyle(2,0,1);
setcolor(RED);
line(445,100,400,161); //for1-6
outtextxy(400,120,"10");
line(560,177,535,242); //for3-4
outtextxy(550,210,"12");
line(515,130,485,165); //for2-7
outtextxy(470,130,"14");
line(520,130,550,160); //for2-3
outtextxy(540,135,"16");
setcolor(RED);
setlinestyle(0,0,3);
ellipse(305,365,0,360,16,36);
setlinestyle(0,0,2);
setcolor(YELLOW);
setlinestyle(0,1,0);
line(90,400,420,400); //for lower line
outtextxy(95,350,"Edge");
line(90,330,420,330); // for upper line
outtextxy(93,388,"Weight");
line(352,330,352,400);
outtextxy(145,350,"1-6");
outtextxy(145,388,"10");
outtextxy(175,350,"3-4");
outtextxy(175,388,"12");
outtextxy(205,350,"2-7");
outtextxy(205,388,"14");
outtextxy(235,350,"2-3");
outtextxy(235,388,"16");
outtextxy(265,350,"7-4");
outtextxy(265,388,"18");
outtextxy(295,350,"5-4");
outtextxy(295,388,"22");
outtextxy(325,350,"7-5");
outtextxy(325,388,"24");
outtextxy(355,350,"6-5");
outtextxy(355,388,"25");
outtextxy(389,350,"1-2");
outtextxy(389,388,"28");
setlinestyle(2,0,1);
setcolor(RED);
line(460,220,525,250);//for 5-4
outtextxy(480,240,"22");
setcolor(YELLOW);
setlinestyle(0,0,1);
line(90,330,90,400);
line(140,330,140,400);
line(90,365,420,365);   //for middle line
line(170,330,170,400);
line(200,330,200,400);
line(230,330,230,400);
line(260,330,260,400);
line(290,330,290,400);
line(320,330,320,400);
line(385,330,385,400);
line(420,330,420,400);
delay(4000);
clearviewport();
//step 7
setcolor(YELLOW);
outtextxy(50,50,"ORIGINAL GRAPH");
circle(90,90,10);  //for1
outtextxy(87,85,"1");
circle(150,120,10);  //for2
outtextxy(149,115,"2");
circle(190,170,10);  //for3
outtextxy(187,165,"3");
circle(110,170,10);  //for7
outtextxy(107,165,"7");
circle(35,170,10);  //for6
outtextxy(33,165,"6");
circle(80,220,10);  //for5
outtextxy(79,215,"5");
circle(150,250,10);  //for4
outtextxy(148,245,"4");
line(152,129,189,160); //for2-3
outtextxy(177,135,"16");
line(81,97,35,160); //for1-6
outtextxy(40,115,"10");
line(139,246,90,224); //for5-4
outtextxy(100,240,"22");
line(140,120,95,100); //for1-2
outtextxy(118,95,"28");
line(145,240,107,180); //for7-4
outtextxy(130,200,"18");
line(157,245,190,180); //for3-4
outtextxy(185,210,"12");
line(150,130,110,160); //for2-7
outtextxy(110,134,"14");
line(80,210,110,180); //for5-7
outtextxy(75,180,"24");
line(45,175,75,213); //for6-5
outtextxy(40,200,"25");
outtextxy(450,50,"STEP 7");
circle(450,90,10);  //for1
outtextxy(448,85,"1");
circle(520,120,10);  //for2
outtextxy(518,115,"2");
circle(400,170,10);  //for6
outtextxy(398,165,"6");
circle(480,170,10);  //for7
outtextxy(479,165,"7");
circle(560,170,10);  //for3
outtextxy(556,165,"3");
circle(450,220,10);  //for5
outtextxy(449,215,"5");
circle(535,250,10);  //for4
outtextxy(530,245,"4");
setlinestyle(2,0,1);
setcolor(RED);
line(445,100,400,161); //for1-6
outtextxy(400,120,"10");
line(560,177,535,242); //for3-4
outtextxy(550,210,"12");
line(515,130,485,165); //for2-7
outtextxy(470,130,"14");
line(520,130,550,160); //for2-3
outtextxy(540,135,"16");
line(460,220,525,250);//for 5-4
outtextxy(480,240,"22");
setcolor(RED);
setlinestyle(0,0,3);
ellipse(335,365,0,360,16,36);
setlinestyle(0,0,2);
line(479,180,449,215);
outtextxy(470,200,"24");
setcolor(GREEN);
settextstyle(TRIPLEX_FONT,HORIZ_DIR,3);
setlinestyle(0,0,1);
outtextxy(458,180,"x");
settextstyle(DEFAULT_FONT,HORIZ_DIR,0);
setcolor(YELLOW);
setlinestyle(0,0,1);
line(90,400,420,400); //for lower line
outtextxy(95,350,"Edge");
line(90,330,420,330); // for upper line
outtextxy(93,388,"Weight");
line(352,330,352,400);
outtextxy(145,350,"1-6");
outtextxy(145,388,"10");
outtextxy(175,350,"3-4");
outtextxy(175,388,"12");
outtextxy(205,350,"2-7");
outtextxy(205,388,"14");
outtextxy(235,350,"2-3");
outtextxy(235,388,"16");
outtextxy(265,350,"7-4");
outtextxy(265,388,"18");
outtextxy(295,350,"5-4");
outtextxy(295,388,"22");
outtextxy(325,350,"7-5");
outtextxy(325,388,"24");
outtextxy(355,350,"6-5");
outtextxy(355,388,"25");
outtextxy(389,350,"1-2");
outtextxy(389,388,"28");
line(90,330,90,400);
line(140,330,140,400);
line(90,365,420,365);   //for middle line
line(170,330,170,400);
line(200,330,200,400);
line(230,330,230,400);
line(260,330,260,400);
line(290,330,290,400);
line(320,330,320,400);
line(385,330,385,400);
line(420,330,420,400);
delay(4000);
clearviewport();
//step 8
setcolor(YELLOW);
outtextxy(50,50,"ORIGINAL GRAPH");
circle(90,90,10);  //for1
outtextxy(87,85,"1");
circle(150,120,10);  //for2
outtextxy(149,115,"2");
circle(190,170,10);  //for3
outtextxy(187,165,"3");
circle(110,170,10);  //for7
outtextxy(107,165,"7");
circle(35,170,10);  //for6
outtextxy(33,165,"6");
circle(80,220,10);  //for5
outtextxy(79,215,"5");
circle(150,250,10);  //for4
outtextxy(148,245,"4");
line(152,129,189,160); //for2-3
outtextxy(177,135,"16");
line(81,97,35,160); //for1-6
outtextxy(40,115,"10");
line(139,246,90,224); //for5-4
outtextxy(100,240,"22");
line(140,120,95,100); //for1-2
outtextxy(118,95,"28");
line(145,240,107,180); //for7-4
outtextxy(130,200,"18");
line(157,245,190,180); //for3-4
outtextxy(185,210,"12");
line(150,130,110,160); //for2-7
outtextxy(110,134,"14");
line(80,210,110,180); //for5-7
outtextxy(75,180,"24");
line(45,175,75,213); //for6-5
outtextxy(40,200,"25");
outtextxy(450,50,"STEP 8");
circle(450,90,10);  //for1
outtextxy(448,85,"1");
circle(520,120,10);  //for2
outtextxy(518,115,"2");
circle(400,170,10);  //for6
outtextxy(398,165,"6");
circle(480,170,10);  //for7
outtextxy(479,165,"7");
circle(560,170,10);  //for3
outtextxy(556,165,"3");
circle(450,220,10);  //for5
outtextxy(449,215,"5");
circle(535,250,10);  //for4
outtextxy(530,245,"4");
setlinestyle(2,0,1);
setcolor(RED);
line(445,100,400,161); //for1-6
outtextxy(400,120,"10");
line(560,177,535,242); //for3-4
outtextxy(550,210,"12");
line(515,130,485,165); //for2-7
outtextxy(470,130,"14");
line(520,130,550,160); //for2-3
outtextxy(540,135,"16");
line(460,220,525,250);//for 5-4
outtextxy(480,240,"22");
line(407,170,440,220);//for 5-4
outtextxy(407,200,"25");
setcolor(RED);
setlinestyle(0,0,3);
ellipse(370,365,0,360,16,36);
settextstyle(DEFAULT_FONT,HORIZ_DIR,0);
setcolor(YELLOW);
setlinestyle(0,1,0);
line(90,400,420,400); //for lower line
outtextxy(95,350,"Edge");
line(90,330,420,330); // for upper line
outtextxy(93,388,"Weight");
line(352,330,352,400);
outtextxy(145,350,"1-6");
outtextxy(145,388,"10");
outtextxy(175,350,"3-4");
outtextxy(175,388,"12");
outtextxy(205,350,"2-7");
outtextxy(205,388,"14");
outtextxy(235,350,"2-3");
outtextxy(235,388,"16");
outtextxy(265,350,"7-4");
outtextxy(265,388,"18");
outtextxy(295,350,"5-4");
outtextxy(295,388,"22");
outtextxy(325,350,"7-5");
outtextxy(325,388,"24");
outtextxy(355,350,"6-5");
outtextxy(355,388,"25");
outtextxy(389,350,"1-2");
outtextxy(389,388,"28");
line(90,330,90,400);
line(140,330,140,400);
line(90,365,420,365);   //for middle line
line(170,330,170,400);
line(200,330,200,400);
line(230,330,230,400);
line(260,330,260,400);
line(290,330,290,400);
line(320,330,320,400);
line(385,330,385,400);
line(420,330,420,400);
delay(4000);
clearviewport();
//step 9
setcolor(YELLOW);
outtextxy(50,50,"ORIGINAL GRAPH");
circle(90,90,10);  //for1
outtextxy(87,85,"1");
circle(150,120,10);  //for2
outtextxy(149,115,"2");
circle(190,170,10);  //for3
outtextxy(187,165,"3");
circle(110,170,10);  //for7
outtextxy(107,165,"7");
circle(35,170,10);  //for6
outtextxy(33,165,"6");
circle(80,220,10);  //for5
outtextxy(79,215,"5");
circle(150,250,10);  //for4
outtextxy(148,245,"4");
line(152,129,189,160); //for2-3
outtextxy(177,135,"16");
line(81,97,35,160); //for1-6
outtextxy(40,115,"10");
line(139,246,90,224); //for5-4
outtextxy(100,240,"22");
line(140,120,95,100); //for1-2
outtextxy(118,95,"28");
line(145,240,107,180); //for7-4
outtextxy(130,200,"18");
line(157,245,190,180); //for3-4
outtextxy(185,210,"12");
line(150,130,110,160); //for2-7
outtextxy(110,134,"14");
line(80,210,110,180); //for5-7
outtextxy(75,180,"24");
line(45,175,75,213); //for6-5
outtextxy(40,200,"25");
outtextxy(450,50,"STEP 9");
circle(450,90,10);  //for1
outtextxy(448,85,"1");
circle(520,120,10);  //for2
outtextxy(518,115,"2");
circle(400,170,10);  //for6
outtextxy(398,165,"6");
circle(480,170,10);  //for7
outtextxy(479,165,"7");
circle(560,170,10);  //for3
outtextxy(556,165,"3");
circle(450,220,10);  //for5
outtextxy(449,215,"5");
circle(535,250,10);  //for4
outtextxy(530,245,"4");
setlinestyle(2,0,1);
setcolor(RED);
line(445,100,400,161); //for1-6
outtextxy(400,120,"10");
line(560,177,535,242); //for3-4
outtextxy(550,210,"12");
line(515,130,485,165); //for2-7
outtextxy(470,130,"14");
line(520,130,550,160); //for2-3
outtextxy(540,135,"16");
line(460,220,525,250);//for 5-4
outtextxy(480,240,"22");
line(407,170,440,220);//for 5-4
outtextxy(407,200,"25");
setcolor(RED);
setlinestyle(0,0,3);
ellipse(403,365,0,360,16,36);
setlinestyle(0,0,1);
line(460,90,510,120);
outtextxy(475,90,"28");
setcolor(GREEN);
settextstyle(TRIPLEX_FONT,HORIZ_DIR,3);
outtextxy(475,85,"x");
setlinestyle(0,0,2);
setcolor(GREEN);
settextstyle(DEFAULT_FONT,HORIZ_DIR,0);
setcolor(YELLOW);
setlinestyle(0,1,0);
line(90,400,420,400); //for lower line
outtextxy(95,350,"Edge");
line(90,330,420,330); // for upper line
outtextxy(93,388,"Weight");
line(352,330,352,400);
outtextxy(145,350,"1-6");
outtextxy(145,388,"10");
outtextxy(175,350,"3-4");
outtextxy(175,388,"12");
outtextxy(205,350,"2-7");
outtextxy(205,388,"14");
outtextxy(235,350,"2-3");
outtextxy(235,388,"16");
outtextxy(265,350,"7-4");
outtextxy(265,388,"18");
outtextxy(295,350,"5-4");
outtextxy(295,388,"22");
outtextxy(325,350,"7-5");
outtextxy(325,388,"24");
outtextxy(355,350,"6-5");
outtextxy(355,388,"25");
outtextxy(389,350,"1-2");
outtextxy(389,388,"28");
line(90,330,90,400);
line(140,330,140,400);
line(90,365,420,365);   //for middle line
line(170,330,170,400);
line(200,330,200,400);
line(230,330,230,400);
line(260,330,260,400);
line(290,330,290,400);
line(320,330,320,400);
line(385,330,385,400);
line(420,330,420,400);
delay(4000);
clearviewport();
//step 10
setcolor(YELLOW);
outtextxy(50,50,"ORIGINAL GRAPH");
circle(90,90,10);  //for1
outtextxy(87,85,"1");
circle(150,120,10);  //for2
outtextxy(149,115,"2");
circle(190,170,10);  //for3
outtextxy(187,165,"3");
circle(110,170,10);  //for7
outtextxy(107,165,"7");
circle(35,170,10);  //for6
outtextxy(33,165,"6");
circle(80,220,10);  //for5
outtextxy(79,215,"5");
circle(150,250,10);  //for4
outtextxy(148,245,"4");
line(152,129,189,160); //for2-3
outtextxy(177,135,"16");
line(81,97,35,160); //for1-6
outtextxy(40,115,"10");
line(139,246,90,224); //for5-4
outtextxy(100,240,"22");
line(140,120,95,100); //for1-2
outtextxy(118,95,"28");
line(145,240,107,180); //for7-4
outtextxy(130,200,"18");
line(157,245,190,180); //for3-4
outtextxy(185,210,"12");
line(150,130,110,160); //for2-7
outtextxy(110,134,"14");
line(80,210,110,180); //for5-7
outtextxy(75,180,"24");
line(45,175,75,213); //for6-5
outtextxy(40,200,"25");
outtextxy(410,50,"Minimum Spanninng Tree");
setcolor(YELLOW);
circle(450,90,10);  //for1
outtextxy(448,85,"1");
circle(520,120,10);  //for2
outtextxy(518,115,"2");
circle(400,170,10);  //for6
outtextxy(398,165,"6");
circle(480,170,10);  //for7
outtextxy(479,165,"7");
circle(560,170,10);  //for3
outtextxy(556,165,"3");
circle(450,220,10);  //for5
outtextxy(449,215,"5");
circle(535,250,10);  //for4
outtextxy(530,245,"4");
setlinestyle(2,0,1);
setcolor(RED);
line(445,100,400,161); //for1-6
outtextxy(400,120,"10");
line(560,177,535,242); //for3-4
outtextxy(550,210,"12");
line(515,130,485,165); //for2-7
outtextxy(470,130,"14");
line(520,130,550,160); //for2-3
outtextxy(540,135,"16");
line(460,220,525,250);//for 5-4
outtextxy(480,240,"22");
line(407,170,440,220);//for 5-4
outtextxy(407,200,"25");
setcolor(GREEN);
outtextxy(140,420,"Minimum Cost is 99");
settextstyle(DEFAULT_FONT,HORIZ_DIR,0);
setcolor(YELLOW);
setlinestyle(0,1,0);
line(90,400,420,400); //for lower line
outtextxy(95,350,"Edge");
line(90,330,420,330); // for upper line
outtextxy(93,388,"Weight");
line(352,330,352,400);
outtextxy(145,350,"1-6");
outtextxy(145,388,"10");
outtextxy(175,350,"3-4");
outtextxy(175,388,"12");
outtextxy(205,350,"2-7");
outtextxy(205,388,"14");
outtextxy(235,350,"2-3");
outtextxy(235,388,"16");
outtextxy(265,350,"7-4");
outtextxy(265,388,"18");
outtextxy(295,350,"5-4");
outtextxy(295,388,"22");
outtextxy(325,350,"7-5");
outtextxy(325,388,"24");
outtextxy(355,350,"6-5");
outtextxy(355,388,"25");
outtextxy(389,350,"1-2");
outtextxy(389,388,"28");
line(90,330,90,400);
line(140,330,140,400);
line(90,365,420,365);   //for middle line
line(170,330,170,400);
line(200,330,200,400);
line(230,330,230,400);
line(260,330,260,400);
line(290,330,290,400);
line(320,330,320,400);
line(385,330,385,400);
line(420,330,420,400);
delay(7000);
clearviewport();
outtextxy(200,200,"THANK YOU!!!");
getch();
cleardevice();
break;
}
default:
{
outtextxy(200,200,"THANK YOU!!!");
}
}
getch();
}
int find(int i) {
while (parent[i])
i = parent[i];
return i;
}
int uni(int i, int j)
{
if (i != j)
{
parent[j] = i;
return 1;
}
return 0;
}
