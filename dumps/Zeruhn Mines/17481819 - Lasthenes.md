# 17481819 - Lasthenes

## Common Data

| Field            | Value                  |
|------------------|------------------------|
| Zone             | Zeruhn Mines (ID: 172) |
| Block Size       | 532 bytes              |
| Total Events     | 8                      |
| References Count | 18                     |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [103](#event-103)        | 0x0001       |     11 |              5 |
| [180](#event-180)        | 0x000C       |    185 |             34 |
| [181](#event-181)        | 0x00C5       |    177 |             30 |
| [204](#event-204)        | 0x0176       |      1 |              1 |
| [65535.1](#event-655351) | 0x0177       |     32 |              6 |
| [228](#event-228)        | 0x0197       |      1 |              1 |
| [225](#event-225)        | 0x0198       |      1 |              1 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x1C9F      |        7327 |
|       1 | 0x1CA0      |        7328 |
|       2 | 0x1CA1      |        7329 |
|       3 | 0x0001      |           1 |
|       4 | 0x0000      |           0 |
|       5 | 0x00C8      |         200 |
|       6 | 0x003C      |          60 |
|       7 | 0x0012      |          18 |
|       8 | 0x00D9      |         217 |
|       9 | 0x0078      |         120 |
|      10 | 0x00B4      |         180 |
|      11 | 0x0028      |          40 |
|      12 | 0xFFFEF616  |  4294899222 |
|      13 | 0x1067B     |       67195 |
|      14 | 0x04E2      |        1250 |
|      15 | 0xFFFF018A  |  4294902154 |
|      16 | 0xCD35      |       52533 |
|      17 | 0x0004      |           4 |

## String References

- **7327**: Not anyone can go in there--the Korroloka Tunnel has been closed for over a hundred years.
- **7328**: However, permission to pass has been granted to adventurers who have proven their worth. Adventurers such as yourself.
- **7329**: Would you like to enter? [Let me through./Not this time.]

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

### Event 103

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 11 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    1E F0 FF FF 7F 1D 00  80 23 21 00               ........#!.    
```

#### Opcodes

```
  0: 0x0001 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0006 [0x1D] PRINT_EVENT_MESSAGE(message_id=7327*)
    → "Not anyone can go in there--the Korroloka Tunnel has been closed for over a hundred years."
  2: 0x0009 [0x23] WAIT_FOR_DIALOG_INTERACTION
  3: 0x000A [0x21] END_EVENT
  4: 0x000B [0x00] END_REQSTACK()
```

### Event 180

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x000C    |
| Data Size    | 185 bytes |
| Instructions | 34        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                                      20 01 42 1E               .B.
0010: F0 FF FF 7F 1D 00 80 23  1D 01 80 23 24 02 80 03  .......#...#$...
0020: 80 04 80 25 02 00 10 04  80 00 C1 00 43 00 43 01  ...%........C.C.
0030: 46 01 45 05 80 F0 FF FF  7F F0 FF FF 7F 66 64 6F  F.E..........fdo
0040: 31 04 80 1C 06 80 38 07  80 45 08 80 F0 FF FF 7F  1.....8..E......
0050: F0 FF FF 7F 63 33 69 6E  04 80 29 01 F0 FF FF 7F  ....c3in..).....
0060: 06 29 01 F0 FF FF 7F 07  45 05 80 F0 FF FF 7F F0  .)......E.......
0070: FF FF 7F 66 64 69 31 04  80 29 01 69 C0 0A 01 03  ...fdi1..).i....
0080: 1C 09 80 27 01 F0 FF FF  7F 08 1C 0A 80 29 01 69  ...'.........).i
0090: C0 0A 01 04 1C 06 80 45  05 80 F0 FF FF 7F F0 FF  .......E........
00A0: FF 7F 66 64 6F 31 04 80  1C 06 80 46 00 45 05 80  ..fdo1.....F.E..
00B0: F0 FF FF 7F F0 FF FF 7F  66 64 69 31 04 80 01 C1  ........fdi1....
00C0: 00 20 00 21 00                                    . .!.           
```

#### Opcodes

```
  0: 0x000C [0x20] SET_CLI_EVENT_UC_FLAG: Lock player control
  1: 0x000E [0x42] SET_CLI_EVENT_CANCEL_DATA()
  2: 0x000F [0x1E] EventEntity looks at LocalPlayer and starts talking
  3: 0x0014 [0x1D] PRINT_EVENT_MESSAGE(message_id=7327*)
    → "Not anyone can go in there--the Korroloka Tunnel has been closed for over a hundred years."
  4: 0x0017 [0x23] WAIT_FOR_DIALOG_INTERACTION
  5: 0x0018 [0x1D] PRINT_EVENT_MESSAGE(message_id=7328*)
    → "However, permission to pass has been granted to adventurers who have proven their worth. Adventurers such as yourself."
  6: 0x001B [0x23] WAIT_FOR_DIALOG_INTERACTION
  7: 0x001C [0x24] CREATE_DIALOG(message_id=7329*, default_option=1*, option_flags=0*)
    → "Would you like to enter? [Let me through./Not this time.]"
  8: 0x0023 [0x25] WAIT_DIALOG_SELECT()
  9: 0x0024 [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x00C1
 10: 0x002C [0x43] SEND_EVENT_UPDATE: Send pending tag to server (packet 0x005B)
 11: 0x002E [0x43] SEND_EVENT_UPDATE: Check pending flag (skip if not pending)
 12: 0x0030 [0x46] CAMERA_CONTROL: Disable user control
 13: 0x0032 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 14: 0x0043 [0x1C] WAIT(60* ticks)
 15: 0x0046 [0x38] SET_CLIENT_EVENT_MODE(mode=18*)
 16: 0x0049 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "c3in" with entities [LocalPlayer, LocalPlayer], work=[217*, 0*]
 17: 0x005A [0x29] REQ_SET_WAIT(priority=0x01, entity_id=LocalPlayer, tag_num=0x06)
 18: 0x0061 [0x29] REQ_SET_WAIT(priority=0x01, entity_id=LocalPlayer, tag_num=0x07)
 19: 0x0068 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 20: 0x0079 [0x29] REQ_SET_WAIT(priority=0x01, entity_id=Korroloka Tunnel (ID: 17481833/0x010AC069), tag_num=0x03)
 21: 0x0080 [0x1C] WAIT(120* ticks)
 22: 0x0083 [0x27] REQ_SET(priority=0x01, entity_id=LocalPlayer, tag_num=0x08)
 23: 0x008A [0x1C] WAIT(180* ticks)
 24: 0x008D [0x29] REQ_SET_WAIT(priority=0x01, entity_id=Korroloka Tunnel (ID: 17481833/0x010AC069), tag_num=0x04)
 25: 0x0094 [0x1C] WAIT(60* ticks)
 26: 0x0097 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 27: 0x00A8 [0x1C] WAIT(60* ticks)
 28: 0x00AB [0x46] CAMERA_CONTROL: Restore default settings
 29: 0x00AD [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 30: 0x00BE [0x01] GOTO 0x00C1

SUBROUTINE_00C1:
 31: 0x00C1 [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
 32: 0x00C3 [0x21] END_EVENT
 33: 0x00C4 [0x00] END_REQSTACK()
```

### Event 181

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x00C5    |
| Data Size    | 177 bytes |
| Instructions | 30        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00C0:                20 01 42  1E F0 FF FF 7F 24 02 80        .B.....$..
00D0: 03 80 04 80 25 02 00 10  04 80 00 72 01 43 00 43  ....%......r.C.C
00E0: 01 46 01 45 05 80 F0 FF  FF 7F F0 FF FF 7F 66 64  .F.E..........fd
00F0: 6F 31 04 80 1C 06 80 38  07 80 45 08 80 F0 FF FF  o1.....8..E.....
0100: 7F F0 FF FF 7F 63 33 6F  75 04 80 29 01 F0 FF FF  .....c3ou..)....
0110: 7F 09 29 01 F0 FF FF 7F  0A 45 05 80 F0 FF FF 7F  ..)......E......
0120: F0 FF FF 7F 66 64 69 31  04 80 29 01 69 C0 0A 01  ....fdi1..).i...
0130: 03 1C 09 80 27 01 F0 FF  FF 7F 0B 1C 0A 80 29 01  ....'.........).
0140: 69 C0 0A 01 04 1C 06 80  45 05 80 F0 FF FF 7F F0  i.......E.......
0150: FF FF 7F 66 64 6F 31 04  80 1C 06 80 46 00 45 05  ...fdo1.....F.E.
0160: 80 F0 FF FF 7F F0 FF FF  7F 66 64 69 31 04 80 01  .........fdi1...
0170: 72 01 20 00 21 00                                 r. .!.          
```

#### Opcodes

```
  0: 0x00C5 [0x20] SET_CLI_EVENT_UC_FLAG: Lock player control
  1: 0x00C7 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  2: 0x00C8 [0x1E] EventEntity looks at LocalPlayer and starts talking
  3: 0x00CD [0x24] CREATE_DIALOG(message_id=7329*, default_option=1*, option_flags=0*)
    → "Would you like to enter? [Let me through./Not this time.]"
  4: 0x00D4 [0x25] WAIT_DIALOG_SELECT()
  5: 0x00D5 [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x0172
  6: 0x00DD [0x43] SEND_EVENT_UPDATE: Send pending tag to server (packet 0x005B)
  7: 0x00DF [0x43] SEND_EVENT_UPDATE: Check pending flag (skip if not pending)
  8: 0x00E1 [0x46] CAMERA_CONTROL: Disable user control
  9: 0x00E3 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 10: 0x00F4 [0x1C] WAIT(60* ticks)
 11: 0x00F7 [0x38] SET_CLIENT_EVENT_MODE(mode=18*)
 12: 0x00FA [0x45] LOAD_SCHEDULED_TASK: Load scheduler "c3ou" with entities [LocalPlayer, LocalPlayer], work=[217*, 0*]
 13: 0x010B [0x29] REQ_SET_WAIT(priority=0x01, entity_id=LocalPlayer, tag_num=0x09)
 14: 0x0112 [0x29] REQ_SET_WAIT(priority=0x01, entity_id=LocalPlayer, tag_num=0x0A)
 15: 0x0119 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 16: 0x012A [0x29] REQ_SET_WAIT(priority=0x01, entity_id=Korroloka Tunnel (ID: 17481833/0x010AC069), tag_num=0x03)
 17: 0x0131 [0x1C] WAIT(120* ticks)
 18: 0x0134 [0x27] REQ_SET(priority=0x01, entity_id=LocalPlayer, tag_num=0x0B)
 19: 0x013B [0x1C] WAIT(180* ticks)
 20: 0x013E [0x29] REQ_SET_WAIT(priority=0x01, entity_id=Korroloka Tunnel (ID: 17481833/0x010AC069), tag_num=0x04)
 21: 0x0145 [0x1C] WAIT(60* ticks)
 22: 0x0148 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 23: 0x0159 [0x1C] WAIT(60* ticks)
 24: 0x015C [0x46] CAMERA_CONTROL: Restore default settings
 25: 0x015E [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 26: 0x016F [0x01] GOTO 0x0172

SUBROUTINE_0172:
 27: 0x0172 [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
 28: 0x0174 [0x21] END_EVENT
 29: 0x0175 [0x00] END_REQSTACK()
```

### Event 204

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0176  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0170:                   00                                    .         
```

#### Opcodes

```
  0: 0x0176 [0x00] END_REQSTACK()
```

### Event 65535.1

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0177   |
| Data Size    | 32 bytes |
| Instructions | 6        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0170:                      32  0B 80 37 0C 80 0D 80 04         2..7.....
0180: 80 0E 80 1F 00 0F 80 10  80 11 80 1F 01 4A 5D C0  .............J].
0190: 0A 01 F8 FF FF 7F 00                              .......         
```

#### Opcodes

```
  0: 0x0177 [0x32] ExtData[1]->MainSpeed = 40* * 0.1
  1: 0x017A [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=-68.074*, z=67.195*, y=0.000*, direction=109.9°*
  2: 0x0183 [0x1F] MOVE_ENTITY: EventEntity moves to X=-65.142*, Z=52.533*, Y=0.004*
  3: 0x018B [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  4: 0x018D [0x4A] Rasmus (ID: 17481821/0x010AC05D) looks at EventEntity
  5: 0x0196 [0x00] END_REQSTACK()
```

### Event 228

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0197  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0190:                      00                                  .        
```

#### Opcodes

```
  0: 0x0197 [0x00] END_REQSTACK()
```

### Event 225

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0198  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0190:                          00                               .       
```

#### Opcodes

```
  0: 0x0198 [0x00] END_REQSTACK()
```
