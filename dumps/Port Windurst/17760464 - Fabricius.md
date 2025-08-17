# 17760464 - Fabricius

## Common Data

| Field            | Value                   |
|------------------|-------------------------|
| Zone             | Port Windurst (ID: 240) |
| Block Size       | 984 bytes               |
| Total Events     | 2                       |
| References Count | 41                      |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [874](#event-874)     | 0x0001       |    793 |            149 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0002      |           2 |
|       1 | 0x0000      |           0 |
|       2 | 0x3E45      |       15941 |
|       3 | 0x3E46      |       15942 |
|       4 | 0x3E47      |       15943 |
|       5 | 0x0001      |           1 |
|       6 | 0x0010      |          16 |
|       7 | 0x04F7      |        1271 |
|       8 | 0x3E48      |       15944 |
|       9 | 0x0007      |           7 |
|      10 | 0x3E55      |       15957 |
|      11 | 0x005A      |          90 |
|      12 | 0x0047      |          71 |
|      13 | 0x3E58      |       15960 |
|      14 | 0x0006      |           6 |
|      15 | 0x0020      |          32 |
|      16 | 0x3E56      |       15958 |
|      17 | 0x0023      |          35 |
|      18 | 0x3E57      |       15959 |
|      19 | 0x0003      |           3 |
|      20 | 0x3E5B      |       15963 |
|      21 | 0x0009      |           9 |
|      22 | 0x3E50      |       15952 |
|      23 | 0x3E51      |       15953 |
|      24 | 0x3E52      |       15954 |
|      25 | 0x003C      |          60 |
|      26 | 0x001E      |          30 |
|      27 | 0x3E53      |       15955 |
|      28 | 0x3E54      |       15956 |
|      29 | 0x0004      |           4 |
|      30 | 0x3E5C      |       15964 |
|      31 | 0x3E4A      |       15946 |
|      32 | 0x3E4B      |       15947 |
|      33 | 0x3E4C      |       15948 |
|      34 | 0x3E4D      |       15949 |
|      35 | 0x3E4E      |       15950 |
|      36 | 0x3E4F      |       15951 |
|      37 | 0x3E59      |       15961 |
|      38 | 0x3E5A      |       15962 |
|      39 | 0x0005      |           5 |
|      40 | 0x3E49      |       15945 |

## String References

- **15944**: What would like to ask about? [I want $6./Learn about $5./Current $3 stock./Cavernous maw locations./Teleporting to a cavernous maw./Nothing right now.]

## Events

### Event 65535

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0000  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000: 00                                                .               
```

#### Opcodes

```
  0: 0x0000 [0x00] END_REQSTACK()
```

### Event 874

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x0001    |
| Data Size    | 793 bytes |
| Instructions | 115       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    42 03 09 00 02 10 03  01 00 03 10 03 02 00 04   B..............
0010: 10 03 04 00 05 10 03 05  00 06 10 03 06 00 07 10  ................
0020: 03 07 00 08 10 03 08 00  09 10 03 01 10 00 80 43  ...............C
0030: 00 43 01 03 00 00 03 10  4A F0 FF FF 7F D0 00 0F  .C......J.......
0040: 01 4A D0 00 0F 01 F0 FF  FF 7F 6F 76 D0 00 0F 01  .J........ov....
0050: 02 00 00 01 80 00 6B 00  2B D0 00 0F 01 02 80 23  ......k.+......#
0060: 2B D0 00 0F 01 03 80 23  01 73 00 2B D0 00 0F 01  +......#.s.+....
0070: 04 80 23 02 01 00 05 80  00 83 00 03 0A 00 01 80  ..#.............
0080: 01 88 00 03 0A 00 06 80  03 02 10 07 80 24 08 80  .............$..
0090: 01 80 0A 00 25 02 00 10  01 80 00 4E 01 29 10 F0  ....%......N.)..
00A0: FF FF 7F 5B 6E D0 00 0F  01 09 80 99 D0 00 0F 01  ...[n...........
00B0: 2B D0 00 0F 01 0A 80 1C  0B 80 23 02 04 00 01 80  +.........#.....
00C0: 80 EF 00 66 0C 80 D0 00  0F 01 D0 00 0F 01 70 61  ...f..........pa
00D0: 73 30 2B D0 00 0F 01 0D  80 23 53 D0 00 0F 01 D0  s0+......#S.....
00E0: 00 0F 01 70 61 73 30 03  01 10 0E 80 01 4B 01 02  ...pas0......K..
00F0: 04 00 05 80 80 13 01 6E  D0 00 0F 01 0F 80 99 D0  .......n........
0100: 00 0F 01 03 04 10 02 00  2B D0 00 0F 01 10 80 23  ........+......#
0110: 01 4B 01 02 04 00 00 80  80 4B 01 6E D0 00 0F 01  .K.......K.n....
0120: 11 80 99 D0 00 0F 01 2B  D0 00 0F 01 12 80 1C 0B  .......+........
0130: 80 23 03 01 10 13 80 43  00 43 01 03 02 10 07 80  .#.....C.C......
0140: 2B D0 00 0F 01 14 80 23  01 4B 01 01 18 03 02 00  +......#.K......
0150: 10 05 80 00 EC 01 66 15  80 D0 00 0F 01 D0 00 0F  ......f.........
0160: 01 74 77 62 30 03 02 10  07 80 2B D0 00 0F 01 16  .twb0.....+.....
0170: 80 23 2B D0 00 0F 01 17  80 23 2B D0 00 0F 01 18  .#+......#+.....
0180: 80 23 66 15 80 D0 00 0F  01 D0 00 0F 01 74 77 62  .#f..........twb
0190: 31 03 04 10 02 00 02 09  00 01 80 02 A6 01 03 03  1...............
01A0: 10 19 80 01 AB 01 03 03  10 1A 80 2B D0 00 0F 01  ...........+....
01B0: 1B 80 23 53 D0 00 0F 01  D0 00 0F 01 74 77 62 31  ..#S........twb1
01C0: 66 15 80 D0 00 0F 01 D0  00 0F 01 74 77 61 30 2B  f..........twa0+
01D0: D0 00 0F 01 1C 80 23 66  15 80 D0 00 0F 01 D0 00  ......#f........
01E0: 0F 01 74 77 61 31 01 73  00 01 18 03 02 00 10 00  ..twa1.s........
01F0: 80 00 39 02 02 04 00 00  80 00 1D 02 2B D0 00 0F  ..9.........+...
0200: 01 12 80 23 03 01 10 13  80 43 00 43 01 03 02 10  ...#.....C.C....
0210: 07 80 2B D0 00 0F 01 14  80 23 01 36 02 03 01 10  ..+......#.6....
0220: 1D 80 43 00 43 01 03 02  10 07 80 2B D0 00 0F 01  ..C.C......+....
0230: 1E 80 23 01 73 00 01 18  03 02 00 10 13 80 00 C4  ..#.s...........
0240: 02 66 15 80 D0 00 0F 01  D0 00 0F 01 74 68 6B 31  .f..........thk1
0250: 2B D0 00 0F 01 1F 80 23  02 05 00 05 80 00 68 02  +......#......h.
0260: 2B D0 00 0F 01 20 80 23  02 06 00 05 80 00 78 02  +.... .#......x.
0270: 2B D0 00 0F 01 21 80 23  02 07 00 05 80 00 88 02  +....!.#........
0280: 2B D0 00 0F 01 22 80 23  03 03 10 08 00 66 15 80  +....".#.....f..
0290: D0 00 0F 01 D0 00 0F 01  74 68 6B 32 2B D0 00 0F  ........thk2+...
02A0: 01 23 80 23 53 D0 00 0F  01 D0 00 0F 01 74 68 6B  .#.#S........thk
02B0: 32 03 02 10 07 80 2B D0  00 0F 01 24 80 23 01 73  2.....+....$.#.s
02C0: 00 01 18 03 02 00 10 1D  80 00 00 03 66 15 80 D0  ............f...
02D0: 00 0F 01 D0 00 0F 01 74  77 61 30 2B D0 00 0F 01  .......twa0+....
02E0: 25 80 23 66 15 80 D0 00  0F 01 D0 00 0F 01 74 77  %.#f..........tw
02F0: 61 31 2B D0 00 0F 01 26  80 23 01 73 00 01 18 03  a1+....&.#.s....
0300: 02 00 10 27 80 00 18 03  03 02 10 07 80 2B D0 00  ...'.........+..
0310: 0F 01 28 80 23 01 18 03  21 00                    ..(.#...!.      
```

#### Opcodes

```
  0: 0x0001 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  1: 0x0002 [0x03] ExtData[1]->WorkLocal[9] = Work_Zone[2]
  2: 0x0007 [0x03] ExtData[1]->WorkLocal[1] = Work_Zone[3]
  3: 0x000C [0x03] ExtData[1]->WorkLocal[2] = Work_Zone[4]
  4: 0x0011 [0x03] ExtData[1]->WorkLocal[4] = Work_Zone[5]
  5: 0x0016 [0x03] ExtData[1]->WorkLocal[5] = Work_Zone[6]
  6: 0x001B [0x03] ExtData[1]->WorkLocal[6] = Work_Zone[7]
  7: 0x0020 [0x03] ExtData[1]->WorkLocal[7] = Work_Zone[8]
  8: 0x0025 [0x03] ExtData[1]->WorkLocal[8] = Work_Zone[9]
  9: 0x002A [0x03] Work_Zone[1] = 2*
 10: 0x002F [0x43] SEND_EVENT_UPDATE: Send pending tag to server (packet 0x005B)
 11: 0x0031 [0x43] SEND_EVENT_UPDATE: Check pending flag (skip if not pending)
 12: 0x0033 [0x03] ExtData[1]->WorkLocal[0] = Work_Zone[3]
 13: 0x0038 [0x4A] LocalPlayer looks at Fabricius (ID: 17760464/0x010F00D0)
 14: 0x0041 [0x4A] Fabricius (ID: 17760464/0x010F00D0) looks at LocalPlayer
 15: 0x004A [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
 16: 0x004B [0x76] CHECK_ENTITY_RENDER_FLAGS: Wait until Fabricius (ID: 17760464/0x010F00D0) Render.Flags0 and Render.Flags3 conditions are met
 17: 0x0050 [0x02] IF !(ExtData[1]->WorkLocal[0] == 0*) GOTO 0x006B
 18: 0x0058 [0x2B] Fabricius (ID: 17760464/0x010F00D0) [15941*]:
    → "Ah, you must be the one they call <Player>. It's an honor to finally make your acquaintance."
 19: 0x005F [0x23] WAIT_FOR_DIALOG_INTERACTION
 20: 0x0060 [0x2B] Fabricius (ID: 17760464/0x010F00D0) [15942*]:
    → "My compatriot Joachim has told me much of your exploits. It'd be my pleasure to assist you any way I can."
 21: 0x0067 [0x23] WAIT_FOR_DIALOG_INTERACTION
 22: 0x0068 [0x01] GOTO 0x0073
 23: 0x006B [0x2B] Fabricius (ID: 17760464/0x010F00D0) [15943*]:
    → "Good day, <Player>. Is there something you need?"
 24: 0x0072 [0x23] WAIT_FOR_DIALOG_INTERACTION

SUBROUTINE_0073:
 25: 0x0073 [0x02] IF !(ExtData[1]->WorkLocal[1] == 1*) GOTO 0x0083
 26: 0x007B [0x03] ExtData[1]->WorkLocal[10] = 0*
 27: 0x0080 [0x01] GOTO 0x0088
 28: 0x0083 [0x03] ExtData[1]->WorkLocal[10] = 16*

SUBROUTINE_0088:
 29: 0x0088 [0x03] Work_Zone[2] = 1271*
 30: 0x008D [0x24] CREATE_DIALOG(message_id=15944*, default_option=0*, option_flags=ExtData[1]->WorkLocal[10])
    → "What would like to ask about? [I want $6./Learn about $5./Current $3 stock./Cavernous maw locations./Teleporting to a cavernous maw./Nothing right now.]"
 31: 0x0094 [0x25] WAIT_DIALOG_SELECT()
 32: 0x0095 [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x014E
 33: 0x009D [0x29] REQ_SET_WAIT(priority=0x10, entity_id=LocalPlayer, tag_num=0x5B)
 34: 0x00A4 [0x6E] Fabricius (ID: 17760464/0x010F00D0) uses emote 7*
 35: 0x00AB [0x99] Wait for Fabricius (ID: 17760464/0x010F00D0) animation to complete
 36: 0x00B0 [0x2B] Fabricius (ID: 17760464/0x010F00D0) [15957*]:
    → "Here for your $5? Let me see what I have for you..."
 37: 0x00B7 [0x1C] WAIT(90* ticks)
 38: 0x00BA [0x23] WAIT_FOR_DIALOG_INTERACTION
 39: 0x00BB [0x02] IF !(ExtData[1]->WorkLocal[4] == 0*) GOTO 0x00EF
 40: 0x00C3 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "pas0" with entities [Fabricius (ID: 17760464/0x010F00D0), Fabricius (ID: 17760464/0x010F00D0)], work=71*
 41: 0x00D2 [0x2B] Fabricius (ID: 17760464/0x010F00D0) [15960*]:
    → "Here you are, <Player>. That should suffice for the time being."
 42: 0x00D9 [0x23] WAIT_FOR_DIALOG_INTERACTION
 43: 0x00DA [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "pas0" with entities [Fabricius (ID: 17760464/0x010F00D0), Fabricius (ID: 17760464/0x010F00D0)]
 44: 0x00E7 [0x03] Work_Zone[1] = 6*
 45: 0x00EC [0x01] GOTO 0x014B
 46: 0x00EF [0x02] IF !(ExtData[1]->WorkLocal[4] == 1*) GOTO 0x0113
 47: 0x00F7 [0x6E] Fabricius (ID: 17760464/0x010F00D0) uses emote 32*
 48: 0x00FE [0x99] Wait for Fabricius (ID: 17760464/0x010F00D0) animation to complete
 49: 0x0103 [0x03] Work_Zone[4] = ExtData[1]->WorkLocal[2]
 50: 0x0108 [0x2B] Fabricius (ID: 17760464/0x010F00D0) [15958*]:
    → "Hm? Why, it appears you already have $2 stones. I'm sorry, <Player>, but it'd be irresponsible of me to furnish you with any more. Heavens forbid I have a hand in stranding you in a foreign world."
 51: 0x010F [0x23] WAIT_FOR_DIALOG_INTERACTION
 52: 0x0110 [0x01] GOTO 0x014B
 53: 0x0113 [0x02] IF !(ExtData[1]->WorkLocal[4] == 2*) GOTO 0x014B
 54: 0x011B [0x6E] Fabricius (ID: 17760464/0x010F00D0) uses emote 35*
 55: 0x0122 [0x99] Wait for Fabricius (ID: 17760464/0x010F00D0) animation to complete
 56: 0x0127 [0x2B] Fabricius (ID: 17760464/0x010F00D0) [15959*]:
    → "Oh dear, I'm afraid I don't have any fully charged stones for you right now. Could you check back again in a while?"
 57: 0x012E [0x1C] WAIT(90* ticks)
 58: 0x0131 [0x23] WAIT_FOR_DIALOG_INTERACTION
 59: 0x0132 [0x03] Work_Zone[1] = 3*
 60: 0x0137 [0x43] SEND_EVENT_UPDATE: Send pending tag to server (packet 0x005B)
 61: 0x0139 [0x43] SEND_EVENT_UPDATE: Check pending flag (skip if not pending)
 62: 0x013B [0x03] Work_Zone[2] = 1271*
 63: 0x0140 [0x2B] Fabricius (ID: 17760464/0x010F00D0) [15963*]:
    → "It'll take me $4 more [minute/minutes] (Earth time) to fully charge another $3."
 64: 0x0147 [0x23] WAIT_FOR_DIALOG_INTERACTION
 65: 0x0148 [0x01] GOTO 0x014B

SUBROUTINE_014B:
 66: 0x014B [0x01] GOTO 0x0318
 67: 0x014E [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x01EC
 68: 0x0156 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "twb0" with entities [Fabricius (ID: 17760464/0x010F00D0), Fabricius (ID: 17760464/0x010F00D0)], work=9*
 69: 0x0165 [0x03] Work_Zone[2] = 1271*
 70: 0x016A [0x2B] Fabricius (ID: 17760464/0x010F00D0) [15952*]:
    → "The function of the $3 is twofold."
 71: 0x0171 [0x23] WAIT_FOR_DIALOG_INTERACTION
 72: 0x0172 [0x2B] Fabricius (ID: 17760464/0x010F00D0) [15953*]:
    → "First and foremost, it's the key by which one gains entry to Abyssea."
 73: 0x0179 [0x23] WAIT_FOR_DIALOG_INTERACTION
 74: 0x017A [0x2B] Fabricius (ID: 17760464/0x010F00D0) [15954*]:
    → "Secondly, it serves as an anchor that secures one's essence to foreign dimensions."
 75: 0x0181 [0x23] WAIT_FOR_DIALOG_INTERACTION
 76: 0x0182 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "twb1" with entities [Fabricius (ID: 17760464/0x010F00D0), Fabricius (ID: 17760464/0x010F00D0)], work=9*
 77: 0x0191 [0x03] Work_Zone[4] = ExtData[1]->WorkLocal[2]
 78: 0x0196 [0x02] IF !(ExtData[1]->WorkLocal[9] <= 0*) GOTO 0x01A6
 79: 0x019E [0x03] Work_Zone[3] = 60*
 80: 0x01A3 [0x01] GOTO 0x01AB
 81: 0x01A6 [0x03] Work_Zone[3] = 30*

SUBROUTINE_01AB:
 82: 0x01AB [0x2B] Fabricius (ID: 17760464/0x010F00D0) [15955*]:
    → "A single stone is good for a $1-minute (Earth time) jaunt in Abyssea, and up to $2 can be in your possession at any given time. Multiplying those two numbers will give you the limit of your stay."
 83: 0x01B2 [0x23] WAIT_FOR_DIALOG_INTERACTION
 84: 0x01B3 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "twb1" with entities [Fabricius (ID: 17760464/0x010F00D0), Fabricius (ID: 17760464/0x010F00D0)]
 85: 0x01C0 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "twa0" with entities [Fabricius (ID: 17760464/0x010F00D0), Fabricius (ID: 17760464/0x010F00D0)], work=9*
 86: 0x01CF [0x2B] Fabricius (ID: 17760464/0x010F00D0) [15956*]:
    → "One thing to remember is that a good twenty hours (Earth time) are required to fully charge one stone. As such, I might not always have one on hand. I must beg your patience in that case."
 87: 0x01D6 [0x23] WAIT_FOR_DIALOG_INTERACTION
 88: 0x01D7 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "twa1" with entities [Fabricius (ID: 17760464/0x010F00D0), Fabricius (ID: 17760464/0x010F00D0)], work=9*
 89: 0x01E6 [0x01] GOTO 0x0073

SUBROUTINE_0236:
 90: 0x0236 [0x01] GOTO 0x0318
 91: 0x0239 [0x02] IF !(Work_Zone[0] == 3*) GOTO 0x02C4
 92: 0x0241 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "thk1" with entities [Fabricius (ID: 17760464/0x010F00D0), Fabricius (ID: 17760464/0x010F00D0)], work=9*
 93: 0x0250 [0x2B] Fabricius (ID: 17760464/0x010F00D0) [15946*]:
    → "Interested in the cavernous maws, are we?"
 94: 0x0257 [0x23] WAIT_FOR_DIALOG_INTERACTION
 95: 0x0258 [0x02] IF !(ExtData[1]->WorkLocal[5] == 1*) GOTO 0x0268
 96: 0x0260 [0x2B] Fabricius (ID: 17760464/0x010F00D0) [15947*]:
    → "La Theine Plateau, Konschtat Highlands, Tahrongi Canyon..."
 97: 0x0267 [0x23] WAIT_FOR_DIALOG_INTERACTION
 98: 0x0268 [0x02] IF !(ExtData[1]->WorkLocal[6] == 1*) GOTO 0x0278
 99: 0x0270 [0x2B] Fabricius (ID: 17760464/0x010F00D0) [15948*]:
    → "Jugner Forest, Valkurm Dunes, Buburimu Peninsula..."
100: 0x0277 [0x23] WAIT_FOR_DIALOG_INTERACTION
101: 0x0278 [0x02] IF !(ExtData[1]->WorkLocal[7] == 1*) GOTO 0x0288
102: 0x0280 [0x2B] Fabricius (ID: 17760464/0x010F00D0) [15949*]:
    → "Xarcabard, North Gustaberg, South Gustaberg..."
103: 0x0287 [0x23] WAIT_FOR_DIALOG_INTERACTION
104: 0x0288 [0x03] Work_Zone[3] = ExtData[1]->WorkLocal[8]
105: 0x028D [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "thk2" with entities [Fabricius (ID: 17760464/0x010F00D0), Fabricius (ID: 17760464/0x010F00D0)], work=9*
106: 0x029C [0x2B] Fabricius (ID: 17760464/0x010F00D0) [15950*]:
    → "In these [zero/three/six/nine] areas gateway maws have manifested."
107: 0x02A3 [0x23] WAIT_FOR_DIALOG_INTERACTION
108: 0x02A4 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "thk2" with entities [Fabricius (ID: 17760464/0x010F00D0), Fabricius (ID: 17760464/0x010F00D0)]
109: 0x02B1 [0x03] Work_Zone[2] = 1271*
110: 0x02B6 [0x2B] Fabricius (ID: 17760464/0x010F00D0) [15951*]:
    → "Planning a trip to Abyssea, I gather? You'd be wise to make a habit of taking stock of your $5 prior to departure."
111: 0x02BD [0x23] WAIT_FOR_DIALOG_INTERACTION
112: 0x02BE [0x01] GOTO 0x0073

SUBROUTINE_0318:
113: 0x0318 [0x21] END_EVENT
114: 0x0319 [0x00] END_REQSTACK()
```

#### Data or dead code:

```
# Dead code (unreachable instructions):
     0x01E9 [0x01] GOTO 0x0318
# Dead code (unreachable instructions):
     0x02C1 [0x01] GOTO 0x0318
     0x02FD [0x01] GOTO 0x0318
```
