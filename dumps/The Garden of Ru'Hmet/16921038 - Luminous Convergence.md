# 16921038 - Luminous Convergence

## Common Data

| Field            | Value                          |
|------------------|--------------------------------|
| Zone             | The Garden of Ru'Hmet (ID: 35) |
| Block Size       | 320 bytes                      |
| Total Events     | 6                              |
| References Count | 11                             |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [100](#event-100)        | 0x0001       |    228 |             32 |
| [203](#event-203)        | 0x00E5       |      1 |              1 |
| [204](#event-204)        | 0x00E6       |      1 |              1 |
| [65535.1](#event-655351) | 0x00E7       |      2 |              2 |
| [65535.2](#event-655352) | 0x00E9       |      2 |              2 |

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
|       7 | 0x012C      |         300 |
|       8 | 0x0258      |         600 |
|       9 | 0x00C9      |         201 |
|      10 | 0x0001      |           1 |

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

### Event 100

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x0001    |
| Data Size    | 228 bytes |
| Instructions | 32        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    20 01 43 00 43 01 46  01 42 45 00 80 F0 FF FF    .C.C.F.BE.....
0010: 7F F0 FF FF 7F 66 64 6F  31 01 80 1C 02 80 38 03  .....fdo1.....8.
0020: 80 45 04 80 F0 FF FF 7F  F0 FF FF 7F 6F 75 7A 61  .E..........ouza
0030: 01 80 45 00 80 F0 FF FF  7F F0 FF FF 7F 66 64 69  ..E..........fdi
0040: 31 01 80 1C 05 80 2D F8  FF FF 7F F8 FF FF 7F 73  1.....-........s
0050: 31 35 31 2D F8 FF FF 7F  F8 FF FF 7F 6C 73 74 34  151-........lst4
0060: 1C 06 80 2D F8 FF FF 7F  F8 FF FF 7F 6C 73 74 36  ...-........lst6
0070: 1C 06 80 2D F8 FF FF 7F  F8 FF FF 7F 6C 73 74 35  ...-........lst5
0080: 1C 07 80 2D F8 FF FF 7F  F8 FF FF 7F 65 6E 64 71  ...-........endq
0090: 4C 1C 08 80 45 00 80 F0  FF FF 7F F0 FF FF 7F 66  L...E..........f
00A0: 64 6F 31 01 80 1C 02 80  45 09 80 F0 FF FF 7F F0  do1.....E.......
00B0: FF FF 7F 77 68 69 31 01  80 4D 52 04 80 F0 FF FF  ...whi1..MR.....
00C0: 7F F0 FF FF 7F 6F 75 7A  61 03 01 10 0A 80 46 00  .....ouza.....F.
00D0: 45 00 80 F0 FF FF 7F F0  FF FF 7F 66 64 69 31 01  E..........fdi1.
00E0: 80 20 00 21 00                                    . .!.           
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
  8: 0x0021 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "ouza" with entities [LocalPlayer, LocalPlayer], work=[94*, 0*]
  9: 0x0032 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 10: 0x0043 [0x1C] WAIT(120* ticks)
 11: 0x0046 [0x2D] CREATE_ZONE_SCHEDULER_TASK: Create scheduler "s151" with entities [EventEntity, EventEntity]
 12: 0x0053 [0x2D] CREATE_ZONE_SCHEDULER_TASK: Create scheduler "lst4" with entities [EventEntity, EventEntity]
 13: 0x0060 [0x1C] WAIT(180* ticks)
 14: 0x0063 [0x2D] CREATE_ZONE_SCHEDULER_TASK: Create scheduler "lst6" with entities [EventEntity, EventEntity]
 15: 0x0070 [0x1C] WAIT(180* ticks)
 16: 0x0073 [0x2D] CREATE_ZONE_SCHEDULER_TASK: Create scheduler "lst5" with entities [EventEntity, EventEntity]
 17: 0x0080 [0x1C] WAIT(300* ticks)
 18: 0x0083 [0x2D] CREATE_ZONE_SCHEDULER_TASK: Create scheduler "endq" with entities [EventEntity, EventEntity]
 19: 0x0090 [0x4C] EventEntity->StatusEvent = 8 // Open door
 20: 0x0091 [0x1C] WAIT(600* ticks)
 21: 0x0094 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 22: 0x00A5 [0x1C] WAIT(60* ticks)
 23: 0x00A8 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "whi1" with entities [LocalPlayer, LocalPlayer], work=[201*, 0*]
 24: 0x00B9 [0x4D] EventEntity->StatusEvent = 9 // Close door
 25: 0x00BA [0x52] END_LOAD_SCHEDULER: End scheduler "ouza" with entities [LocalPlayer, LocalPlayer], work=94*
 26: 0x00C9 [0x03] Work_Zone[1] = 1*
 27: 0x00CE [0x46] CAMERA_CONTROL: Restore default settings
 28: 0x00D0 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 29: 0x00E1 [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
 30: 0x00E3 [0x21] END_EVENT
 31: 0x00E4 [0x00] END_REQSTACK()
```

### Event 203

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x00E5  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00E0:                00                                      .          
```

#### Opcodes

```
  0: 0x00E5 [0x00] END_REQSTACK()
```

### Event 204

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x00E6  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00E0:                   00                                    .         
```

#### Opcodes

```
  0: 0x00E6 [0x00] END_REQSTACK()
```

### Event 65535.1

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x00E7  |
| Data Size    | 2 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00E0:                      4C  00                              L.       
```

#### Opcodes

```
  0: 0x00E7 [0x4C] EventEntity->StatusEvent = 8 // Open door
  1: 0x00E8 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x00E9  |
| Data Size    | 2 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00E0:                             4D 00                          M.     
```

#### Opcodes

```
  0: 0x00E9 [0x4D] EventEntity->StatusEvent = 9 // Close door
  1: 0x00EA [0x00] END_REQSTACK()
```
