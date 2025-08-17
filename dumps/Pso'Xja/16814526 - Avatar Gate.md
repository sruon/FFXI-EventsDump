# 16814526 - Avatar Gate

## Common Data

| Field            | Value           |
|------------------|-----------------|
| Zone             | Pso'Xja (ID: 9) |
| Block Size       | 1424 bytes      |
| Total Events     | 4               |
| References Count | 25              |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [13](#event-13)       | 0x0001       |     85 |             17 |
| [6](#event-6)         | 0x0056       |    327 |             53 |
| [7](#event-7)         | 0x019D       |    877 |             96 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x01E0      |         480 |
|       1 | 0x01A4      |         420 |
|       2 | 0x00B4      |         180 |
|       3 | 0x00C8      |         200 |
|       4 | 0x0000      |           0 |
|       5 | 0x003C      |          60 |
|       6 | 0x0013      |          19 |
|       7 | 0x0019      |          25 |
|       8 | 0x000F      |          15 |
|       9 | 0x1D1A      |        7450 |
|      10 | 0x005A      |          90 |
|      11 | 0x012C      |         300 |
|      12 | 0x001E      |          30 |
|      13 | 0x009B      |         155 |
|      14 | 0x0050      |          80 |
|      15 | 0x0154      |         340 |
|      16 | 0x00AA      |         170 |
|      17 | 0x0002      |           2 |
|      18 | 0x0001      |           1 |
|      19 | 0x0078      |         120 |
|      20 | 0x1D1C      |        7452 |
|      21 | 0x0208      |         520 |
|      22 | 0x00C9      |         201 |
|      23 | 0x002D      |          45 |
|      24 | 0x00D7      |         215 |

## String References

- **7450**: The $3 flashes with blinding light!
- **7452**: ...But the door remains closed. You have no choice but to return to Jeuno.

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

### Event 13

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 85 bytes |
| Instructions | 17       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    20 01 46 01 42 2D F8  FF FF 7F F8 FF FF 7F 66    .F.B-........f
0010: 78 73 74 2D F8 FF FF 7F  F8 FF FF 7F 73 31 31 39  xst-........s119
0020: 1C 00 80 4C 1C 01 80 4D  1C 02 80 45 03 80 F0 FF  ...L...M...E....
0030: FF 7F F0 FF FF 7F 66 64  6F 31 04 80 1C 05 80 45  ......fdo1.....E
0040: 03 80 F0 FF FF 7F F0 FF  FF 7F 66 64 69 31 04 80  ..........fdi1..
0050: 46 00 20 00 21 00                                 F. .!.          
```

#### Opcodes

```
  0: 0x0001 [0x20] SET_CLI_EVENT_UC_FLAG: Lock player control
  1: 0x0003 [0x46] CAMERA_CONTROL: Disable user control
  2: 0x0005 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  3: 0x0006 [0x2D] CREATE_ZONE_SCHEDULER_TASK: Create scheduler "fxst" with entities [EventEntity, EventEntity]
  4: 0x0013 [0x2D] CREATE_ZONE_SCHEDULER_TASK: Create scheduler "s119" with entities [EventEntity, EventEntity]
  5: 0x0020 [0x1C] WAIT(480* ticks)
  6: 0x0023 [0x4C] EventEntity->StatusEvent = 8 // Open door
  7: 0x0024 [0x1C] WAIT(420* ticks)
  8: 0x0027 [0x4D] EventEntity->StatusEvent = 9 // Close door
  9: 0x0028 [0x1C] WAIT(180* ticks)
 10: 0x002B [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 11: 0x003C [0x1C] WAIT(60* ticks)
 12: 0x003F [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 13: 0x0050 [0x46] CAMERA_CONTROL: Restore default settings
 14: 0x0052 [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
 15: 0x0054 [0x21] END_EVENT
 16: 0x0055 [0x00] END_REQSTACK()
```

### Event 6

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x0056    |
| Data Size    | 327 bytes |
| Instructions | 53        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:                   20 01  42 46 01 45 03 80 F8 FF         .BF.E....
0060: FF 7F F8 FF FF 7F 66 64  6F 31 04 80 1C 05 80 38  ......fdo1.....8
0070: 06 80 29 08 F0 FF FF 7F  03 79 00 F0 FF FF 7F F0  ..)......y......
0080: FF FF 7F 29 0B F0 FF FF  7F 05 45 07 80 F8 FF FF  ...)......E.....
0090: 7F F8 FF FF 7F 73 30 38  39 04 80 45 03 80 F8 FF  .....s089..E....
00A0: FF 7F F8 FF FF 7F 66 64  69 31 04 80 1C 08 80 48  ......fdi1.....H
00B0: 09 80 23 1C 05 80 2D F8  FF FF 7F F8 FF FF 7F 66  ..#...-........f
00C0: 78 73 74 2D F8 FF FF 7F  F8 FF FF 7F 73 31 31 39  xst-........s119
00D0: 1C 00 80 4C 1C 0A 80 27  0B F0 FF FF 7F 06 1C 0B  ...L...'........
00E0: 80 4D 1A DC 02 1C 05 80  1C 0C 80 52 07 80 F8 FF  .M.........R....
00F0: FF 7F F8 FF FF 7F 73 30  38 39 2A 0B F0 FF FF 7F  ......s089*.....
0100: 27 10 F0 FF FF 7F 10 27  10 D6 91 00 01 02 45 0D  '......'......E.
0110: 80 F0 FF FF 7F F0 FF FF  7F 63 61 30 30 04 80 1A  .........ca00...
0120: BB 02 2D F8 FF FF 7F F8  FF FF 7F 73 74 61 74 1C  ..-........stat.
0130: 0E 80 2D F8 FF FF 7F F8  FF FF 7F 73 31 33 36 1C  ..-........s136.
0140: 0F 80 4C 27 10 F0 FF FF  7F 11 1C 05 80 1C 0C 80  ..L'............
0150: 1A DC 02 1C 10 80 2D F8  FF FF 7F F8 FF FF 7F 6B  ......-........k
0160: 69 6C 6C 2A 10 F0 FF FF  7F 1C 03 80 52 0D 80 F0  ill*........R...
0170: FF FF 7F F0 FF FF 7F 63  61 30 30 4E 00 F0 FF FF  .......ca00N....
0180: 7F 80 F0 FF FF 7F 46 00  45 03 80 F0 FF FF 7F F0  ......F.E.......
0190: FF FF 7F 66 64 69 31 04  80 20 00 21 00           ...fdi1.. .!.   
```

#### Opcodes

```
  0: 0x0056 [0x20] SET_CLI_EVENT_UC_FLAG: Lock player control
  1: 0x0058 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  2: 0x0059 [0x46] CAMERA_CONTROL: Disable user control
  3: 0x005B [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [EventEntity, EventEntity], work=[200*, 0*]
  4: 0x006C [0x1C] WAIT(60* ticks)
  5: 0x006F [0x38] SET_CLIENT_EVENT_MODE(mode=19*)
  6: 0x0072 [0x29] REQ_SET_WAIT(priority=0x08, entity_id=LocalPlayer, tag_num=0x03)
  7: 0x0079 [0x79] LocalPlayer looks at LocalPlayer (Basic look)
  8: 0x0083 [0x29] REQ_SET_WAIT(priority=0x0B, entity_id=LocalPlayer, tag_num=0x05)
  9: 0x008A [0x45] LOAD_SCHEDULED_TASK: Load scheduler "s089" with entities [EventEntity, EventEntity], work=[25*, 0*]
 10: 0x009B [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi1" with entities [EventEntity, EventEntity], work=[200*, 0*]
 11: 0x00AC [0x1C] WAIT(15* ticks)
 12: 0x00AF [0x48] [System] [7450*]:
    → "The $3 flashes with blinding light!"
 13: 0x00B2 [0x23] WAIT_FOR_DIALOG_INTERACTION
 14: 0x00B3 [0x1C] WAIT(60* ticks)
 15: 0x00B6 [0x2D] CREATE_ZONE_SCHEDULER_TASK: Create scheduler "fxst" with entities [EventEntity, EventEntity]
 16: 0x00C3 [0x2D] CREATE_ZONE_SCHEDULER_TASK: Create scheduler "s119" with entities [EventEntity, EventEntity]
 17: 0x00D0 [0x1C] WAIT(480* ticks)
 18: 0x00D3 [0x4C] EventEntity->StatusEvent = 8 // Open door
 19: 0x00D4 [0x1C] WAIT(90* ticks)
 20: 0x00D7 [0x27] REQ_SET(priority=0x0B, entity_id=LocalPlayer, tag_num=0x06)
 21: 0x00DE [0x1C] WAIT(300* ticks)
 22: 0x00E1 [0x4D] EventEntity->StatusEvent = 9 // Close door
 23: 0x00E2 [0x1A] CALL_SUBROUTINE(address=0x02DC)
 24: 0x00E5 [0x1C] WAIT(60* ticks)
 25: 0x00E8 [0x1C] WAIT(30* ticks)
 26: 0x00EB [0x52] END_LOAD_SCHEDULER: End scheduler "s089" with entities [EventEntity, EventEntity], work=25*
 27: 0x00FA [0x2A] GET_REQ_LEVEL(level=11, entity_id=LocalPlayer)
 28: 0x0100 [0x27] REQ_SET(priority=0x10, entity_id=LocalPlayer, tag_num=0x10)
 29: 0x0107 [0x27] REQ_SET(priority=0x10, entity_id=??? (ID: 16814550/0x010091D6), tag_num=0x02)
 30: 0x010E [0x45] LOAD_SCHEDULED_TASK: Load scheduler "ca00" with entities [LocalPlayer, LocalPlayer], work=[155*, 0*]
 31: 0x011F [0x1A] CALL_SUBROUTINE(address=0x02BB)
 32: 0x0122 [0x2D] CREATE_ZONE_SCHEDULER_TASK: Create scheduler "stat" with entities [EventEntity, EventEntity]
 33: 0x012F [0x1C] WAIT(80* ticks)
 34: 0x0132 [0x2D] CREATE_ZONE_SCHEDULER_TASK: Create scheduler "s136" with entities [EventEntity, EventEntity]
 35: 0x013F [0x1C] WAIT(340* ticks)
 36: 0x0142 [0x4C] EventEntity->StatusEvent = 8 // Open door
 37: 0x0143 [0x27] REQ_SET(priority=0x10, entity_id=LocalPlayer, tag_num=0x11)
 38: 0x014A [0x1C] WAIT(60* ticks)
 39: 0x014D [0x1C] WAIT(30* ticks)
 40: 0x0150 [0x1A] CALL_SUBROUTINE(address=0x02DC)
 41: 0x0153 [0x1C] WAIT(170* ticks)
 42: 0x0156 [0x2D] CREATE_ZONE_SCHEDULER_TASK: Create scheduler "kill" with entities [EventEntity, EventEntity]
 43: 0x0163 [0x2A] GET_REQ_LEVEL(level=16, entity_id=LocalPlayer)
 44: 0x0169 [0x1C] WAIT(200* ticks)
 45: 0x016C [0x52] END_LOAD_SCHEDULER: End scheduler "ca00" with entities [LocalPlayer, LocalPlayer], work=155*
 46: 0x017B [0x4E] SET_ENTITY_HIDE_FLAG: Show LocalPlayer
 47: 0x0181 [0x80] LOAD_WAIT(entity=LocalPlayer)
 48: 0x0186 [0x46] CAMERA_CONTROL: Restore default settings
 49: 0x0188 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 50: 0x0199 [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
 51: 0x019B [0x21] END_EVENT
 52: 0x019C [0x00] END_REQSTACK()
```

### Event 7

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x019D    |
| Data Size    | 877 bytes |
| Instructions | 35        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0190:                                         20 01 42                .B
01A0: 46 01 02 07 10 11 80 00  B2 01 03 01 10 11 80 01  F...............
01B0: B7 01 03 01 10 12 80 45  03 80 F8 FF FF 7F F8 FF  .......E........
01C0: FF 7F 66 64 6F 31 04 80  1C 05 80 38 06 80 29 08  ..fdo1.....8..).
01D0: F0 FF FF 7F 03 29 0B F0  FF FF 7F 05 45 07 80 F8  .....)......E...
01E0: FF FF 7F F8 FF FF 7F 73  30 38 39 04 80 45 03 80  .......s089..E..
01F0: F8 FF FF 7F F8 FF FF 7F  66 64 69 31 04 80 1C 08  ........fdi1....
0200: 80 48 09 80 23 1C 05 80  2D F8 FF FF 7F F8 FF FF  .H..#...-.......
0210: 7F 66 78 73 74 2D F8 FF  FF 7F F8 FF FF 7F 73 31  .fxst-........s1
0220: 31 39 1C 00 80 45 03 80  F0 FF FF 7F F0 FF FF 7F  19...E..........
0230: 66 64 6F 31 04 80 1C 13  80 02 07 10 11 80 00 45  fdo1...........E
0240: 02 48 14 80 23 1C 15 80  52 07 80 F8 FF FF 7F F8  .H..#...R.......
0250: FF FF 7F 73 30 38 39 4E  00 F0 FF FF 7F 80 F0 FF  ...s089N........
0260: FF 7F 46 00 45 03 80 F0  FF FF 7F F0 FF FF 7F 66  ..F.E..........f
0270: 64 69 31 04 80 20 00 21  00 45 03 80 F0 FF FF 7F  di1.. .!.E......
0280: F0 FF FF 7F 66 64 69 30  04 80 55 03 80 F0 FF FF  ....fdi0..U.....
0290: 7F F0 FF FF 7F 66 64 69  30 1B 45 03 80 F0 FF FF  .....fdi0.E.....
02A0: 7F F0 FF FF 7F 66 64 6F  30 04 80 55 03 80 F0 FF  .....fdo0..U....
02B0: FF 7F F0 FF FF 7F 66 64  6F 30 1B 45 03 80 F0 FF  ......fdo0.E....
02C0: FF 7F F0 FF FF 7F 66 64  69 31 04 80 55 03 80 F0  ......fdi1..U...
02D0: FF FF 7F F0 FF FF 7F 66  64 69 31 1B 45 03 80 F0  .......fdi1.E...
02E0: FF FF 7F F0 FF FF 7F 66  64 6F 31 04 80 55 03 80  .......fdo1..U..
02F0: F0 FF FF 7F F0 FF FF 7F  66 64 6F 31 1B 45 16 80  ........fdo1.E..
0300: F0 FF FF 7F F0 FF FF 7F  77 68 69 31 04 80 55 16  ........whi1..U.
0310: 80 F0 FF FF 7F F0 FF FF  7F 77 68 69 31 1B 45 16  .........whi1.E.
0320: 80 F0 FF FF 7F F0 FF FF  7F 77 68 6F 31 04 80 55  .........who1..U
0330: 16 80 F0 FF FF 7F F0 FF  FF 7F 77 68 6F 31 1B 45  ..........who1.E
0340: 16 80 F0 FF FF 7F F0 FF  FF 7F 77 68 6F 32 04 80  ..........who2..
0350: 55 16 80 F0 FF FF 7F F0  FF FF 7F 77 68 6F 32 1B  U..........who2.
0360: 45 16 80 F0 FF FF 7F F0  FF FF 7F 77 68 6F 33 04  E..........who3.
0370: 80 55 16 80 F0 FF FF 7F  F0 FF FF 7F 77 68 6F 33  .U..........who3
0380: 1B 62 12 80 F0 FF FF 7F  F0 FF FF 7F 6D 61 69 6E  .b..........main
0390: 04 80 1C 17 80 45 03 80  F0 FF FF 7F F0 FF FF 7F  .....E..........
03A0: 66 64 6F 31 04 80 55 03  80 F0 FF FF 7F F0 FF FF  fdo1..U.........
03B0: 7F 66 64 6F 31 1B 45 03  80 F0 FF FF 7F F0 FF FF  .fdo1.E.........
03C0: 7F 66 64 69 31 04 80 62  11 80 F0 FF FF 7F F0 FF  .fdi1..b........
03D0: FF 7F 6D 61 69 6E 04 80  1C 0C 80 55 03 80 F0 FF  ..main.....U....
03E0: FF 7F F0 FF FF 7F 66 64  69 31 1B 45 03 80 F0 FF  ......fdi1.E....
03F0: FF 7F F0 FF FF 7F 62 6C  6F 6E 04 80 45 16 80 F0  ......blon..E...
0400: FF FF 7F F0 FF FF 7F 62  6C 6F 6E 04 80 1B 45 16  .......blon...E.
0410: 80 F0 FF FF 7F F0 FF FF  7F 77 68 69 30 04 80 55  .........whi0..U
0420: 16 80 F0 FF FF 7F F0 FF  FF 7F 77 68 69 30 1B 45  ..........whi0.E
0430: 16 80 F0 FF FF 7F F0 FF  FF 7F 77 68 6F 30 04 80  ..........who0..
0440: 55 16 80 F0 FF FF 7F F0  FF FF 7F 77 68 6F 30 1B  U..........who0.
0450: 45 18 80 F0 FF FF 7F F0  FF FF 7F 65 66 6F 6E 04  E..........efon.
0460: 80 55 18 80 F0 FF FF 7F  F0 FF FF 7F 65 66 6F 6E  .U..........efon
0470: 1B 45 03 80 F0 FF FF 7F  F0 FF FF 7F 66 64 69 73  .E..........fdis
0480: 04 80 1B 45 03 80 F0 FF  FF 7F F0 FF FF 7F 66 64  ...E..........fd
0490: 6F 73 04 80 55 03 80 F0  FF FF 7F F0 FF FF 7F 66  os..U..........f
04A0: 64 6F 73 1B 45 03 80 F0  FF FF 7F F0 FF FF 7F 66  dos.E..........f
04B0: 64 69 66 04 80 1B 45 03  80 F0 FF FF 7F F0 FF FF  dif...E.........
04C0: 7F 66 64 6F 66 04 80 55  03 80 F0 FF FF 7F F0 FF  .fdof..U........
04D0: FF 7F 66 64 6F 66 1B 45  03 80 F0 FF FF 7F F0 FF  ..fdof.E........
04E0: FF 7F 66 64 69 70 04 80  1B 45 03 80 F0 FF FF 7F  ..fdip...E......
04F0: F0 FF FF 7F 66 64 6F 70  04 80 55 03 80 F0 FF FF  ....fdop..U.....
0500: 7F F0 FF FF 7F 66 64 6F  70 1B                    .....fdop.      
```

#### Opcodes

```
  0: 0x019D [0x20] SET_CLI_EVENT_UC_FLAG: Lock player control
  1: 0x019F [0x42] SET_CLI_EVENT_CANCEL_DATA()
  2: 0x01A0 [0x46] CAMERA_CONTROL: Disable user control
  3: 0x01A2 [0x02] IF !(Work_Zone[7] == 2*) GOTO 0x01B2
  4: 0x01AA [0x03] Work_Zone[1] = 2*
  5: 0x01AF [0x01] GOTO 0x01B7
  6: 0x01B2 [0x03] Work_Zone[1] = 1*

SUBROUTINE_01B7:
  7: 0x01B7 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [EventEntity, EventEntity], work=[200*, 0*]
  8: 0x01C8 [0x1C] WAIT(60* ticks)
  9: 0x01CB [0x38] SET_CLIENT_EVENT_MODE(mode=19*)
 10: 0x01CE [0x29] REQ_SET_WAIT(priority=0x08, entity_id=LocalPlayer, tag_num=0x03)
 11: 0x01D5 [0x29] REQ_SET_WAIT(priority=0x0B, entity_id=LocalPlayer, tag_num=0x05)
 12: 0x01DC [0x45] LOAD_SCHEDULED_TASK: Load scheduler "s089" with entities [EventEntity, EventEntity], work=[25*, 0*]
 13: 0x01ED [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi1" with entities [EventEntity, EventEntity], work=[200*, 0*]
 14: 0x01FE [0x1C] WAIT(15* ticks)
 15: 0x0201 [0x48] [System] [7450*]:
    → "The $3 flashes with blinding light!"
 16: 0x0204 [0x23] WAIT_FOR_DIALOG_INTERACTION
 17: 0x0205 [0x1C] WAIT(60* ticks)
 18: 0x0208 [0x2D] CREATE_ZONE_SCHEDULER_TASK: Create scheduler "fxst" with entities [EventEntity, EventEntity]
 19: 0x0215 [0x2D] CREATE_ZONE_SCHEDULER_TASK: Create scheduler "s119" with entities [EventEntity, EventEntity]
 20: 0x0222 [0x1C] WAIT(480* ticks)
 21: 0x0225 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 22: 0x0236 [0x1C] WAIT(120* ticks)
 23: 0x0239 [0x02] IF !(Work_Zone[7] == 2*) GOTO 0x0245
 24: 0x0241 [0x48] [System] [7452*]:
    → "...But the door remains closed. You have no choice but to return to Jeuno."
 25: 0x0244 [0x23] WAIT_FOR_DIALOG_INTERACTION
 26: 0x0245 [0x1C] WAIT(520* ticks)
 27: 0x0248 [0x52] END_LOAD_SCHEDULER: End scheduler "s089" with entities [EventEntity, EventEntity], work=25*
 28: 0x0257 [0x4E] SET_ENTITY_HIDE_FLAG: Show LocalPlayer
 29: 0x025D [0x80] LOAD_WAIT(entity=LocalPlayer)
 30: 0x0262 [0x46] CAMERA_CONTROL: Restore default settings
 31: 0x0264 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 32: 0x0275 [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
 33: 0x0277 [0x21] END_EVENT
 34: 0x0278 [0x00] END_REQSTACK()
```

#### Data or dead code:

```
# Dead code (unreachable instructions):
     0x0279 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi0" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
     0x028A [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "fdi0" with entities [LocalPlayer, LocalPlayer], work=200*
     0x0299 [0x1B] RETURN
     0x029A [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo0" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
     0x02AB [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "fdo0" with entities [LocalPlayer, LocalPlayer], work=200*
     0x02BA [0x1B] RETURN
     0x02BB [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
     0x02CC [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "fdi1" with entities [LocalPlayer, LocalPlayer], work=200*
     0x02DB [0x1B] RETURN
     0x02DC [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
     0x02ED [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=200*
     0x02FC [0x1B] RETURN
     0x02FD [0x45] LOAD_SCHEDULED_TASK: Load scheduler "whi1" with entities [LocalPlayer, LocalPlayer], work=[201*, 0*]
     0x030E [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "whi1" with entities [LocalPlayer, LocalPlayer], work=201*
     0x031D [0x1B] RETURN
     0x031E [0x45] LOAD_SCHEDULED_TASK: Load scheduler "who1" with entities [LocalPlayer, LocalPlayer], work=[201*, 0*]
     0x032F [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "who1" with entities [LocalPlayer, LocalPlayer], work=201*
     0x033E [0x1B] RETURN
     0x033F [0x45] LOAD_SCHEDULED_TASK: Load scheduler "who2" with entities [LocalPlayer, LocalPlayer], work=[201*, 0*]
     0x0350 [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "who2" with entities [LocalPlayer, LocalPlayer], work=201*
     0x035F [0x1B] RETURN
     0x0360 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "who3" with entities [LocalPlayer, LocalPlayer], work=[201*, 0*]
     0x0371 [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "who3" with entities [LocalPlayer, LocalPlayer], work=201*
     0x0380 [0x1B] RETURN
     0x0381 [0x62] LOAD_EVENT_SCHEDULER: Load scheduler "main" with entities [LocalPlayer, LocalPlayer], work=[1*, 0*]
     0x0392 [0x1C] WAIT(45* ticks)
     0x0395 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
     0x03A6 [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=200*
     0x03B5 [0x1B] RETURN
     0x03B6 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
     0x03C7 [0x62] LOAD_EVENT_SCHEDULER: Load scheduler "main" with entities [LocalPlayer, LocalPlayer], work=[2*, 0*]
     0x03D8 [0x1C] WAIT(30* ticks)
     0x03DB [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "fdi1" with entities [LocalPlayer, LocalPlayer], work=200*
     0x03EA [0x1B] RETURN
     0x03EB [0x45] LOAD_SCHEDULED_TASK: Load scheduler "blon" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
     0x03FC [0x45] LOAD_SCHEDULED_TASK: Load scheduler "blon" with entities [LocalPlayer, LocalPlayer], work=[201*, 0*]
     0x040D [0x1B] RETURN
     0x040E [0x45] LOAD_SCHEDULED_TASK: Load scheduler "whi0" with entities [LocalPlayer, LocalPlayer], work=[201*, 0*]
     0x041F [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "whi0" with entities [LocalPlayer, LocalPlayer], work=201*
     0x042E [0x1B] RETURN
     0x042F [0x45] LOAD_SCHEDULED_TASK: Load scheduler "who0" with entities [LocalPlayer, LocalPlayer], work=[201*, 0*]
     0x0440 [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "who0" with entities [LocalPlayer, LocalPlayer], work=201*
     0x044F [0x1B] RETURN
     0x0450 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "efon" with entities [LocalPlayer, LocalPlayer], work=[215*, 0*]
     0x0461 [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "efon" with entities [LocalPlayer, LocalPlayer], work=215*
     0x0470 [0x1B] RETURN
     0x0471 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdis" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
     0x0482 [0x1B] RETURN
     0x0483 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdos" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
     0x0494 [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "fdos" with entities [LocalPlayer, LocalPlayer], work=200*
     0x04A3 [0x1B] RETURN
     0x04A4 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdif" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
     0x04B5 [0x1B] RETURN
     0x04B6 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdof" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
     0x04C7 [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "fdof" with entities [LocalPlayer, LocalPlayer], work=200*
     0x04D6 [0x1B] RETURN
     0x04D7 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdip" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
     0x04E8 [0x1B] RETURN
     0x04E9 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdop" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
     0x04FA [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "fdop" with entities [LocalPlayer, LocalPlayer], work=200*
     0x0509 [0x1B] RETURN
```
