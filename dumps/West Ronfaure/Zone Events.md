# 0x7FFFFFF0 - Zone Events

## Common Data

| Field            | Value                   |
|------------------|-------------------------|
| Zone             | West Ronfaure (ID: 100) |
| Block Size       | 1336 bytes              |
| Total Events     | 11                      |
| References Count | 56                      |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [255](#event-255)        | 0x0001       |    122 |             25 |
| [105](#event-105)        | 0x007B       |      1 |              1 |
| [65535.1](#event-655351) | 0x007C       |      4 |              2 |
| [65534](#event-65534)    | 0x0080       |      1 |              1 |
| [65535.2](#event-655352) | 0x0081       |     10 |              2 |
| [65535.3](#event-655353) | 0x008B       |     10 |              2 |
| [65535.4](#event-655354) | 0x0095       |     23 |              7 |
| [137](#event-137)        | 0x00AC       |    489 |             71 |
| [65535.5](#event-655355) | 0x0295       |     20 |              3 |
| [55](#event-55)          | 0x02A9       |    370 |             49 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x1D37      |        7479 |
|       1 | 0x0000      |           0 |
|       2 | 0x0001      |           1 |
|       3 | 0x0002      |           2 |
|       4 | 0x0003      |           3 |
|       5 | 0x0004      |           4 |
|       6 | 0x0005      |           5 |
|       7 | 0x0006      |           6 |
|       8 | 0xFFFC06C4  |  4294706884 |
|       9 | 0x670E2     |      422114 |
|      10 | 0xFFFEEAA8  |  4294896296 |
|      11 | 0x0C08      |        3080 |
|      12 | 0xFFFC01D0  |  4294705616 |
|      13 | 0x668ED     |      420077 |
|      14 | 0xFFFEEAA9  |  4294896297 |
|      15 | 0x07D4      |        2004 |
|      16 | 0x003C      |          60 |
|      17 | 0x0FF6      |        4086 |
|      18 | 0xFFFC0EA2  |  4294708898 |
|      19 | 0x668BE     |      420030 |
|      20 | 0x00C8      |         200 |
|      21 | 0x00A3      |         163 |
|      22 | 0x0013      |          19 |
|      23 | 0xFFF6804F  |  4294344783 |
|      24 | 0x43F51     |      278353 |
|      25 | 0xFFFF36D5  |  4294915797 |
|      26 | 0x07F8      |        2040 |
|      27 | 0x00F5      |         245 |
|      28 | 0x1EDE      |        7902 |
|      29 | 0x1EDF      |        7903 |
|      30 | 0x1EE0      |        7904 |
|      31 | 0x1EE1      |        7905 |
|      32 | 0x1EE2      |        7906 |
|      33 | 0x1EE3      |        7907 |
|      34 | 0x1EE4      |        7908 |
|      35 | 0x1EE5      |        7909 |
|      36 | 0x1EE6      |        7910 |
|      37 | 0x1EE7      |        7911 |
|      38 | 0x000A      |          10 |
|      39 | 0x1EE8      |        7912 |
|      40 | 0x006D      |         109 |
|      41 | 0xFFFC03FA  |  4294706170 |
|      42 | 0x66E73     |      421491 |
|      43 | 0x0D16      |        3350 |
|      44 | 0x0090      |         144 |
|      45 | 0xFFFDC8D6  |  4294822102 |
|      46 | 0x3E472     |      255090 |
|      47 | 0xFFFF161C  |  4294907420 |
|      48 | 0x0C66      |        3174 |
|      49 | 0x1F79      |        8057 |
|      50 | 0x001E      |          30 |
|      51 | 0x1F7A      |        8058 |
|      52 | 0x1F7B      |        8059 |
|      53 | 0x1F7F      |        8063 |
|      54 | 0x1F7C      |        8060 |
|      55 | 0x00C9      |         201 |

## String References

- **7479**: Where do you want to goiScroll +j [Nowhere/San d'Oria/Windurst/Ghelsba Lift/Hot Springs Valley/Bastok]
- **7905**: Any idea? [I have a pretty good idea./Not a clue.]

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

### Event 255

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x0001    |
| Data Size    | 122 bytes |
| Instructions | 25        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    24 00 80 01 80 01 80  25 02 00 10 01 80 00 19   $......%.......
0010: 00 03 01 10 01 80 01 79  00 02 00 10 02 80 00 29  .......y.......)
0020: 00 03 01 10 02 80 01 79  00 02 00 10 03 80 00 39  .......y.......9
0030: 00 03 01 10 03 80 01 79  00 02 00 10 04 80 00 49  .......y.......I
0040: 00 03 01 10 04 80 01 79  00 02 00 10 05 80 00 59  .......y.......Y
0050: 00 03 01 10 05 80 01 79  00 02 00 10 06 80 00 69  .......y.......i
0060: 00 03 01 10 06 80 01 79  00 02 00 10 07 80 00 79  .......y.......y
0070: 00 03 01 10 07 80 01 79  00 21 00                 .......y.!.     
```

#### Opcodes

```
  0: 0x0001 [0x24] CREATE_DIALOG(message_id=7479*, default_option=0*, option_flags=0*)
    → "Where do you want to goiScroll +j [Nowhere/San d'Oria/Windurst/Ghelsba Lift/Hot Springs Valley/Bastok]"
  1: 0x0008 [0x25] WAIT_DIALOG_SELECT()
  2: 0x0009 [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x0019
  3: 0x0011 [0x03] Work_Zone[1] = 0*
  4: 0x0016 [0x01] GOTO 0x0079
  5: 0x0019 [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x0029
  6: 0x0021 [0x03] Work_Zone[1] = 1*
  7: 0x0026 [0x01] GOTO 0x0079
  8: 0x0029 [0x02] IF !(Work_Zone[0] == 2*) GOTO 0x0039
  9: 0x0031 [0x03] Work_Zone[1] = 2*
 10: 0x0036 [0x01] GOTO 0x0079
 11: 0x0039 [0x02] IF !(Work_Zone[0] == 3*) GOTO 0x0049
 12: 0x0041 [0x03] Work_Zone[1] = 3*
 13: 0x0046 [0x01] GOTO 0x0079
 14: 0x0049 [0x02] IF !(Work_Zone[0] == 4*) GOTO 0x0059
 15: 0x0051 [0x03] Work_Zone[1] = 4*
 16: 0x0056 [0x01] GOTO 0x0079
 17: 0x0059 [0x02] IF !(Work_Zone[0] == 5*) GOTO 0x0069
 18: 0x0061 [0x03] Work_Zone[1] = 5*
 19: 0x0066 [0x01] GOTO 0x0079
 20: 0x0069 [0x02] IF !(Work_Zone[0] == 6*) GOTO 0x0079
 21: 0x0071 [0x03] Work_Zone[1] = 6*
 22: 0x0076 [0x01] GOTO 0x0079

SUBROUTINE_0079:
 23: 0x0079 [0x21] END_EVENT
 24: 0x007A [0x00] END_REQSTACK()
```

### Event 105

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x007B  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0070:                                   00                         .    
```

#### Opcodes

```
  0: 0x007B [0x00] END_REQSTACK()
```

### Event 65535.1

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x007C  |
| Data Size    | 4 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0070:                                      39 03 80 00              9...
```

#### Opcodes

```
  0: 0x007C [0x39] SET_ENTITY_DIRECTION(direction=0.0°*)
  1: 0x007F [0x00] END_REQSTACK()
```

### Event 65534

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0080  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0080: 00                                                .               
```

#### Opcodes

```
  0: 0x0080 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0081   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0080:    37 08 80 09 80 0A 80  0B 80 00                  7.........     
```

#### Opcodes

```
  0: 0x0081 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=-260.412*, z=422.114*, y=-71.000*, direction=270.7°*
  1: 0x008A [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x008B   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0080:                                   37 0C 80 0D 80             7....
0090: 0E 80 0F 80 00                                    .....           
```

#### Opcodes

```
  0: 0x008B [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=-261.680*, z=420.077*, y=-70.999*, direction=176.1°*
  1: 0x0094 [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0095   |
| Data Size    | 23 bytes |
| Instructions | 7        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0090:                1C 10 80  4B F8 FF FF 7F 11 80 6F       ...K......o
00A0: 70 1F 00 12 80 13 80 0E  80 1F 01 00              p...........    
```

#### Opcodes

```
  0: 0x0095 [0x1C] WAIT(60* ticks)
  1: 0x0098 [0x4B] UPDATE_ENTITY_YAW(entity=EventEntity, yaw=22.4°*)
  2: 0x009F [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  3: 0x00A0 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  4: 0x00A1 [0x1F] MOVE_ENTITY: EventEntity moves to X=-258.398*, Z=420.030*, Y=-70.999*
  5: 0x00A9 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  6: 0x00AB [0x00] END_REQSTACK()
```

### Event 137

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x00AC    |
| Data Size    | 489 bytes |
| Instructions | 71        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00A0:                                      20 01 46 01               .F.
00B0: 42 45 14 80 F0 FF FF 7F  F0 FF FF 7F 66 64 6F 31  BE..........fdo1
00C0: 01 80 55 14 80 F0 FF FF  7F F0 FF FF 7F 66 64 6F  ..U..........fdo
00D0: 31 5C 00 15 80 5C 01 15  80 38 16 80 37 17 80 18  1\...\...8..7...
00E0: 80 19 80 1A 80 97 01 80  02 80 45 1B 80 F0 FF FF  ..........E.....
00F0: 7F F0 FF FF 7F 78 30 30  30 01 80 55 1B 80 F0 FF  .....x000..U....
0100: FF 7F F0 FF FF 7F 78 30  30 30 45 14 80 F0 FF FF  ......x000E.....
0110: 7F F0 FF FF 7F 66 64 69  31 01 80 55 14 80 F0 FF  .....fdi1..U....
0120: FF 7F F0 FF FF 7F 66 64  69 31 4A A6 42 06 01 F0  ......fdi1J.B...
0130: FF FF 7F 6F 76 A6 42 06  01 2B A6 42 06 01 1C 80  ...ov.B..+.B....
0140: 23 27 02 A6 42 06 01 0B  27 03 A6 42 06 01 0F 2B  #'..B...'..B...+
0150: A6 42 06 01 1D 80 23 2A  03 A6 42 06 01 45 1B 80  .B....#*..B..E..
0160: F0 FF FF 7F F0 FF FF 7F  78 30 30 31 01 80 55 1B  ........x001..U.
0170: 80 F0 FF FF 7F F0 FF FF  7F 78 30 30 31 2B A6 42  .........x001+.B
0180: 06 01 1E 80 23 24 1F 80  02 80 01 80 25 45 1B 80  ....#$......%E..
0190: F0 FF FF 7F F0 FF FF 7F  78 30 30 32 01 80 27 03  ........x002..'.
01A0: A6 42 06 01 09 02 00 10  01 80 00 B8 01 2B A6 42  .B...........+.B
01B0: 06 01 20 80 23 01 CB 01  02 00 10 02 80 00 CB 01  .. .#...........
01C0: 2B A6 42 06 01 21 80 23  01 CB 01 2A 03 A6 42 06  +.B..!.#...*..B.
01D0: 01 55 1B 80 F0 FF FF 7F  F0 FF FF 7F 78 30 30 32  .U..........x002
01E0: 2B A6 42 06 01 22 80 23  4A A6 42 06 01 F0 FF FF  +.B..".#J.B.....
01F0: 7F 2B A6 42 06 01 23 80  23 6F 76 A6 42 06 01 27  .+.B..#.#ov.B..'
0200: 03 A6 42 06 01 10 2B A6  42 06 01 24 80 23 27 04  ..B...+.B..$.#'.
0210: A6 42 06 01 11 1C 10 80  45 1B 80 F0 FF FF 7F F0  .B......E.......
0220: FF FF 7F 78 30 30 33 01  80 55 1B 80 F0 FF FF 7F  ...x003..U......
0230: F0 FF FF 7F 78 30 30 33  2B A6 42 06 01 25 80 23  ....x003+.B..%.#
0240: 2A 04 A6 42 06 01 27 03  A6 42 06 01 0A 1C 26 80  *..B..'..B....&.
0250: 2B A6 42 06 01 27 80 23  45 14 80 F0 FF FF 7F F0  +.B..'.#E.......
0260: FF FF 7F 66 64 6F 32 01  80 55 14 80 F0 FF FF 7F  ...fdo2..U......
0270: F0 FF FF 7F 66 64 6F 32  5C 00 28 80 5C 01 28 80  ....fdo2\.(.\.(.
0280: 46 00 45 14 80 F0 FF FF  7F F0 FF FF 7F 66 64 69  F.E..........fdi
0290: 32 01 80 21 00                                    2..!.           
```

#### Opcodes

```
  0: 0x00AC [0x20] SET_CLI_EVENT_UC_FLAG: Lock player control
  1: 0x00AE [0x46] CAMERA_CONTROL: Disable user control
  2: 0x00B0 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  3: 0x00B1 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
  4: 0x00C2 [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=200*
  5: 0x00D1 [0x5C] MUSIC_CONTROL: Set Idle (Day) music to song 163*
  6: 0x00D5 [0x5C] MUSIC_CONTROL: Set Idle (Night) music to song 163*
  7: 0x00D9 [0x38] SET_CLIENT_EVENT_MODE(mode=19*)
  8: 0x00DC [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=-622.513*, z=278.353*, y=-51.499*, direction=179.3°*
  9: 0x00E5 [0x97] SAVE_SET_WIND_VALUES(wind_base=0x8001, wind_width=0x8002)
 10: 0x00EA [0x45] LOAD_SCHEDULED_TASK: Load scheduler "x000" with entities [LocalPlayer, LocalPlayer], work=[245*, 0*]
 11: 0x00FB [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "x000" with entities [LocalPlayer, LocalPlayer], work=245*
 12: 0x010A [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 13: 0x011B [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "fdi1" with entities [LocalPlayer, LocalPlayer], work=200*
 14: 0x012A [0x4A] Esca (ID: 17187494/0x010642A6) looks at LocalPlayer
 15: 0x0133 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
 16: 0x0134 [0x76] CHECK_ENTITY_RENDER_FLAGS: Wait until Esca (ID: 17187494/0x010642A6) Render.Flags0 and Render.Flags3 conditions are met
 17: 0x0139 [0x2B] Esca (ID: 17187494/0x010642A6) [7902*]:
    → "What do you want? You want to know if I've seen that earring before?"
 18: 0x0140 [0x23] WAIT_FOR_DIALOG_INTERACTION
 19: 0x0141 [0x27] REQ_SET(priority=0x02, entity_id=Esca (ID: 17187494/0x010642A6), tag_num=0x0B)
 20: 0x0148 [0x27] REQ_SET(priority=0x03, entity_id=Esca (ID: 17187494/0x010642A6), tag_num=0x0F)
 21: 0x014F [0x2B] Esca (ID: 17187494/0x010642A6) [7903*]:
    → "...! Where did you get that? Ah, I must have dropped it that time I was... Damn, I'm so clumsy!"
 22: 0x0156 [0x23] WAIT_FOR_DIALOG_INTERACTION
 23: 0x0157 [0x2A] GET_REQ_LEVEL(level=3, entity_id=Esca (ID: 17187494/0x010642A6))
 24: 0x015D [0x45] LOAD_SCHEDULED_TASK: Load scheduler "x001" with entities [LocalPlayer, LocalPlayer], work=[245*, 0*]
 25: 0x016E [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "x001" with entities [LocalPlayer, LocalPlayer], work=245*
 26: 0x017D [0x2B] Esca (ID: 17187494/0x010642A6) [7904*]:
    → "Well, I guess you found me out. I was the one who mugged Brugaire for his father's inheritance. Even if I am a thief, a lady likes to look her best when doing her job. By the way, do you have any idea what I stole?"
 27: 0x0184 [0x23] WAIT_FOR_DIALOG_INTERACTION
 28: 0x0185 [0x24] CREATE_DIALOG(message_id=7905*, default_option=1*, option_flags=0*)
    → "Any idea? [I have a pretty good idea./Not a clue.]"
 29: 0x018C [0x25] WAIT_DIALOG_SELECT()
 30: 0x018D [0x45] LOAD_SCHEDULED_TASK: Load scheduler "x002" with entities [LocalPlayer, LocalPlayer], work=[245*, 0*]
 31: 0x019E [0x27] REQ_SET(priority=0x03, entity_id=Esca (ID: 17187494/0x010642A6), tag_num=0x09)
 32: 0x01A5 [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x01B8
 33: 0x01AD [0x2B] Esca (ID: 17187494/0x010642A6) [7906*]:
    → "That's right, a piece of the armor said to have been worn by the legendary last dragoon."
 34: 0x01B4 [0x23] WAIT_FOR_DIALOG_INTERACTION
 35: 0x01B5 [0x01] GOTO 0x01CB
 36: 0x01B8 [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x01CB
 37: 0x01C0 [0x2B] Esca (ID: 17187494/0x010642A6) [7907*]:
    → "Unbelievable. You come after me even though you don't know what you're looking for? The thing I took was a piece of the armor said to have been worn by the legendary last dragoon."
 38: 0x01C7 [0x23] WAIT_FOR_DIALOG_INTERACTION
 39: 0x01C8 [0x01] GOTO 0x01CB

SUBROUTINE_01CB:
 40: 0x01CB [0x2A] GET_REQ_LEVEL(level=3, entity_id=Esca (ID: 17187494/0x010642A6))
 41: 0x01D1 [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "x002" with entities [LocalPlayer, LocalPlayer], work=245*
 42: 0x01E0 [0x2B] Esca (ID: 17187494/0x010642A6) [7908*]:
    → "My employer is one of the many people who are after that armor."
 43: 0x01E7 [0x23] WAIT_FOR_DIALOG_INTERACTION
 44: 0x01E8 [0x4A] Esca (ID: 17187494/0x010642A6) looks at LocalPlayer
 45: 0x01F1 [0x2B] Esca (ID: 17187494/0x010642A6) [7909*]:
    → "The name of my employer? You know, he never told me. I was just told to bury the armor in a certain spot in exchange for a small fortune in gil."
 46: 0x01F8 [0x23] WAIT_FOR_DIALOG_INTERACTION
 47: 0x01F9 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
 48: 0x01FA [0x76] CHECK_ENTITY_RENDER_FLAGS: Wait until Esca (ID: 17187494/0x010642A6) Render.Flags0 and Render.Flags3 conditions are met
 49: 0x01FF [0x27] REQ_SET(priority=0x03, entity_id=Esca (ID: 17187494/0x010642A6), tag_num=0x10)
 50: 0x0206 [0x2B] Esca (ID: 17187494/0x010642A6) [7910*]:
    → "I've already been paid for the job, so I'll tell you where I buried it. But on one condition: You can't tell Brugaire that I was the thief. I don't need him breathing down my neck when I'm trying to work."
 51: 0x020D [0x23] WAIT_FOR_DIALOG_INTERACTION
 52: 0x020E [0x27] REQ_SET(priority=0x04, entity_id=Esca (ID: 17187494/0x010642A6), tag_num=0x11)
 53: 0x0215 [0x1C] WAIT(60* ticks)
 54: 0x0218 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "x003" with entities [LocalPlayer, LocalPlayer], work=[245*, 0*]
 55: 0x0229 [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "x003" with entities [LocalPlayer, LocalPlayer], work=245*
 56: 0x0238 [0x2B] Esca (ID: 17187494/0x010642A6) [7911*]:
    → "Right. The armor is buried on a small island that can be reached through the Eldieme Necropolis. A monster has been put on guard over the spot though, so don't think you can just waltz in and scoop it up."
 57: 0x023F [0x23] WAIT_FOR_DIALOG_INTERACTION
 58: 0x0240 [0x2A] GET_REQ_LEVEL(level=4, entity_id=Esca (ID: 17187494/0x010642A6))
 59: 0x0246 [0x27] REQ_SET(priority=0x03, entity_id=Esca (ID: 17187494/0x010642A6), tag_num=0x0A)
 60: 0x024D [0x1C] WAIT(10* ticks)
 61: 0x0250 [0x2B] Esca (ID: 17187494/0x010642A6) [7912*]:
    → "Oh, and give me back my earring. I wear those for good luck."
 62: 0x0257 [0x23] WAIT_FOR_DIALOG_INTERACTION
 63: 0x0258 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo2" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 64: 0x0269 [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "fdo2" with entities [LocalPlayer, LocalPlayer], work=200*
 65: 0x0278 [0x5C] MUSIC_CONTROL: Set Idle (Day) music to song 109*
 66: 0x027C [0x5C] MUSIC_CONTROL: Set Idle (Night) music to song 109*
 67: 0x0280 [0x46] CAMERA_CONTROL: Restore default settings
 68: 0x0282 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi2" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 69: 0x0293 [0x21] END_EVENT
 70: 0x0294 [0x00] END_REQSTACK()
```

### Event 65535.5

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0295   |
| Data Size    | 20 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0290:                79 00 F8  FF FF 7F B0 42 06 01 37       y......B..7
02A0: 29 80 2A 80 0E 80 2B 80  00                       ).*...+..       
```

#### Opcodes

```
  0: 0x0295 [0x79] EventEntity looks at Vilatroire (ID: 17187504/0x010642B0) (Basic look)
  1: 0x029F [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=-261.126*, z=421.491*, y=-70.999*, direction=294.4°*
  2: 0x02A8 [0x00] END_REQSTACK()
```

### Event 55

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x02A9    |
| Data Size    | 370 bytes |
| Instructions | 49        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
02A0:                             42 46 01 03 00 00 05           BF.....
02B0: 10 45 14 80 F8 FF FF 7F  F8 FF FF 7F 66 64 6F 30  .E..........fdo0
02C0: 01 80 55 14 80 F8 FF FF  7F F8 FF FF 7F 66 64 6F  ..U..........fdo
02D0: 30 4E 00 DC 42 06 01 4E  00 DD 42 06 01 38 16 80  0N..B..N..B..8..
02E0: 79 00 F0 FF FF 7F DC 42  06 01 03 05 10 02 10 03  y......B........
02F0: 06 10 02 10 03 07 10 02  10 15 05 10 2C 80 15 06  ............,...
0300: 10 10 80 3F 07 10 07 10  10 80 37 2D 80 2E 80 2F  ...?......7-.../
0310: 80 30 80 45 06 80 F8 FF  FF 7F F8 FF FF 7F 73 30  .0.E..........s0
0320: 30 31 01 80 4A DC 42 06  01 F0 FF FF 7F 45 14 80  01..J.B......E..
0330: F8 FF FF 7F F8 FF FF 7F  66 64 69 31 01 80 2B DC  ........fdi1..+.
0340: 42 06 01 31 80 23 66 32  80 DC 42 06 01 DC 42 06  B..1.#f2..B...B.
0350: 01 74 6C 6B 30 2B DC 42  06 01 33 80 23 02 04 10  .tlk0+.B..3.#...
0360: 01 80 01 AF 03 66 32 80  DC 42 06 01 DC 42 06 01  .....f2..B...B..
0370: 74 6C 6B 31 03 05 10 04  10 03 06 10 04 10 03 07  tlk1............
0380: 10 04 10 15 05 10 2C 80  15 06 10 10 80 3F 07 10  ......,......?..
0390: 07 10 10 80 02 00 00 01  80 00 A7 03 2B DC 42 06  ............+.B.
03A0: 01 34 80 23 01 AF 03 2B  DC 42 06 01 35 80 23 66  .4.#...+.B..5.#f
03B0: 32 80 DC 42 06 01 DC 42  06 01 70 61 73 30 2B DC  2..B...B..pas0+.
03C0: 42 06 01 36 80 23 52 06  80 F8 FF FF 7F F8 FF FF  B..6.#R.........
03D0: 7F 73 30 30 31 45 14 80  F8 FF FF 7F F8 FF FF 7F  .s001E..........
03E0: 66 64 6F 31 01 80 55 14  80 F8 FF FF 7F F8 FF FF  fdo1..U.........
03F0: 7F 66 64 6F 31 46 00 45  37 80 F0 FF FF 7F F0 FF  .fdo1F.E7.......
0400: FF 7F 71 73 74 63 01 80  45 14 80 F8 FF FF 7F F8  ..qstc..E.......
0410: FF FF 7F 66 64 69 32 01  80 21 00                 ...fdi2..!.     
```

#### Opcodes

```
  0: 0x02A9 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  1: 0x02AA [0x46] CAMERA_CONTROL: Disable user control
  2: 0x02AC [0x03] ExtData[1]->WorkLocal[0] = Work_Zone[5]
  3: 0x02B1 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo0" with entities [EventEntity, EventEntity], work=[200*, 0*]
  4: 0x02C2 [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "fdo0" with entities [EventEntity, EventEntity], work=200*
  5: 0x02D1 [0x4E] SET_ENTITY_HIDE_FLAG: Show Camereine (ID: 17187548/0x010642DC)
  6: 0x02D7 [0x4E] SET_ENTITY_HIDE_FLAG: Show Unnamed NPC (ID: 17187549/0x010642DD)
  7: 0x02DD [0x38] SET_CLIENT_EVENT_MODE(mode=19*)
  8: 0x02E0 [0x79] LocalPlayer looks at Camereine (ID: 17187548/0x010642DC) (Basic look)
  9: 0x02EA [0x03] Work_Zone[5] = Work_Zone[2]
 10: 0x02EF [0x03] Work_Zone[6] = Work_Zone[2]
 11: 0x02F4 [0x03] Work_Zone[7] = Work_Zone[2]
 12: 0x02F9 [0x15] Work_Zone[5] /= 144*
 13: 0x02FE [0x15] Work_Zone[6] /= 60*
 14: 0x0303 [0x3F] Work_Zone[7] = Work_Zone[7] % 60*
 15: 0x030A [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=-145.194*, z=255.090*, y=-59.876*, direction=279.0°*
 16: 0x0313 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "s001" with entities [EventEntity, EventEntity], work=[5*, 0*]
 17: 0x0324 [0x4A] Camereine (ID: 17187548/0x010642DC) looks at LocalPlayer
 18: 0x032D [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi1" with entities [EventEntity, EventEntity], work=[200*, 0*]
 19: 0x033E [0x2B] Camereine (ID: 17187548/0x010642DC) [8057*]:
    → "You've helped our poor girl find her way home! I don't know how to thank you!"
 20: 0x0345 [0x23] WAIT_FOR_DIALOG_INTERACTION
 21: 0x0346 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [Camereine (ID: 17187548/0x010642DC), Camereine (ID: 17187548/0x010642DC)], work=30*
 22: 0x0355 [0x2B] Camereine (ID: 17187548/0x010642DC) [8058*]:
    → "And to think you made it here in a mere $3 [hour/hours] ($4 [minute/minutes] and $5 [second/seconds] Earth time)!"
 23: 0x035C [0x23] WAIT_FOR_DIALOG_INTERACTION
 24: 0x035D [0x02] IF !(Work_Zone[4] == 0*) GOTO 0x03AF
 25: 0x0365 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk1" with entities [Camereine (ID: 17187548/0x010642DC), Camereine (ID: 17187548/0x010642DC)], work=30*
 26: 0x0374 [0x03] Work_Zone[5] = Work_Zone[4]
 27: 0x0379 [0x03] Work_Zone[6] = Work_Zone[4]
 28: 0x037E [0x03] Work_Zone[7] = Work_Zone[4]
 29: 0x0383 [0x15] Work_Zone[5] /= 144*
 30: 0x0388 [0x15] Work_Zone[6] /= 60*
 31: 0x038D [0x3F] Work_Zone[7] = Work_Zone[7] % 60*
 32: 0x0394 [0x02] IF !(ExtData[1]->WorkLocal[0] == 0*) GOTO 0x03A7
 33: 0x039C [0x2B] Camereine (ID: 17187548/0x010642DC) [8059*]:
    → "Oh, and by the way, the fastest adventurer to date has been %0. That talented rider traversed the same course as you in $3 [hour/hours] ($4 [minute/minutes] and $5 [second/seconds] Earth time)!"
 34: 0x03A3 [0x23] WAIT_FOR_DIALOG_INTERACTION
 35: 0x03A4 [0x01] GOTO 0x03AF
 36: 0x03A7 [0x2B] Camereine (ID: 17187548/0x010642DC) [8063*]:
    → "Oh, and by the way, the fastest adventurer to date has been...you! Your remarkable record of $3 [hour/hours] ($4 [minute/minutes] and $5 [second/seconds] Earth time) still stands strong!"
 37: 0x03AE [0x23] WAIT_FOR_DIALOG_INTERACTION

SUBROUTINE_03AF:
 38: 0x03AF [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "pas0" with entities [Camereine (ID: 17187548/0x010642DC), Camereine (ID: 17187548/0x010642DC)], work=30*
 39: 0x03BE [0x2B] Camereine (ID: 17187548/0x010642DC) [8060*]:
    → "Anyway, please take this as a token of our appreciation. And stop by again sometime. We may have more work for you!"
 40: 0x03C5 [0x23] WAIT_FOR_DIALOG_INTERACTION
 41: 0x03C6 [0x52] END_LOAD_SCHEDULER: End scheduler "s001" with entities [EventEntity, EventEntity], work=5*
 42: 0x03D5 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [EventEntity, EventEntity], work=[200*, 0*]
 43: 0x03E6 [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "fdo1" with entities [EventEntity, EventEntity], work=200*
 44: 0x03F5 [0x46] CAMERA_CONTROL: Restore default settings
 45: 0x03F7 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "qstc" with entities [LocalPlayer, LocalPlayer], work=[201*, 0*]
 46: 0x0408 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi2" with entities [EventEntity, EventEntity], work=[200*, 0*]
 47: 0x0419 [0x21] END_EVENT
 48: 0x041A [0x00] END_REQSTACK()
```
