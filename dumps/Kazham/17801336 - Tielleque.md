# 17801336 - Tielleque

## Common Data

| Field            | Value            |
|------------------|------------------|
| Zone             | Kazham (ID: 250) |
| Block Size       | 428 bytes        |
| Total Events     | 5                |
| References Count | 23               |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [10016](#event-10016) | 0x0001       |    259 |             57 |
| [10017](#event-10017) | 0x0104       |     16 |              6 |
| [313](#event-313)     | 0x0114       |     12 |              3 |
| [315](#event-315)     | 0x0120       |     12 |              3 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0xFFFFFFFC  |  4294967292 |
|       1 | 0x2985      |       10629 |
|       2 | 0xFFFFFFFD  |  4294967293 |
|       3 | 0x0003      |           3 |
|       4 | 0x0006      |           6 |
|       5 | 0x2980      |       10624 |
|       6 | 0x2981      |       10625 |
|       7 | 0x2982      |       10626 |
|       8 | 0x0000      |           0 |
|       9 | 0x40000000  |  1073741824 |
|      10 | 0x0001      |           1 |
|      11 | 0x2983      |       10627 |
|      12 | 0xFFFFFFFF  |  4294967295 |
|      13 | 0x00C8      |         200 |
|      14 | 0x0020      |          32 |
|      15 | 0x005A      |          90 |
|      16 | 0x003C      |          60 |
|      17 | 0x00C9      |         201 |
|      18 | 0x008A      |         138 |
|      19 | 0x297B      |       10619 |
|      20 | 0x297E      |       10622 |
|      21 | 0x297F      |       10623 |
|      22 | 0x297A      |       10618 |

## String References

- **10618**: If you wish to ride a chocobo, you must possess $6 and have a high enough job level.
- **10619**: You can rent a chocobo for $0 gil. I see you currently have $1 gil.
- **10622**: Do you wish to rent a chocobo? [Yes, I do./No, thank you.]
- **10623**: You don't have enough gil.
- **10624**: I realize that you are in a hurry, [sir/ma'am]. However, might I make a simple request? One of our associate's chocobos has lost her way and cannot return home.
- **10625**: Would you be so kind as to deliver her to [the Kingdom/the Republic/the Federation/the Duchy/the Duchy/the Duchy/the hidden] stables in [Southern San d'Oria/the Bastok Mines/Windurst Woods/Upper Jeuno/Lower Jeuno/Port Jeuno/Norg]?
- **10626**: Lend a helping hand? [I have better things to do./Of course!]
- **10627**: Oh, thank you so very much! You shall be rewarded by our associates upon delivery of the chocobo.
- **10629**: Would you be so kind as to deliver her to [the entrance to the Gustav Tunnel (B-8)/Bibiki Bay (G-10)/the entrance of Uggalepih Temple (J-11)]?

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

### Event 10016

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x0001    |
| Data Size    | 259 bytes |
| Instructions | 49        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    02 02 10 00 80 00 10  00 42 1D 01 80 23 21 00   ........B...#!.
0010: 02 02 10 02 80 00 5E 00  1E F0 FF FF 7F 02 05 10  ......^.........
0020: 03 80 00 2A 00 03 05 10  04 80 1D 05 80 23 1D 06  ...*.........#..
0030: 80 23 24 07 80 08 80 08  80 25 02 00 10 08 80 00  .#$......%......
0040: 4C 00 03 01 10 09 80 21  00 01 5E 00 02 00 10 0A  L......!..^.....
0050: 80 00 5E 00 1D 0B 80 23  01 66 00 01 5E 00 02 02  ..^....#.f..^...
0060: 10 0C 80 00 9B 00 42 45  0D 80 F8 FF FF 7F F8 FF  ......BE........
0070: FF 7F 66 64 6F 32 08 80  02 04 10 08 80 00 99 00  ..fdo2..........
0080: 5D 0E 80 0F 80 1C 10 80  45 11 80 F8 FF FF 7F F8  ].......E.......
0090: FF FF 7F 63 68 63 6F 08  80 21 00 03 09 10 12 80  ...chco..!......
00A0: 1E F0 FF FF 7F 1D 13 80  23 24 14 80 0A 80 08 80  ........#$......
00B0: 25 02 00 10 08 80 00 FD  00 02 03 10 02 10 04 EF  %...............
00C0: 00 42 45 0D 80 F8 FF FF  7F F8 FF FF 7F 66 64 6F  .BE..........fdo
00D0: 31 08 80 02 04 10 08 80  00 EC 00 45 11 80 F8 FF  1..........E....
00E0: FF 7F F8 FF FF 7F 63 68  63 6F 08 80 01 F8 00 1D  ......chco......
00F0: 15 80 23 03 01 10 09 80  21 00 01 02 01 03 01 10  ..#.....!.......
0100: 09 80 21 00                                       ..!.            
```

#### Opcodes

```
  0: 0x0001 [0x02] IF !(Work_Zone[2] == 4294967292*) GOTO 0x0010
  1: 0x0009 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  2: 0x000A [0x1D] PRINT_EVENT_MESSAGE(message_id=10629*)
    → "Would you be so kind as to deliver her to [the entrance to the Gustav Tunnel (B-8)/Bibiki Bay (G-10)/the entrance of Uggalepih Temple (J-11)]?"
  3: 0x000D [0x23] WAIT_FOR_DIALOG_INTERACTION
  4: 0x000E [0x21] END_EVENT
  5: 0x000F [0x00] END_REQSTACK()
  6: 0x0010 [0x02] IF !(Work_Zone[2] == 4294967293*) GOTO 0x005E
  7: 0x0018 [0x1E] EventEntity looks at LocalPlayer and starts talking
  8: 0x001D [0x02] IF !(Work_Zone[5] == 3*) GOTO 0x002A
  9: 0x0025 [0x03] Work_Zone[5] = 6*
 10: 0x002A [0x1D] PRINT_EVENT_MESSAGE(message_id=10624*)
    → "I realize that you are in a hurry, [sir/ma'am]. However, might I make a simple request? One of our associate's chocobos has lost her way and cannot return home."
 11: 0x002D [0x23] WAIT_FOR_DIALOG_INTERACTION
 12: 0x002E [0x1D] PRINT_EVENT_MESSAGE(message_id=10625*)
    → "Would you be so kind as to deliver her to [the Kingdom/the Republic/the Federation/the Duchy/the Duchy/the Duchy/the hidden] stables in [Southern San d'Oria/the Bastok Mines/Windurst Woods/Upper Jeuno/Lower Jeuno/Port Jeuno/Norg]?"
 13: 0x0031 [0x23] WAIT_FOR_DIALOG_INTERACTION
 14: 0x0032 [0x24] CREATE_DIALOG(message_id=10626*, default_option=0*, option_flags=0*)
    → "Lend a helping hand? [I have better things to do./Of course!]"
 15: 0x0039 [0x25] WAIT_DIALOG_SELECT()
 16: 0x003A [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x004C
 17: 0x0042 [0x03] Work_Zone[1] = 1073741824*
 18: 0x0047 [0x21] END_EVENT
 19: 0x0048 [0x00] END_REQSTACK()

SUBROUTINE_005E:
 20: 0x005E [0x02] IF !(Work_Zone[2] == 4294967295*) GOTO 0x009B

SUBROUTINE_0066:
 21: 0x0066 [0x42] SET_CLI_EVENT_CANCEL_DATA()
 22: 0x0067 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo2" with entities [EventEntity, EventEntity], work=[200*, 0*]
 23: 0x0078 [0x02] IF !(Work_Zone[4] == 0*) GOTO 0x0099
 24: 0x0080 [0x5D] SET_MUSIC_VOLUME(volume=32*, fade_time=90*)
 25: 0x0085 [0x1C] WAIT(60* ticks)
 26: 0x0088 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "chco" with entities [EventEntity, EventEntity], work=[201*, 0*]
 27: 0x0099 [0x21] END_EVENT
 28: 0x009A [0x00] END_REQSTACK()
 29: 0x009B [0x03] Work_Zone[9] = 138*
 30: 0x00A0 [0x1E] EventEntity looks at LocalPlayer and starts talking
 31: 0x00A5 [0x1D] PRINT_EVENT_MESSAGE(message_id=10619*)
    → "You can rent a chocobo for $0 gil. I see you currently have $1 gil."
 32: 0x00A8 [0x23] WAIT_FOR_DIALOG_INTERACTION
 33: 0x00A9 [0x24] CREATE_DIALOG(message_id=10622*, default_option=1*, option_flags=0*)
    → "Do you wish to rent a chocobo? [Yes, I do./No, thank you.]"
 34: 0x00B0 [0x25] WAIT_DIALOG_SELECT()
 35: 0x00B1 [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x00FD
 36: 0x00B9 [0x02] IF !(Work_Zone[3] < Work_Zone[2]) GOTO 0x00EF
 37: 0x00C1 [0x42] SET_CLI_EVENT_CANCEL_DATA()
 38: 0x00C2 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [EventEntity, EventEntity], work=[200*, 0*]
 39: 0x00D3 [0x02] IF !(Work_Zone[4] == 0*) GOTO 0x00EC
 40: 0x00DB [0x45] LOAD_SCHEDULED_TASK: Load scheduler "chco" with entities [EventEntity, EventEntity], work=[201*, 0*]
 41: 0x00EC [0x01] GOTO 0x00F8
 42: 0x00EF [0x1D] PRINT_EVENT_MESSAGE(message_id=10623*)
    → "You don't have enough gil."
 43: 0x00F2 [0x23] WAIT_FOR_DIALOG_INTERACTION
 44: 0x00F3 [0x03] Work_Zone[1] = 1073741824*

SUBROUTINE_00F8:
 45: 0x00F8 [0x21] END_EVENT
 46: 0x00F9 [0x00] END_REQSTACK()

SUBROUTINE_0102:
 47: 0x0102 [0x21] END_EVENT
 48: 0x0103 [0x00] END_REQSTACK()
```

#### Data or dead code:

```
# Dead code (unreachable instructions):
     0x0049 [0x01] GOTO 0x005E
     0x005B [0x01] GOTO 0x005E
# Dead code (unreachable instructions):
     0x00FA [0x01] GOTO 0x0102
```

### Event 10017

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0104   |
| Data Size    | 16 bytes |
| Instructions | 6        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0100:             03 09 10 12  80 1E F0 FF FF 7F 1D 16      ............
0110: 80 23 21 00                                       .#!.            
```

#### Opcodes

```
  0: 0x0104 [0x03] Work_Zone[9] = 138*
  1: 0x0109 [0x1E] EventEntity looks at LocalPlayer and starts talking
  2: 0x010E [0x1D] PRINT_EVENT_MESSAGE(message_id=10618*)
    → "If you wish to ride a chocobo, you must possess $6 and have a high enough job level."
  3: 0x0111 [0x23] WAIT_FOR_DIALOG_INTERACTION
  4: 0x0112 [0x21] END_EVENT
  5: 0x0113 [0x00] END_REQSTACK()
```

### Event 313

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0114   |
| Data Size    | 12 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0110:             92 01 F8 FF  FF 7F 80 F8 FF FF 7F 00      ............
```

#### Opcodes

```
  0: 0x0114 [0x92] EventEntity->Render.Flags3 ^= 0x01
  1: 0x011A [0x80] LOAD_WAIT(entity=EventEntity)
  2: 0x011F [0x00] END_REQSTACK()
```

### Event 315

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0120   |
| Data Size    | 12 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0120: 92 01 F8 FF FF 7F 80 F8  FF FF 7F 00              ............    
```

#### Opcodes

```
  0: 0x0120 [0x92] EventEntity->Render.Flags3 ^= 0x01
  1: 0x0126 [0x80] LOAD_WAIT(entity=EventEntity)
  2: 0x012B [0x00] END_REQSTACK()
```
