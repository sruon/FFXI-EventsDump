# 17195776 - Nomad Moogle

## Common Data

| Field            | Value                       |
|------------------|-----------------------------|
| Zone             | La Theine Plateau (ID: 102) |
| Block Size       | 476 bytes                   |
| Total Events     | 27                          |
| References Count | 0                           |

## List of Events

| Event ID                   | Entrypoint   |   Size |   Instructions |
|----------------------------|--------------|--------|----------------|
| [65535](#event-65535)      | 0x0000       |      1 |              1 |
| [65535.1](#event-655351)   | 0x0001       |     14 |              2 |
| [65535.2](#event-655352)   | 0x000F       |     14 |              2 |
| [65535.3](#event-655353)   | 0x001D       |     14 |              2 |
| [65535.4](#event-655354)   | 0x002B       |     14 |              2 |
| [65535.5](#event-655355)   | 0x0039       |     14 |              2 |
| [65535.6](#event-655356)   | 0x0047       |     14 |              2 |
| [65535.7](#event-655357)   | 0x0055       |     14 |              2 |
| [65535.8](#event-655358)   | 0x0063       |     14 |              2 |
| [65535.9](#event-655359)   | 0x0071       |     14 |              2 |
| [65535.10](#event-6553510) | 0x007F       |     14 |              2 |
| [65535.11](#event-6553511) | 0x008D       |     14 |              2 |
| [65535.12](#event-6553512) | 0x009B       |     14 |              2 |
| [65535.13](#event-6553513) | 0x00A9       |     14 |              2 |
| [65535.14](#event-6553514) | 0x00B7       |     14 |              2 |
| [65535.15](#event-6553515) | 0x00C5       |     14 |              2 |
| [65535.16](#event-6553516) | 0x00D3       |     14 |              2 |
| [65535.17](#event-6553517) | 0x00E1       |     14 |              2 |
| [65535.18](#event-6553518) | 0x00EF       |     14 |              2 |
| [65535.19](#event-6553519) | 0x00FD       |     14 |              2 |
| [65535.20](#event-6553520) | 0x010B       |     14 |              2 |
| [65535.21](#event-6553521) | 0x0119       |     14 |              2 |
| [65535.22](#event-6553522) | 0x0127       |     14 |              2 |
| [65535.23](#event-6553523) | 0x0135       |     14 |              2 |
| [65535.24](#event-6553524) | 0x0143       |     14 |              2 |
| [226](#event-226)          | 0x0151       |      7 |              2 |
| [227](#event-227)          | 0x0158       |      7 |              2 |

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

### Event 65535.1

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    2C F8 FF FF 7F F8 FF  FF 7F 65 78 70 30 00      ,........exp0. 
```

#### Opcodes

```
  0: 0x0001 [0x2C] CREATE_SCHEDULER_TASK: Create scheduler "exp0" with entities [EventEntity, EventEntity]
  1: 0x000E [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x000F   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                                               53                 S
0010: F8 FF FF 7F F8 FF FF 7F  65 78 70 30 00           ........exp0.   
```

#### Opcodes

```
  0: 0x000F [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "exp0" with entities [EventEntity, EventEntity]
  1: 0x001C [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x001D   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                                         2C F8 FF               ,..
0020: FF 7F F8 FF FF 7F 65 78  70 31 00                 ......exp1.     
```

#### Opcodes

```
  0: 0x001D [0x2C] CREATE_SCHEDULER_TASK: Create scheduler "exp1" with entities [EventEntity, EventEntity]
  1: 0x002A [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x002B   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                                   53 F8 FF FF 7F             S....
0030: F8 FF FF 7F 65 78 70 31  00                       ....exp1.       
```

#### Opcodes

```
  0: 0x002B [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "exp1" with entities [EventEntity, EventEntity]
  1: 0x0038 [0x00] END_REQSTACK()
```

### Event 65535.5

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0039   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:                             2C F8 FF FF 7F F8 FF           ,......
0040: FF 7F 67 61 6B 30 00                              ..gak0.         
```

#### Opcodes

```
  0: 0x0039 [0x2C] CREATE_SCHEDULER_TASK: Create scheduler "gak0" with entities [EventEntity, EventEntity]
  1: 0x0046 [0x00] END_REQSTACK()
```

### Event 65535.6

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0047   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                      53  F8 FF FF 7F F8 FF FF 7F         S........
0050: 67 61 6B 30 00                                    gak0.           
```

#### Opcodes

```
  0: 0x0047 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "gak0" with entities [EventEntity, EventEntity]
  1: 0x0054 [0x00] END_REQSTACK()
```

### Event 65535.7

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0055   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:                2C F8 FF  FF 7F F8 FF FF 7F 67 61       ,........ga
0060: 6B 31 00                                          k1.             
```

#### Opcodes

```
  0: 0x0055 [0x2C] CREATE_SCHEDULER_TASK: Create scheduler "gak1" with entities [EventEntity, EventEntity]
  1: 0x0062 [0x00] END_REQSTACK()
```

### Event 65535.8

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0063   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060:          53 F8 FF FF 7F  F8 FF FF 7F 67 61 6B 31     S........gak1
0070: 00                                                .               
```

#### Opcodes

```
  0: 0x0063 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "gak1" with entities [EventEntity, EventEntity]
  1: 0x0070 [0x00] END_REQSTACK()
```

### Event 65535.9

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0071   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0070:    2C F8 FF FF 7F F8 FF  FF 7F 6A 6F 62 30 00      ,........job0. 
```

#### Opcodes

```
  0: 0x0071 [0x2C] CREATE_SCHEDULER_TASK: Create scheduler "job0" with entities [EventEntity, EventEntity]
  1: 0x007E [0x00] END_REQSTACK()
```

### Event 65535.10

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x007F   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0070:                                               53                 S
0080: F8 FF FF 7F F8 FF FF 7F  6A 6F 62 30 00           ........job0.   
```

#### Opcodes

```
  0: 0x007F [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "job0" with entities [EventEntity, EventEntity]
  1: 0x008C [0x00] END_REQSTACK()
```

### Event 65535.11

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x008D   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0080:                                         2C F8 FF               ,..
0090: FF 7F F8 FF FF 7F 6A 6F  62 31 00                 ......job1.     
```

#### Opcodes

```
  0: 0x008D [0x2C] CREATE_SCHEDULER_TASK: Create scheduler "job1" with entities [EventEntity, EventEntity]
  1: 0x009A [0x00] END_REQSTACK()
```

### Event 65535.12

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x009B   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0090:                                   53 F8 FF FF 7F             S....
00A0: F8 FF FF 7F 6A 6F 62 31  00                       ....job1.       
```

#### Opcodes

```
  0: 0x009B [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "job1" with entities [EventEntity, EventEntity]
  1: 0x00A8 [0x00] END_REQSTACK()
```

### Event 65535.13

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00A9   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00A0:                             2C F8 FF FF 7F F8 FF           ,......
00B0: FF 7F 68 61 70 30 00                              ..hap0.         
```

#### Opcodes

```
  0: 0x00A9 [0x2C] CREATE_SCHEDULER_TASK: Create scheduler "hap0" with entities [EventEntity, EventEntity]
  1: 0x00B6 [0x00] END_REQSTACK()
```

### Event 65535.14

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00B7   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00B0:                      53  F8 FF FF 7F F8 FF FF 7F         S........
00C0: 68 61 70 30 00                                    hap0.           
```

#### Opcodes

```
  0: 0x00B7 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "hap0" with entities [EventEntity, EventEntity]
  1: 0x00C4 [0x00] END_REQSTACK()
```

### Event 65535.15

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00C5   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00C0:                2C F8 FF  FF 7F F8 FF FF 7F 68 61       ,........ha
00D0: 70 31 00                                          p1.             
```

#### Opcodes

```
  0: 0x00C5 [0x2C] CREATE_SCHEDULER_TASK: Create scheduler "hap1" with entities [EventEntity, EventEntity]
  1: 0x00D2 [0x00] END_REQSTACK()
```

### Event 65535.16

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00D3   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00D0:          53 F8 FF FF 7F  F8 FF FF 7F 68 61 70 31     S........hap1
00E0: 00                                                .               
```

#### Opcodes

```
  0: 0x00D3 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "hap1" with entities [EventEntity, EventEntity]
  1: 0x00E0 [0x00] END_REQSTACK()
```

### Event 65535.17

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00E1   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00E0:    2C F8 FF FF 7F F8 FF  FF 7F 6E 65 77 30 00      ,........new0. 
```

#### Opcodes

```
  0: 0x00E1 [0x2C] CREATE_SCHEDULER_TASK: Create scheduler "new0" with entities [EventEntity, EventEntity]
  1: 0x00EE [0x00] END_REQSTACK()
```

### Event 65535.18

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00EF   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00E0:                                               53                 S
00F0: F8 FF FF 7F F8 FF FF 7F  6E 65 77 30 00           ........new0.   
```

#### Opcodes

```
  0: 0x00EF [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "new0" with entities [EventEntity, EventEntity]
  1: 0x00FC [0x00] END_REQSTACK()
```

### Event 65535.19

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00FD   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00F0:                                         2C F8 FF               ,..
0100: FF 7F F8 FF FF 7F 6E 65  77 31 00                 ......new1.     
```

#### Opcodes

```
  0: 0x00FD [0x2C] CREATE_SCHEDULER_TASK: Create scheduler "new1" with entities [EventEntity, EventEntity]
  1: 0x010A [0x00] END_REQSTACK()
```

### Event 65535.20

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x010B   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0100:                                   53 F8 FF FF 7F             S....
0110: F8 FF FF 7F 6E 65 77 31  00                       ....new1.       
```

#### Opcodes

```
  0: 0x010B [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "new1" with entities [EventEntity, EventEntity]
  1: 0x0118 [0x00] END_REQSTACK()
```

### Event 65535.21

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0119   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0110:                             2C F8 FF FF 7F F8 FF           ,......
0120: FF 7F 74 6C 6B 30 00                              ..tlk0.         
```

#### Opcodes

```
  0: 0x0119 [0x2C] CREATE_SCHEDULER_TASK: Create scheduler "tlk0" with entities [EventEntity, EventEntity]
  1: 0x0126 [0x00] END_REQSTACK()
```

### Event 65535.22

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0127   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0120:                      53  F8 FF FF 7F F8 FF FF 7F         S........
0130: 74 6C 6B 30 00                                    tlk0.           
```

#### Opcodes

```
  0: 0x0127 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "tlk0" with entities [EventEntity, EventEntity]
  1: 0x0134 [0x00] END_REQSTACK()
```

### Event 65535.23

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0135   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0130:                2C F8 FF  FF 7F F8 FF FF 7F 74 6C       ,........tl
0140: 6B 31 00                                          k1.             
```

#### Opcodes

```
  0: 0x0135 [0x2C] CREATE_SCHEDULER_TASK: Create scheduler "tlk1" with entities [EventEntity, EventEntity]
  1: 0x0142 [0x00] END_REQSTACK()
```

### Event 65535.24

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0143   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0140:          53 F8 FF FF 7F  F8 FF FF 7F 74 6C 6B 31     S........tlk1
0150: 00                                                .               
```

#### Opcodes

```
  0: 0x0143 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "tlk1" with entities [EventEntity, EventEntity]
  1: 0x0150 [0x00] END_REQSTACK()
```

### Event 226

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0151  |
| Data Size    | 7 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0150:    92 01 F8 FF FF 7F 00                            .......        
```

#### Opcodes

```
  0: 0x0151 [0x92] EventEntity->Render.Flags3 ^= 0x01
  1: 0x0157 [0x00] END_REQSTACK()
```

### Event 227

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0158  |
| Data Size    | 7 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0150:                          92 01 F8 FF FF 7F 00             ....... 
```

#### Opcodes

```
  0: 0x0158 [0x92] EventEntity->Render.Flags3 ^= 0x01
  1: 0x015E [0x00] END_REQSTACK()
```
