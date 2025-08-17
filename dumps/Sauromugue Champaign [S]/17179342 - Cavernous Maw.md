# 17179342 - Cavernous Maw

## Common Data

| Field            | Value                             |
|------------------|-----------------------------------|
| Zone             | Sauromugue Champaign [S] (ID: 98) |
| Block Size       | 584 bytes                         |
| Total Events     | 13                                |
| References Count | 14                                |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [101](#event-101)        | 0x0001       |    221 |             33 |
| [102](#event-102)        | 0x00DE       |    218 |             32 |
| [700](#event-700)        | 0x01B8       |      1 |              1 |
| [701](#event-701)        | 0x01B9       |      1 |              1 |
| [265](#event-265)        | 0x01BA       |      1 |              1 |
| [65535.1](#event-655351) | 0x01BB       |      5 |              2 |
| [65535.2](#event-655352) | 0x01C0       |      5 |              2 |
| [702](#event-702)        | 0x01C5       |      1 |              1 |
| [703](#event-703)        | 0x01C6       |      1 |              1 |
| [31](#event-31)          | 0x01C7       |      1 |              1 |
| [32](#event-32)          | 0x01C8       |      1 |              1 |
| [33](#event-33)          | 0x01C9       |      1 |              1 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x1B9D      |        7069 |
|       1 | 0x038E      |         910 |
|       2 | 0x1BA0      |        7072 |
|       3 | 0x0001      |           1 |
|       4 | 0x0000      |           0 |
|       5 | 0x00C8      |         200 |
|       6 | 0x003C      |          60 |
|       7 | 0x0013      |          19 |
|       8 | 0x0155      |         341 |
|       9 | 0x1B9F      |        7071 |
|      10 | 0x00C9      |         201 |
|      11 | 0x1B9E      |        7070 |
|      12 | 0x0914      |        2324 |
|      13 | 0x0915      |        2325 |

## String References

- **7069**: You can feel the warm, moist breath of the maw on your skin.
- **7070**: An unseen force is drawing you towards the maw.
- **7071**: A portal has opened within the depths of the maw.
- **7072**: Raise your $3? [Yes./No.]

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

### Event 101

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x0001    |
| Data Size    | 221 bytes |
| Instructions | 33        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    20 01 48 00 80 23 03  02 10 01 80 24 02 80 03    .H..#.....$...
0010: 80 04 80 25 02 00 10 04  80 00 CF 00 43 00 43 01  ...%........C.C.
0020: 42 46 01 03 01 10 03 80  45 05 80 F0 FF FF 7F F0  BF......E.......
0030: FF FF 7F 66 64 6F 31 04  80 1C 06 80 38 07 80 29  ...fdo1.....8..)
0040: 01 F0 FF FF 7F 04 45 08  80 F0 FF FF 7F F0 FF FF  ......E.........
0050: 7F 61 74 31 38 04 80 45  05 80 F0 FF FF 7F F0 FF  .at18..E........
0060: FF 7F 66 64 69 31 04 80  48 09 80 1C 06 80 45 05  ..fdi1..H.....E.
0070: 80 F0 FF FF 7F F0 FF FF  7F 62 6C 6F 6E 04 80 45  .........blon..E
0080: 0A 80 F0 FF FF 7F F0 FF  FF 7F 62 6C 6F 6E 04 80  ..........blon..
0090: 45 05 80 F0 FF FF 7F F0  FF FF 7F 6F 76 6C 31 04  E..........ovl1.
00A0: 80 45 08 80 F0 FF FF 7F  F0 FF FF 7F 77 61 72 70  .E..........warp
00B0: 04 80 29 01 F0 FF FF 7F  05 45 05 80 F0 FF FF 7F  ..)......E......
00C0: F0 FF FF 7F 62 6C 6F 66  04 80 46 00 01 DA 00 02  ....blof..F.....
00D0: 00 10 03 80 00 DA 00 01  DA 00 20 00 21 00        .......... .!.  
```

#### Opcodes

```
  0: 0x0001 [0x20] SET_CLI_EVENT_UC_FLAG: Lock player control
  1: 0x0003 [0x48] [System] [7069*]:
    → "You can feel the warm, moist breath of the maw on your skin."
  2: 0x0006 [0x23] WAIT_FOR_DIALOG_INTERACTION
  3: 0x0007 [0x03] Work_Zone[2] = 910*
  4: 0x000C [0x24] CREATE_DIALOG(message_id=7072*, default_option=1*, option_flags=0*)
    → "Raise your $3? [Yes./No.]"
  5: 0x0013 [0x25] WAIT_DIALOG_SELECT()
  6: 0x0014 [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x00CF
  7: 0x001C [0x43] SEND_EVENT_UPDATE: Send pending tag to server (packet 0x005B)
  8: 0x001E [0x43] SEND_EVENT_UPDATE: Check pending flag (skip if not pending)
  9: 0x0020 [0x42] SET_CLI_EVENT_CANCEL_DATA()
 10: 0x0021 [0x46] CAMERA_CONTROL: Disable user control
 11: 0x0023 [0x03] Work_Zone[1] = 1*
 12: 0x0028 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 13: 0x0039 [0x1C] WAIT(60* ticks)
 14: 0x003C [0x38] SET_CLIENT_EVENT_MODE(mode=19*)
 15: 0x003F [0x29] REQ_SET_WAIT(priority=0x01, entity_id=LocalPlayer, tag_num=0x04)
 16: 0x0046 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "at18" with entities [LocalPlayer, LocalPlayer], work=[341*, 0*]
 17: 0x0057 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 18: 0x0068 [0x48] [System] [7071*]:
    → "A portal has opened within the depths of the maw."
 19: 0x006B [0x1C] WAIT(60* ticks)
 20: 0x006E [0x45] LOAD_SCHEDULED_TASK: Load scheduler "blon" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 21: 0x007F [0x45] LOAD_SCHEDULED_TASK: Load scheduler "blon" with entities [LocalPlayer, LocalPlayer], work=[201*, 0*]
 22: 0x0090 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "ovl1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 23: 0x00A1 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "warp" with entities [LocalPlayer, LocalPlayer], work=[341*, 0*]
 24: 0x00B2 [0x29] REQ_SET_WAIT(priority=0x01, entity_id=LocalPlayer, tag_num=0x05)
 25: 0x00B9 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "blof" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 26: 0x00CA [0x46] CAMERA_CONTROL: Restore default settings
 27: 0x00CC [0x01] GOTO 0x00DA
 28: 0x00CF [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x00DA
 29: 0x00D7 [0x01] GOTO 0x00DA

SUBROUTINE_00DA:
 30: 0x00DA [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
 31: 0x00DC [0x21] END_EVENT
 32: 0x00DD [0x00] END_REQSTACK()
```

### Event 102

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x00DE    |
| Data Size    | 218 bytes |
| Instructions | 32        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00D0:                                            20 01                 .
00E0: 48 0B 80 23 03 02 10 01  80 24 02 80 03 80 04 80  H..#.....$......
00F0: 25 02 00 10 04 80 00 A9  01 43 00 43 01 42 46 01  %........C.C.BF.
0100: 03 01 10 03 80 45 05 80  F0 FF FF 7F F0 FF FF 7F  .....E..........
0110: 66 64 6F 31 04 80 1C 06  80 38 07 80 29 01 F0 FF  fdo1.....8..)...
0120: FF 7F 04 45 08 80 F0 FF  FF 7F F0 FF FF 7F 61 74  ...E..........at
0130: 31 38 04 80 45 05 80 F0  FF FF 7F F0 FF FF 7F 66  18..E..........f
0140: 64 69 31 04 80 1C 06 80  45 05 80 F0 FF FF 7F F0  di1.....E.......
0150: FF FF 7F 62 6C 6F 6E 04  80 45 0A 80 F0 FF FF 7F  ...blon..E......
0160: F0 FF FF 7F 62 6C 6F 6E  04 80 45 05 80 F0 FF FF  ....blon..E.....
0170: 7F F0 FF FF 7F 6F 76 6C  31 04 80 45 08 80 F0 FF  .....ovl1..E....
0180: FF 7F F0 FF FF 7F 77 61  72 70 04 80 29 01 F0 FF  ......warp..)...
0190: FF 7F 05 45 05 80 F0 FF  FF 7F F0 FF FF 7F 62 6C  ...E..........bl
01A0: 6F 66 04 80 46 00 01 B4  01 02 00 10 03 80 00 B4  of..F...........
01B0: 01 01 B4 01 20 00 21 00                           .... .!.        
```

#### Opcodes

```
  0: 0x00DE [0x20] SET_CLI_EVENT_UC_FLAG: Lock player control
  1: 0x00E0 [0x48] [System] [7070*]:
    → "An unseen force is drawing you towards the maw."
  2: 0x00E3 [0x23] WAIT_FOR_DIALOG_INTERACTION
  3: 0x00E4 [0x03] Work_Zone[2] = 910*
  4: 0x00E9 [0x24] CREATE_DIALOG(message_id=7072*, default_option=1*, option_flags=0*)
    → "Raise your $3? [Yes./No.]"
  5: 0x00F0 [0x25] WAIT_DIALOG_SELECT()
  6: 0x00F1 [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x01A9
  7: 0x00F9 [0x43] SEND_EVENT_UPDATE: Send pending tag to server (packet 0x005B)
  8: 0x00FB [0x43] SEND_EVENT_UPDATE: Check pending flag (skip if not pending)
  9: 0x00FD [0x42] SET_CLI_EVENT_CANCEL_DATA()
 10: 0x00FE [0x46] CAMERA_CONTROL: Disable user control
 11: 0x0100 [0x03] Work_Zone[1] = 1*
 12: 0x0105 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 13: 0x0116 [0x1C] WAIT(60* ticks)
 14: 0x0119 [0x38] SET_CLIENT_EVENT_MODE(mode=19*)
 15: 0x011C [0x29] REQ_SET_WAIT(priority=0x01, entity_id=LocalPlayer, tag_num=0x04)
 16: 0x0123 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "at18" with entities [LocalPlayer, LocalPlayer], work=[341*, 0*]
 17: 0x0134 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 18: 0x0145 [0x1C] WAIT(60* ticks)
 19: 0x0148 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "blon" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 20: 0x0159 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "blon" with entities [LocalPlayer, LocalPlayer], work=[201*, 0*]
 21: 0x016A [0x45] LOAD_SCHEDULED_TASK: Load scheduler "ovl1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 22: 0x017B [0x45] LOAD_SCHEDULED_TASK: Load scheduler "warp" with entities [LocalPlayer, LocalPlayer], work=[341*, 0*]
 23: 0x018C [0x29] REQ_SET_WAIT(priority=0x01, entity_id=LocalPlayer, tag_num=0x05)
 24: 0x0193 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "blof" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 25: 0x01A4 [0x46] CAMERA_CONTROL: Restore default settings
 26: 0x01A6 [0x01] GOTO 0x01B4
 27: 0x01A9 [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x01B4
 28: 0x01B1 [0x01] GOTO 0x01B4

SUBROUTINE_01B4:
 29: 0x01B4 [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
 30: 0x01B6 [0x21] END_EVENT
 31: 0x01B7 [0x00] END_REQSTACK()
```

### Event 700

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x01B8  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
01B0:                          00                               .       
```

#### Opcodes

```
  0: 0x01B8 [0x00] END_REQSTACK()
```

### Event 701

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x01B9  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
01B0:                             00                             .      
```

#### Opcodes

```
  0: 0x01B9 [0x00] END_REQSTACK()
```

### Event 265

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x01BA  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
01B0:                                00                           .     
```

#### Opcodes

```
  0: 0x01BA [0x00] END_REQSTACK()
```

### Event 65535.1

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x01BB  |
| Data Size    | 5 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
01B0:                                   B6 00 0C 80 00             .....
```

#### Opcodes

```
  0: 0x01BB [0xB6] ENTITY_APPEARANCE_HANDLER(case=Hair style, value=2324*)
  1: 0x01BF [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x01C0  |
| Data Size    | 5 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
01C0: B6 00 0D 80 00                                    .....           
```

#### Opcodes

```
  0: 0x01C0 [0xB6] ENTITY_APPEARANCE_HANDLER(case=Hair style, value=2325*)
  1: 0x01C4 [0x00] END_REQSTACK()
```

### Event 702

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x01C5  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
01C0:                00                                      .          
```

#### Opcodes

```
  0: 0x01C5 [0x00] END_REQSTACK()
```

### Event 703

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x01C6  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
01C0:                   00                                    .         
```

#### Opcodes

```
  0: 0x01C6 [0x00] END_REQSTACK()
```

### Event 31

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x01C7  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
01C0:                      00                                  .        
```

#### Opcodes

```
  0: 0x01C7 [0x00] END_REQSTACK()
```

### Event 32

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x01C8  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
01C0:                          00                               .       
```

#### Opcodes

```
  0: 0x01C8 [0x00] END_REQSTACK()
```

### Event 33

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x01C9  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
01C0:                             00                             .      
```

#### Opcodes

```
  0: 0x01C9 [0x00] END_REQSTACK()
```
