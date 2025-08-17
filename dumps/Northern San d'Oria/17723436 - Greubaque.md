# 17723436 - Greubaque

## Common Data

| Field            | Value                         |
|------------------|-------------------------------|
| Zone             | Northern San d'Oria (ID: 231) |
| Block Size       | 536 bytes                     |
| Total Events     | 4                             |
| References Count | 19                            |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [73](#event-73)       | 0x0001       |      1 |              1 |
| [628](#event-628)     | 0x0002       |    425 |            100 |
| [74](#event-74)       | 0x01AB       |      1 |              1 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0002      |           2 |
|       1 | 0x1B4C      |        6988 |
|       2 | 0x0000      |           0 |
|       3 | 0x1BDF      |        7135 |
|       4 | 0x1B4D      |        6989 |
|       5 | 0x0001      |           1 |
|       6 | 0x1BE1      |        7137 |
|       7 | 0x00C8      |         200 |
|       8 | 0x005A      |          90 |
|       9 | 0x1BE0      |        7136 |
|      10 | 0x1BE2      |        7138 |
|      11 | 0x1B51      |        6993 |
|      12 | 0x1B77      |        7031 |
|      13 | 0x1B55      |        6997 |
|      14 | 0x1B54      |        6996 |
|      15 | 0x1B53      |        6995 |
|      16 | 0x1B52      |        6994 |
|      17 | 0x1BE3      |        7139 |
|      18 | 0x1BDE      |        7134 |

## String References

- **6988**: Request...? [[Advanced synthesis/Synthesis/Synthesis] image support./Information on synthesis materials./Nothing.]
- **6989**: Image support: $0 gil. [Accept./Decline.]
- **6993**: Necessary skills: [Fishing/Woodworking/Smithing/Goldsmithing/Clothcraft/Leatherworking/Bonecraft/Alchemy/Cooking][ /, Woodworking/, Smithing/, Goldsmithing/, Clothcraft/, Leatherworking/, Bonecraft/, Alchemy/, Cooking][ /, Woodworking/, Smithing/, Goldsmithing/, Clothcraft/, Leatherworking/, Bonecraft/, Alchemy/, Cooking][ /, & Woodworking/, & Smithing/, & Goldsmithing/, & Clothcraft/, & Leatherworking/, & Bonecraft/, & Alchemy/, & Cooking] Necessary crystal: $4 Necessary items:
- **6994**: $4 x $0 $5 x $0$0 $6 x $0 $7 x $0$3
- **6995**: $4 x $0 $5 x $0$0 $6 x $0
- **6996**: $4 x $0 $5 x $0$0
- **6997**: $4 x $0
- **7031**: Necessary skills: [Fishing/Woodworking/Smithing/Goldsmithing/Clothcraft/Leatherworking/Bonecraft/Alchemy/Cooking][ /, Woodworking/, Smithing/, Goldsmithing/, Clothcraft/, Leatherworking/, Bonecraft/, Alchemy/, Cooking][ /, Woodworking/, Smithing/, Goldsmithing/, Clothcraft/, Leatherworking/, Bonecraft/, Alchemy/, Cooking][ /, & Woodworking/, & Smithing/, & Goldsmithing/, & Clothcraft/, & Leatherworking/, & Bonecraft/, & Alchemy/, & Cooking] Necessary crystal: $4 Necessary key item: $3 Necessary items:
- **7134**: Can't you see I'm busy? We are up to our ears in work these days!
- **7135**: No, you should try it on your own.
- **7136**: Oh, I'm sorry. The guildmaster is displeased when we give help for free. "A friend is but a competitor," he likes to say.
- **7137**: All right. Close your eyes, and focus on the craft.
- **7138**: Hmm... Well, I'd recommend someone of your skill to try crafting $0. Here's what you'll need:
- **7139**: Did you get that? Remember, our guildmaster is strict, but behind his grim face lies joy at seeing new apprentices. Come back any time, friend!

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

### Event 73

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0001  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    00                                              .              
```

#### Opcodes

```
  0: 0x0001 [0x00] END_REQSTACK()
```

### Event 628

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x0002    |
| Data Size    | 425 bytes |
| Instructions | 100       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:       3E 05 10 00 80 A5  01 24 01 80 00 80 02 80    >......$......
0010: 25 02 00 10 02 80 00 87  00 02 07 10 02 80 01 28  %..............(
0020: 00 1D 03 80 23 01 84 00  24 04 80 05 80 02 80 25  ....#...$......%
0030: 02 00 10 02 80 00 79 00  02 06 10 02 10 04 72 00  ......y.......r.
0040: 1D 06 80 23 42 45 07 80  F8 FF FF 7F F8 FF FF 7F  ...#BE..........
0050: 66 64 6F 31 02 80 1C 08  80 45 07 80 F8 FF FF 7F  fdo1.....E......
0060: F8 FF FF 7F 66 64 69 31  02 80 03 01 10 05 80 01  ....fdi1........
0070: 76 00 1D 09 80 23 01 84  00 02 00 10 05 80 00 84  v....#..........
0080: 00 01 84 00 01 A2 01 02  00 10 05 80 00 97 01 03  ................
0090: 08 10 00 80 8C 00 08 10  03 10 04 10 8C 01 03 02  ................
00A0: 10 40 10 1D 0A 80 23 03  03 10 41 10 03 04 10 42  .@....#...A....B
00B0: 10 03 05 10 43 10 03 06  10 44 10 03 07 10 55 10  ....C....D....U.
00C0: 02 07 10 02 80 00 CF 00  48 0B 80 23 01 D3 00 48  ........H..#...H
00D0: 0C 80 23 03 02 10 45 10  03 03 10 46 10 03 04 10  ..#...E....F....
00E0: 47 10 03 05 10 48 10 03  06 10 4D 10 03 07 10 4E  G....H....M....N
00F0: 10 03 08 10 4F 10 03 09  10 50 10 02 07 10 02 80  ....O....P......
0100: 00 0A 01 48 0D 80 23 01  90 01 02 08 10 02 80 00  ...H..#.........
0110: 19 01 48 0E 80 23 01 90  01 02 09 10 02 80 00 28  ..H..#.........(
0120: 01 48 0F 80 23 01 90 01  48 10 80 23 03 02 10 49  .H..#...H..#...I
0130: 10 03 03 10 4A 10 03 04  10 4B 10 03 05 10 4C 10  ....J....K....L.
0140: 03 06 10 51 10 03 07 10  52 10 03 08 10 53 10 03  ...Q....R....S..
0150: 09 10 54 10 02 06 10 02  80 00 5F 01 01 90 01 02  ..T......._.....
0160: 07 10 02 80 00 6E 01 48  0D 80 23 01 90 01 02 08  .....n.H..#.....
0170: 10 02 80 00 7D 01 48 0E  80 23 01 90 01 02 09 10  ....}.H..#......
0180: 02 80 00 8C 01 48 0F 80  23 01 90 01 48 10 80 23  .....H..#...H..#
0190: 1D 11 80 23 01 A2 01 02  00 10 00 80 00 A2 01 01  ...#............
01A0: A2 01 01 A9 01 1D 12 80  23 21 00                 ........#!.     
```

#### Opcodes

```
  0: 0x0002 [0x3E] IF !(Work_Zone[5] bit 2*) GOTO 0x01A5
  1: 0x0009 [0x24] CREATE_DIALOG(message_id=6988*, default_option=2*, option_flags=0*)
    → "Request...? [[Advanced synthesis/Synthesis/Synthesis] image support./Information on synthesis materials./Nothing.]"
  2: 0x0010 [0x25] WAIT_DIALOG_SELECT()
  3: 0x0011 [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x0087
  4: 0x0019 [0x02] IF !(Work_Zone[7] == 0*) GOTO 0x0028
  5: 0x0021 [0x1D] PRINT_EVENT_MESSAGE(message_id=7135*)
    → "No, you should try it on your own."
  6: 0x0024 [0x23] WAIT_FOR_DIALOG_INTERACTION
  7: 0x0025 [0x01] GOTO 0x0084
  8: 0x0028 [0x24] CREATE_DIALOG(message_id=6989*, default_option=1*, option_flags=0*)
    → "Image support: $0 gil. [Accept./Decline.]"
  9: 0x002F [0x25] WAIT_DIALOG_SELECT()
 10: 0x0030 [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x0079
 11: 0x0038 [0x02] IF !(Work_Zone[6] < Work_Zone[2]) GOTO 0x0072
 12: 0x0040 [0x1D] PRINT_EVENT_MESSAGE(message_id=7137*)
    → "All right. Close your eyes, and focus on the craft."
 13: 0x0043 [0x23] WAIT_FOR_DIALOG_INTERACTION
 14: 0x0044 [0x42] SET_CLI_EVENT_CANCEL_DATA()
 15: 0x0045 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [EventEntity, EventEntity], work=[200*, 0*]
 16: 0x0056 [0x1C] WAIT(90* ticks)
 17: 0x0059 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi1" with entities [EventEntity, EventEntity], work=[200*, 0*]
 18: 0x006A [0x03] Work_Zone[1] = 1*
 19: 0x006F [0x01] GOTO 0x0076
 20: 0x0072 [0x1D] PRINT_EVENT_MESSAGE(message_id=7136*)
    → "Oh, I'm sorry. The guildmaster is displeased when we give help for free. "A friend is but a competitor," he likes to say."
 21: 0x0075 [0x23] WAIT_FOR_DIALOG_INTERACTION

SUBROUTINE_0076:
 22: 0x0076 [0x01] GOTO 0x0084
 23: 0x0079 [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x0084
 24: 0x0081 [0x01] GOTO 0x0084

SUBROUTINE_0084:
 25: 0x0084 [0x01] GOTO 0x01A2
 26: 0x0087 [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x0197
 27: 0x008F [0x03] Work_Zone[8] = 2*
 28: 0x0094 [0x8C] CRAFTING_HANDLER(mode=0x00) // Initialize crafting session
 29: 0x009C [0x8C] CRAFTING_HANDLER(mode=0x01) // End crafting session
 30: 0x009E [0x03] Work_Zone[2] = Work_Zone[64]
 31: 0x00A3 [0x1D] PRINT_EVENT_MESSAGE(message_id=7138*)
    → "Hmm... Well, I'd recommend someone of your skill to try crafting $0. Here's what you'll need:"
 32: 0x00A6 [0x23] WAIT_FOR_DIALOG_INTERACTION
 33: 0x00A7 [0x03] Work_Zone[3] = Work_Zone[65]
 34: 0x00AC [0x03] Work_Zone[4] = Work_Zone[66]
 35: 0x00B1 [0x03] Work_Zone[5] = Work_Zone[67]
 36: 0x00B6 [0x03] Work_Zone[6] = Work_Zone[68]
 37: 0x00BB [0x03] Work_Zone[7] = Work_Zone[85]
 38: 0x00C0 [0x02] IF !(Work_Zone[7] == 0*) GOTO 0x00CF
 39: 0x00C8 [0x48] [System] [6993*]:
    → "Necessary skills: [Fishing/Woodworking/Smithing/Goldsmithing/Clothcraft/Leatherworking/Bonecraft/Alchemy/Cooking][ /, Woodworking/, Smithing/, Goldsmithing/, Clothcraft/, Leatherworking/, Bonecraft/, Alchemy/, Cooking][ /, Woodworking/, Smithing/, Goldsmithing/, Clothcraft/, Leatherworking/, Bonecraft/, Alchemy/, Cooking][ /, & Woodworking/, & Smithing/, & Goldsmithing/, & Clothcraft/, & Leatherworking/, & Bonecraft/, & Alchemy/, & Cooking] Necessary crystal: $4 Necessary items:"
 40: 0x00CB [0x23] WAIT_FOR_DIALOG_INTERACTION
 41: 0x00CC [0x01] GOTO 0x00D3
 42: 0x00CF [0x48] [System] [7031*]:
    → "Necessary skills: [Fishing/Woodworking/Smithing/Goldsmithing/Clothcraft/Leatherworking/Bonecraft/Alchemy/Cooking][ /, Woodworking/, Smithing/, Goldsmithing/, Clothcraft/, Leatherworking/, Bonecraft/, Alchemy/, Cooking][ /, Woodworking/, Smithing/, Goldsmithing/, Clothcraft/, Leatherworking/, Bonecraft/, Alchemy/, Cooking][ /, & Woodworking/, & Smithing/, & Goldsmithing/, & Clothcraft/, & Leatherworking/, & Bonecraft/, & Alchemy/, & Cooking] Necessary crystal: $4 Necessary key item: $3 Necessary items:"
 43: 0x00D2 [0x23] WAIT_FOR_DIALOG_INTERACTION

SUBROUTINE_00D3:
 44: 0x00D3 [0x03] Work_Zone[2] = Work_Zone[69]
 45: 0x00D8 [0x03] Work_Zone[3] = Work_Zone[70]
 46: 0x00DD [0x03] Work_Zone[4] = Work_Zone[71]
 47: 0x00E2 [0x03] Work_Zone[5] = Work_Zone[72]
 48: 0x00E7 [0x03] Work_Zone[6] = Work_Zone[77]
 49: 0x00EC [0x03] Work_Zone[7] = Work_Zone[78]
 50: 0x00F1 [0x03] Work_Zone[8] = Work_Zone[79]
 51: 0x00F6 [0x03] Work_Zone[9] = Work_Zone[80]
 52: 0x00FB [0x02] IF !(Work_Zone[7] == 0*) GOTO 0x010A
 53: 0x0103 [0x48] [System] [6997*]:
    → "$4 x $0"
 54: 0x0106 [0x23] WAIT_FOR_DIALOG_INTERACTION
 55: 0x0107 [0x01] GOTO 0x0190
 56: 0x010A [0x02] IF !(Work_Zone[8] == 0*) GOTO 0x0119
 57: 0x0112 [0x48] [System] [6996*]:
    → "$4 x $0 $5 x $0$0"
 58: 0x0115 [0x23] WAIT_FOR_DIALOG_INTERACTION
 59: 0x0116 [0x01] GOTO 0x0190
 60: 0x0119 [0x02] IF !(Work_Zone[9] == 0*) GOTO 0x0128
 61: 0x0121 [0x48] [System] [6995*]:
    → "$4 x $0 $5 x $0$0 $6 x $0"
 62: 0x0124 [0x23] WAIT_FOR_DIALOG_INTERACTION
 63: 0x0125 [0x01] GOTO 0x0190
 64: 0x0128 [0x48] [System] [6994*]:
    → "$4 x $0 $5 x $0$0 $6 x $0 $7 x $0$3"
 65: 0x012B [0x23] WAIT_FOR_DIALOG_INTERACTION
 66: 0x012C [0x03] Work_Zone[2] = Work_Zone[73]
 67: 0x0131 [0x03] Work_Zone[3] = Work_Zone[74]
 68: 0x0136 [0x03] Work_Zone[4] = Work_Zone[75]
 69: 0x013B [0x03] Work_Zone[5] = Work_Zone[76]
 70: 0x0140 [0x03] Work_Zone[6] = Work_Zone[81]
 71: 0x0145 [0x03] Work_Zone[7] = Work_Zone[82]
 72: 0x014A [0x03] Work_Zone[8] = Work_Zone[83]
 73: 0x014F [0x03] Work_Zone[9] = Work_Zone[84]
 74: 0x0154 [0x02] IF !(Work_Zone[6] == 0*) GOTO 0x015F
 75: 0x015C [0x01] GOTO 0x0190
 76: 0x015F [0x02] IF !(Work_Zone[7] == 0*) GOTO 0x016E
 77: 0x0167 [0x48] [System] [6997*]:
    → "$4 x $0"
 78: 0x016A [0x23] WAIT_FOR_DIALOG_INTERACTION
 79: 0x016B [0x01] GOTO 0x0190
 80: 0x016E [0x02] IF !(Work_Zone[8] == 0*) GOTO 0x017D
 81: 0x0176 [0x48] [System] [6996*]:
    → "$4 x $0 $5 x $0$0"
 82: 0x0179 [0x23] WAIT_FOR_DIALOG_INTERACTION
 83: 0x017A [0x01] GOTO 0x0190
 84: 0x017D [0x02] IF !(Work_Zone[9] == 0*) GOTO 0x018C
 85: 0x0185 [0x48] [System] [6995*]:
    → "$4 x $0 $5 x $0$0 $6 x $0"
 86: 0x0188 [0x23] WAIT_FOR_DIALOG_INTERACTION
 87: 0x0189 [0x01] GOTO 0x0190
 88: 0x018C [0x48] [System] [6994*]:
    → "$4 x $0 $5 x $0$0 $6 x $0 $7 x $0$3"
 89: 0x018F [0x23] WAIT_FOR_DIALOG_INTERACTION

SUBROUTINE_0190:
 90: 0x0190 [0x1D] PRINT_EVENT_MESSAGE(message_id=7139*)
    → "Did you get that? Remember, our guildmaster is strict, but behind his grim face lies joy at seeing new apprentices. Come back any time, friend!"
 91: 0x0193 [0x23] WAIT_FOR_DIALOG_INTERACTION
 92: 0x0194 [0x01] GOTO 0x01A2
 93: 0x0197 [0x02] IF !(Work_Zone[0] == 2*) GOTO 0x01A2
 94: 0x019F [0x01] GOTO 0x01A2

SUBROUTINE_01A2:
 95: 0x01A2 [0x01] GOTO 0x01A9
 96: 0x01A5 [0x1D] PRINT_EVENT_MESSAGE(message_id=7134*)
    → "Can't you see I'm busy? We are up to our ears in work these days!"
 97: 0x01A8 [0x23] WAIT_FOR_DIALOG_INTERACTION

SUBROUTINE_01A9:
 98: 0x01A9 [0x21] END_EVENT
 99: 0x01AA [0x00] END_REQSTACK()
```

### Event 74

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x01AB  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
01A0:                                   00                         .    
```

#### Opcodes

```
  0: 0x01AB [0x00] END_REQSTACK()
```
