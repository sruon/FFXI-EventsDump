# 17563870 - Ancient Magical Gizmo

## Common Data

| Field            | Value                          |
|------------------|--------------------------------|
| Zone             | Inner Horutoto Ruins (ID: 192) |
| Block Size       | 412 bytes                      |
| Total Events     | 3                              |
| References Count | 10                             |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [52](#event-52)       | 0x0001       |    153 |             24 |
| [53](#event-53)       | 0x009A       |    188 |             25 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x00C8      |         200 |
|       1 | 0x0000      |           0 |
|       2 | 0x003C      |          60 |
|       3 | 0x0013      |          19 |
|       4 | 0x005E      |          94 |
|       5 | 0x001E      |          30 |
|       6 | 0x0078      |         120 |
|       7 | 0x005A      |          90 |
|       8 | 0x0064      |         100 |
|       9 | 0x002D      |          45 |

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

### Event 52

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x0001    |
| Data Size    | 153 bytes |
| Instructions | 23        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    46 01 42 45 00 80 F0  FF FF 7F F0 FF FF 7F 66   F.BE..........f
0010: 64 6F 31 01 80 1C 02 80  38 03 80 45 04 80 F0 FF  do1.....8..E....
0020: FF 7F F0 FF FF 7F 6D 64  73 33 01 80 27 0B F0 FF  ......mds3..'...
0030: FF 7F 08 45 00 80 F0 FF  FF 7F F0 FF FF 7F 66 64  ...E..........fd
0040: 69 31 01 80 1C 05 80 4C  1C 06 80 45 00 80 F0 FF  i1.....L...E....
0050: FF 7F F0 FF FF 7F 66 64  6F 31 01 80 1C 02 80 2C  ......fdo1.....,
0060: F8 FF FF 7F F8 FF FF 7F  6D 67 30 33 52 04 80 F0  ........mg03R...
0070: FF FF 7F F0 FF FF 7F 6D  64 73 33 1C 07 80 4D 1C  .......mds3...M.
0080: 02 80 46 00 45 00 80 F0  FF FF 7F F0 FF FF 7F 66  ..F.E..........f
0090: 64 69 31 01 80 20 00 21  00 00                    di1.. .!..      
```

#### Opcodes

```
  0: 0x0001 [0x46] CAMERA_CONTROL: Disable user control
  1: 0x0003 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  2: 0x0004 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
  3: 0x0015 [0x1C] WAIT(60* ticks)
  4: 0x0018 [0x38] SET_CLIENT_EVENT_MODE(mode=19*)
  5: 0x001B [0x45] LOAD_SCHEDULED_TASK: Load scheduler "mds3" with entities [LocalPlayer, LocalPlayer], work=[94*, 0*]
  6: 0x002C [0x27] REQ_SET(priority=0x0B, entity_id=LocalPlayer, tag_num=0x08)
  7: 0x0033 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
  8: 0x0044 [0x1C] WAIT(30* ticks)
  9: 0x0047 [0x4C] EventEntity->StatusEvent = 8 // Open door
 10: 0x0048 [0x1C] WAIT(120* ticks)
 11: 0x004B [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 12: 0x005C [0x1C] WAIT(60* ticks)
 13: 0x005F [0x2C] CREATE_SCHEDULER_TASK: Create scheduler "mg03" with entities [EventEntity, EventEntity]
 14: 0x006C [0x52] END_LOAD_SCHEDULER: End scheduler "mds3" with entities [LocalPlayer, LocalPlayer], work=94*
 15: 0x007B [0x1C] WAIT(90* ticks)
 16: 0x007E [0x4D] EventEntity->StatusEvent = 9 // Close door
 17: 0x007F [0x1C] WAIT(60* ticks)
 18: 0x0082 [0x46] CAMERA_CONTROL: Restore default settings
 19: 0x0084 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 20: 0x0095 [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
 21: 0x0097 [0x21] END_EVENT
 22: 0x0098 [0x00] END_REQSTACK()
```

#### Data or dead code:

```
# Dead code (unreachable instructions):
     0x0099 [0x00] END_REQSTACK()
```

### Event 53

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x009A    |
| Data Size    | 188 bytes |
| Instructions | 25        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0090:                                46 01 42 45 00 80            F.BE..
00A0: F0 FF FF 7F F0 FF FF 7F  66 64 6F 31 01 80 1C 02  ........fdo1....
00B0: 80 38 03 80 45 04 80 F0  FF FF 7F F0 FF FF 7F 6D  .8..E..........m
00C0: 64 30 33 01 80 27 0B F0  FF FF 7F 08 45 00 80 F0  d03..'......E...
00D0: FF FF 7F F0 FF FF 7F 66  64 69 31 01 80 1C 05 80  .......fdi1.....
00E0: 4C 2D F8 FF FF 7F F8 FF  FF 7F 70 74 64 36 2C F8  L-........ptd6,.
00F0: FF FF 7F F8 FF FF 7F 6F  6D 64 36 1C 08 80 2C F8  .......omd6...,.
0100: FF FF 7F F8 FF FF 7F 6B  6F 64 36 1C 09 80 45 00  .......kod6...E.
0110: 80 F0 FF FF 7F F0 FF FF  7F 66 64 6F 31 01 80 1C  .........fdo1...
0120: 02 80 52 04 80 F0 FF FF  7F F0 FF FF 7F 6D 64 30  ..R..........md0
0130: 33 2D F8 FF FF 7F F8 FF  FF 7F 6B 70 64 36 4D 46  3-........kpd6MF
0140: 00 45 00 80 F0 FF FF 7F  F0 FF FF 7F 66 64 69 31  .E..........fdi1
0150: 01 80 20 00 21 00                                 .. .!.          
```

#### Opcodes

```
  0: 0x009A [0x46] CAMERA_CONTROL: Disable user control
  1: 0x009C [0x42] SET_CLI_EVENT_CANCEL_DATA()
  2: 0x009D [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
  3: 0x00AE [0x1C] WAIT(60* ticks)
  4: 0x00B1 [0x38] SET_CLIENT_EVENT_MODE(mode=19*)
  5: 0x00B4 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "md03" with entities [LocalPlayer, LocalPlayer], work=[94*, 0*]
  6: 0x00C5 [0x27] REQ_SET(priority=0x0B, entity_id=LocalPlayer, tag_num=0x08)
  7: 0x00CC [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
  8: 0x00DD [0x1C] WAIT(30* ticks)
  9: 0x00E0 [0x4C] EventEntity->StatusEvent = 8 // Open door
 10: 0x00E1 [0x2D] CREATE_ZONE_SCHEDULER_TASK: Create scheduler "ptd6" with entities [EventEntity, EventEntity]
 11: 0x00EE [0x2C] CREATE_SCHEDULER_TASK: Create scheduler "omd6" with entities [EventEntity, EventEntity]
 12: 0x00FB [0x1C] WAIT(100* ticks)
 13: 0x00FE [0x2C] CREATE_SCHEDULER_TASK: Create scheduler "kod6" with entities [EventEntity, EventEntity]
 14: 0x010B [0x1C] WAIT(45* ticks)
 15: 0x010E [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 16: 0x011F [0x1C] WAIT(60* ticks)
 17: 0x0122 [0x52] END_LOAD_SCHEDULER: End scheduler "md03" with entities [LocalPlayer, LocalPlayer], work=94*
 18: 0x0131 [0x2D] CREATE_ZONE_SCHEDULER_TASK: Create scheduler "kpd6" with entities [EventEntity, EventEntity]
 19: 0x013E [0x4D] EventEntity->StatusEvent = 9 // Close door
 20: 0x013F [0x46] CAMERA_CONTROL: Restore default settings
 21: 0x0141 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 22: 0x0152 [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
 23: 0x0154 [0x21] END_EVENT
 24: 0x0155 [0x00] END_REQSTACK()
```
