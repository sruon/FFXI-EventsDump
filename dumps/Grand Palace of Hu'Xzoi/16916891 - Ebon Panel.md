# 16916891 - Ebon Panel

## Common Data

| Field            | Value                            |
|------------------|----------------------------------|
| Zone             | Grand Palace of Hu'Xzoi (ID: 34) |
| Block Size       | 268 bytes                        |
| Total Events     | 2                                |
| References Count | 9                                |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [120](#event-120)     | 0x0001       |    204 |             28 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x00C8      |         200 |
|       1 | 0x0000      |           0 |
|       2 | 0x003C      |          60 |
|       3 | 0x0013      |          19 |
|       4 | 0x005E      |          94 |
|       5 | 0x0078      |         120 |
|       6 | 0x00B4      |         180 |
|       7 | 0x0168      |         360 |
|       8 | 0x00F0      |         240 |

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
| Data Size    | 204 bytes |
| Instructions | 28        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    20 01 43 00 43 01 46  01 42 45 00 80 F0 FF FF    .C.C.F.BE.....
0010: 7F F0 FF FF 7F 66 64 6F  31 01 80 1C 02 80 38 03  .....fdo1.....8.
0020: 80 45 04 80 F0 FF FF 7F  F0 FF FF 7F 74 6F 77 31  .E..........tow1
0030: 01 80 45 00 80 F0 FF FF  7F F0 FF FF 7F 66 64 69  ..E..........fdi
0040: 31 01 80 1C 05 80 2D F8  FF FF 7F F8 FF FF 7F 73  1.....-........s
0050: 31 35 30 2D F8 FF FF 7F  F8 FF FF 7F 31 63 6F 6E  150-........1con
0060: 1C 06 80 2D F8 FF FF 7F  F8 FF FF 7F 32 73 65 6E  ...-........2sen
0070: 1C 02 80 2D F8 FF FF 7F  F8 FF FF 7F 33 6B 69 72  ...-........3kir
0080: 1C 07 80 45 00 80 F0 FF  FF 7F F0 FF FF 7F 66 64  ...E..........fd
0090: 6F 31 01 80 1C 02 80 2D  F8 FF FF 7F F8 FF FF 7F  o1.....-........
00A0: 6D 6F 64 6F 1C 08 80 52  04 80 F0 FF FF 7F F0 FF  modo...R........
00B0: FF 7F 74 6F 77 31 46 00  45 00 80 F0 FF FF 7F F0  ..tow1F.E.......
00C0: FF FF 7F 66 64 69 31 01  80 20 00 21 00           ...fdi1.. .!.   
```

#### Opcodes

```
  0: 0x0001 [0x20] SET_CLI_EVENT_UC_FLAG: Lock player control
  1: 0x0003 [0x43] SEND_EVENT_UPDATE: Send pending tag to server (packet 0x005B)
  2: 0x0005 [0x43] SEND_EVENT_UPDATE: Check pending flag (skip if not pending)
  3: 0x0007 [0x46] CAMERA_CONTROL: Disable user control
  4: 0x0009 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  5: 0x000A [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
  6: 0x001B [0x1C] WAIT(60* ticks)
  7: 0x001E [0x38] SET_CLIENT_EVENT_MODE(mode=19*)
  8: 0x0021 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "tow1" with entities [LocalPlayer, LocalPlayer], work=[94*, 0*]
  9: 0x0032 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 10: 0x0043 [0x1C] WAIT(120* ticks)
 11: 0x0046 [0x2D] CREATE_ZONE_SCHEDULER_TASK: Create scheduler "s150" with entities [EventEntity, EventEntity]
 12: 0x0053 [0x2D] CREATE_ZONE_SCHEDULER_TASK: Create scheduler "1con" with entities [EventEntity, EventEntity]
 13: 0x0060 [0x1C] WAIT(180* ticks)
 14: 0x0063 [0x2D] CREATE_ZONE_SCHEDULER_TASK: Create scheduler "2sen" with entities [EventEntity, EventEntity]
 15: 0x0070 [0x1C] WAIT(60* ticks)
 16: 0x0073 [0x2D] CREATE_ZONE_SCHEDULER_TASK: Create scheduler "3kir" with entities [EventEntity, EventEntity]
 17: 0x0080 [0x1C] WAIT(360* ticks)
 18: 0x0083 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 19: 0x0094 [0x1C] WAIT(60* ticks)
 20: 0x0097 [0x2D] CREATE_ZONE_SCHEDULER_TASK: Create scheduler "modo" with entities [EventEntity, EventEntity]
 21: 0x00A4 [0x1C] WAIT(240* ticks)
 22: 0x00A7 [0x52] END_LOAD_SCHEDULER: End scheduler "tow1" with entities [LocalPlayer, LocalPlayer], work=94*
 23: 0x00B6 [0x46] CAMERA_CONTROL: Restore default settings
 24: 0x00B8 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 25: 0x00C9 [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
 26: 0x00CB [0x21] END_EVENT
 27: 0x00CC [0x00] END_REQSTACK()
```
