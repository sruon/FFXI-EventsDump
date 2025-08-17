# 17572252 - Ancient Magical Gizmo

## Common Data

| Field            | Value                          |
|------------------|--------------------------------|
| Zone             | Outer Horutoto Ruins (ID: 194) |
| Block Size       | 400 bytes                      |
| Total Events     | 3                              |
| References Count | 8                              |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [48](#event-48)       | 0x0001       |    197 |             28 |
| [60](#event-60)       | 0x00C6       |    142 |             23 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x00C8      |         200 |
|       1 | 0x0000      |           0 |
|       2 | 0x003C      |          60 |
|       3 | 0x0013      |          19 |
|       4 | 0x005E      |          94 |
|       5 | 0x0032      |          50 |
|       6 | 0x005A      |          90 |
|       7 | 0x0078      |         120 |

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
| Data Size    | 197 bytes |
| Instructions | 28        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    46 01 42 03 01 10 05  10 45 00 80 F0 FF FF 7F   F.B.....E......
0010: F0 FF FF 7F 66 64 6F 31  01 80 1C 02 80 38 03 80  ....fdo1.....8..
0020: 45 04 80 F0 FF FF 7F F0  FF FF 7F 6D 64 31 33 01  E..........md13.
0030: 80 27 0B F0 FF FF 7F 0D  45 00 80 F0 FF FF 7F F0  .'......E.......
0040: FF FF 7F 66 64 69 31 01  80 1C 05 80 4C 2D F8 FF  ...fdi1.....L-..
0050: FF 7F F8 FF FF 7F 70 74  63 31 2C F8 FF FF 7F F8  ......ptc1,.....
0060: FF FF 7F 6F 6D 63 31 1C  02 80 2C F8 FF FF 7F F8  ...omc1...,.....
0070: FF FF 7F 6B 6F 63 31 1C  02 80 45 00 80 F0 FF FF  ...koc1...E.....
0080: 7F F0 FF FF 7F 66 64 6F  31 01 80 1C 02 80 2D F8  .....fdo1.....-.
0090: FF FF 7F F8 FF FF 7F 6B  70 63 31 2C F8 FF FF 7F  .......kpc1,....
00A0: F8 FF FF 7F 6D 67 31 33  1C 06 80 4D 1C 02 80 46  ....mg13...M...F
00B0: 00 45 00 80 F0 FF FF 7F  F0 FF FF 7F 66 64 69 31  .E..........fdi1
00C0: 01 80 20 00 21 00                                 .. .!.          
```

#### Opcodes

```
  0: 0x0001 [0x46] CAMERA_CONTROL: Disable user control
  1: 0x0003 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  2: 0x0004 [0x03] Work_Zone[1] = Work_Zone[5]
  3: 0x0009 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
  4: 0x001A [0x1C] WAIT(60* ticks)
  5: 0x001D [0x38] SET_CLIENT_EVENT_MODE(mode=19*)
  6: 0x0020 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "md13" with entities [LocalPlayer, LocalPlayer], work=[94*, 0*]
  7: 0x0031 [0x27] REQ_SET(priority=0x0B, entity_id=LocalPlayer, tag_num=0x0D)
  8: 0x0038 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
  9: 0x0049 [0x1C] WAIT(50* ticks)
 10: 0x004C [0x4C] EventEntity->StatusEvent = 8 // Open door
 11: 0x004D [0x2D] CREATE_ZONE_SCHEDULER_TASK: Create scheduler "ptc1" with entities [EventEntity, EventEntity]
 12: 0x005A [0x2C] CREATE_SCHEDULER_TASK: Create scheduler "omc1" with entities [EventEntity, EventEntity]
 13: 0x0067 [0x1C] WAIT(60* ticks)
 14: 0x006A [0x2C] CREATE_SCHEDULER_TASK: Create scheduler "koc1" with entities [EventEntity, EventEntity]
 15: 0x0077 [0x1C] WAIT(60* ticks)
 16: 0x007A [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 17: 0x008B [0x1C] WAIT(60* ticks)
 18: 0x008E [0x2D] CREATE_ZONE_SCHEDULER_TASK: Create scheduler "kpc1" with entities [EventEntity, EventEntity]
 19: 0x009B [0x2C] CREATE_SCHEDULER_TASK: Create scheduler "mg13" with entities [EventEntity, EventEntity]
 20: 0x00A8 [0x1C] WAIT(90* ticks)
 21: 0x00AB [0x4D] EventEntity->StatusEvent = 9 // Close door
 22: 0x00AC [0x1C] WAIT(60* ticks)
 23: 0x00AF [0x46] CAMERA_CONTROL: Restore default settings
 24: 0x00B1 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 25: 0x00C2 [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
 26: 0x00C4 [0x21] END_EVENT
 27: 0x00C5 [0x00] END_REQSTACK()
```

### Event 60

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x00C6    |
| Data Size    | 142 bytes |
| Instructions | 23        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00C0:                   46 01  42 03 01 10 04 10 45 00        F.B.....E.
00D0: 80 F0 FF FF 7F F0 FF FF  7F 66 64 6F 31 01 80 1C  .........fdo1...
00E0: 02 80 38 03 80 45 04 80  F0 FF FF 7F F0 FF FF 7F  ..8..E..........
00F0: 6D 73 31 33 01 80 27 0B  F0 FF FF 7F 0D 45 00 80  ms13..'......E..
0100: F0 FF FF 7F F0 FF FF 7F  66 64 69 31 01 80 1C 05  ........fdi1....
0110: 80 4C 1C 07 80 45 00 80  F0 FF FF 7F F0 FF FF 7F  .L...E..........
0120: 66 64 6F 31 01 80 1C 02  80 2C F8 FF FF 7F F8 FF  fdo1.....,......
0130: FF 7F 6D 73 31 33 1C 06  80 4D 1C 02 80 46 00 45  ..ms13...M...F.E
0140: 00 80 F0 FF FF 7F F0 FF  FF 7F 66 64 69 31 01 80  ..........fdi1..
0150: 20 00 21 00                                        .!.            
```

#### Opcodes

```
  0: 0x00C6 [0x46] CAMERA_CONTROL: Disable user control
  1: 0x00C8 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  2: 0x00C9 [0x03] Work_Zone[1] = Work_Zone[4]
  3: 0x00CE [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
  4: 0x00DF [0x1C] WAIT(60* ticks)
  5: 0x00E2 [0x38] SET_CLIENT_EVENT_MODE(mode=19*)
  6: 0x00E5 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "ms13" with entities [LocalPlayer, LocalPlayer], work=[94*, 0*]
  7: 0x00F6 [0x27] REQ_SET(priority=0x0B, entity_id=LocalPlayer, tag_num=0x0D)
  8: 0x00FD [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
  9: 0x010E [0x1C] WAIT(50* ticks)
 10: 0x0111 [0x4C] EventEntity->StatusEvent = 8 // Open door
 11: 0x0112 [0x1C] WAIT(120* ticks)
 12: 0x0115 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 13: 0x0126 [0x1C] WAIT(60* ticks)
 14: 0x0129 [0x2C] CREATE_SCHEDULER_TASK: Create scheduler "ms13" with entities [EventEntity, EventEntity]
 15: 0x0136 [0x1C] WAIT(90* ticks)
 16: 0x0139 [0x4D] EventEntity->StatusEvent = 9 // Close door
 17: 0x013A [0x1C] WAIT(60* ticks)
 18: 0x013D [0x46] CAMERA_CONTROL: Restore default settings
 19: 0x013F [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 20: 0x0150 [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
 21: 0x0152 [0x21] END_EVENT
 22: 0x0153 [0x00] END_REQSTACK()
```
