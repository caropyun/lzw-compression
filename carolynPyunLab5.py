###
# CS 3C Advanced Data Structures and Algorithms in Python
# Description:  This program encodes a given text file using LZW Compression
#               Converts text in data.txt using LZW, writes into cplzw.txt
#               Prints the dictionary created for encoding
# Solution File: carolynPyunLab5.py
# Date:  2/15/22
###

import sys


def main():
    file = open("data.txt")
    data = file.read()
    file.close()

    # Dictionary
    dictionary = {chr(i): i - 97 for i in range(97, 97 + 26)}
    dictionary[" "] = 26
    dictionary[","] = 27
    dictionary["."] = 28
    size = len(dictionary)

    encoded_data = []   # Stores the data encoded
    string = ""

    for symbol in data:   # Loops through each character
        symbol = symbol.lower()   # Convert to lowercase bc dictionary lowercase
        string_with_symbol = string + symbol
        if string_with_symbol in dictionary:   # If can match to key in dict
            string = string_with_symbol
        else:
            if symbol == '' or symbol == "\n":   # Skip the "" and new line read
                continue
            else:   # Update dictionary and size
                encoded_data.append(dictionary[string])
                dictionary[string_with_symbol] = size  # add to end
                size += 1
                string = symbol

    if string in dictionary:
        encoded_data.append(dictionary[string])

    # Write to cplzw.txt
    f = open("cplzw.txt", "a")
    for result in encoded_data:
        f.write(str(result))
        f.write('\n')
    f.close()

    # Print dictionary
    for item in dictionary:
        print(f"{item.upper()} {dictionary[item]}")


if __name__ == "__main__":
    main()

'''
A 0
B 1
C 2
D 3
E 4
F 5
G 6
H 7
I 8
J 9
K 10
L 11
M 12
N 13
O 14
P 15
Q 16
R 17
S 18
T 19
U 20
V 21
W 22
X 23
Y 24
Z 25
  26
, 27
. 28
TH 29
HE 30
E  31
 T 32
TI 33
IM 34
ME 35
E T 36
TR 37
RA 38
AV 39
VE 40
EL 41
LL 42
LE 43
ER 44
R, 45
,  46
 F 47
FO 48
OR 49
R  50
 S 51
SO 52
O  53
 I 54
IT 55
T  56
 W 57
WI 58
IL 59
LL  60
 B 61
BE 62
E C 63
CO 64
ON 65
NV 66
VEN 67
NI 68
IE 69
EN 70
NT 71
T T 72
TO 73
O S 74
SP 75
PE 76
EA 77
AK 78
K  79
 O 80
OF 81
F  82
 H 83
HI 84
IM, 85
,W 86
WA 87
AS 88
S  89
 E 90
EX 91
XP 92
PO 93
OU 94
UN 95
ND 96
DI 97
IN 98
NG 99
G  100
 A 101
A  102
 R 103
RE 104
EC 105
CON 106
NDI 107
ITE 108
E M 109
MA 110
AT 111
TT 112
TE 113
ER  114
 TO 115
O U 116
US 117
S. 118
.  119
 HI 120
IS 121
S G 122
GR 123
REY 124
Y  125
 EY 126
YE 127
ES 128
S S 129
SH 130
HO 131
ONE 132
E A 133
AN 134
NDT 135
TW 136
WIN 137
NK 138
KL 139
LED 140
D, 141
, A 142
AND 143
D  144
 HIS 145
S U 146
USU 147
UA 148
AL 149
LLY 150
Y P 151
PA 152
ALE 153
E F 154
FA 155
AC 156
CE 157
E W 158
WAS 159
S F 160
FL 161
LU 162
USH 163
HED 164
D A 165
AND  166
 AN 167
NIM 168
MAT 169
TED 170
D. 171
. T 172
THE 173
EF 174
FI 175
IR 176
RE  177
 BU 178
UR 179
RN 180
NE 181
ED 182
D B 183
BR 184
RI 185
IG 186
GH 187
HT 188
TL 189
LY 190
Y A 191
AND T 192
THE  193
 SO 194
OFT 195
T R 196
RAD 197
DIA 198
ANC 199
CE  200
 OF 201
F T 202
THE I 203
INC 204
CA 205
ANDE 206
ESC 207
CEN 208
NTL 209
LI 210
IGH 211
HTS 212
S I 213
IN  214
 TH 215
HE  216
 L 217
LIL 218
LIE 219
ES  220
 OF  221
 SI 222
ILV 223
VER 224
R C 225
CAU 226
UG 227
GHT 228
T TH 229
HE B 230
BU 231
UB 232
BB 233
BL 234
LES 235
S T 236
THA 237
AT  238
 FL 239
LA 240
ASH 241
HED  242
 AND 243
DP 244
PAS 245
SS 246
SE 247
ED  248
 IN 249
N  250
 OU 251
UR  252
 G 253
GL 254
LAS 255
SSE 256
ES. 257
'''