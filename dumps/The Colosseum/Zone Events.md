# 0x7FFFFFF0 - Zone Events

## Common Data

| Field            | Value                  |
|------------------|------------------------|
| Zone             | The Colosseum (ID: 71) |
| Block Size       | 328 bytes              |
| Total Events     | 7                      |
| References Count | 16                     |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [65534](#event-65534) | 0x0001       |      1 |              1 |
| [50](#event-50)       | 0x0002       |      9 |              4 |
| [800](#event-800)     | 0x000B       |     52 |              8 |
| [801](#event-801)     | 0x003F       |     52 |              8 |
| [802](#event-802)     | 0x0073       |     52 |              8 |
| [803](#event-803)     | 0x00A7       |     52 |              8 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0001      |           1 |
|       1 | 0x00C8      |         200 |
|       2 | 0x0000      |           0 |
|       3 | 0x003C      |          60 |
|       4 | 0xFFF6E659  |  4294370905 |
|       5 | 0x9BD5      |       39893 |
|       6 | 0x0FFC      |        4092 |
|       7 | 0xFFF6E6E1  |  4294371041 |
|       8 | 0xFFFF6365  |  4294927205 |
|       9 | 0x0004      |           4 |
|      10 | 0xFFF8FC97  |  4294507671 |
|      11 | 0x9CD6      |       40150 |
|      12 | 0x07F5      |        2037 |
|      13 | 0xFFF8FC1E  |  4294507550 |
|      14 | 0xFFFF63AD  |  4294927277 |
|      15 | 0x07FE      |        2046 |

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

### Event 50

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0002  |
| Data Size    | 9 bytes |
| Instructions | 4       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:       20 01 03 01 10 00  80 21 00                    ......!.     
```

#### Opcodes

```
  0: 0x0002 [0x20] SET_CLI_EVENT_UC_FLAG: Lock player control
  1: 0x0004 [0x03] Work_Zone[1] = 1*
  2: 0x0009 [0x21] END_EVENT
  3: 0x000A [0x00] END_REQSTACK()
```

### Event 800

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x000B   |
| Data Size    | 52 bytes |
| Instructions | 8        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                                   42 45 01 80 F8             BE...
0010: FF FF 7F F8 FF FF 7F 66  64 6F 31 02 80 1C 03 80  .......fdo1.....
0020: 47 00 04 80 05 80 02 80  06 80 47 01 45 01 80 F8  G.........G.E...
0030: FF FF 7F F8 FF FF 7F 66  64 69 31 02 80 21 00     .......fdi1..!. 
```

#### Opcodes

```
  0: 0x000B [0x42] SET_CLI_EVENT_CANCEL_DATA()
  1: 0x000C [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [EventEntity, EventEntity], work=[200*, 0*]
  2: 0x001D [0x1C] WAIT(60* ticks)
  3: 0x0020 [0x47] UPDATE_PLAYER_POS(-596.391*, 39.893*, 0.000*, yaw=359.6°*)
  4: 0x002A [0x47] WAIT_PLAYER_POS_UPDATE
  5: 0x002C [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi1" with entities [EventEntity, EventEntity], work=[200*, 0*]
  6: 0x003D [0x21] END_EVENT
  7: 0x003E [0x00] END_REQSTACK()
```

### Event 801

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x003F   |
| Data Size    | 52 bytes |
| Instructions | 8        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:                                               42                 B
0040: 45 01 80 F8 FF FF 7F F8  FF FF 7F 66 64 6F 31 02  E..........fdo1.
0050: 80 1C 03 80 47 00 07 80  08 80 02 80 09 80 47 01  ....G.........G.
0060: 45 01 80 F8 FF FF 7F F8  FF FF 7F 66 64 69 31 02  E..........fdi1.
0070: 80 21 00                                          .!.             
```

#### Opcodes

```
  0: 0x003F [0x42] SET_CLI_EVENT_CANCEL_DATA()
  1: 0x0040 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [EventEntity, EventEntity], work=[200*, 0*]
  2: 0x0051 [0x1C] WAIT(60* ticks)
  3: 0x0054 [0x47] UPDATE_PLAYER_POS(-596.255*, -40.091*, 0.000*, yaw=0.4°*)
  4: 0x005E [0x47] WAIT_PLAYER_POS_UPDATE
  5: 0x0060 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi1" with entities [EventEntity, EventEntity], work=[200*, 0*]
  6: 0x0071 [0x21] END_EVENT
  7: 0x0072 [0x00] END_REQSTACK()
```

### Event 802

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0073   |
| Data Size    | 52 bytes |
| Instructions | 8        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0070:          42 45 01 80 F8  FF FF 7F F8 FF FF 7F 66     BE..........f
0080: 64 6F 31 02 80 1C 03 80  47 00 0A 80 0B 80 02 80  do1.....G.......
0090: 0C 80 47 01 45 01 80 F8  FF FF 7F F8 FF FF 7F 66  ..G.E..........f
00A0: 64 69 31 02 80 21 00                              di1..!.         
```

#### Opcodes

```
  0: 0x0073 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  1: 0x0074 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [EventEntity, EventEntity], work=[200*, 0*]
  2: 0x0085 [0x1C] WAIT(60* ticks)
  3: 0x0088 [0x47] UPDATE_PLAYER_POS(-459.625*, 40.150*, 0.000*, yaw=179.0°*)
  4: 0x0092 [0x47] WAIT_PLAYER_POS_UPDATE
  5: 0x0094 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi1" with entities [EventEntity, EventEntity], work=[200*, 0*]
  6: 0x00A5 [0x21] END_EVENT
  7: 0x00A6 [0x00] END_REQSTACK()
```

### Event 803

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00A7   |
| Data Size    | 52 bytes |
| Instructions | 8        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00A0:                      42  45 01 80 F8 FF FF 7F F8         BE.......
00B0: FF FF 7F 66 64 6F 31 02  80 1C 03 80 47 00 0D 80  ...fdo1.....G...
00C0: 0E 80 02 80 0F 80 47 01  45 01 80 F8 FF FF 7F F8  ......G.E.......
00D0: FF FF 7F 66 64 69 31 02  80 21 00                 ...fdi1..!.     
```

#### Opcodes

```
  0: 0x00A7 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  1: 0x00A8 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [EventEntity, EventEntity], work=[200*, 0*]
  2: 0x00B9 [0x1C] WAIT(60* ticks)
  3: 0x00BC [0x47] UPDATE_PLAYER_POS(-459.746*, -40.019*, 0.000*, yaw=179.8°*)
  4: 0x00C6 [0x47] WAIT_PLAYER_POS_UPDATE
  5: 0x00C8 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi1" with entities [EventEntity, EventEntity], work=[200*, 0*]
  6: 0x00D9 [0x21] END_EVENT
  7: 0x00DA [0x00] END_REQSTACK()
```
