# 16916829 - Particle Gate

## Common Data

| Field            | Value                            |
|------------------|----------------------------------|
| Zone             | Grand Palace of Hu'Xzoi (ID: 34) |
| Block Size       | 376 bytes                        |
| Total Events     | 6                                |
| References Count | 11                               |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [65534](#event-65534)    | 0x0001       |      1 |              1 |
| [56](#event-56)          | 0x0002       |    282 |             43 |
| [0](#event-0)            | 0x011C       |      1 |              1 |
| [65535.1](#event-655351) | 0x011D       |      2 |              2 |
| [65535.2](#event-655352) | 0x011F       |      2 |              2 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x1C5A      |        7258 |
|       1 | 0x0001      |           1 |
|       2 | 0x0000      |           0 |
|       3 | 0x00C8      |         200 |
|       4 | 0x003C      |          60 |
|       5 | 0x0013      |          19 |
|       6 | 0x005E      |          94 |
|       7 | 0x0078      |         120 |
|       8 | 0x00B4      |         180 |
|       9 | 0x00C9      |         201 |
|      10 | 0x00F0      |         240 |

## String References

- **7258**: Open the portal? [Yes./No.]

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

### Event 65534

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

### Event 56

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x0002    |
| Data Size    | 282 bytes |
| Instructions | 43        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:       20 01 20 01 24 00  80 01 80 02 80 25 02 00     . .$......%..
0010: 10 02 80 00 08 01 43 00  43 01 46 01 42 45 03 80  ......C.C.F.BE..
0020: F0 FF FF 7F F0 FF FF 7F  66 64 6F 31 02 80 1C 04  ........fdo1....
0030: 80 38 05 80 45 06 80 F0  FF FF 7F F0 FF FF 7F 73  .8..E..........s
0040: 69 6E 31 02 80 29 01 F0  FF FF 7F 07 29 01 F0 FF  in1..)......)...
0050: FF 7F 05 45 03 80 F0 FF  FF 7F F0 FF FF 7F 66 64  ...E..........fd
0060: 69 31 02 80 1C 07 80 2D  F8 FF FF 7F F8 FF FF 7F  i1.....-........
0070: 73 31 34 38 2D F8 FF FF  7F F8 FF FF 7F 63 72 79  s148-........cry
0080: 68 54 F8 FF FF 7F F8 FF  FF 7F 63 72 79 68 1C 04  hT........cryh..
0090: 80 2D F8 FF FF 7F F8 FF  FF 7F 73 65 6E 68 54 F8  .-........senhT.
00A0: FF FF 7F F8 FF FF 7F 73  65 6E 68 4C 1C 04 80 27  .......senhL...'
00B0: 01 F0 FF FF 7F 06 1C 08  80 4D 1C 04 80 45 03 80  .........M...E..
00C0: F0 FF FF 7F F0 FF FF 7F  66 64 6F 31 02 80 1C 04  ........fdo1....
00D0: 80 45 09 80 F0 FF FF 7F  F0 FF FF 7F 77 68 69 31  .E..........whi1
00E0: 02 80 2D F8 FF FF 7F F8  FF FF 7F 64 6F 6F 72 46  ..-........doorF
00F0: 00 1C 0A 80 45 03 80 F0  FF FF 7F F0 FF FF 7F 66  ....E..........f
0100: 64 69 31 02 80 01 18 01  02 00 10 01 80 00 18 01  di1.............
0110: 03 01 10 02 80 01 18 01  20 00 21 00              ........ .!.    
```

#### Opcodes

```
  0: 0x0002 [0x20] SET_CLI_EVENT_UC_FLAG: Lock player control
  1: 0x0004 [0x20] SET_CLI_EVENT_UC_FLAG: Lock player control
  2: 0x0006 [0x24] CREATE_DIALOG(message_id=7258*, default_option=1*, option_flags=0*)
    → "Open the portal? [Yes./No.]"
  3: 0x000D [0x25] WAIT_DIALOG_SELECT()
  4: 0x000E [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x0108
  5: 0x0016 [0x43] SEND_EVENT_UPDATE: Send pending tag to server (packet 0x005B)
  6: 0x0018 [0x43] SEND_EVENT_UPDATE: Check pending flag (skip if not pending)
  7: 0x001A [0x46] CAMERA_CONTROL: Disable user control
  8: 0x001C [0x42] SET_CLI_EVENT_CANCEL_DATA()
  9: 0x001D [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 10: 0x002E [0x1C] WAIT(60* ticks)
 11: 0x0031 [0x38] SET_CLIENT_EVENT_MODE(mode=19*)
 12: 0x0034 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "sin1" with entities [LocalPlayer, LocalPlayer], work=[94*, 0*]
 13: 0x0045 [0x29] REQ_SET_WAIT(priority=0x01, entity_id=LocalPlayer, tag_num=0x07)
 14: 0x004C [0x29] REQ_SET_WAIT(priority=0x01, entity_id=LocalPlayer, tag_num=0x05)
 15: 0x0053 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 16: 0x0064 [0x1C] WAIT(120* ticks)
 17: 0x0067 [0x2D] CREATE_ZONE_SCHEDULER_TASK: Create scheduler "s148" with entities [EventEntity, EventEntity]
 18: 0x0074 [0x2D] CREATE_ZONE_SCHEDULER_TASK: Create scheduler "cryh" with entities [EventEntity, EventEntity]
 19: 0x0081 [0x54] WAIT_MAP_SCHEDULER: Wait for scheduler "cryh" with entities [EventEntity, EventEntity]
 20: 0x008E [0x1C] WAIT(60* ticks)
 21: 0x0091 [0x2D] CREATE_ZONE_SCHEDULER_TASK: Create scheduler "senh" with entities [EventEntity, EventEntity]
 22: 0x009E [0x54] WAIT_MAP_SCHEDULER: Wait for scheduler "senh" with entities [EventEntity, EventEntity]
 23: 0x00AB [0x4C] EventEntity->StatusEvent = 8 // Open door
 24: 0x00AC [0x1C] WAIT(60* ticks)
 25: 0x00AF [0x27] REQ_SET(priority=0x01, entity_id=LocalPlayer, tag_num=0x06)
 26: 0x00B6 [0x1C] WAIT(180* ticks)
 27: 0x00B9 [0x4D] EventEntity->StatusEvent = 9 // Close door
 28: 0x00BA [0x1C] WAIT(60* ticks)
 29: 0x00BD [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 30: 0x00CE [0x1C] WAIT(60* ticks)
 31: 0x00D1 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "whi1" with entities [LocalPlayer, LocalPlayer], work=[201*, 0*]
 32: 0x00E2 [0x2D] CREATE_ZONE_SCHEDULER_TASK: Create scheduler "door" with entities [EventEntity, EventEntity]
 33: 0x00EF [0x46] CAMERA_CONTROL: Restore default settings
 34: 0x00F1 [0x1C] WAIT(240* ticks)
 35: 0x00F4 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 36: 0x0105 [0x01] GOTO 0x0118
 37: 0x0108 [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x0118
 38: 0x0110 [0x03] Work_Zone[1] = 0*
 39: 0x0115 [0x01] GOTO 0x0118

SUBROUTINE_0118:
 40: 0x0118 [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
 41: 0x011A [0x21] END_EVENT
 42: 0x011B [0x00] END_REQSTACK()
```

### Event 0

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x011C  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0110:                                      00                       .   
```

#### Opcodes

```
  0: 0x011C [0x00] END_REQSTACK()
```

### Event 65535.1

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x011D  |
| Data Size    | 2 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0110:                                         4C 00                  L. 
```

#### Opcodes

```
  0: 0x011D [0x4C] EventEntity->StatusEvent = 8 // Open door
  1: 0x011E [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x011F  |
| Data Size    | 2 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0110:                                               4D                 M
0120: 00                                                .               
```

#### Opcodes

```
  0: 0x011F [0x4D] EventEntity->StatusEvent = 9 // Close door
  1: 0x0120 [0x00] END_REQSTACK()
```
