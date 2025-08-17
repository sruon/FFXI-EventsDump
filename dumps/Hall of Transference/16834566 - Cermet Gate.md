# 16834566 - Cermet Gate

## Common Data

| Field            | Value                         |
|------------------|-------------------------------|
| Zone             | Hall of Transference (ID: 14) |
| Block Size       | 564 bytes                     |
| Total Events     | 10                            |
| References Count | 11                            |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [150](#event-150)        | 0x0001       |    262 |             34 |
| [65535.1](#event-655351) | 0x0107       |    189 |             17 |
| [151](#event-151)        | 0x01C4       |      1 |              1 |
| [152](#event-152)        | 0x01C5       |      1 |              1 |
| [153](#event-153)        | 0x01C6       |      2 |              2 |
| [154](#event-154)        | 0x01C8       |      2 |              2 |
| [65535.2](#event-655352) | 0x01CA       |      2 |              2 |
| [65535.3](#event-655353) | 0x01CC       |      2 |              2 |
| [160](#event-160)        | 0x01CE       |      1 |              1 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x1B9E      |        7070 |
|       1 | 0x0001      |           1 |
|       2 | 0x0000      |           0 |
|       3 | 0x00C8      |         200 |
|       4 | 0x0078      |         120 |
|       5 | 0x0013      |          19 |
|       6 | 0x00A0      |         160 |
|       7 | 0x003C      |          60 |
|       8 | 0x01E0      |         480 |
|       9 | 0x00C9      |         201 |
|      10 | 0x00B4      |         180 |

## String References

- **7070**: Proceed onward? [Yes./No.]

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

### Event 150

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x0001    |
| Data Size    | 262 bytes |
| Instructions | 34        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    20 01 24 00 80 01 80  02 80 25 02 00 10 02 80    .$......%.....
0010: 00 F3 00 42 46 01 45 03  80 F0 FF FF 7F F0 FF FF  ...BF.E.........
0020: 7F 66 64 6F 31 02 80 1C  04 80 38 05 80 29 01 F0  .fdo1.....8..)..
0030: FF FF 7F 0A 45 06 80 F8  FF FF 7F F8 FF FF 7F 7A  ....E..........z
0040: 31 34 66 02 80 45 03 80  F0 FF FF 7F F0 FF FF 7F  14f..E..........
0050: 66 64 69 31 02 80 1C 07  80 2D F8 FF FF 7F F8 FF  fdi1.....-......
0060: FF 7F 67 74 65 32 1C 08  80 27 01 06 E0 00 01 05  ..gte2...'......
0070: 52 06 80 F8 FF FF 7F F8  FF FF 7F 7A 31 34 66 45  R..........z14fE
0080: 03 80 F0 FF FF 7F F0 FF  FF 7F 62 6C 6F 6E 02 80  ..........blon..
0090: 45 09 80 F0 FF FF 7F F0  FF FF 7F 62 6C 6F 6E 02  E..........blon.
00A0: 80 45 06 80 F8 FF FF 7F  F8 FF FF 7F 7A 31 34 67  .E..........z14g
00B0: 02 80 1C 0A 80 45 03 80  F0 FF FF 7F F0 FF FF 7F  .....E..........
00C0: 66 64 6F 31 02 80 1C 07  80 52 06 80 F8 FF FF 7F  fdo1.....R......
00D0: F8 FF FF 7F 7A 31 34 67  45 03 80 F0 FF FF 7F F0  ....z14gE.......
00E0: FF FF 7F 62 6C 6F 66 02  80 03 01 10 01 80 46 00  ...blof.......F.
00F0: 01 03 01 02 00 10 01 80  00 03 01 03 01 10 02 80  ................
0100: 01 03 01 20 00 21 00                              ... .!.         
```

#### Opcodes

```
  0: 0x0001 [0x20] SET_CLI_EVENT_UC_FLAG: Lock player control
  1: 0x0003 [0x24] CREATE_DIALOG(message_id=7070*, default_option=1*, option_flags=0*)
    → "Proceed onward? [Yes./No.]"
  2: 0x000A [0x25] WAIT_DIALOG_SELECT()
  3: 0x000B [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x00F3
  4: 0x0013 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  5: 0x0014 [0x46] CAMERA_CONTROL: Disable user control
  6: 0x0016 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
  7: 0x0027 [0x1C] WAIT(120* ticks)
  8: 0x002A [0x38] SET_CLIENT_EVENT_MODE(mode=19*)
  9: 0x002D [0x29] REQ_SET_WAIT(priority=0x01, entity_id=LocalPlayer, tag_num=0x0A)
 10: 0x0034 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "z14f" with entities [EventEntity, EventEntity], work=[160*, 0*]
 11: 0x0045 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 12: 0x0056 [0x1C] WAIT(60* ticks)
 13: 0x0059 [0x2D] CREATE_ZONE_SCHEDULER_TASK: Create scheduler "gte2" with entities [EventEntity, EventEntity]
 14: 0x0066 [0x1C] WAIT(480* ticks)
 15: 0x0069 [0x27] REQ_SET(priority=0x01, entity_id=Cermet Gate (ID: 16834566/0x0100E006), tag_num=0x05)
 16: 0x0070 [0x52] END_LOAD_SCHEDULER: End scheduler "z14f" with entities [EventEntity, EventEntity], work=160*
 17: 0x007F [0x45] LOAD_SCHEDULED_TASK: Load scheduler "blon" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 18: 0x0090 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "blon" with entities [LocalPlayer, LocalPlayer], work=[201*, 0*]
 19: 0x00A1 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "z14g" with entities [EventEntity, EventEntity], work=[160*, 0*]
 20: 0x00B2 [0x1C] WAIT(180* ticks)
 21: 0x00B5 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 22: 0x00C6 [0x1C] WAIT(60* ticks)
 23: 0x00C9 [0x52] END_LOAD_SCHEDULER: End scheduler "z14g" with entities [EventEntity, EventEntity], work=160*
 24: 0x00D8 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "blof" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 25: 0x00E9 [0x03] Work_Zone[1] = 1*
 26: 0x00EE [0x46] CAMERA_CONTROL: Restore default settings
 27: 0x00F0 [0x01] GOTO 0x0103
 28: 0x00F3 [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x0103
 29: 0x00FB [0x03] Work_Zone[1] = 0*
 30: 0x0100 [0x01] GOTO 0x0103

SUBROUTINE_0103:
 31: 0x0103 [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
 32: 0x0105 [0x21] END_EVENT
 33: 0x0106 [0x00] END_REQSTACK()
```

### Event 65535.1

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x0107    |
| Data Size    | 189 bytes |
| Instructions | 17        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0100:                      29  01 F0 FF FF 7F 0A 45 06         )......E.
0110: 80 F8 FF FF 7F F8 FF FF  7F 7A 31 34 66 02 80 45  .........z14f..E
0120: 03 80 F0 FF FF 7F F0 FF  FF 7F 66 64 69 31 02 80  ..........fdi1..
0130: 1C 07 80 2D F8 FF FF 7F  F8 FF FF 7F 67 74 65 32  ...-........gte2
0140: 1C 08 80 27 01 06 E0 00  01 05 52 06 80 F8 FF FF  ...'......R.....
0150: 7F F8 FF FF 7F 7A 31 34  66 45 03 80 F0 FF FF 7F  .....z14fE......
0160: F0 FF FF 7F 62 6C 6F 6E  02 80 45 09 80 F0 FF FF  ....blon..E.....
0170: 7F F0 FF FF 7F 62 6C 6F  6E 02 80 45 06 80 F8 FF  .....blon..E....
0180: FF 7F F8 FF FF 7F 7A 31  34 67 02 80 1C 0A 80 45  ......z14g.....E
0190: 03 80 F0 FF FF 7F F0 FF  FF 7F 66 64 6F 31 02 80  ..........fdo1..
01A0: 1C 07 80 52 06 80 F8 FF  FF 7F F8 FF FF 7F 7A 31  ...R..........z1
01B0: 34 67 45 03 80 F0 FF FF  7F F0 FF FF 7F 62 6C 6F  4gE..........blo
01C0: 66 02 80 00                                       f...            
```

#### Opcodes

```
  0: 0x0107 [0x29] REQ_SET_WAIT(priority=0x01, entity_id=LocalPlayer, tag_num=0x0A)
  1: 0x010E [0x45] LOAD_SCHEDULED_TASK: Load scheduler "z14f" with entities [EventEntity, EventEntity], work=[160*, 0*]
  2: 0x011F [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
  3: 0x0130 [0x1C] WAIT(60* ticks)
  4: 0x0133 [0x2D] CREATE_ZONE_SCHEDULER_TASK: Create scheduler "gte2" with entities [EventEntity, EventEntity]
  5: 0x0140 [0x1C] WAIT(480* ticks)
  6: 0x0143 [0x27] REQ_SET(priority=0x01, entity_id=Cermet Gate (ID: 16834566/0x0100E006), tag_num=0x05)
  7: 0x014A [0x52] END_LOAD_SCHEDULER: End scheduler "z14f" with entities [EventEntity, EventEntity], work=160*
  8: 0x0159 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "blon" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
  9: 0x016A [0x45] LOAD_SCHEDULED_TASK: Load scheduler "blon" with entities [LocalPlayer, LocalPlayer], work=[201*, 0*]
 10: 0x017B [0x45] LOAD_SCHEDULED_TASK: Load scheduler "z14g" with entities [EventEntity, EventEntity], work=[160*, 0*]
 11: 0x018C [0x1C] WAIT(180* ticks)
 12: 0x018F [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 13: 0x01A0 [0x1C] WAIT(60* ticks)
 14: 0x01A3 [0x52] END_LOAD_SCHEDULER: End scheduler "z14g" with entities [EventEntity, EventEntity], work=160*
 15: 0x01B2 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "blof" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 16: 0x01C3 [0x00] END_REQSTACK()
```

### Event 151

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x01C4  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
01C0:             00                                        .           
```

#### Opcodes

```
  0: 0x01C4 [0x00] END_REQSTACK()
```

### Event 152

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

### Event 153

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x01C6  |
| Data Size    | 2 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
01C0:                   4C 00                                 L.        
```

#### Opcodes

```
  0: 0x01C6 [0x4C] EventEntity->StatusEvent = 8 // Open door
  1: 0x01C7 [0x00] END_REQSTACK()
```

### Event 154

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x01C8  |
| Data Size    | 2 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
01C0:                          4D 00                            M.      
```

#### Opcodes

```
  0: 0x01C8 [0x4D] EventEntity->StatusEvent = 9 // Close door
  1: 0x01C9 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x01CA  |
| Data Size    | 2 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
01C0:                                4C 00                        L.    
```

#### Opcodes

```
  0: 0x01CA [0x4C] EventEntity->StatusEvent = 8 // Open door
  1: 0x01CB [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x01CC  |
| Data Size    | 2 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
01C0:                                      4D 00                    M.  
```

#### Opcodes

```
  0: 0x01CC [0x4D] EventEntity->StatusEvent = 9 // Close door
  1: 0x01CD [0x00] END_REQSTACK()
```

### Event 160

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x01CE  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
01C0:                                            00                   . 
```

#### Opcodes

```
  0: 0x01CE [0x00] END_REQSTACK()
```
