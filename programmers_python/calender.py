
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
48
49
50
51
52
53
54
55
56
57
58
59
60
61
62
63
64
65
66
67
68
69
70
71
72
73
74
75
76
77
78
79
80
81
82
83
84
85
86
87
88
89
90
91
92
93
94
95
96
97
98
99
100
101
102
103
104
105
106
107
108
109
110
111
112
113
114
def solution(a, b):

    answer = ''

    if (a == 1) :
        if(b % 7 == 1) : answer = 'FRI' 
        elif (b % 7 == 2) : answer = 'SAT' 
        elif (b % 7 == 3) : answer = 'SUN' 
        elif (b % 7 == 4) : answer = 'MON' 
        elif (b % 7 == 5) : answer = 'TUE' 
        elif (b % 7 == 6) : answer = 'WED' 
        elif (b % 7 == 0) : answer = 'THU' 

    elif (a == 2) : 
        if(b % 7 == 1) : answer = 'MON' 
        elif (b % 7 == 2) : answer = 'TUE' 
        elif (b % 7 == 3) : answer = 'WED' 
        elif (b % 7 == 4) : answer = 'THU' 
        elif (b % 7 == 5) : answer = 'FRI' 
        elif (b % 7 == 6) : answer = 'SAT' 
        elif (b % 7 == 0) : answer = 'SUN'

    elif (a == 3) : 
        if(b % 7 == 1) : answer = 'TUE' 
        elif (b % 7 == 2) : answer = 'WED' 
        elif (b % 7 == 3) : answer = 'THU' 
        elif (b % 7 == 4) : answer = 'FRI' 
        elif (b % 7 == 5) : answer = 'SAT' 
        elif (b % 7 == 6) : answer = 'SUN' 
        elif (b % 7 == 0) : answer = 'MON' 

    elif (a == 4) : 
        if(b % 7 == 1) : answer = 'FRI' 
        elif (b % 7 == 2) : answer = 'SAT' 
        elif (b % 7 == 3) : answer = 'SUN' 
        elif (b % 7 == 4) : answer = 'MON' 
        elif (b % 7 == 5) : answer = 'TUE' 
        elif (b % 7 == 6) : answer = 'WED' 
        elif (b % 7 == 0) : answer = 'THU' 

    elif (a == 5) : 
        if(b % 7 == 1) : answer = 'SUN' 
        elif (b % 7 == 2) : answer = 'MON' 
        elif (b % 7 == 3) : answer = 'TUE' 
        elif (b % 7 == 4) : answer = 'WED' 
        elif (b % 7 == 5) : answer = 'THU' 
        elif (b % 7 == 6) : answer = 'FRI' 
        elif (b % 7 == 0) : answer = 'SAT' 

    elif (a == 6) : 
        if(b % 7 == 1) : answer = 'WED' 
        elif (b % 7 == 2) : answer = 'THU' 
        elif (b % 7 == 3) : answer = 'FRI' 
        elif (b % 7 == 4) : answer = 'SAT' 
        elif (b % 7 == 5) : answer = 'SUN' 
        elif (b % 7 == 6) : answer = 'MON' 
        elif (b % 7 == 0) : answer = 'TUE' 

    elif (a == 7) : 
        if(b % 7 == 1) : answer = 'FRI' 
        elif (b % 7 == 2) : answer = 'SAT' 
        elif (b % 7 == 3) : answer = 'SUN' 
        elif (b % 7 == 4) : answer = 'MON' 
        elif (b % 7 == 5) : answer = 'TUE' 
        elif (b % 7 == 6) : answer = 'WED' 
        elif (b % 7 == 0) : answer = 'THU' 

    elif (a == 8) : 
        if(b % 7 == 1) : answer = 'MON' 
        elif (b % 7 == 2) : answer = 'TUE' 
        elif (b % 7 == 3) : answer = 'WED' 
        elif (b % 7 == 4) : answer = 'THU' 
        elif (b % 7 == 5) : answer = 'FRI' 
        elif (b % 7 == 6) : answer = 'SAT' 
        elif (b % 7 == 0) : answer = 'SUN' 

    elif (a == 9) : 
        if(b % 7 == 1) : answer = 'THU' 
        elif (b % 7 == 2) : answer = 'FRI' 
        elif (b % 7 == 3) : answer = 'SAT' 
        elif (b % 7 == 4) : answer = 'SUN' 
        elif (b % 7 == 5) : answer = 'MON' 
        elif (b % 7 == 6) : answer = 'TUE' 
        elif (b % 7 == 0) : answer = 'WED' 

    if (a == 10) :
        if(b % 7 == 1) : answer = 'SAT' 
        elif (b % 7 == 2) : answer = 'SUN' 
        elif (b % 7 == 3) : answer = 'MON' 
        elif (b % 7 == 4) : answer = 'TUE' 
        elif (b % 7 == 5) : answer = 'WED' 
        elif (b % 7 == 6) : answer = 'THU' 
        elif (b % 7 == 0) : answer = 'FRI' 

    elif (a == 11) : 
        if(b % 7 == 1) : answer = 'THU' 
        elif (b % 7 == 2) : answer = 'WED' 
        elif (b % 7 == 3) : answer = 'THU' 
        elif (b % 7 == 4) : answer = 'FRI' 
        elif (b % 7 == 5) : answer = 'SAT' 
        elif (b % 7 == 6) : answer = 'SUN' 
        elif (b % 7 == 0) : answer = 'MON' 

    elif (a == 12) : 
        if(b % 7 == 1) : answer = 'THU' 
        elif (b % 7 == 2) : answer = 'FRI' 
        elif (b % 7 == 3) : answer = 'SAT' 
        elif (b % 7 == 4) : answer = 'SUN' 
        elif (b % 7 == 5) : answer = 'MON' 
        elif (b % 7 == 6) : answer = 'TUE' 
        elif (b % 7 == 0) : answer = 'WED' 

    return answer
