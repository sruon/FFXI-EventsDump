# 17261138 - Song Runes

## Common Data

| Field            | Value                        |
|------------------|------------------------------|
| Zone             | Buburimu Peninsula (ID: 118) |
| Block Size       | 224 bytes                    |
| Total Events     | 5                            |
| References Count | 3                            |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [0](#event-0)            | 0x0001       |      1 |              1 |
| [2](#event-2)            | 0x0002       |     22 |              5 |
| [65535.1](#event-655351) | 0x0018       |    148 |             10 |
| [65535.2](#event-655352) | 0x00AC       |      1 |              1 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x00C9      |         201 |
|       1 | 0x0000      |           0 |
|       2 | 0x0092      |         146 |

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

### Event 0

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

### Event 2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0002   |
| Data Size    | 22 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:       20 01 42 45 00 80  F0 FF FF 7F F0 FF FF 7F     .BE..........
0010: 71 73 74 63 01 80 21 00                           qstc..!.        
```

#### Opcodes

```
  0: 0x0002 [0x20] SET_CLI_EVENT_UC_FLAG: Lock player control
  1: 0x0004 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  2: 0x0005 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "qstc" with entities [LocalPlayer, LocalPlayer], work=[201*, 0*]
  3: 0x0016 [0x21] END_EVENT
  4: 0x0017 [0x00] END_REQSTACK()
```

### Event 65535.1

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x0018    |
| Data Size    | 148 bytes |
| Instructions | 10        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                          45 00 80 F0 FF FF 7F F0          E.......
0020: FF FF 7F 77 68 6F 31 01  80 55 00 80 F0 FF FF 7F  ...who1..U......
0030: F0 FF FF 7F 77 68 6F 31  45 00 80 F0 FF FF 7F F0  ....who1E.......
0040: FF FF 7F 77 68 69 31 01  80 45 02 80 F8 FF FF 7F  ...whi1..E......
0050: F8 FF FF 7F 63 6D 31 33  01 80 55 02 80 F8 FF FF  ....cm13..U.....
0060: 7F F8 FF FF 7F 63 6D 31  33 45 00 80 F0 FF FF 7F  .....cm13E......
0070: F0 FF FF 7F 77 68 6F 31  01 80 55 00 80 F0 FF FF  ....who1..U.....
0080: 7F F0 FF FF 7F 77 68 6F  31 45 00 80 F0 FF FF 7F  .....who1E......
0090: F0 FF FF 7F 77 68 69 31  01 80 45 02 80 F8 FF FF  ....whi1..E.....
00A0: 7F F8 FF FF 7F 63 6D 31  35 01 80 00              .....cm15...    
```

#### Opcodes

```
  0: 0x0018 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "who1" with entities [LocalPlayer, LocalPlayer], work=[201*, 0*]
  1: 0x0029 [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "who1" with entities [LocalPlayer, LocalPlayer], work=201*
  2: 0x0038 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "whi1" with entities [LocalPlayer, LocalPlayer], work=[201*, 0*]
  3: 0x0049 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "cm13" with entities [EventEntity, EventEntity], work=[146*, 0*]
  4: 0x005A [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "cm13" with entities [EventEntity, EventEntity], work=146*
  5: 0x0069 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "who1" with entities [LocalPlayer, LocalPlayer], work=[201*, 0*]
  6: 0x007A [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "who1" with entities [LocalPlayer, LocalPlayer], work=201*
  7: 0x0089 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "whi1" with entities [LocalPlayer, LocalPlayer], work=[201*, 0*]
  8: 0x009A [0x45] LOAD_SCHEDULED_TASK: Load scheduler "cm15" with entities [EventEntity, EventEntity], work=[146*, 0*]
  9: 0x00AB [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x00AC  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00A0:                                      00                       .   
```

#### Opcodes

```
  0: 0x00AC [0x00] END_REQSTACK()
```
