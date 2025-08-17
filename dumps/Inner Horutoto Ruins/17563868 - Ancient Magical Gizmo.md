# 17563868 - Ancient Magical Gizmo

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
| [48](#event-48)       | 0x0001       |    152 |             23 |
| [49](#event-49)       | 0x0099       |    188 |             25 |

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

### Event 48

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x0001    |
| Data Size    | 152 bytes |
| Instructions | 23        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    46 01 42 45 00 80 F0  FF FF 7F F0 FF FF 7F 66   F.BE..........f
0010: 64 6F 31 01 80 1C 02 80  38 03 80 45 04 80 F0 FF  do1.....8..E....
0020: FF 7F F0 FF FF 7F 6D 64  73 31 01 80 27 0B F0 FF  ......mds1..'...
0030: FF 7F 06 45 00 80 F0 FF  FF 7F F0 FF FF 7F 66 64  ...E..........fd
0040: 69 31 01 80 1C 05 80 4C  1C 06 80 45 00 80 F0 FF  i1.....L...E....
0050: FF 7F F0 FF FF 7F 66 64  6F 31 01 80 1C 02 80 2C  ......fdo1.....,
0060: F8 FF FF 7F F8 FF FF 7F  6D 67 30 31 52 04 80 F0  ........mg01R...
0070: FF FF 7F F0 FF FF 7F 6D  64 73 31 1C 07 80 4D 1C  .......mds1...M.
0080: 02 80 46 00 45 00 80 F0  FF FF 7F F0 FF FF 7F 66  ..F.E..........f
0090: 64 69 31 01 80 20 00 21  00                       di1.. .!.       
```

#### Opcodes

```
  0: 0x0001 [0x46] CAMERA_CONTROL: Disable user control
  1: 0x0003 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  2: 0x0004 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
  3: 0x0015 [0x1C] WAIT(60* ticks)
  4: 0x0018 [0x38] SET_CLIENT_EVENT_MODE(mode=19*)
  5: 0x001B [0x45] LOAD_SCHEDULED_TASK: Load scheduler "mds1" with entities [LocalPlayer, LocalPlayer], work=[94*, 0*]
  6: 0x002C [0x27] REQ_SET(priority=0x0B, entity_id=LocalPlayer, tag_num=0x06)
  7: 0x0033 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
  8: 0x0044 [0x1C] WAIT(30* ticks)
  9: 0x0047 [0x4C] EventEntity->StatusEvent = 8 // Open door
 10: 0x0048 [0x1C] WAIT(120* ticks)
 11: 0x004B [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 12: 0x005C [0x1C] WAIT(60* ticks)
 13: 0x005F [0x2C] CREATE_SCHEDULER_TASK: Create scheduler "mg01" with entities [EventEntity, EventEntity]
 14: 0x006C [0x52] END_LOAD_SCHEDULER: End scheduler "mds1" with entities [LocalPlayer, LocalPlayer], work=94*
 15: 0x007B [0x1C] WAIT(90* ticks)
 16: 0x007E [0x4D] EventEntity->StatusEvent = 9 // Close door
 17: 0x007F [0x1C] WAIT(60* ticks)
 18: 0x0082 [0x46] CAMERA_CONTROL: Restore default settings
 19: 0x0084 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 20: 0x0095 [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
 21: 0x0097 [0x21] END_EVENT
 22: 0x0098 [0x00] END_REQSTACK()
```

### Event 49

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x0099    |
| Data Size    | 188 bytes |
| Instructions | 25        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0090:                             46 01 42 45 00 80 F0           F.BE...
00A0: FF FF 7F F0 FF FF 7F 66  64 6F 31 01 80 1C 02 80  .......fdo1.....
00B0: 38 03 80 45 04 80 F0 FF  FF 7F F0 FF FF 7F 6D 64  8..E..........md
00C0: 30 31 01 80 27 0B F0 FF  FF 7F 06 45 00 80 F0 FF  01..'......E....
00D0: FF 7F F0 FF FF 7F 66 64  69 31 01 80 1C 05 80 4C  ......fdi1.....L
00E0: 2D F8 FF FF 7F F8 FF FF  7F 70 74 64 35 2C F8 FF  -........ptd5,..
00F0: FF 7F F8 FF FF 7F 6F 6D  64 35 1C 08 80 2C F8 FF  ......omd5...,..
0100: FF 7F F8 FF FF 7F 6B 6F  64 35 1C 09 80 45 00 80  ......kod5...E..
0110: F0 FF FF 7F F0 FF FF 7F  66 64 6F 31 01 80 1C 02  ........fdo1....
0120: 80 52 04 80 F0 FF FF 7F  F0 FF FF 7F 6D 64 30 31  .R..........md01
0130: 2D F8 FF FF 7F F8 FF FF  7F 6B 70 64 35 4D 46 00  -........kpd5MF.
0140: 45 00 80 F0 FF FF 7F F0  FF FF 7F 66 64 69 31 01  E..........fdi1.
0150: 80 20 00 21 00                                    . .!.           
```

#### Opcodes

```
  0: 0x0099 [0x46] CAMERA_CONTROL: Disable user control
  1: 0x009B [0x42] SET_CLI_EVENT_CANCEL_DATA()
  2: 0x009C [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
  3: 0x00AD [0x1C] WAIT(60* ticks)
  4: 0x00B0 [0x38] SET_CLIENT_EVENT_MODE(mode=19*)
  5: 0x00B3 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "md01" with entities [LocalPlayer, LocalPlayer], work=[94*, 0*]
  6: 0x00C4 [0x27] REQ_SET(priority=0x0B, entity_id=LocalPlayer, tag_num=0x06)
  7: 0x00CB [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
  8: 0x00DC [0x1C] WAIT(30* ticks)
  9: 0x00DF [0x4C] EventEntity->StatusEvent = 8 // Open door
 10: 0x00E0 [0x2D] CREATE_ZONE_SCHEDULER_TASK: Create scheduler "ptd5" with entities [EventEntity, EventEntity]
 11: 0x00ED [0x2C] CREATE_SCHEDULER_TASK: Create scheduler "omd5" with entities [EventEntity, EventEntity]
 12: 0x00FA [0x1C] WAIT(100* ticks)
 13: 0x00FD [0x2C] CREATE_SCHEDULER_TASK: Create scheduler "kod5" with entities [EventEntity, EventEntity]
 14: 0x010A [0x1C] WAIT(45* ticks)
 15: 0x010D [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 16: 0x011E [0x1C] WAIT(60* ticks)
 17: 0x0121 [0x52] END_LOAD_SCHEDULER: End scheduler "md01" with entities [LocalPlayer, LocalPlayer], work=94*
 18: 0x0130 [0x2D] CREATE_ZONE_SCHEDULER_TASK: Create scheduler "kpd5" with entities [EventEntity, EventEntity]
 19: 0x013D [0x4D] EventEntity->StatusEvent = 9 // Close door
 20: 0x013E [0x46] CAMERA_CONTROL: Restore default settings
 21: 0x0140 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 22: 0x0151 [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
 23: 0x0153 [0x21] END_EVENT
 24: 0x0154 [0x00] END_REQSTACK()
```
