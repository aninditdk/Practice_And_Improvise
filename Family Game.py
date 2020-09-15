'''
Family Game
In this lockdown a family of N members decided to play a game the rules of which are :-

All N members are made to sit uniformly in a circle (ie. from 1 to N in clockwise direction).
The game start with the person sitting at first position.
A song is played in the background. The lyrics of the song are denoted by a string which consists of only letters 'x' and 'y'. Assume that each lyric of the song is a single letter. 
If the lyric 'x' occurs in the song, the member who is currently holding the Parcel passes it on to the next member. This passing takes place in clockwise direction.
If the lyric 'y' occurs in the song, the member who is currently holding the Parcel loses his/her chances of winning the game. He/she hands over the parcel to the next member (in clockwise direction) and moves out.
The game continues until a single member survives in the end. He/she will be the winner of the game.
Note that the song repeats continuously ie. while the game is going on, if at all the song ends, the stereo system will automatically start playing the song from the start without any delay.
You have to find out the member who wins the game.

Input :

The input consists of 2 lines. The first line consists of N, the member of family in the class. The next line consists of a string denoting the lyrics of the song the teacher plays.

Output :

Print a single integer denoting the roll number of the student who wins the game.

Constraints :

2≤N≤100000

1≤|S|≤10000, where |S| denotes the length of the input string. It is guaranteed that at least 1 lyric in the song will be a 'y'

Note: Copy and paste is disabled for all the questions. Try not to use other ides.



Sample input:

3

xyx



Output:

1



ExplanationStarting from 1 lyrics : 'x' therefore he passes the ballto 2nd 

2nd turn lyrics : 'y' therefore 2nd member gets out of game and passes to 3rd

3rd turn lyrics : 'x' therefore 3rd passes ball to first.

4th turn lyrics : 'x' passes to 3rd 

5th turn lyrics: 'y' therefore gets eliminated.

Hence person sitting at position 1 won this game.
'''

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class CircularLinkedlist:
    def __init__(self):
        self.head = None

    def print_list(self):
        cur = self.head

        while cur:
            print(cur.data)
            cur = cur.next
            if cur == self.head:
                break

    def append(self, data):
        if not self.head:
            self.head = Node(data)
            self.head.next = self.head
        else:
            new_node = Node(data)
            cur = self.head
            while cur.next != self.head:
                cur=cur.next
            cur.next = new_node
            new_node.next = self.head

    def remove(self,key):
        if self.head.data == key:
            cur = self.head
            while cur.next != self.head:
                cur = cur.next
            cur.next = self.head.next
            self.head = self.head.next
        else:
            cur = self.head
            prev = None
            while cur.next != self.head:
                prev = cur
                cur = cur.next
                if cur.data == key:
                    prev.next = cur.next
                    cur = cur.next

    def len_circularlinkedlist(self):
        if not self.head:
            return 0
        cur = self.head
        count = 1
        while cur.next != self.head:
            count = count + 1
            cur = cur.next
        return count

    def final_func(self,cllistB):
        cur = self.head
        cur1 = cllistA.head

        if cllistA.len_circularlinkedlist() == 1:
            return cllistA.head.data

        while cllistA.len_circularlinkedlist() != 1:
            if cur.data == 'x':
                cur = cur.next
                cur1 = cur1.next
            elif cur.data == 'y':
                a = cur1.next
                cllistA.remove(cur1.data)
                cur = cur.next
                cur1 = a
        return cllistA.head.data


cllistA = CircularLinkedlist()
cllistB = CircularLinkedlist()

N = int(input())
s = input()
for i in range(N):
    cllistA.append(str(i+1))
