# 17600585 - Ildy-Goldy

## Common Data

| Field            | Value                       |
|------------------|-----------------------------|
| Zone             | Cloister of Gales (ID: 201) |
| Block Size       | 404 bytes                   |
| Total Events     | 15                          |
| References Count | 6                           |

## List of Events

| Event ID                   | Entrypoint   |   Size |   Instructions |
|----------------------------|--------------|--------|----------------|
| [65535](#event-65535)      | 0x0000       |      1 |              1 |
| [32000](#event-32000)      | 0x0001       |      1 |              1 |
| [65535.1](#event-655351)   | 0x0002       |     10 |              2 |
| [65535.2](#event-655352)   | 0x000C       |      1 |              1 |
| [65535.3](#event-655353)   | 0x000D       |     57 |              5 |
| [65535.4](#event-655354)   | 0x0046       |     29 |              3 |
| [65535.5](#event-655355)   | 0x0063       |     16 |              2 |
| [65535.6](#event-655356)   | 0x0073       |     14 |              2 |
| [65535.7](#event-655357)   | 0x0081       |     16 |              2 |
| [65535.8](#event-655358)   | 0x0091       |     14 |              2 |
| [65535.9](#event-655359)   | 0x009F       |     16 |              2 |
| [65535.10](#event-6553510) | 0x00AF       |     14 |              2 |
| [65535.11](#event-6553511) | 0x00BD       |     16 |              2 |
| [65535.12](#event-6553512) | 0x00CD       |     14 |              2 |
| [65535.13](#event-6553513) | 0x00DB       |     85 |             12 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x536D      |       21357 |
|       1 | 0x7122      |       28962 |
|       2 | 0xFFFFB8D3  |  4294949075 |
|       3 | 0x018A      |         394 |
|       4 | 0x002F      |          47 |
|       5 | 0x0064      |         100 |

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

### Event 32000

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

### Event 65535.1

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0002   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:       37 00 80 01 80 02  80 03 80 00                7.........    
```

#### Opcodes

```
  0: 0x0002 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=21.357*, z=28.962*, y=-18.221*, direction=34.6°*
  1: 0x000B [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x000C  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                                      00                       .   
```

#### Opcodes

```
  0: 0x000C [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x000D   |
| Data Size    | 57 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                                         66 04 80               f..
0010: F8 FF FF 7F 48 90 0C 01  6D 61 69 6E 53 F8 FF FF  ....H...mainS...
0020: 7F 48 90 0C 01 6D 61 69  6E 66 04 80 F8 FF FF 7F  .H...mainf......
0030: 48 90 0C 01 6D 61 69 6E  53 F8 FF FF 7F 48 90 0C  H...mainS....H..
0040: 01 6D 61 69 6E 00                                 .main.          
```

#### Opcodes

```
  0: 0x000D [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "main" with entities [EventEntity, EV_GARUDA (ID: 17600584/0x010C9048)], work=47*
  1: 0x001C [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "main" with entities [EventEntity, EV_GARUDA (ID: 17600584/0x010C9048)]
  2: 0x0029 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "main" with entities [EventEntity, EV_GARUDA (ID: 17600584/0x010C9048)], work=47*
  3: 0x0038 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "main" with entities [EventEntity, EV_GARUDA (ID: 17600584/0x010C9048)]
  4: 0x0045 [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0046   |
| Data Size    | 29 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                   66 04  80 F8 FF FF 7F F8 FF FF        f.........
0050: 7F 6F 75 74 30 53 F8 FF  FF 7F F8 FF FF 7F 6F 75  .out0S........ou
0060: 74 30 00                                          t0.             
```

#### Opcodes

```
  0: 0x0046 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "out0" with entities [EventEntity, EventEntity], work=47*
  1: 0x0055 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "out0" with entities [EventEntity, EventEntity]
  2: 0x0062 [0x00] END_REQSTACK()
```

### Event 65535.5

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0063   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060:          66 04 80 F8 FF  FF 7F F8 FF FF 7F 62 74     f..........bt
0070: 6C 30 00                                          l0.             
```

#### Opcodes

```
  0: 0x0063 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "btl0" with entities [EventEntity, EventEntity], work=47*
  1: 0x0072 [0x00] END_REQSTACK()
```

### Event 65535.6

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0073   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0070:          53 F8 FF FF 7F  F8 FF FF 7F 62 74 6C 30     S........btl0
0080: 00                                                .               
```

#### Opcodes

```
  0: 0x0073 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "btl0" with entities [EventEntity, EventEntity]
  1: 0x0080 [0x00] END_REQSTACK()
```

### Event 65535.7

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0081   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0080:    66 04 80 F8 FF FF 7F  F8 FF FF 7F 69 6E 30 30   f..........in00
0090: 00                                                .               
```

#### Opcodes

```
  0: 0x0081 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "in00" with entities [EventEntity, EventEntity], work=47*
  1: 0x0090 [0x00] END_REQSTACK()
```

### Event 65535.8

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0091   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0090:    53 F8 FF FF 7F F8 FF  FF 7F 69 6E 30 30 00      S........in00. 
```

#### Opcodes

```
  0: 0x0091 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "in00" with entities [EventEntity, EventEntity]
  1: 0x009E [0x00] END_REQSTACK()
```

### Event 65535.9

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x009F   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0090:                                               66                 f
00A0: 04 80 F8 FF FF 7F F8 FF  FF 7F 6D 61 69 6E 00     ..........main. 
```

#### Opcodes

```
  0: 0x009F [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "main" with entities [EventEntity, EventEntity], work=47*
  1: 0x00AE [0x00] END_REQSTACK()
```

### Event 65535.10

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00AF   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00A0:                                               53                 S
00B0: F8 FF FF 7F F8 FF FF 7F  6D 61 69 6E 00           ........main.   
```

#### Opcodes

```
  0: 0x00AF [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "main" with entities [EventEntity, EventEntity]
  1: 0x00BC [0x00] END_REQSTACK()
```

### Event 65535.11

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00BD   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00B0:                                         66 04 80               f..
00C0: F8 FF FF 7F F8 FF FF 7F  6F 75 74 30 00           ........out0.   
```

#### Opcodes

```
  0: 0x00BD [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "out0" with entities [EventEntity, EventEntity], work=47*
  1: 0x00CC [0x00] END_REQSTACK()
```

### Event 65535.12

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00CD   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00C0:                                         53 F8 FF               S..
00D0: FF 7F F8 FF FF 7F 6F 75  74 30 00                 ......out0.     
```

#### Opcodes

```
  0: 0x00CD [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "out0" with entities [EventEntity, EventEntity]
  1: 0x00DA [0x00] END_REQSTACK()
```

### Event 65535.13

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00DB   |
| Data Size    | 85 bytes |
| Instructions | 12       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00D0:                                   4E 00 49 90 0C             N.I..
00E0: 01 4E 00 48 90 0C 01 80  49 90 0C 01 80 48 90 0C  .N.H....I....H..
00F0: 01 66 04 80 F8 FF FF 7F  F8 FF FF 7F 6D 61 69 6E  .f..........main
0100: 53 F8 FF FF 7F F8 FF FF  7F 6D 61 69 6E 1C 05 80  S........main...
0110: 66 04 80 F8 FF FF 7F F8  FF FF 7F 6D 61 69 6E 53  f..........mainS
0120: F8 FF FF 7F F8 FF FF 7F  6D 61 69 6E 20 00 21 00  ........main .!.
```

#### Opcodes

```
  0: 0x00DB [0x4E] SET_ENTITY_HIDE_FLAG: Show Ildy-Goldy (ID: 17600585/0x010C9049)
  1: 0x00E1 [0x4E] SET_ENTITY_HIDE_FLAG: Show EV_GARUDA (ID: 17600584/0x010C9048)
  2: 0x00E7 [0x80] LOAD_WAIT(entity=Ildy-Goldy (ID: 17600585/0x010C9049))
  3: 0x00EC [0x80] LOAD_WAIT(entity=EV_GARUDA (ID: 17600584/0x010C9048))
  4: 0x00F1 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "main" with entities [EventEntity, EventEntity], work=47*
  5: 0x0100 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "main" with entities [EventEntity, EventEntity]
  6: 0x010D [0x1C] WAIT(100* ticks)
  7: 0x0110 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "main" with entities [EventEntity, EventEntity], work=47*
  8: 0x011F [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "main" with entities [EventEntity, EventEntity]
  9: 0x012C [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
 10: 0x012E [0x21] END_EVENT
 11: 0x012F [0x00] END_REQSTACK()
```
