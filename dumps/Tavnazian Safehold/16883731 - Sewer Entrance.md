# 16883731 - Sewer Entrance

## Common Data

| Field            | Value                       |
|------------------|-----------------------------|
| Zone             | Tavnazian Safehold (ID: 26) |
| Block Size       | 244 bytes                   |
| Total Events     | 6                           |
| References Count | 10                          |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [502](#event-502)        | 0x0001       |    156 |             30 |
| [103](#event-103)        | 0x009D       |      1 |              1 |
| [65535.1](#event-655351) | 0x009E       |      2 |              2 |
| [65535.2](#event-655352) | 0x00A0       |      2 |              2 |
| [116](#event-116)        | 0x00A2       |      1 |              1 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x1964      |        6500 |
|       1 | 0x0001      |           1 |
|       2 | 0x0000      |           0 |
|       3 | 0x00C8      |         200 |
|       4 | 0x003C      |          60 |
|       5 | 0x0013      |          19 |
|       6 | 0x005E      |          94 |
|       7 | 0x005A      |          90 |
|       8 | 0x00F0      |         240 |
|       9 | 0x0064      |         100 |

## String References

- **6500**: Proceed onward? [Yes./No.]

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

### Event 502

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x0001    |
| Data Size    | 156 bytes |
| Instructions | 30        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    20 01 24 00 80 01 80  02 80 25 02 00 10 02 80    .$......%.....
0010: 00 89 00 46 01 42 45 03  80 F0 FF FF 7F F0 FF FF  ...F.BE.........
0020: 7F 66 64 6F 31 02 80 1C  04 80 38 05 80 45 06 80  .fdo1.....8..E..
0030: F0 FF FF 7F F0 FF FF 7F  74 62 30 31 02 80 29 01  ........tb01..).
0040: F0 FF FF 7F 1F 45 03 80  F0 FF FF 7F F0 FF FF 7F  .....E..........
0050: 66 64 69 31 02 80 1C 04  80 4C 1C 07 80 27 01 F0  fdi1.....L...'..
0060: FF FF 7F 20 1C 08 80 4D  1C 09 80 45 03 80 F0 FF  ... ...M...E....
0070: FF 7F F0 FF FF 7F 66 64  6F 31 02 80 1C 04 80 03  ......fdo1......
0080: 01 10 01 80 46 00 01 99  00 02 00 10 01 80 00 99  ....F...........
0090: 00 03 01 10 02 80 01 99  00 20 00 21 00           ......... .!.   
```

#### Opcodes

```
  0: 0x0001 [0x20] SET_CLI_EVENT_UC_FLAG: Lock player control
  1: 0x0003 [0x24] CREATE_DIALOG(message_id=6500*, default_option=1*, option_flags=0*)
    → "Proceed onward? [Yes./No.]"
  2: 0x000A [0x25] WAIT_DIALOG_SELECT()
  3: 0x000B [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x0089
  4: 0x0013 [0x46] CAMERA_CONTROL: Disable user control
  5: 0x0015 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  6: 0x0016 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
  7: 0x0027 [0x1C] WAIT(60* ticks)
  8: 0x002A [0x38] SET_CLIENT_EVENT_MODE(mode=19*)
  9: 0x002D [0x45] LOAD_SCHEDULED_TASK: Load scheduler "tb01" with entities [LocalPlayer, LocalPlayer], work=[94*, 0*]
 10: 0x003E [0x29] REQ_SET_WAIT(priority=0x01, entity_id=LocalPlayer, tag_num=0x1F)
 11: 0x0045 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 12: 0x0056 [0x1C] WAIT(60* ticks)
 13: 0x0059 [0x4C] EventEntity->StatusEvent = 8 // Open door
 14: 0x005A [0x1C] WAIT(90* ticks)
 15: 0x005D [0x27] REQ_SET(priority=0x01, entity_id=LocalPlayer, tag_num=0x20)
 16: 0x0064 [0x1C] WAIT(240* ticks)
 17: 0x0067 [0x4D] EventEntity->StatusEvent = 9 // Close door
 18: 0x0068 [0x1C] WAIT(100* ticks)
 19: 0x006B [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 20: 0x007C [0x1C] WAIT(60* ticks)
 21: 0x007F [0x03] Work_Zone[1] = 1*
 22: 0x0084 [0x46] CAMERA_CONTROL: Restore default settings
 23: 0x0086 [0x01] GOTO 0x0099
 24: 0x0089 [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x0099
 25: 0x0091 [0x03] Work_Zone[1] = 0*
 26: 0x0096 [0x01] GOTO 0x0099

SUBROUTINE_0099:
 27: 0x0099 [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
 28: 0x009B [0x21] END_EVENT
 29: 0x009C [0x00] END_REQSTACK()
```

### Event 103

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x009D  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0090:                                         00                     .  
```

#### Opcodes

```
  0: 0x009D [0x00] END_REQSTACK()
```

### Event 65535.1

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x009E  |
| Data Size    | 2 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0090:                                            4C 00                L.
```

#### Opcodes

```
  0: 0x009E [0x4C] EventEntity->StatusEvent = 8 // Open door
  1: 0x009F [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x00A0  |
| Data Size    | 2 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00A0: 4D 00                                             M.              
```

#### Opcodes

```
  0: 0x00A0 [0x4D] EventEntity->StatusEvent = 9 // Close door
  1: 0x00A1 [0x00] END_REQSTACK()
```

### Event 116

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x00A2  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00A0:       00                                            .             
```

#### Opcodes

```
  0: 0x00A2 [0x00] END_REQSTACK()
```
