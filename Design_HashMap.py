"""Design a HashMap without using any built-in hash table libraries.

Implement the MyHashMap class:

    MyHashMap() initializes the object with an empty map.
    void put(int key, int value) inserts a (key, value) pair into the HashMap. If the key already exists in the map, update the corresponding value.
    int get(int key) returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key.
    void remove(key) removes the key and its corresponding value if the map contains the mapping for the key.

 

Example 1:

Input
["MyHashMap", "put", "put", "get", "get", "put", "get", "remove", "get"]
[[], [1, 1], [2, 2], [1], [3], [2, 1], [2], [2], [2]]
Output    LeetCode Logo

Problem List
0
Premium
Debugging...
Debugging...
Description
Editorial
Editorial
Solutions
Solutions
Submissions
Submissions
Code
Testcase
Test Result
Test Result
706. Design HashMap
Solved
Easy
Topics
Companies

Design a HashMap without using any built-in hash table libraries.

Implement the MyHashMap class:

    MyHashMap() initializes the object with an empty map.
    void put(int key, int value) inserts a (key, value) pair into the HashMap. If the key already exists in the map, update the corresponding value.
    int get(int key) returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key.
    void remove(key) removes the key and its corresponding value if the map contains the mapping for the key.

 

Example 1:

Input
["MyHashMap", "put", "put", "get", "get", "put", "get", "remove", "get"]
[[], [1, 1], [2, 2], [1], [3], [2, 1], [2], [2], [2]]
Output
[null, null, null, 1, -1, null, 1, null, -1]

Explanation
MyHashMap myHashMap = new MyHashMap();
myHashMap.put(1, 1); // The map is now [[1,1]]
myHashMap.put(2, 2); // The map is now [[1,1], [2,2]]
myHashMap.get(1);    // return 1, The map is now [[1,1], [2,2]]
myHashMap.get(3);    // return -1 (i.e., not found), The map is now [[1,1], [2,2]]
myHashMap.put(2, 1); // The map is now [[1,1], [2,1]] (i.e., update the existing value)
myHashMap.get(2);    // return 1, The map is now [[1,1], [2,1]]
myHashMap.remove(2); // remove the mapping for 2, The map is now [[1,1]]
myHashMap.get(2);    // return -1 (i.e., not found), The map is now [[1,1]]

 

Constraints:

    0 <= key, value <= 106
    At most 104 calls will be made to put, get, and remove.

Seen this question in a real interview before?
1/4
Yes
No
Accepted
559.4K
Submissions
850.6K
Acceptance Rate
65.8%
Topics
Array
Hash Table
Linked List
Design
Hash Function
Companies
Similar Questions
Design HashSet
Easy
Design Skiplist
Hard
Discussion (71)
💡 Discussion Rules

1. Please don't post any solutions in this discussion.

2. The problem discussion is for asking questions about the problem or for sharing tips - anything except for solutions.

3. If you'd like to share your solution for feedback and ideas, please head to the solutions tab and post it there.
firefly1
50 Days Badge 2022
Mar 05, 2023

I think this should be marked as medium not easy
74
Show 3 Replies
Reply
TheSithPadawan
50 Days Badge 2022
Oct 27, 2018

I was just skimming through the solutions in the discuss section and I'm curious why no one incorporated load factor and rehash in their design? From the mostly voted solutions, it seems like they did not change the size of the hashmap from the beginning.
54
Show 5 Replies
Reply
souvikmkhrj
100 Days Badge 2023
Oct 04, 2023

People Who watched a YT video and still struggling :

Read more
33
Show 2 Replies
Reply
c-m-d-
100 Days Badge 2022
May 14, 2023

Solving this problem "optimally" is maybe the hardest question on this site, should it still be Easy just because its trivial to cheese it?
28
Reply
akialter
100 Days Badge 2023
Oct 04, 2023

The requirements need to be more specific (i.e. what is the expected runtime of each operation, what is the memory constraint)
25
Show 1 Replies
Reply
anwendeng
Mar LeetCoding Challenge
Oct 04, 2023

How can be designing hash map easy? I used (a*x+b)%p as hash function, and implement it in a standard way. Of course, Due to the constraint 0 <= key, value <= 10^6, there is some very very supereasy way, the most of posted solutions use the easy way. Learn the standard way to design a hash map is a lesson for programmers!
23
Show 3 Replies
Reply
MrAke
30 Days of Pandas
Oct 04, 2023

I think this is not an easy problem!!
31
Show 4 Replies
Reply
Msey
100 Days Badge 2022
Apr 01, 2023

If we do "rehashing" then it's definitely not an easy question
11
Reply
timtam85
Sep 29, 2018

One of the follow-ups for this question is how to make it a concurrent hashmap. Using one lock will serialize all the operations which leads to a very low efficiency. Based on the assumption that the number of read operation will be much more than write operation, my idea is to have separate read and write lock. Any other ideas?
9
Show 1 Replies
Reply
LeetCode
Apr 22, 2022

This problem is the Daily LeetCoding Challenge for April, Day 22.

Feel free to share anything related to this problem here!

You can ask questions, discuss what you've learned from this problem, or show off how many days of streak you've made!
    LeetCode Logo

Problem List
0
Premium
Debugging...
Debugging...
Description
Editorial
Editorial
Solutions
Solutions
Submissions
Submissions
Code
Testcase
Test Result
Test Result
706. Design HashMap
Solved
Easy
Topics
Companies

Design a HashMap without using any built-in hash table libraries.

Implement the MyHashMap class:

    MyHashMap() initializes the object with an empty map.
    void put(int key, int value) inserts a (key, value) pair into the HashMap. If the key already exists in the map, update the corresponding value.
    int get(int key) returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key.
    void remove(key) removes the key and its corresponding value if the map contains the mapping for the key.

 

Example 1:

Input
["MyHashMap", "put", "put", "get", "get", "put", "get", "remove", "get"]
[[], [1, 1], [2, 2], [1], [3], [2, 1], [2], [2], [2]]
Output
[null, null, null, 1, -1, null, 1, null, -1]

Explanation
MyHashMap myHashMap = new MyHashMap();
myHashMap.put(1, 1); // The map is now [[1,1]]
myHashMap.put(2, 2); // The map is now [[1,1], [2,2]]
myHashMap.get(1);    // return 1, The map is now [[1,1], [2,2]]
myHashMap.get(3);    // return -1 (i.e., not found), The map is now [[1,1], [2,2]]
myHashMap.put(2, 1); // The map is now [[1,1], [2,1]] (i.e., update the existing value)
myHashMap.get(2);    // return 1, The map is now [[1,1], [2,1]]
myHashMap.remove(2); // remove the mapping for 2, The map is now [[1,1]]
myHashMap.get(2);    // return -1 (i.e., not found), The map is now [[1,1]]

 

Constraints:

    0 <= key, value <= 106
    At most 104 calls will be made to put, get, and remove.

Seen this question in a real interview before?
1/4
Yes
No
Accepted
559.4K
Submissions
850.6K
Acceptance Rate
65.8%
Topics
Array
Hash Table
Linked List
Design
Hash Function
Companies
Similar Questions
Design HashSet
Easy
Design Skiplist
Hard
Discussion (71)
💡 Discussion Rules

1. Please don't post any solutions in this discussion.

2. The problem discussion is for asking questions about the problem or for sharing tips - anything except for solutions.

3. If you'd like to share your solution for feedback and ideas, please head to the solutions tab and post it there.
firefly1
50 Days Badge 2022
Mar 05, 2023

I think this should be marked as medium not easy
74
Show 3 Replies
Reply
TheSithPadawan
50 Days Badge 2022
Oct 27, 2018

I was just skimming through the solutions in the discuss section and I'm curious why no one incorporated load factor and rehash in their design? From the mostly voted solutions, it seems like they did not change the size of the hashmap from the beginning.
54
Show 5 Replies
Reply
souvikmkhrj
100 Days Badge 2023
Oct 04, 2023

People Who watched a YT video and still struggling :

Read more
33
Show 2 Replies
Reply
c-m-d-
100 Days Badge 2022
May 14, 2023

Solving this problem "optimally" is maybe the hardest question on this site, should it still be Easy just because its trivial to cheese it?
28
Reply
akialter
100 Days Badge 2023
Oct 04, 2023

The requirements need to be more specific (i.e. what is the expected runtime of each operation, what is the memory constraint)
25
Show 1 Replies
Reply
anwendeng
Mar LeetCoding Challenge
Oct 04, 2023

How can be designing hash map easy? I used (a*x+b)%p as hash function, and implement it in a standard way. Of course, Due to the constraint 0 <= key, value <= 10^6, there is some very very supereasy way, the most of posted solutions use the easy way. Learn the standard way to design a hash map is a lesson for programmers!
23
Show 3 Replies
Reply
MrAke
30 Days of Pandas
Oct 04, 2023

I think this is not an easy problem!!
31
Show 4 Replies
Reply
Msey
100 Days Badge 2022
Apr 01, 2023

If we do "rehashing" then it's definitely not an easy question
11
Reply
timtam85
Sep 29, 2018

One of the follow-ups for this question is how to make it a concurrent hashmap. Using one lock will serialize all the operations which leads to a very low efficiency. Based on the assumption that the number of read operation will be much more than write operation, my idea is to have separate read and write lock. Any other ideas?
9
Show 1 Replies
Reply
LeetCode
Apr 22, 2022

This problem is the Daily LeetCoding Challenge for April, Day 22.

Feel free to share anything related to this problem here!

You can ask questions, discuss what you've learned from this problem, or show off how many days of streak you've made!

If you'd like to share a detailed solution to the problem, please create a new post in the discuss section and provide

    Detailed Explanations: Describe the algorithm you used to solve this problem. Include any insights you used to solve this problem.
    Images that help explain the algorithm.
    Language and Code you used to pass the problem.
    Time and Space complexity analysis.

📌 Do you want to learn the problem thoroughly?
Read ⭐ LeetCode Official Solution⭐ to learn the 3 approaches to the problem with detailed explanations to the algorithms, codes, and complexity analysis.
Spoiler Alert! We'll explain this 1 approach in the official solution

If you're new to Daily LeetCoding Challenge, check out this post!


Read more
6
Reply
Copyright ©️ 2024 LeetCode All rights reserved
7
8
9
5
6    LeetCode Logo

Problem List
0
Premium
Debugging...
Debugging...
Description
Editorial
Editorial
Solutions
Solutions
Submissions
Submissions
Code
Testcase
Test Result
Test Result
706. Design HashMap
Solved
Easy
Topics
Companies

Design a HashMap without using any built-in hash table libraries.

Implement the MyHashMap class:

    MyHashMap() initializes the object with an empty map.
    void put(int key, int value) inserts a (key, value) pair into the HashMap. If the key already exists in the map, update the corresponding value.
    int get(int key) returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key.
    void remove(key) removes the key and its corresponding value if the map contains the mapping for the key.

 

Example 1:

Input
["MyHashMap", "put", "put", "get", "get", "put", "get", "remove", "get"]
[[], [1, 1], [2, 2], [1], [3], [2, 1], [2], [2], [2]]
Output
[null, null, null, 1, -1, null, 1, null, -1]

Explanation
MyHashMap myHashMap = new MyHashMap();
myHashMap.put(1, 1); // The map is now [[1,1]]
myHashMap.put(2, 2); // The map is now [[1,1], [2,2]]
myHashMap.get(1);    // return 1, The map is now [[1,1], [2,2]]
myHashMap.get(3);    // return -1 (i.e., not found), The map is now [[1,1], [2,2]]
myHashMap.put(2, 1); // The map is now [[1,1], [2,1]] (i.e., update the existing value)
myHashMap.get(2);    // return 1, The map is now [[1,1], [2,1]]
myHashMap.remove(2); // remove the mapping for 2, The map is now [[1,1]]
myHashMap.get(2);    // return -1 (i.e., not found), The map is now [[1,1]]

 

Constraints:

    0 <= key, value <= 106
    At most 104 calls will be made to put, get, and remove.

Seen this question in a real interview before?
1/4
Yes
No
Accepted
559.4K
Submissions
850.6K
Acceptance Rate
65.8%
Topics
Array
Hash Table
Linked List
Design
Hash Function
Companies
Similar Questions
Design HashSet
Easy
Design Skiplist
Hard
Discussion (71)
💡 Discussion Rules

1. Please don't post any solutions in this discussion.

2. The problem discussion is for asking questions about the problem or for sharing tips - anything except for solutions.

3. If you'd like to share your solution for feedback and ideas, please head to the solutions tab and post it there.
firefly1
50 Days Badge 2022
Mar 05, 2023

I think this should be marked as medium not easy
74
Show 3 Replies
Reply
TheSithPadawan
50 Days Badge 2022
Oct 27, 2018

I was just skimming through the solutions in the discuss section and I'm curious why no one incorporated load factor and rehash in their design? From the mostly voted solutions, it seems like they did not change the size of the hashmap from the beginning.
54
Show 5 Replies
Reply
souvikmkhrj
100 Days Badge 2023
Oct 04, 2023

People Who watched a YT video and still struggling :

Read more
33
Show 2 Replies
Reply
c-m-d-
100 Days Badge 2022
May 14, 2023

Solving this problem "optimally" is maybe the hardest question on this site, should it still be Easy just because its trivial to cheese it?
28
Reply
akialter
100 Days Badge 2023
Oct 04, 2023

The requirements need to be more specific (i.e. what is the expected runtime of each operation, what is the memory constraint)
25
Show 1 Replies
Reply
anwendeng
Mar LeetCoding Challenge
Oct 04, 2023

How can be designing hash map easy? I used (a*x+b)%p as hash function, and implement it in a standard way. Of course, Due to the constraint 0 <= key, value <= 10^6, there is some very very supereasy way, the most of posted solutions use the easy way. Learn the standard way to design a hash map is a lesson for programmers!
23
Show 3 Replies
Reply
MrAke
30 Days of Pandas
Oct 04, 2023

I think this is not an easy problem!!
31
Show 4 Replies
Reply
Msey
100 Days Badge 2022
Apr 01, 2023

If we do "rehashing" then it's definitely not an easy question
11
Reply
timtam85
Sep 29, 2018

One of the follow-ups for this question is how to make it a concurrent hashmap. Using one lock will serialize all the operations which leads to a very low efficiency. Based on the assumption that the number of read operation will be much more than write operation, my idea is to have separate read and write lock. Any other ideas?
9
Show 1 Replies
Reply
LeetCode
Apr 22, 2022

This problem is the Daily LeetCoding Challenge for April, Day 22.

Feel free to share anything related to this problem here!

You can ask questions, discuss what you've learned from this problem, or show off how many days of streak you've made!

If you'd like to share a detailed solution to the problem, please create a new post in the discuss section and provide

    Detailed Explanations: Describe the algorithm you used to solve this problem. Include any insights you used to solve this problem.
    Images that help explain the algorithm.
    Language and Code you used to pass the problem.
    Time and Space complexity analysis.

📌 Do you want to learn the problem thoroughly?
Read ⭐ LeetCode Official Solution⭐ to learn the 3 approaches to the problem with detailed explanations to the algorithms, codes, and complexity analysis.
Spoiler Alert! We'll explain this 1 approach in the official solution

If you're new to Daily LeetCoding Challenge, check out this post!


Read more
6
Reply
Copyright ©️ 2024 LeetCode All rights reserved

Saved to local
Upgrade to Cloud Saving
["MyHashMap","put","put","get","get","put","get","remove","get"]
[[],[1,1],[2,2],[1],[3],[2,1],[2],[2],[2]]


Saved to local
Upgrade to Cloud Saving
["MyHashMap","put","put","get","get","put","get","remove","get"]
[[],[1,1],[2,2],[1],[3],[2,1],[2],[2],[2]]
1


If you'd like to share a detailed solution to the problem, please create a new post in the discuss section and provide

    Detailed Explanations: Describe the algorithm you used to solve this problem. Include any insights you used to solve this problem.
    Images that help explain the algorithm.
    Language and Code you used to pass the problem.
    Time and Space complexity analysis.

📌 Do you want to learn the problem thoroughly?
Read ⭐ LeetCode Official Solution⭐ to learn the 3 approaches to the problem with detailed explanations to the algorithms, codes, and complexity analysis.
Spoiler Alert! We'll explain this 1 approach in the official solution

If you're new to Daily LeetCoding Challenge, check out this post!


Read more
6
Reply
Copyright ©️ 2024 LeetCode All rights reserved

Saved to local
Upgrade to Cloud Saving
["MyHashMap","put","put","get","get","put","get","remove","get"]
[[],[1,1],[2,2],[1],[3],[2,1],[2],[2],[2]]
1


[null, null, null, 1, -1, null, 1, null, -1]

Explanation
MyHashMap myHashMap = new MyHashMap();
myHashMap.put(1, 1); // The map is now [[1,1]]
myHashMap.put(2, 2); // The map is now [[1,1], [2,2]]
myHashMap.get(1);    // return 1, The map is now [[1,1], [2,2]]
myHashMap.get(3);    // return -1 (i.e., not found), The map is now [[1,1], [2,2]]
myHashMap.put(2, 1); // The map is now [[1,1], [2,1]] (i.e., update the existing value)
myHashMap.get(2);    // return 1, The map is now [[1,1], [2,1]]
myHashMap.remove(2); // remove the mapping for 2, The map is now [[1,1]]
myHashMap.get(2);    // return -1 (i.e., not found), The map is now [[1,1]]

 

Constraints:

    0 <= key, value <= 106
    At most 104 calls will be made to put, get, and remove.
"""


class MyHashMap:

    def __init__(self):
        self.h = [-1] * (10**6 +1)

    def put(self, key: int, value: int) -> None:
        self.h[key] = value

    def get(self, key: int) -> int:
        return self.h[key]

    def remove(self, key: int) -> None:
        self.h[key] = -1


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)