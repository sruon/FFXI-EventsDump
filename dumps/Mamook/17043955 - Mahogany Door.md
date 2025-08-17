# 17043955 - Mahogany Door

## Common Data

| Field            | Value           |
|------------------|-----------------|
| Zone             | Mamook (ID: 65) |
| Block Size       | 252 bytes       |
| Total Events     | 5               |
| References Count | 7               |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [216](#event-216)        | 0x0001       |    144 |             26 |
| [32000](#event-32000)    | 0x0091       |      1 |              1 |
| [65535.1](#event-655351) | 0x0092       |      2 |              2 |
| [65535.2](#event-655352) | 0x0094       |     40 |              6 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x00C8      |         200 |
|       1 | 0x0000      |           0 |
|       2 | 0x003C      |          60 |
|       3 | 0x0013      |          19 |
|       4 | 0x00D9      |         217 |
|       5 | 0x00B4      |         180 |
|       6 | 0x00F0      |         240 |

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

### Event 216

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x0001    |
| Data Size    | 144 bytes |
| Instructions | 26        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    20 01 43 00 43 01 46  01 42 45 00 80 F0 FF FF    .C.C.F.BE.....
0010: 7F F0 FF FF 7F 66 64 6F  31 01 80 1C 02 80 38 03  .....fdo1.....8.
0020: 80 45 04 80 F0 FF FF 7F  F0 FF FF 7F 62 63 36 35  .E..........bc65
0030: 01 80 29 01 F0 FF FF 7F  0A 29 01 F0 FF FF 7F 08  ..)......)......
0040: 45 00 80 F0 FF FF 7F F0  FF FF 7F 66 64 69 31 01  E..........fdi1.
0050: 80 1C 02 80 4C 1C 02 80  27 01 F0 FF FF 7F 09 1C  ....L...'.......
0060: 05 80 45 00 80 F0 FF FF  7F F0 FF FF 7F 66 64 6F  ..E..........fdo
0070: 31 01 80 1C 02 80 4D 46  00 1C 06 80 45 00 80 F0  1.....MF....E...
0080: FF FF 7F F0 FF FF 7F 66  64 69 31 01 80 20 00 21  .......fdi1.. .!
0090: 00                                                .               
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
  8: 0x0021 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "bc65" with entities [LocalPlayer, LocalPlayer], work=[217*, 0*]
  9: 0x0032 [0x29] REQ_SET_WAIT(priority=0x01, entity_id=LocalPlayer, tag_num=0x0A)
 10: 0x0039 [0x29] REQ_SET_WAIT(priority=0x01, entity_id=LocalPlayer, tag_num=0x08)
 11: 0x0040 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 12: 0x0051 [0x1C] WAIT(60* ticks)
 13: 0x0054 [0x4C] EventEntity->StatusEvent = 8 // Open door
 14: 0x0055 [0x1C] WAIT(60* ticks)
 15: 0x0058 [0x27] REQ_SET(priority=0x01, entity_id=LocalPlayer, tag_num=0x09)
 16: 0x005F [0x1C] WAIT(180* ticks)
 17: 0x0062 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 18: 0x0073 [0x1C] WAIT(60* ticks)
 19: 0x0076 [0x4D] EventEntity->StatusEvent = 9 // Close door
 20: 0x0077 [0x46] CAMERA_CONTROL: Restore default settings
 21: 0x0079 [0x1C] WAIT(240* ticks)
 22: 0x007C [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 23: 0x008D [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
 24: 0x008F [0x21] END_EVENT
 25: 0x0090 [0x00] END_REQSTACK()
```

### Event 32000

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0091  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0090:    00                                              .              
```

#### Opcodes

```
  0: 0x0091 [0x00] END_REQSTACK()
```

### Event 65535.1

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0092  |
| Data Size    | 2 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0090:       4C 00                                         L.            
```

#### Opcodes

```
  0: 0x0092 [0x4C] EventEntity->StatusEvent = 8 // Open door
  1: 0x0093 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0094   |
| Data Size    | 40 bytes |
| Instructions | 6        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0090:             1C 05 80 4D  1C 02 80 45 00 80 F0 FF      ...M...E....
00A0: FF 7F F0 FF FF 7F 66 64  6F 31 01 80 55 00 80 F0  ......fdo1..U...
00B0: FF FF 7F F0 FF FF 7F 66  64 6F 31 00              .......fdo1.    
```

#### Opcodes

```
  0: 0x0094 [0x1C] WAIT(180* ticks)
  1: 0x0097 [0x4D] EventEntity->StatusEvent = 9 // Close door
  2: 0x0098 [0x1C] WAIT(60* ticks)
  3: 0x009B [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
  4: 0x00AC [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=200*
  5: 0x00BB [0x00] END_REQSTACK()
```
