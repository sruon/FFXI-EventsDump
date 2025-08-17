# 16834569 - Large Apparatus

## Common Data

| Field            | Value                         |
|------------------|-------------------------------|
| Zone             | Hall of Transference (ID: 14) |
| Block Size       | 1424 bytes                    |
| Total Events     | 6                             |
| References Count | 28                            |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [120](#event-120)        | 0x0001       |    201 |             25 |
| [65535.1](#event-655351) | 0x00CA       |    141 |             17 |
| [121](#event-121)        | 0x0157       |      1 |              1 |
| [122](#event-122)        | 0x0158       |    242 |             42 |
| [160](#event-160)        | 0x024A       |    685 |             81 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x00C8      |         200 |
|       1 | 0x0000      |           0 |
|       2 | 0x0078      |         120 |
|       3 | 0x0013      |          19 |
|       4 | 0x005E      |          94 |
|       5 | 0x003C      |          60 |
|       6 | 0x00FA      |         250 |
|       7 | 0x04B0      |        1200 |
|       8 | 0x03E8      |        1000 |
|       9 | 0x1C82      |        7298 |
|      10 | 0x1C83      |        7299 |
|      11 | 0x1C84      |        7300 |
|      12 | 0x0001      |           1 |
|      13 | 0x40000000  |  1073741824 |
|      14 | 0x1C85      |        7301 |
|      15 | 0x0384      |         900 |
|      16 | 0x00B4      |         180 |
|      17 | 0x0076      |         118 |
|      18 | 0x001E      |          30 |
|      19 | 0x0028      |          40 |
|      20 | 0x0046      |          70 |
|      21 | 0x1C81      |        7297 |
|      22 | 0x0064      |         100 |
|      23 | 0x1C80      |        7296 |
|      24 | 0x000A      |          10 |
|      25 | 0x0005      |           5 |
|      26 | 0x0006      |           6 |
|      27 | 0x0039      |          57 |

## String References

- **7298**: By sealing off a portion of your memory, your destiny within this realm of Promyvion can be altered.
- **7299**: This will allow you to return to the entrance of the crag, having forgotten all events regarding this place.
- **7300**: Seal off your memories? [Yes./No.]
- **7301**: Are you sure? [Absolutely./No.]

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

### Event 120

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x0001    |
| Data Size    | 201 bytes |
| Instructions | 25        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    20 01 42 46 01 45 00  80 F0 FF FF 7F F0 FF FF    .BF.E.........
0010: 7F 66 64 6F 31 01 80 1C  02 80 38 03 80 29 01 F0  .fdo1.....8..)..
0020: FF FF 7F 09 45 04 80 F8  FF FF 7F F8 FF FF 7F 7A  ....E..........z
0030: 31 34 61 01 80 45 00 80  F0 FF FF 7F F0 FF FF 7F  14a..E..........
0040: 66 64 69 31 01 80 1C 05  80 2D F8 FF FF 7F F8 FF  fdi1.....-......
0050: FF 7F 32 73 77 31 1C 06  80 52 04 80 F8 FF FF 7F  ..2sw1...R......
0060: F8 FF FF 7F 7A 31 34 61  45 00 80 F0 FF FF 7F F0  ....z14aE.......
0070: FF FF 7F 6F 76 6C 31 01  80 45 04 80 F8 FF FF 7F  ...ovl1..E......
0080: F8 FF FF 7F 7A 31 34 62  01 80 1C 07 80 45 00 80  ....z14b.....E..
0090: F0 FF FF 7F F0 FF FF 7F  66 64 6F 31 01 80 1C 05  ........fdo1....
00A0: 80 52 04 80 F8 FF FF 7F  F8 FF FF 7F 7A 31 34 62  .R..........z14b
00B0: 46 00 1C 05 80 45 00 80  F0 FF FF 7F F0 FF FF 7F  F....E..........
00C0: 66 64 69 31 01 80 20 00  21 00                    fdi1.. .!.      
```

#### Opcodes

```
  0: 0x0001 [0x20] SET_CLI_EVENT_UC_FLAG: Lock player control
  1: 0x0003 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  2: 0x0004 [0x46] CAMERA_CONTROL: Disable user control
  3: 0x0006 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
  4: 0x0017 [0x1C] WAIT(120* ticks)
  5: 0x001A [0x38] SET_CLIENT_EVENT_MODE(mode=19*)
  6: 0x001D [0x29] REQ_SET_WAIT(priority=0x01, entity_id=LocalPlayer, tag_num=0x09)
  7: 0x0024 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "z14a" with entities [EventEntity, EventEntity], work=[94*, 0*]
  8: 0x0035 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
  9: 0x0046 [0x1C] WAIT(60* ticks)
 10: 0x0049 [0x2D] CREATE_ZONE_SCHEDULER_TASK: Create scheduler "2sw1" with entities [EventEntity, EventEntity]
 11: 0x0056 [0x1C] WAIT(250* ticks)
 12: 0x0059 [0x52] END_LOAD_SCHEDULER: End scheduler "z14a" with entities [EventEntity, EventEntity], work=94*
 13: 0x0068 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "ovl1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 14: 0x0079 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "z14b" with entities [EventEntity, EventEntity], work=[94*, 0*]
 15: 0x008A [0x1C] WAIT(1200* ticks)
 16: 0x008D [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 17: 0x009E [0x1C] WAIT(60* ticks)
 18: 0x00A1 [0x52] END_LOAD_SCHEDULER: End scheduler "z14b" with entities [EventEntity, EventEntity], work=94*
 19: 0x00B0 [0x46] CAMERA_CONTROL: Restore default settings
 20: 0x00B2 [0x1C] WAIT(60* ticks)
 21: 0x00B5 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 22: 0x00C6 [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
 23: 0x00C8 [0x21] END_EVENT
 24: 0x00C9 [0x00] END_REQSTACK()
```

### Event 65535.1

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x00CA    |
| Data Size    | 141 bytes |
| Instructions | 17        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00C0:                                20 01 42 46 01 45             .BF.E
00D0: 00 80 F8 FF FF 7F F8 FF  FF 7F 66 64 6F 31 01 80  ..........fdo1..
00E0: 1C 02 80 38 03 80 29 01  F0 FF FF 7F 09 45 04 80  ...8..)......E..
00F0: F8 FF FF 7F F8 FF FF 7F  7A 31 34 61 01 80 45 00  ........z14a..E.
0100: 80 F8 FF FF 7F F8 FF FF  7F 66 64 69 31 01 80 1C  .........fdi1...
0110: 05 80 2D F8 FF FF 7F F8  FF FF 7F 32 73 77 31 1C  ..-........2sw1.
0120: 06 80 52 04 80 F8 FF FF  7F F8 FF FF 7F 7A 31 34  ..R..........z14
0130: 61 45 00 80 F0 FF FF 7F  F0 FF FF 7F 6F 76 6C 31  aE..........ovl1
0140: 01 80 45 04 80 F8 FF FF  7F F8 FF FF 7F 7A 31 34  ..E..........z14
0150: 62 01 80 1C 08 80 00                              b......         
```

#### Opcodes

```
  0: 0x00CA [0x20] SET_CLI_EVENT_UC_FLAG: Lock player control
  1: 0x00CC [0x42] SET_CLI_EVENT_CANCEL_DATA()
  2: 0x00CD [0x46] CAMERA_CONTROL: Disable user control
  3: 0x00CF [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [EventEntity, EventEntity], work=[200*, 0*]
  4: 0x00E0 [0x1C] WAIT(120* ticks)
  5: 0x00E3 [0x38] SET_CLIENT_EVENT_MODE(mode=19*)
  6: 0x00E6 [0x29] REQ_SET_WAIT(priority=0x01, entity_id=LocalPlayer, tag_num=0x09)
  7: 0x00ED [0x45] LOAD_SCHEDULED_TASK: Load scheduler "z14a" with entities [EventEntity, EventEntity], work=[94*, 0*]
  8: 0x00FE [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi1" with entities [EventEntity, EventEntity], work=[200*, 0*]
  9: 0x010F [0x1C] WAIT(60* ticks)
 10: 0x0112 [0x2D] CREATE_ZONE_SCHEDULER_TASK: Create scheduler "2sw1" with entities [EventEntity, EventEntity]
 11: 0x011F [0x1C] WAIT(250* ticks)
 12: 0x0122 [0x52] END_LOAD_SCHEDULER: End scheduler "z14a" with entities [EventEntity, EventEntity], work=94*
 13: 0x0131 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "ovl1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 14: 0x0142 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "z14b" with entities [EventEntity, EventEntity], work=[94*, 0*]
 15: 0x0153 [0x1C] WAIT(1000* ticks)
 16: 0x0156 [0x00] END_REQSTACK()
```

### Event 121

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0157  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0150:                      00                                  .        
```

#### Opcodes

```
  0: 0x0157 [0x00] END_REQSTACK()
```

### Event 122

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x0158    |
| Data Size    | 242 bytes |
| Instructions | 40        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0150:                          20 01 48 09 80 23 48 0A           .H..#H.
0160: 80 23 24 0B 80 0C 80 01  80 25 02 00 10 0C 80 00  .#$......%......
0170: 7C 01 03 01 10 0D 80 21  00 01 7C 01 24 0E 80 0C  |......!..|.$...
0180: 80 01 80 25 02 00 10 0C  80 00 96 01 03 01 10 0D  ...%............
0190: 80 21 00 01 96 01 42 46  01 43 00 43 01 45 00 80  .!....BF.C.C.E..
01A0: F0 FF FF 7F F0 FF FF 7F  66 64 6F 31 01 80 1C 02  ........fdo1....
01B0: 80 38 03 80 29 01 F0 FF  FF 7F 09 45 04 80 F8 FF  .8..)......E....
01C0: FF 7F F8 FF FF 7F 7A 31  34 61 01 80 45 00 80 F0  ......z14a..E...
01D0: FF FF 7F F0 FF FF 7F 66  64 69 31 01 80 1C 05 80  .......fdi1.....
01E0: 2D F8 FF FF 7F F8 FF FF  7F 32 73 77 32 1C 06 80  -........2sw2...
01F0: 52 04 80 F8 FF FF 7F F8  FF FF 7F 7A 31 34 61 45  R..........z14aE
0200: 00 80 F0 FF FF 7F F0 FF  FF 7F 6F 76 6C 31 01 80  ..........ovl1..
0210: 45 04 80 F8 FF FF 7F F8  FF FF 7F 7A 31 34 62 01  E..........z14b.
0220: 80 1C 0F 80 45 00 80 F0  FF FF 7F F0 FF FF 7F 66  ....E..........f
0230: 64 6F 31 01 80 1C 05 80  52 04 80 F8 FF FF 7F F8  do1.....R.......
0240: FF FF 7F 7A 31 34 62 30  21 00                    ...z14b0!.      
```

#### Opcodes

```
  0: 0x0158 [0x20] SET_CLI_EVENT_UC_FLAG: Lock player control
  1: 0x015A [0x48] [System] [7298*]:
    → "By sealing off a portion of your memory, your destiny within this realm of Promyvion can be altered."
  2: 0x015D [0x23] WAIT_FOR_DIALOG_INTERACTION
  3: 0x015E [0x48] [System] [7299*]:
    → "This will allow you to return to the entrance of the crag, having forgotten all events regarding this place."
  4: 0x0161 [0x23] WAIT_FOR_DIALOG_INTERACTION
  5: 0x0162 [0x24] CREATE_DIALOG(message_id=7300*, default_option=1*, option_flags=0*)
    → "Seal off your memories? [Yes./No.]"
  6: 0x0169 [0x25] WAIT_DIALOG_SELECT()
  7: 0x016A [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x017C
  8: 0x0172 [0x03] Work_Zone[1] = 1073741824*
  9: 0x0177 [0x21] END_EVENT
 10: 0x0178 [0x00] END_REQSTACK()

SUBROUTINE_017C:
 11: 0x017C [0x24] CREATE_DIALOG(message_id=7301*, default_option=1*, option_flags=0*)
    → "Are you sure? [Absolutely./No.]"
 12: 0x0183 [0x25] WAIT_DIALOG_SELECT()
 13: 0x0184 [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x0196
 14: 0x018C [0x03] Work_Zone[1] = 1073741824*
 15: 0x0191 [0x21] END_EVENT
 16: 0x0192 [0x00] END_REQSTACK()

SUBROUTINE_0196:
 17: 0x0196 [0x42] SET_CLI_EVENT_CANCEL_DATA()
 18: 0x0197 [0x46] CAMERA_CONTROL: Disable user control
 19: 0x0199 [0x43] SEND_EVENT_UPDATE: Send pending tag to server (packet 0x005B)
 20: 0x019B [0x43] SEND_EVENT_UPDATE: Check pending flag (skip if not pending)
 21: 0x019D [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 22: 0x01AE [0x1C] WAIT(120* ticks)
 23: 0x01B1 [0x38] SET_CLIENT_EVENT_MODE(mode=19*)
 24: 0x01B4 [0x29] REQ_SET_WAIT(priority=0x01, entity_id=LocalPlayer, tag_num=0x09)
 25: 0x01BB [0x45] LOAD_SCHEDULED_TASK: Load scheduler "z14a" with entities [EventEntity, EventEntity], work=[94*, 0*]
 26: 0x01CC [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 27: 0x01DD [0x1C] WAIT(60* ticks)
 28: 0x01E0 [0x2D] CREATE_ZONE_SCHEDULER_TASK: Create scheduler "2sw2" with entities [EventEntity, EventEntity]
 29: 0x01ED [0x1C] WAIT(250* ticks)
 30: 0x01F0 [0x52] END_LOAD_SCHEDULER: End scheduler "z14a" with entities [EventEntity, EventEntity], work=94*
 31: 0x01FF [0x45] LOAD_SCHEDULED_TASK: Load scheduler "ovl1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 32: 0x0210 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "z14b" with entities [EventEntity, EventEntity], work=[94*, 0*]
 33: 0x0221 [0x1C] WAIT(900* ticks)
 34: 0x0224 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 35: 0x0235 [0x1C] WAIT(60* ticks)
 36: 0x0238 [0x52] END_LOAD_SCHEDULER: End scheduler "z14b" with entities [EventEntity, EventEntity], work=94*
 37: 0x0247 [0x30] SET_UCOFF_CONTINUE_ZERO()
 38: 0x0248 [0x21] END_EVENT
 39: 0x0249 [0x00] END_REQSTACK()
```

#### Data or dead code:

```
# Dead code (unreachable instructions):
     0x0179 [0x01] GOTO 0x017C
# Dead code (unreachable instructions):
     0x0193 [0x01] GOTO 0x0196
```

### Event 160

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x024A    |
| Data Size    | 685 bytes |
| Instructions | 81        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0240:                                20 01 42 46 01 29             .BF.)
0250: 0B 09 E0 00 01 02 29 08  F0 FF FF 7F 04 27 0B F0  ......)......'..
0260: FF FF 7F 07 1C 10 80 2A  0B F0 FF FF 7F 4A F0 FF  .......*.....J..
0270: FF 7F 06 E0 00 01 45 11  80 F8 FF FF 7F F8 FF FF  ......E.........
0280: 7F 73 65 34 39 01 80 29  0B 06 E0 00 01 07 1C 12  .se49..)........
0290: 80 52 04 80 F8 FF FF 7F  F8 FF FF 7F 7A 31 34 62  .R..........z14b
02A0: 45 00 80 F0 FF FF 7F F0  FF FF 7F 6F 76 6C 31 01  E..........ovl1.
02B0: 80 45 11 80 F8 FF FF 7F  F8 FF FF 7F 73 31 33 38  .E..........s138
02C0: 01 80 1C 13 80 45 00 80  F0 FF FF 7F F0 FF FF 7F  .....E..........
02D0: 66 64 6F 31 01 80 1C 05  80 29 0B 17 E0 00 01 04  fdo1.....)......
02E0: 29 0B 18 E0 00 01 04 4E  00 17 E0 00 01 4E 00 18  )......N.....N..
02F0: E0 00 01 80 17 E0 00 01  80 18 E0 00 01 52 11 80  .............R..
0300: F8 FF FF 7F F8 FF FF 7F  73 31 33 38 45 11 80 F8  ........s138E...
0310: FF FF 7F F8 FF FF 7F 73  65 38 30 01 80 27 0B 17  .......se80..'..
0320: E0 00 01 01 27 0B 18 E0  00 01 01 1C 14 80 52 04  ....'.........R.
0330: 80 F8 FF FF 7F F8 FF FF  7F 7A 31 34 62 45 11 80  .........z14bE..
0340: F8 FF FF 7F F8 FF FF 7F  73 30 30 30 01 80 45 00  ........s000..E.
0350: 80 F0 FF FF 7F F0 FF FF  7F 66 64 69 31 01 80 45  .........fdi1..E
0360: 11 80 F8 FF FF 7F F8 FF  FF 7F 73 65 38 31 01 80  ..........se81..
0370: 1C 14 80 52 11 80 F8 FF  FF 7F F8 FF FF 7F 73 30  ...R..........s0
0380: 30 30 45 11 80 F8 FF FF  7F F8 FF FF 7F 73 30 30  00E..........s00
0390: 31 01 80 45 11 80 F8 FF  FF 7F F8 FF FF 7F 73 65  1..E..........se
03A0: 38 32 01 80 2B 18 E0 00  01 15 80 23 1C 16 80 2B  82..+......#...+
03B0: 17 E0 00 01 17 80 23 1C  02 80 29 0B 06 E0 00 01  ......#...).....
03C0: 08 1C 18 80 27 0B F0 FF  FF 7F 08 52 11 80 F8 FF  ....'......R....
03D0: FF 7F F8 FF FF 7F 73 30  30 31 02 09 10 19 80 00  ......s001......
03E0: F6 03 45 11 80 F8 FF FF  7F F8 FF FF 7F 73 30 30  ..E..........s00
03F0: 33 01 80 01 23 04 02 09  10 1A 80 00 12 04 45 11  3...#.........E.
0400: 80 F8 FF FF 7F F8 FF FF  7F 73 30 30 33 01 80 01  .........s003...
0410: 23 04 45 11 80 F8 FF FF  7F F8 FF FF 7F 73 30 30  #.E..........s00
0420: 32 01 80 1C 02 80 45 00  80 F0 FF FF 7F F0 FF FF  2.....E.........
0430: 7F 66 64 6F 31 01 80 1C  05 80 02 09 10 19 80 00  .fdo1...........
0440: 54 04 52 11 80 F8 FF FF  7F F8 FF FF 7F 73 30 30  T.R..........s00
0450: 33 01 7D 04 02 09 10 1A  80 00 6E 04 52 11 80 F8  3.}.......n.R...
0460: FF FF 7F F8 FF FF 7F 73  30 30 33 01 7D 04 52 11  .......s003.}.R.
0470: 80 F8 FF FF 7F F8 FF FF  7F 73 30 30 32 2A 0B 17  .........s002*..
0480: E0 00 01 2A 0B 18 E0 00  01 9F 1B 80 17 E0 00 01  ...*............
0490: 17 E0 00 01 6B 69 6C 6C  01 80 9F 1B 80 18 E0 00  ....kill........
04A0: 01 18 E0 00 01 6B 69 6C  6C 01 80 4E 01 17 E0 00  .....kill..N....
04B0: 01 4E 01 18 E0 00 01 29  0B 17 E0 00 01 02 29 0B  .N.....)......).
04C0: 18 E0 00 01 02 2A 0B F0  FF FF 7F 29 0B 06 E0 00  .....*.....)....
04D0: 01 02 4E 00 F0 FF FF 7F  46 00 02 06 10 0C 80 00  ..N.....F.......
04E0: F3 04 45 00 80 F0 FF FF  7F F0 FF FF 7F 66 64 69  ..E..........fdi
04F0: 31 01 80 20 00 21 00                              1.. .!.         
```

#### Opcodes

```
  0: 0x024A [0x20] SET_CLI_EVENT_UC_FLAG: Lock player control
  1: 0x024C [0x42] SET_CLI_EVENT_CANCEL_DATA()
  2: 0x024D [0x46] CAMERA_CONTROL: Disable user control
  3: 0x024F [0x29] REQ_SET_WAIT(priority=0x0B, entity_id=Large Apparatus (ID: 16834569/0x0100E009), tag_num=0x02)
  4: 0x0256 [0x29] REQ_SET_WAIT(priority=0x08, entity_id=LocalPlayer, tag_num=0x04)
  5: 0x025D [0x27] REQ_SET(priority=0x0B, entity_id=LocalPlayer, tag_num=0x07)
  6: 0x0264 [0x1C] WAIT(180* ticks)
  7: 0x0267 [0x2A] GET_REQ_LEVEL(level=11, entity_id=LocalPlayer)
  8: 0x026D [0x4A] LocalPlayer looks at Cermet Gate (ID: 16834566/0x0100E006)
  9: 0x0276 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "se49" with entities [EventEntity, EventEntity], work=[118*, 0*]
 10: 0x0287 [0x29] REQ_SET_WAIT(priority=0x0B, entity_id=Cermet Gate (ID: 16834566/0x0100E006), tag_num=0x07)
 11: 0x028E [0x1C] WAIT(30* ticks)
 12: 0x0291 [0x52] END_LOAD_SCHEDULER: End scheduler "z14b" with entities [EventEntity, EventEntity], work=94*
 13: 0x02A0 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "ovl1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 14: 0x02B1 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "s138" with entities [EventEntity, EventEntity], work=[118*, 0*]
 15: 0x02C2 [0x1C] WAIT(40* ticks)
 16: 0x02C5 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 17: 0x02D6 [0x1C] WAIT(60* ticks)
 18: 0x02D9 [0x29] REQ_SET_WAIT(priority=0x0B, entity_id=??? (ID: 16834583/0x0100E017), tag_num=0x04)
 19: 0x02E0 [0x29] REQ_SET_WAIT(priority=0x0B, entity_id=??? (ID: 16834584/0x0100E018), tag_num=0x04)
 20: 0x02E7 [0x4E] SET_ENTITY_HIDE_FLAG: Show ??? (ID: 16834583/0x0100E017)
 21: 0x02ED [0x4E] SET_ENTITY_HIDE_FLAG: Show ??? (ID: 16834584/0x0100E018)
 22: 0x02F3 [0x80] LOAD_WAIT(entity=??? (ID: 16834583/0x0100E017))
 23: 0x02F8 [0x80] LOAD_WAIT(entity=??? (ID: 16834584/0x0100E018))
 24: 0x02FD [0x52] END_LOAD_SCHEDULER: End scheduler "s138" with entities [EventEntity, EventEntity], work=118*
 25: 0x030C [0x45] LOAD_SCHEDULED_TASK: Load scheduler "se80" with entities [EventEntity, EventEntity], work=[118*, 0*]
 26: 0x031D [0x27] REQ_SET(priority=0x0B, entity_id=??? (ID: 16834583/0x0100E017), tag_num=0x01)
 27: 0x0324 [0x27] REQ_SET(priority=0x0B, entity_id=??? (ID: 16834584/0x0100E018), tag_num=0x01)
 28: 0x032B [0x1C] WAIT(70* ticks)
 29: 0x032E [0x52] END_LOAD_SCHEDULER: End scheduler "z14b" with entities [EventEntity, EventEntity], work=94*
 30: 0x033D [0x45] LOAD_SCHEDULED_TASK: Load scheduler "s000" with entities [EventEntity, EventEntity], work=[118*, 0*]
 31: 0x034E [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 32: 0x035F [0x45] LOAD_SCHEDULED_TASK: Load scheduler "se81" with entities [EventEntity, EventEntity], work=[118*, 0*]
 33: 0x0370 [0x1C] WAIT(70* ticks)
 34: 0x0373 [0x52] END_LOAD_SCHEDULER: End scheduler "s000" with entities [EventEntity, EventEntity], work=118*
 35: 0x0382 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "s001" with entities [EventEntity, EventEntity], work=[118*, 0*]
 36: 0x0393 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "se82" with entities [EventEntity, EventEntity], work=[118*, 0*]
 37: 0x03A4 [0x2B] ??? (ID: 16834584/0x0100E018) [7297*]:
    → "Nooo!!!"
 38: 0x03AB [0x23] WAIT_FOR_DIALOG_INTERACTION
 39: 0x03AC [0x1C] WAIT(100* ticks)
 40: 0x03AF [0x2B] ??? (ID: 16834583/0x0100E017) [7296*]:
    → "Wha...? Aaagghh!"
 41: 0x03B6 [0x23] WAIT_FOR_DIALOG_INTERACTION
 42: 0x03B7 [0x1C] WAIT(120* ticks)
 43: 0x03BA [0x29] REQ_SET_WAIT(priority=0x0B, entity_id=Cermet Gate (ID: 16834566/0x0100E006), tag_num=0x08)
 44: 0x03C1 [0x1C] WAIT(10* ticks)
 45: 0x03C4 [0x27] REQ_SET(priority=0x0B, entity_id=LocalPlayer, tag_num=0x08)
 46: 0x03CB [0x52] END_LOAD_SCHEDULER: End scheduler "s001" with entities [EventEntity, EventEntity], work=118*
 47: 0x03DA [0x02] IF !(Work_Zone[9] == 5*) GOTO 0x03F6
 48: 0x03E2 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "s003" with entities [EventEntity, EventEntity], work=[118*, 0*]
 49: 0x03F3 [0x01] GOTO 0x0423
 50: 0x03F6 [0x02] IF !(Work_Zone[9] == 6*) GOTO 0x0412
 51: 0x03FE [0x45] LOAD_SCHEDULED_TASK: Load scheduler "s003" with entities [EventEntity, EventEntity], work=[118*, 0*]
 52: 0x040F [0x01] GOTO 0x0423
 53: 0x0412 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "s002" with entities [EventEntity, EventEntity], work=[118*, 0*]

SUBROUTINE_0423:
 54: 0x0423 [0x1C] WAIT(120* ticks)
 55: 0x0426 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 56: 0x0437 [0x1C] WAIT(60* ticks)
 57: 0x043A [0x02] IF !(Work_Zone[9] == 5*) GOTO 0x0454
 58: 0x0442 [0x52] END_LOAD_SCHEDULER: End scheduler "s003" with entities [EventEntity, EventEntity], work=118*
 59: 0x0451 [0x01] GOTO 0x047D
 60: 0x0454 [0x02] IF !(Work_Zone[9] == 6*) GOTO 0x046E
 61: 0x045C [0x52] END_LOAD_SCHEDULER: End scheduler "s003" with entities [EventEntity, EventEntity], work=118*
 62: 0x046B [0x01] GOTO 0x047D
 63: 0x046E [0x52] END_LOAD_SCHEDULER: End scheduler "s002" with entities [EventEntity, EventEntity], work=118*

SUBROUTINE_047D:
 64: 0x047D [0x2A] GET_REQ_LEVEL(level=11, entity_id=??? (ID: 16834583/0x0100E017))
 65: 0x0483 [0x2A] GET_REQ_LEVEL(level=11, entity_id=??? (ID: 16834584/0x0100E018))
 66: 0x0489 [0x9F] LOAD_SCHEDULED_TASK_ALT: Load scheduler "kill" with entities [??? (ID: 16834583/0x0100E017), ??? (ID: 16834583/0x0100E017)], work=[57*, 0*]
 67: 0x049A [0x9F] LOAD_SCHEDULED_TASK_ALT: Load scheduler "kill" with entities [??? (ID: 16834584/0x0100E018), ??? (ID: 16834584/0x0100E018)], work=[57*, 0*]
 68: 0x04AB [0x4E] SET_ENTITY_HIDE_FLAG: Hide ??? (ID: 16834583/0x0100E017)
 69: 0x04B1 [0x4E] SET_ENTITY_HIDE_FLAG: Hide ??? (ID: 16834584/0x0100E018)
 70: 0x04B7 [0x29] REQ_SET_WAIT(priority=0x0B, entity_id=??? (ID: 16834583/0x0100E017), tag_num=0x02)
 71: 0x04BE [0x29] REQ_SET_WAIT(priority=0x0B, entity_id=??? (ID: 16834584/0x0100E018), tag_num=0x02)
 72: 0x04C5 [0x2A] GET_REQ_LEVEL(level=11, entity_id=LocalPlayer)
 73: 0x04CB [0x29] REQ_SET_WAIT(priority=0x0B, entity_id=Cermet Gate (ID: 16834566/0x0100E006), tag_num=0x02)
 74: 0x04D2 [0x4E] SET_ENTITY_HIDE_FLAG: Show LocalPlayer
 75: 0x04D8 [0x46] CAMERA_CONTROL: Restore default settings
 76: 0x04DA [0x02] IF !(Work_Zone[6] == 1*) GOTO 0x04F3
 77: 0x04E2 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 78: 0x04F3 [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
 79: 0x04F5 [0x21] END_EVENT
 80: 0x04F6 [0x00] END_REQSTACK()
```
