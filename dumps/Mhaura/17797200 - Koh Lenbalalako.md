# 17797200 - Koh Lenbalalako

## Common Data

| Field            | Value            |
|------------------|------------------|
| Zone             | Mhaura (ID: 249) |
| Block Size       | 2032 bytes       |
| Total Events     | 19               |
| References Count | 43               |

## List of Events

| Event ID                   | Entrypoint   |   Size |   Instructions |
|----------------------------|--------------|--------|----------------|
| [65535](#event-65535)      | 0x0000       |      1 |              1 |
| [10007](#event-10007)      | 0x0001       |      7 |              2 |
| [10032](#event-10032)      | 0x0008       |      7 |              2 |
| [65535.1](#event-655351)   | 0x000F       |     10 |              2 |
| [65535.2](#event-655352)   | 0x0019       |     10 |              2 |
| [65535.3](#event-655353)   | 0x0023       |     10 |              2 |
| [65535.4](#event-655354)   | 0x002D       |     14 |              4 |
| [65535.5](#event-655355)   | 0x003B       |    164 |             26 |
| [65535.6](#event-655356)   | 0x00DF       |    665 |             82 |
| [65535.7](#event-655357)   | 0x0378       |    752 |             95 |
| [65535.8](#event-655358)   | 0x0668       |     19 |              5 |
| [65535.9](#event-655359)   | 0x067B       |     27 |              3 |
| [10009](#event-10009)      | 0x0696       |      7 |              2 |
| [10011](#event-10011)      | 0x069D       |      7 |              2 |
| [65535.10](#event-6553510) | 0x06A4       |      7 |              2 |
| [65535.11](#event-6553511) | 0x06AB       |     10 |              2 |
| [65535.12](#event-6553512) | 0x06B5       |     27 |              7 |
| [65535.13](#event-6553513) | 0x06D0       |     11 |              3 |
| [65535.14](#event-6553514) | 0x06DB       |     13 |              3 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0xFFFEEC71  |  4294896753 |
|       1 | 0x8AAD      |       35501 |
|       2 | 0xFFFFFF6A  |  4294967146 |
|       3 | 0x0F43      |        3907 |
|       4 | 0x2FAE      |       12206 |
|       5 | 0xFFFFB3D5  |  4294947797 |
|       6 | 0x5DBA      |       23994 |
|       7 | 0x078F      |        1935 |
|       8 | 0x30C5      |       12485 |
|       9 | 0xFFFFB034  |  4294946868 |
|      10 | 0x5DB4      |       23988 |
|      11 | 0x00A8      |         168 |
|      12 | 0x000D      |          13 |
|      13 | 0xFFFF3A91  |  4294916753 |
|      14 | 0x8E95      |       36501 |
|      15 | 0x0012      |          18 |
|      16 | 0x0008      |           8 |
|      17 | 0x0010      |          16 |
|      18 | 0x0000      |           0 |
|      19 | 0x0014      |          20 |
|      20 | 0x00C8      |         200 |
|      21 | 0x003C      |          60 |
|      22 | 0x001E      |          30 |
|      23 | 0x00C9      |         201 |
|      24 | 0x00A0      |         160 |
|      25 | 0x0090      |         144 |
|      26 | 0x0050      |          80 |
|      27 | 0x0064      |         100 |
|      28 | 0x0028      |          40 |
|      29 | 0x34B0      |       13488 |
|      30 | 0xFFFFAB74  |  4294945652 |
|      31 | 0x5D91      |       23953 |
|      32 | 0xFFFE9F4D  |  4294877005 |
|      33 | 0x1BB65     |      113509 |
|      34 | 0xFFFFFB50  |  4294966096 |
|      35 | 0x02CB      |         715 |
|      36 | 0xFFFEA104  |  4294877444 |
|      37 | 0x1B823     |      112675 |
|      38 | 0xFFFFFB46  |  4294966086 |
|      39 | 0x0001      |           1 |
|      40 | 0xFFFEA418  |  4294878232 |
|      41 | 0x1B748     |      112456 |
|      42 | 0x0007      |           7 |

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

### Event 10007

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0001  |
| Data Size    | 7 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    92 01 F8 FF FF 7F 00                            .......        
```

#### Opcodes

```
  0: 0x0001 [0x92] EventEntity->Render.Flags3 ^= 0x01
  1: 0x0007 [0x00] END_REQSTACK()
```

### Event 10032

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0008  |
| Data Size    | 7 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                          92 01 F8 FF FF 7F 00             ....... 
```

#### Opcodes

```
  0: 0x0008 [0x92] EventEntity->Render.Flags3 ^= 0x01
  1: 0x000E [0x00] END_REQSTACK()
```

### Event 65535.1

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x000F   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                                               37                 7
0010: 00 80 01 80 02 80 03 80  00                       .........       
```

#### Opcodes

```
  0: 0x000F [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=-70.543*, z=35.501*, y=-0.150*, direction=343.4°*
  1: 0x0018 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0019   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                             37 04 80 05 80 06 80           7......
0020: 07 80 00                                          ...             
```

#### Opcodes

```
  0: 0x0019 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=12.206*, z=-19.499*, y=23.994*, direction=170.1°*
  1: 0x0022 [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0023   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:          37 08 80 09 80  0A 80 0B 80 00              7.........   
```

#### Opcodes

```
  0: 0x0023 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=12.485*, z=-20.428*, y=23.988*, direction=14.8°*
  1: 0x002C [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x002D   |
| Data Size    | 14 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                                         32 0C 80               2..
0030: 1F 00 0D 80 0E 80 02 80  1F 01 00                 ...........     
```

#### Opcodes

```
  0: 0x002D [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x0030 [0x1F] MOVE_ENTITY: EventEntity moves to X=-50.543*, Z=36.501*, Y=-0.150*
  2: 0x0038 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x003A [0x00] END_REQSTACK()
```

### Event 65535.5

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x003B    |
| Data Size    | 164 bytes |
| Instructions | 26        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:                                   46 01 42 77 0F             F.Bw.
0040: 80 10 80 45 11 80 F0 FF  FF 7F F0 FF FF 7F 73 30  ...E..........s0
0050: 31 39 12 80 27 0B 51 90  0F 01 09 27 0B 52 90 0F  19..'.Q....'.R..
0060: 01 0A 27 0B 53 90 0F 01  0A 27 0B 54 90 0F 01 08  ..'.S....'.T....
0070: 27 0B 55 90 0F 01 08 27  0B 56 90 0F 01 08 27 0B  '.U....'.V....'.
0080: 57 90 0F 01 0B 27 0B 58  90 0F 01 08 27 0B 59 90  W....'.X....'.Y.
0090: 0F 01 06 27 0B 5A 90 0F  01 07 27 0B 5B 90 0F 01  ...'.Z....'.[...
00A0: 09 27 0B 5C 90 0F 01 07  27 0B 5D 90 0F 01 04 27  .'.\....'.]....'
00B0: 0B 5E 90 0F 01 04 27 0B  5F 90 0F 01 07 27 0B 60  .^....'._....'.`
00C0: 90 0F 01 04 2A 0B 54 90  0F 01 55 11 80 F0 FF FF  ....*.T...U.....
00D0: 7F F0 FF FF 7F 73 30 31  39 46 00 20 00 21 00     .....s019F. .!. 
```

#### Opcodes

```
  0: 0x003B [0x46] CAMERA_CONTROL: Disable user control
  1: 0x003D [0x42] SET_CLI_EVENT_CANCEL_DATA()
  2: 0x003E [0x77] SET_EVENT_TIME_WEATHER(hour=18*, weather=8*)
  3: 0x0043 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "s019" with entities [LocalPlayer, LocalPlayer], work=[16*, 0*]
  4: 0x0054 [0x27] REQ_SET(priority=0x0B, entity_id=OYAMISURA01 (ID: 17797201/0x010F9051), tag_num=0x09)
  5: 0x005B [0x27] REQ_SET(priority=0x0B, entity_id=OYAMISURA02 (ID: 17797202/0x010F9052), tag_num=0x0A)
  6: 0x0062 [0x27] REQ_SET(priority=0x0B, entity_id=OYAMISURA03 (ID: 17797203/0x010F9053), tag_num=0x0A)
  7: 0x0069 [0x27] REQ_SET(priority=0x0B, entity_id=OYAMISURA04 (ID: 17797204/0x010F9054), tag_num=0x08)
  8: 0x0070 [0x27] REQ_SET(priority=0x0B, entity_id=OYAMISURA05 (ID: 17797205/0x010F9055), tag_num=0x08)
  9: 0x0077 [0x27] REQ_SET(priority=0x0B, entity_id=OYAMISURA06 (ID: 17797206/0x010F9056), tag_num=0x08)
 10: 0x007E [0x27] REQ_SET(priority=0x0B, entity_id=OYAMISURA07 (ID: 17797207/0x010F9057), tag_num=0x0B)
 11: 0x0085 [0x27] REQ_SET(priority=0x0B, entity_id=OYAMISURA08 (ID: 17797208/0x010F9058), tag_num=0x08)
 12: 0x008C [0x27] REQ_SET(priority=0x0B, entity_id=OYAMISURA09 (ID: 17797209/0x010F9059), tag_num=0x06)
 13: 0x0093 [0x27] REQ_SET(priority=0x0B, entity_id=KOMISURA01 (ID: 17797210/0x010F905A), tag_num=0x07)
 14: 0x009A [0x27] REQ_SET(priority=0x0B, entity_id=KOMISURA02 (ID: 17797211/0x010F905B), tag_num=0x09)
 15: 0x00A1 [0x27] REQ_SET(priority=0x0B, entity_id=KOMISURA03 (ID: 17797212/0x010F905C), tag_num=0x07)
 16: 0x00A8 [0x27] REQ_SET(priority=0x0B, entity_id=Chocobo (ID: 17797213/0x010F905D), tag_num=0x04)
 17: 0x00AF [0x27] REQ_SET(priority=0x0B, entity_id=Chocobo02 (ID: 17797214/0x010F905E), tag_num=0x04)
 18: 0x00B6 [0x27] REQ_SET(priority=0x0B, entity_id=Chocobo03 (ID: 17797215/0x010F905F), tag_num=0x07)
 19: 0x00BD [0x27] REQ_SET(priority=0x0B, entity_id=Chocobo04 (ID: 17797216/0x010F9060), tag_num=0x04)
 20: 0x00C4 [0x2A] GET_REQ_LEVEL(level=11, entity_id=OYAMISURA04 (ID: 17797204/0x010F9054))
 21: 0x00CA [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "s019" with entities [LocalPlayer, LocalPlayer], work=16*
 22: 0x00D9 [0x46] CAMERA_CONTROL: Restore default settings
 23: 0x00DB [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
 24: 0x00DD [0x21] END_EVENT
 25: 0x00DE [0x00] END_REQSTACK()
```

### Event 65535.6

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x00DF    |
| Data Size    | 665 bytes |
| Instructions | 82        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00D0:                                               46                 F
00E0: 01 42 4E 00 57 90 0F 01  4E 00 53 90 0F 01 4E 00  .BN.W...N.S...N.
00F0: 52 90 0F 01 4E 00 5B 90  0F 01 4E 00 5F 90 0F 01  R...N.[...N._...
0100: 4E 01 64 90 0F 01 4E 00  61 90 0F 01 4E 00 62 90  N.d...N.a...N.b.
0110: 0F 01 4E 00 63 90 0F 01  80 57 90 0F 01 80 53 90  ..N.c....W....S.
0120: 0F 01 80 52 90 0F 01 80  5B 90 0F 01 80 5F 90 0F  ...R....[...._..
0130: 01 80 61 90 0F 01 80 62  90 0F 01 80 63 90 0F 01  ..a....b....c...
0140: 77 13 80 10 80 29 0B 52  90 0F 01 08 29 0B 53 90  w....).R....).S.
0150: 0F 01 08 29 0B 57 90 0F  01 09 29 0B 5B 90 0F 01  ...).W....).[...
0160: 07 45 14 80 F0 FF FF 7F  F0 FF FF 7F 6F 76 6C 31  .E..........ovl1
0170: 12 80 45 11 80 F0 FF FF  7F F0 FF FF 7F 73 30 32  ..E..........s02
0180: 31 12 80 27 0A 57 90 0F  01 0C 27 0A 52 90 0F 01  1..'.W....'.R...
0190: 0B 27 0A 53 90 0F 01 0B  27 0A 5F 90 0F 01 08 2A  .'.S....'._....*
01A0: 0A 57 90 0F 01 4A 57 90  0F 01 5F 90 0F 01 1C 13  .W...JW..._.....
01B0: 80 27 0A 64 90 0F 01 07  6F 76 57 90 0F 01 2A 0A  .'.d....ovW...*.
01C0: 5F 90 0F 01 52 11 80 F0  FF FF 7F F0 FF FF 7F 73  _...R..........s
01D0: 30 32 31 45 14 80 F0 FF  FF 7F F0 FF FF 7F 6F 76  021E..........ov
01E0: 6C 31 12 80 45 11 80 F0  FF FF 7F F0 FF FF 7F 73  l1..E..........s
01F0: 30 32 35 12 80 4E 00 64  90 0F 01 27 0A 61 90 0F  025..N.d...'.a..
0200: 01 07 27 0A 63 90 0F 01  07 1C 15 80 4A 57 90 0F  ..'.c.......JW..
0210: 01 64 90 0F 01 1C 16 80  52 11 80 F0 FF FF 7F F0  .d......R.......
0220: FF FF 7F 73 30 32 35 45  14 80 F0 FF FF 7F F0 FF  ...s025E........
0230: FF 7F 6F 76 6C 31 12 80  45 14 80 F0 FF FF 7F F0  ..ovl1..E.......
0240: FF FF 7F 62 6C 6F 6E 12  80 45 17 80 F0 FF FF 7F  ...blon..E......
0250: F0 FF FF 7F 62 6C 6F 6E  12 80 45 11 80 F0 FF FF  ....blon..E.....
0260: 7F F0 FF FF 7F 73 30 32  32 12 80 27 0B 57 90 0F  .....s022..'.W..
0270: 01 0D 27 0A 5B 90 0F 01  0A 2A 0A 63 90 0F 01 73  ..'.[....*.c...s
0280: 18 80 63 90 0F 01 57 90  0F 01 1C 15 80 73 18 80  ..c...W......s..
0290: 61 90 0F 01 57 90 0F 01  4A 53 90 0F 01 64 90 0F  a...W...JS...d..
02A0: 01 45 14 80 F0 FF FF 7F  F0 FF FF 7F 62 6C 6F 66  .E..........blof
02B0: 12 80 55 11 80 F0 FF FF  7F F0 FF FF 7F 73 30 32  ..U..........s02
02C0: 32 45 14 80 F0 FF FF 7F  F0 FF FF 7F 6F 76 6C 31  2E..........ovl1
02D0: 12 80 45 11 80 F0 FF FF  7F F0 FF FF 7F 73 30 32  ..E..........s02
02E0: 33 12 80 27 0A 62 90 0F  01 07 27 0A 5F 90 0F 01  3..'.b....'._...
02F0: 09 73 18 80 64 90 0F 01  57 90 0F 01 4A 53 90 0F  .s..d...W...JS..
0300: 01 62 90 0F 01 6F 76 52  90 0F 01 4A 53 90 0F 01  .b...ovR...JS...
0310: 61 90 0F 01 1C 15 80 4A  52 90 0F 01 62 90 0F 01  a......JR...b...
0320: 1C 15 80 4A 53 90 0F 01  5B 90 0F 01 55 11 80 F0  ...JS...[...U...
0330: FF FF 7F F0 FF FF 7F 73  30 32 33 45 11 80 F0 FF  .......s023E....
0340: FF 7F F0 FF FF 7F 73 30  32 34 12 80 45 19 80 F0  ......s024..E...
0350: FF FF 7F F0 FF FF 7F 6E  61 6B 32 12 80 2A 0A 62  .......nak2..*.b
0360: 90 0F 01 55 11 80 F0 FF  FF 7F F0 FF FF 7F 73 30  ...U..........s0
0370: 32 34 46 00 20 00 21 00                           24F. .!.        
```

#### Opcodes

```
  0: 0x00DF [0x46] CAMERA_CONTROL: Disable user control
  1: 0x00E1 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  2: 0x00E2 [0x4E] SET_ENTITY_HIDE_FLAG: Show OYAMISURA07 (ID: 17797207/0x010F9057)
  3: 0x00E8 [0x4E] SET_ENTITY_HIDE_FLAG: Show OYAMISURA03 (ID: 17797203/0x010F9053)
  4: 0x00EE [0x4E] SET_ENTITY_HIDE_FLAG: Show OYAMISURA02 (ID: 17797202/0x010F9052)
  5: 0x00F4 [0x4E] SET_ENTITY_HIDE_FLAG: Show KOMISURA02 (ID: 17797211/0x010F905B)
  6: 0x00FA [0x4E] SET_ENTITY_HIDE_FLAG: Show Chocobo03 (ID: 17797215/0x010F905F)
  7: 0x0100 [0x4E] SET_ENTITY_HIDE_FLAG: Hide Yagudo04 (ID: 17797220/0x010F9064)
  8: 0x0106 [0x4E] SET_ENTITY_HIDE_FLAG: Show Yagudo01 (ID: 17797217/0x010F9061)
  9: 0x010C [0x4E] SET_ENTITY_HIDE_FLAG: Show Yagudo02 (ID: 17797218/0x010F9062)
 10: 0x0112 [0x4E] SET_ENTITY_HIDE_FLAG: Show Yagudo03 (ID: 17797219/0x010F9063)
 11: 0x0118 [0x80] LOAD_WAIT(entity=OYAMISURA07 (ID: 17797207/0x010F9057))
 12: 0x011D [0x80] LOAD_WAIT(entity=OYAMISURA03 (ID: 17797203/0x010F9053))
 13: 0x0122 [0x80] LOAD_WAIT(entity=OYAMISURA02 (ID: 17797202/0x010F9052))
 14: 0x0127 [0x80] LOAD_WAIT(entity=KOMISURA02 (ID: 17797211/0x010F905B))
 15: 0x012C [0x80] LOAD_WAIT(entity=Chocobo03 (ID: 17797215/0x010F905F))
 16: 0x0131 [0x80] LOAD_WAIT(entity=Yagudo01 (ID: 17797217/0x010F9061))
 17: 0x0136 [0x80] LOAD_WAIT(entity=Yagudo02 (ID: 17797218/0x010F9062))
 18: 0x013B [0x80] LOAD_WAIT(entity=Yagudo03 (ID: 17797219/0x010F9063))
 19: 0x0140 [0x77] SET_EVENT_TIME_WEATHER(hour=20*, weather=8*)
 20: 0x0145 [0x29] REQ_SET_WAIT(priority=0x0B, entity_id=OYAMISURA02 (ID: 17797202/0x010F9052), tag_num=0x08)
 21: 0x014C [0x29] REQ_SET_WAIT(priority=0x0B, entity_id=OYAMISURA03 (ID: 17797203/0x010F9053), tag_num=0x08)
 22: 0x0153 [0x29] REQ_SET_WAIT(priority=0x0B, entity_id=OYAMISURA07 (ID: 17797207/0x010F9057), tag_num=0x09)
 23: 0x015A [0x29] REQ_SET_WAIT(priority=0x0B, entity_id=KOMISURA02 (ID: 17797211/0x010F905B), tag_num=0x07)
 24: 0x0161 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "ovl1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 25: 0x0172 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "s021" with entities [LocalPlayer, LocalPlayer], work=[16*, 0*]
 26: 0x0183 [0x27] REQ_SET(priority=0x0A, entity_id=OYAMISURA07 (ID: 17797207/0x010F9057), tag_num=0x0C)
 27: 0x018A [0x27] REQ_SET(priority=0x0A, entity_id=OYAMISURA02 (ID: 17797202/0x010F9052), tag_num=0x0B)
 28: 0x0191 [0x27] REQ_SET(priority=0x0A, entity_id=OYAMISURA03 (ID: 17797203/0x010F9053), tag_num=0x0B)
 29: 0x0198 [0x27] REQ_SET(priority=0x0A, entity_id=Chocobo03 (ID: 17797215/0x010F905F), tag_num=0x08)
 30: 0x019F [0x2A] GET_REQ_LEVEL(level=10, entity_id=OYAMISURA07 (ID: 17797207/0x010F9057))
 31: 0x01A5 [0x4A] OYAMISURA07 (ID: 17797207/0x010F9057) looks at Chocobo03 (ID: 17797215/0x010F905F)
 32: 0x01AE [0x1C] WAIT(20* ticks)
 33: 0x01B1 [0x27] REQ_SET(priority=0x0A, entity_id=Yagudo04 (ID: 17797220/0x010F9064), tag_num=0x07)
 34: 0x01B8 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
 35: 0x01B9 [0x76] CHECK_ENTITY_RENDER_FLAGS: Wait until OYAMISURA07 (ID: 17797207/0x010F9057) Render.Flags0 and Render.Flags3 conditions are met
 36: 0x01BE [0x2A] GET_REQ_LEVEL(level=10, entity_id=Chocobo03 (ID: 17797215/0x010F905F))
 37: 0x01C4 [0x52] END_LOAD_SCHEDULER: End scheduler "s021" with entities [LocalPlayer, LocalPlayer], work=16*
 38: 0x01D3 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "ovl1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 39: 0x01E4 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "s025" with entities [LocalPlayer, LocalPlayer], work=[16*, 0*]
 40: 0x01F5 [0x4E] SET_ENTITY_HIDE_FLAG: Show Yagudo04 (ID: 17797220/0x010F9064)
 41: 0x01FB [0x27] REQ_SET(priority=0x0A, entity_id=Yagudo01 (ID: 17797217/0x010F9061), tag_num=0x07)
 42: 0x0202 [0x27] REQ_SET(priority=0x0A, entity_id=Yagudo03 (ID: 17797219/0x010F9063), tag_num=0x07)
 43: 0x0209 [0x1C] WAIT(60* ticks)
 44: 0x020C [0x4A] OYAMISURA07 (ID: 17797207/0x010F9057) looks at Yagudo04 (ID: 17797220/0x010F9064)
 45: 0x0215 [0x1C] WAIT(30* ticks)
 46: 0x0218 [0x52] END_LOAD_SCHEDULER: End scheduler "s025" with entities [LocalPlayer, LocalPlayer], work=16*
 47: 0x0227 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "ovl1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 48: 0x0238 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "blon" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 49: 0x0249 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "blon" with entities [LocalPlayer, LocalPlayer], work=[201*, 0*]
 50: 0x025A [0x45] LOAD_SCHEDULED_TASK: Load scheduler "s022" with entities [LocalPlayer, LocalPlayer], work=[16*, 0*]
 51: 0x026B [0x27] REQ_SET(priority=0x0B, entity_id=OYAMISURA07 (ID: 17797207/0x010F9057), tag_num=0x0D)
 52: 0x0272 [0x27] REQ_SET(priority=0x0A, entity_id=KOMISURA02 (ID: 17797211/0x010F905B), tag_num=0x0A)
 53: 0x0279 [0x2A] GET_REQ_LEVEL(level=10, entity_id=Yagudo03 (ID: 17797219/0x010F9063))
 54: 0x027F [0x73] Yagudo03 (ID: 17797219/0x010F9063) casts magic 160* on OYAMISURA07 (ID: 17797207/0x010F9057)
 55: 0x028A [0x1C] WAIT(60* ticks)
 56: 0x028D [0x73] Yagudo01 (ID: 17797217/0x010F9061) casts magic 160* on OYAMISURA07 (ID: 17797207/0x010F9057)
 57: 0x0298 [0x4A] OYAMISURA03 (ID: 17797203/0x010F9053) looks at Yagudo04 (ID: 17797220/0x010F9064)
 58: 0x02A1 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "blof" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 59: 0x02B2 [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "s022" with entities [LocalPlayer, LocalPlayer], work=16*
 60: 0x02C1 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "ovl1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 61: 0x02D2 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "s023" with entities [LocalPlayer, LocalPlayer], work=[16*, 0*]
 62: 0x02E3 [0x27] REQ_SET(priority=0x0A, entity_id=Yagudo02 (ID: 17797218/0x010F9062), tag_num=0x07)
 63: 0x02EA [0x27] REQ_SET(priority=0x0A, entity_id=Chocobo03 (ID: 17797215/0x010F905F), tag_num=0x09)
 64: 0x02F1 [0x73] Yagudo04 (ID: 17797220/0x010F9064) casts magic 160* on OYAMISURA07 (ID: 17797207/0x010F9057)
 65: 0x02FC [0x4A] OYAMISURA03 (ID: 17797203/0x010F9053) looks at Yagudo02 (ID: 17797218/0x010F9062)
 66: 0x0305 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
 67: 0x0306 [0x76] CHECK_ENTITY_RENDER_FLAGS: Wait until OYAMISURA02 (ID: 17797202/0x010F9052) Render.Flags0 and Render.Flags3 conditions are met
 68: 0x030B [0x4A] OYAMISURA03 (ID: 17797203/0x010F9053) looks at Yagudo01 (ID: 17797217/0x010F9061)
 69: 0x0314 [0x1C] WAIT(60* ticks)
 70: 0x0317 [0x4A] OYAMISURA02 (ID: 17797202/0x010F9052) looks at Yagudo02 (ID: 17797218/0x010F9062)
 71: 0x0320 [0x1C] WAIT(60* ticks)
 72: 0x0323 [0x4A] OYAMISURA03 (ID: 17797203/0x010F9053) looks at KOMISURA02 (ID: 17797211/0x010F905B)
 73: 0x032C [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "s023" with entities [LocalPlayer, LocalPlayer], work=16*
 74: 0x033B [0x45] LOAD_SCHEDULED_TASK: Load scheduler "s024" with entities [LocalPlayer, LocalPlayer], work=[16*, 0*]
 75: 0x034C [0x45] LOAD_SCHEDULED_TASK: Load scheduler "nak2" with entities [LocalPlayer, LocalPlayer], work=[144*, 0*]
 76: 0x035D [0x2A] GET_REQ_LEVEL(level=10, entity_id=Yagudo02 (ID: 17797218/0x010F9062))
 77: 0x0363 [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "s024" with entities [LocalPlayer, LocalPlayer], work=16*
 78: 0x0372 [0x46] CAMERA_CONTROL: Restore default settings
 79: 0x0374 [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
 80: 0x0376 [0x21] END_EVENT
 81: 0x0377 [0x00] END_REQSTACK()
```

### Event 65535.7

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x0378    |
| Data Size    | 752 bytes |
| Instructions | 95        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0370:                          46 01 42 45 14 80 F8 FF          F.BE....
0380: FF 7F F8 FF FF 7F 66 64  6F 31 12 80 1C 15 80 4E  ......fdo1.....N
0390: 01 F0 FF FF 7F 4E 01 62  90 0F 01 29 0A 61 90 0F  .....N.b...).a..
03A0: 01 05 29 0A 62 90 0F 01  05 29 0A 63 90 0F 01 05  ..).b....).c....
03B0: 29 0A 64 90 0F 01 05 29  0A 50 90 0F 01 04 29 0A  ).d....).P....).
03C0: 51 90 0F 01 08 29 0A 52  90 0F 01 09 29 0A 53 90  Q....).R....).S.
03D0: 0F 01 09 29 0A 54 90 0F  01 07 29 0A 55 90 0F 01  ...).T....).U...
03E0: 07 29 0A 56 90 0F 01 07  29 0A 57 90 0F 01 0A 29  .).V....).W....)
03F0: 0A 58 90 0F 01 07 29 0A  5A 90 0F 01 06 29 0A 5B  .X....).Z....).[
0400: 90 0F 01 08 29 0A 5C 90  0F 01 06 27 08 51 90 0F  ....).\....'.Q..
0410: 01 05 27 08 54 90 0F 01  05 27 08 55 90 0F 01 05  ..'.T....'.U....
0420: 27 08 57 90 0F 01 06 29  08 58 90 0F 01 05 45 11  '.W....).X....E.
0430: 80 F0 FF FF 7F F0 FF FF  7F 73 30 32 36 12 80 45  .........s026..E
0440: 14 80 F8 FF FF 7F F8 FF  FF 7F 66 64 69 31 12 80  ..........fdi1..
0450: 55 11 80 F0 FF FF 7F F0  FF FF 7F 73 30 32 36 45  U..........s026E
0460: 14 80 F0 FF FF 7F F0 FF  FF 7F 6F 76 6C 31 12 80  ..........ovl1..
0470: 45 11 80 F0 FF FF 7F F0  FF FF 7F 73 30 32 37 12  E..........s027.
0480: 80 4E 00 62 90 0F 01 27  08 56 90 0F 01 09 1C 1A  .N.b...'.V......
0490: 80 4A 52 90 0F 01 63 90  0F 01 4A 53 90 0F 01 63  .JR...c...JS...c
04A0: 90 0F 01 1C 13 80 4A 50  90 0F 01 63 90 0F 01 2A  ......JP...c...*
04B0: 08 56 90 0F 01 55 11 80  F0 FF FF 7F F0 FF FF 7F  .V...U..........
04C0: 73 30 32 37 80 62 90 0F  01 45 14 80 F0 FF FF 7F  s027.b...E......
04D0: F0 FF FF 7F 6F 76 6C 31  12 80 45 11 80 F0 FF FF  ....ovl1..E.....
04E0: 7F F0 FF FF 7F 73 30 32  38 12 80 4A 61 90 0F 01  .....s028..Ja...
04F0: 62 90 0F 01 4A 5A 90 0F  01 62 90 0F 01 4A 5B 90  b...JZ...b...J[.
0500: 0F 01 62 90 0F 01 6F 76  5B 90 0F 01 27 08 57 90  ..b...ov[...'.W.
0510: 0F 01 07 29 08 51 90 0F  01 06 27 0A 62 90 0F 01  ...).Q....'.b...
0520: 08 27 0A 63 90 0F 01 08  27 0A 64 90 0F 01 08 1C  .'.c....'.d.....
0530: 15 80 52 11 80 F0 FF FF  7F F0 FF FF 7F 73 30 32  ..R..........s02
0540: 38 45 14 80 F0 FF FF 7F  F0 FF FF 7F 6F 76 6C 31  8E..........ovl1
0550: 12 80 45 11 80 F0 FF FF  7F F0 FF FF 7F 73 30 32  ..E..........s02
0560: 39 12 80 1C 1B 80 29 08  51 90 0F 01 0A 2A 0A 63  9.....).Q....*.c
0570: 90 0F 01 45 14 80 F8 FF  FF 7F F8 FF FF 7F 66 64  ...E..........fd
0580: 6F 31 12 80 1C 15 80 52  11 80 F0 FF FF 7F F0 FF  o1.....R........
0590: FF 7F 73 30 32 39 45 11  80 F0 FF FF 7F F0 FF FF  ..s029E.........
05A0: 7F 73 30 33 30 12 80 29  0A 61 90 0F 01 06 29 0A  .s030..).a....).
05B0: 62 90 0F 01 06 29 0A 63  90 0F 01 06 29 0A 64 90  b....).c....).d.
05C0: 0F 01 06 29 0A 50 90 0F  01 05 27 0A 51 90 0F 01  ...).P....'.Q...
05D0: 0B 27 0A 62 90 0F 01 09  4A 50 90 0F 01 51 90 0F  .'.b....JP...Q..
05E0: 01 6F 76 50 90 0F 01 4A  64 90 0F 01 51 90 0F 01  .ovP...Jd...Q...
05F0: 45 14 80 F8 FF FF 7F F8  FF FF 7F 66 64 69 31 12  E..........fdi1.
0600: 80 1C 13 80 4A 64 90 0F  01 51 90 0F 01 1C 13 80  ....Jd...Q......
0610: 27 0A 64 90 0F 01 09 1C  16 80 79 00 50 90 0F 01  '.d.......y.P...
0620: 51 90 0F 01 27 0A 5B 90  0F 01 0B 1E 50 90 0F 01  Q...'.[.....P...
0630: 1C 1C 80 27 0A 50 90 0F  01 0A 1C 1C 80 45 14 80  ...'.P.......E..
0640: F8 FF FF 7F F8 FF FF 7F  66 64 6F 31 12 80 1C 15  ........fdo1....
0650: 80 45 14 80 F8 FF FF 7F  F8 FF FF 7F 66 64 69 31  .E..........fdi1
0660: 12 80 46 00 20 00 21 00                           ..F. .!.        
```

#### Opcodes

```
  0: 0x0378 [0x46] CAMERA_CONTROL: Disable user control
  1: 0x037A [0x42] SET_CLI_EVENT_CANCEL_DATA()
  2: 0x037B [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [EventEntity, EventEntity], work=[200*, 0*]
  3: 0x038C [0x1C] WAIT(60* ticks)
  4: 0x038F [0x4E] SET_ENTITY_HIDE_FLAG: Hide LocalPlayer
  5: 0x0395 [0x4E] SET_ENTITY_HIDE_FLAG: Hide Yagudo02 (ID: 17797218/0x010F9062)
  6: 0x039B [0x29] REQ_SET_WAIT(priority=0x0A, entity_id=Yagudo01 (ID: 17797217/0x010F9061), tag_num=0x05)
  7: 0x03A2 [0x29] REQ_SET_WAIT(priority=0x0A, entity_id=Yagudo02 (ID: 17797218/0x010F9062), tag_num=0x05)
  8: 0x03A9 [0x29] REQ_SET_WAIT(priority=0x0A, entity_id=Yagudo03 (ID: 17797219/0x010F9063), tag_num=0x05)
  9: 0x03B0 [0x29] REQ_SET_WAIT(priority=0x0A, entity_id=Yagudo04 (ID: 17797220/0x010F9064), tag_num=0x05)
 10: 0x03B7 [0x29] REQ_SET_WAIT(priority=0x0A, entity_id=Koh Lenbalalako (ID: 17797200/0x010F9050), tag_num=0x04)
 11: 0x03BE [0x29] REQ_SET_WAIT(priority=0x0A, entity_id=OYAMISURA01 (ID: 17797201/0x010F9051), tag_num=0x08)
 12: 0x03C5 [0x29] REQ_SET_WAIT(priority=0x0A, entity_id=OYAMISURA02 (ID: 17797202/0x010F9052), tag_num=0x09)
 13: 0x03CC [0x29] REQ_SET_WAIT(priority=0x0A, entity_id=OYAMISURA03 (ID: 17797203/0x010F9053), tag_num=0x09)
 14: 0x03D3 [0x29] REQ_SET_WAIT(priority=0x0A, entity_id=OYAMISURA04 (ID: 17797204/0x010F9054), tag_num=0x07)
 15: 0x03DA [0x29] REQ_SET_WAIT(priority=0x0A, entity_id=OYAMISURA05 (ID: 17797205/0x010F9055), tag_num=0x07)
 16: 0x03E1 [0x29] REQ_SET_WAIT(priority=0x0A, entity_id=OYAMISURA06 (ID: 17797206/0x010F9056), tag_num=0x07)
 17: 0x03E8 [0x29] REQ_SET_WAIT(priority=0x0A, entity_id=OYAMISURA07 (ID: 17797207/0x010F9057), tag_num=0x0A)
 18: 0x03EF [0x29] REQ_SET_WAIT(priority=0x0A, entity_id=OYAMISURA08 (ID: 17797208/0x010F9058), tag_num=0x07)
 19: 0x03F6 [0x29] REQ_SET_WAIT(priority=0x0A, entity_id=KOMISURA01 (ID: 17797210/0x010F905A), tag_num=0x06)
 20: 0x03FD [0x29] REQ_SET_WAIT(priority=0x0A, entity_id=KOMISURA02 (ID: 17797211/0x010F905B), tag_num=0x08)
 21: 0x0404 [0x29] REQ_SET_WAIT(priority=0x0A, entity_id=KOMISURA03 (ID: 17797212/0x010F905C), tag_num=0x06)
 22: 0x040B [0x27] REQ_SET(priority=0x08, entity_id=OYAMISURA01 (ID: 17797201/0x010F9051), tag_num=0x05)
 23: 0x0412 [0x27] REQ_SET(priority=0x08, entity_id=OYAMISURA04 (ID: 17797204/0x010F9054), tag_num=0x05)
 24: 0x0419 [0x27] REQ_SET(priority=0x08, entity_id=OYAMISURA05 (ID: 17797205/0x010F9055), tag_num=0x05)
 25: 0x0420 [0x27] REQ_SET(priority=0x08, entity_id=OYAMISURA07 (ID: 17797207/0x010F9057), tag_num=0x06)
 26: 0x0427 [0x29] REQ_SET_WAIT(priority=0x08, entity_id=OYAMISURA08 (ID: 17797208/0x010F9058), tag_num=0x05)
 27: 0x042E [0x45] LOAD_SCHEDULED_TASK: Load scheduler "s026" with entities [LocalPlayer, LocalPlayer], work=[16*, 0*]
 28: 0x043F [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi1" with entities [EventEntity, EventEntity], work=[200*, 0*]
 29: 0x0450 [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "s026" with entities [LocalPlayer, LocalPlayer], work=16*
 30: 0x045F [0x45] LOAD_SCHEDULED_TASK: Load scheduler "ovl1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 31: 0x0470 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "s027" with entities [LocalPlayer, LocalPlayer], work=[16*, 0*]
 32: 0x0481 [0x4E] SET_ENTITY_HIDE_FLAG: Show Yagudo02 (ID: 17797218/0x010F9062)
 33: 0x0487 [0x27] REQ_SET(priority=0x08, entity_id=OYAMISURA06 (ID: 17797206/0x010F9056), tag_num=0x09)
 34: 0x048E [0x1C] WAIT(80* ticks)
 35: 0x0491 [0x4A] OYAMISURA02 (ID: 17797202/0x010F9052) looks at Yagudo03 (ID: 17797219/0x010F9063)
 36: 0x049A [0x4A] OYAMISURA03 (ID: 17797203/0x010F9053) looks at Yagudo03 (ID: 17797219/0x010F9063)
 37: 0x04A3 [0x1C] WAIT(20* ticks)
 38: 0x04A6 [0x4A] Koh Lenbalalako (ID: 17797200/0x010F9050) looks at Yagudo03 (ID: 17797219/0x010F9063)
 39: 0x04AF [0x2A] GET_REQ_LEVEL(level=8, entity_id=OYAMISURA06 (ID: 17797206/0x010F9056))
 40: 0x04B5 [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "s027" with entities [LocalPlayer, LocalPlayer], work=16*
 41: 0x04C4 [0x80] LOAD_WAIT(entity=Yagudo02 (ID: 17797218/0x010F9062))
 42: 0x04C9 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "ovl1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 43: 0x04DA [0x45] LOAD_SCHEDULED_TASK: Load scheduler "s028" with entities [LocalPlayer, LocalPlayer], work=[16*, 0*]
 44: 0x04EB [0x4A] Yagudo01 (ID: 17797217/0x010F9061) looks at Yagudo02 (ID: 17797218/0x010F9062)
 45: 0x04F4 [0x4A] KOMISURA01 (ID: 17797210/0x010F905A) looks at Yagudo02 (ID: 17797218/0x010F9062)
 46: 0x04FD [0x4A] KOMISURA02 (ID: 17797211/0x010F905B) looks at Yagudo02 (ID: 17797218/0x010F9062)
 47: 0x0506 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
 48: 0x0507 [0x76] CHECK_ENTITY_RENDER_FLAGS: Wait until KOMISURA02 (ID: 17797211/0x010F905B) Render.Flags0 and Render.Flags3 conditions are met
 49: 0x050C [0x27] REQ_SET(priority=0x08, entity_id=OYAMISURA07 (ID: 17797207/0x010F9057), tag_num=0x07)
 50: 0x0513 [0x29] REQ_SET_WAIT(priority=0x08, entity_id=OYAMISURA01 (ID: 17797201/0x010F9051), tag_num=0x06)
 51: 0x051A [0x27] REQ_SET(priority=0x0A, entity_id=Yagudo02 (ID: 17797218/0x010F9062), tag_num=0x08)
 52: 0x0521 [0x27] REQ_SET(priority=0x0A, entity_id=Yagudo03 (ID: 17797219/0x010F9063), tag_num=0x08)
 53: 0x0528 [0x27] REQ_SET(priority=0x0A, entity_id=Yagudo04 (ID: 17797220/0x010F9064), tag_num=0x08)
 54: 0x052F [0x1C] WAIT(60* ticks)
 55: 0x0532 [0x52] END_LOAD_SCHEDULER: End scheduler "s028" with entities [LocalPlayer, LocalPlayer], work=16*
 56: 0x0541 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "ovl1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 57: 0x0552 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "s029" with entities [LocalPlayer, LocalPlayer], work=[16*, 0*]
 58: 0x0563 [0x1C] WAIT(100* ticks)
 59: 0x0566 [0x29] REQ_SET_WAIT(priority=0x08, entity_id=OYAMISURA01 (ID: 17797201/0x010F9051), tag_num=0x0A)
 60: 0x056D [0x2A] GET_REQ_LEVEL(level=10, entity_id=Yagudo03 (ID: 17797219/0x010F9063))
 61: 0x0573 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [EventEntity, EventEntity], work=[200*, 0*]
 62: 0x0584 [0x1C] WAIT(60* ticks)
 63: 0x0587 [0x52] END_LOAD_SCHEDULER: End scheduler "s029" with entities [LocalPlayer, LocalPlayer], work=16*
 64: 0x0596 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "s030" with entities [LocalPlayer, LocalPlayer], work=[16*, 0*]
 65: 0x05A7 [0x29] REQ_SET_WAIT(priority=0x0A, entity_id=Yagudo01 (ID: 17797217/0x010F9061), tag_num=0x06)
 66: 0x05AE [0x29] REQ_SET_WAIT(priority=0x0A, entity_id=Yagudo02 (ID: 17797218/0x010F9062), tag_num=0x06)
 67: 0x05B5 [0x29] REQ_SET_WAIT(priority=0x0A, entity_id=Yagudo03 (ID: 17797219/0x010F9063), tag_num=0x06)
 68: 0x05BC [0x29] REQ_SET_WAIT(priority=0x0A, entity_id=Yagudo04 (ID: 17797220/0x010F9064), tag_num=0x06)
 69: 0x05C3 [0x29] REQ_SET_WAIT(priority=0x0A, entity_id=Koh Lenbalalako (ID: 17797200/0x010F9050), tag_num=0x05)
 70: 0x05CA [0x27] REQ_SET(priority=0x0A, entity_id=OYAMISURA01 (ID: 17797201/0x010F9051), tag_num=0x0B)
 71: 0x05D1 [0x27] REQ_SET(priority=0x0A, entity_id=Yagudo02 (ID: 17797218/0x010F9062), tag_num=0x09)
 72: 0x05D8 [0x4A] Koh Lenbalalako (ID: 17797200/0x010F9050) looks at OYAMISURA01 (ID: 17797201/0x010F9051)
 73: 0x05E1 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
 74: 0x05E2 [0x76] CHECK_ENTITY_RENDER_FLAGS: Wait until Koh Lenbalalako (ID: 17797200/0x010F9050) Render.Flags0 and Render.Flags3 conditions are met
 75: 0x05E7 [0x4A] Yagudo04 (ID: 17797220/0x010F9064) looks at OYAMISURA01 (ID: 17797201/0x010F9051)
 76: 0x05F0 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi1" with entities [EventEntity, EventEntity], work=[200*, 0*]
 77: 0x0601 [0x1C] WAIT(20* ticks)
 78: 0x0604 [0x4A] Yagudo04 (ID: 17797220/0x010F9064) looks at OYAMISURA01 (ID: 17797201/0x010F9051)
 79: 0x060D [0x1C] WAIT(20* ticks)
 80: 0x0610 [0x27] REQ_SET(priority=0x0A, entity_id=Yagudo04 (ID: 17797220/0x010F9064), tag_num=0x09)
 81: 0x0617 [0x1C] WAIT(30* ticks)
 82: 0x061A [0x79] Koh Lenbalalako (ID: 17797200/0x010F9050) looks at OYAMISURA01 (ID: 17797201/0x010F9051) (Basic look)
 83: 0x0624 [0x27] REQ_SET(priority=0x0A, entity_id=KOMISURA02 (ID: 17797211/0x010F905B), tag_num=0x0B)
 84: 0x062B [0x1E] EventEntity looks at Koh Lenbalalako (ID: 17797200/0x010F9050) and starts talking
 85: 0x0630 [0x1C] WAIT(40* ticks)
 86: 0x0633 [0x27] REQ_SET(priority=0x0A, entity_id=Koh Lenbalalako (ID: 17797200/0x010F9050), tag_num=0x0A)
 87: 0x063A [0x1C] WAIT(40* ticks)
 88: 0x063D [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [EventEntity, EventEntity], work=[200*, 0*]
 89: 0x064E [0x1C] WAIT(60* ticks)
 90: 0x0651 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi1" with entities [EventEntity, EventEntity], work=[200*, 0*]
 91: 0x0662 [0x46] CAMERA_CONTROL: Restore default settings
 92: 0x0664 [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
 93: 0x0666 [0x21] END_EVENT
 94: 0x0667 [0x00] END_REQSTACK()
```

### Event 65535.8

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0668   |
| Data Size    | 19 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0660:                          32 0C 80 1F 00 1D 80 1E          2.......
0670: 80 1F 80 1F 01 1E 51 90  0F 01 00                 ......Q....     
```

#### Opcodes

```
  0: 0x0668 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x066B [0x1F] MOVE_ENTITY: EventEntity moves to X=13.488*, Z=-21.644*, Y=23.953*
  2: 0x0673 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0675 [0x1E] EventEntity looks at OYAMISURA01 (ID: 17797201/0x010F9051) and starts talking
  4: 0x067A [0x00] END_REQSTACK()
```

### Event 65535.9

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x067B   |
| Data Size    | 27 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0670:                                   2C 50 90 0F 01             ,P...
0680: 50 90 0F 01 72 65 73 31  53 F8 FF FF 7F F8 FF FF  P...res1S.......
0690: 7F 72 65 73 31 00                                 .res1.          
```

#### Opcodes

```
  0: 0x067B [0x2C] CREATE_SCHEDULER_TASK: Create scheduler "res1" with entities [Koh Lenbalalako (ID: 17797200/0x010F9050), Koh Lenbalalako (ID: 17797200/0x010F9050)]
  1: 0x0688 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "res1" with entities [EventEntity, EventEntity]
  2: 0x0695 [0x00] END_REQSTACK()
```

### Event 10009

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0696  |
| Data Size    | 7 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0690:                   92 01  F8 FF FF 7F 00                 .......   
```

#### Opcodes

```
  0: 0x0696 [0x92] EventEntity->Render.Flags3 ^= 0x01
  1: 0x069C [0x00] END_REQSTACK()
```

### Event 10011

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x069D  |
| Data Size    | 7 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0690:                                         92 01 F8               ...
06A0: FF FF 7F 00                                       ....            
```

#### Opcodes

```
  0: 0x069D [0x92] EventEntity->Render.Flags3 ^= 0x01
  1: 0x06A3 [0x00] END_REQSTACK()
```

### Event 65535.10

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x06A4  |
| Data Size    | 7 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
06A0:             92 01 F8 FF  FF 7F 00                     .......     
```

#### Opcodes

```
  0: 0x06A4 [0x92] EventEntity->Render.Flags3 ^= 0x01
  1: 0x06AA [0x00] END_REQSTACK()
```

### Event 65535.11

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x06AB   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
06A0:                                   37 20 80 21 80             7 .!.
06B0: 22 80 23 80 00                                    ".#..           
```

#### Opcodes

```
  0: 0x06AB [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=-90.291*, z=113.509*, y=-1.200*, direction=62.8°*
  1: 0x06B4 [0x00] END_REQSTACK()
```

### Event 65535.12

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x06B5   |
| Data Size    | 27 bytes |
| Instructions | 7        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
06B0:                32 0C 80  1F 00 24 80 25 80 26 80       2....$.%.&.
06C0: 1F 01 6F 6E F8 FF FF 7F  27 80 99 F8 FF FF 7F 00  ..on....'.......
```

#### Opcodes

```
  0: 0x06B5 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x06B8 [0x1F] MOVE_ENTITY: EventEntity moves to X=-89.852*, Z=112.675*, Y=-1.210*
  2: 0x06C0 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x06C2 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x06C3 [0x6E] EventEntity uses emote 1*
  5: 0x06CA [0x99] Wait for EventEntity animation to complete
  6: 0x06CF [0x00] END_REQSTACK()
```

### Event 65535.13

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x06D0   |
| Data Size    | 11 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
06D0: 1F 00 28 80 29 80 26 80  1F 01 00                 ..(.).&....     
```

#### Opcodes

```
  0: 0x06D0 [0x1F] MOVE_ENTITY: EventEntity moves to X=-89.064*, Z=112.456*, Y=-1.210*
  1: 0x06D8 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  2: 0x06DA [0x00] END_REQSTACK()
```

### Event 65535.14

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x06DB   |
| Data Size    | 13 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
06D0:                                   6E F8 FF FF 7F             n....
06E0: 2A 80 99 F8 FF FF 7F 00                           *.......        
```

#### Opcodes

```
  0: 0x06DB [0x6E] EventEntity uses emote 7*
  1: 0x06E2 [0x99] Wait for EventEntity animation to complete
  2: 0x06E7 [0x00] END_REQSTACK()
```
