# 17494806 - Noillurie

## Common Data

| Field            | Value                                |
|------------------|--------------------------------------|
| Zone             | The Eldieme Necropolis [S] (ID: 175) |
| Block Size       | 704 bytes                            |
| Total Events     | 36                                   |
| References Count | 6                                    |

## List of Events

| Event ID                   | Entrypoint   |   Size |   Instructions |
|----------------------------|--------------|--------|----------------|
| [65535](#event-65535)      | 0x0000       |      1 |              1 |
| [49](#event-49)            | 0x0001       |      7 |              2 |
| [65535.1](#event-655351)   | 0x0008       |     16 |              2 |
| [65535.2](#event-655352)   | 0x0018       |     14 |              2 |
| [65535.3](#event-655353)   | 0x0026       |     16 |              2 |
| [65535.4](#event-655354)   | 0x0036       |     14 |              2 |
| [65535.5](#event-655355)   | 0x0044       |     16 |              2 |
| [65535.6](#event-655356)   | 0x0054       |     14 |              2 |
| [65535.7](#event-655357)   | 0x0062       |     16 |              2 |
| [65535.8](#event-655358)   | 0x0072       |     14 |              2 |
| [65535.9](#event-655359)   | 0x0080       |     16 |              2 |
| [65535.10](#event-6553510) | 0x0090       |     14 |              2 |
| [65535.11](#event-6553511) | 0x009E       |     16 |              2 |
| [65535.12](#event-6553512) | 0x00AE       |     14 |              2 |
| [65535.13](#event-6553513) | 0x00BC       |     16 |              2 |
| [65535.14](#event-6553514) | 0x00CC       |     14 |              2 |
| [65535.15](#event-6553515) | 0x00DA       |     16 |              2 |
| [65535.16](#event-6553516) | 0x00EA       |     14 |              2 |
| [65535.17](#event-6553517) | 0x00F8       |     16 |              2 |
| [65535.18](#event-6553518) | 0x0108       |     14 |              2 |
| [65535.19](#event-6553519) | 0x0116       |     16 |              2 |
| [65535.20](#event-6553520) | 0x0126       |     14 |              2 |
| [65535.21](#event-6553521) | 0x0134       |     16 |              2 |
| [65535.22](#event-6553522) | 0x0144       |     14 |              2 |
| [65535.23](#event-6553523) | 0x0152       |     16 |              2 |
| [65535.24](#event-6553524) | 0x0162       |     14 |              2 |
| [65535.25](#event-6553525) | 0x0170       |     16 |              2 |
| [65535.26](#event-6553526) | 0x0180       |     14 |              2 |
| [65535.27](#event-6553527) | 0x018E       |     16 |              2 |
| [65535.28](#event-6553528) | 0x019E       |     14 |              2 |
| [65535.29](#event-6553529) | 0x01AC       |     16 |              2 |
| [65535.30](#event-6553530) | 0x01BC       |     14 |              2 |
| [65535.31](#event-6553531) | 0x01CA       |     16 |              2 |
| [65535.32](#event-6553532) | 0x01DA       |     14 |              2 |
| [65535.33](#event-6553533) | 0x01E8       |     16 |              2 |
| [65535.34](#event-6553534) | 0x01F8       |     14 |              2 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0964      |        2404 |
|       1 | 0x0968      |        2408 |
|       2 | 0x0969      |        2409 |
|       3 | 0x096A      |        2410 |
|       4 | 0x0B4E      |        2894 |
|       5 | 0x0B4F      |        2895 |

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

### Event 49

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0001  |
| Data Size    | 7 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    92 01 F8 FF FF 7F 00                            .......        
```

#### Opcodes

```
  0: 0x0001 [0x92] EventEntity->Render.Flags3 ^= 0x01
  1: 0x0007 [0x00] END_REQSTACK()
```

### Event 65535.1

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0008   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                          5B 00 80 F8 FF FF 7F F8          [.......
0010: FF FF 7F 79 65 73 30 00                           ...yes0.        
```

#### Opcodes

```
  0: 0x0008 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "yes0" with entities [EventEntity, EventEntity], work=2404*
  1: 0x0017 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0018   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                          53 F8 FF FF 7F F8 FF FF          S.......
0020: 7F 79 65 73 30 00                                 .yes0.          
```

#### Opcodes

```
  0: 0x0018 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "yes0" with entities [EventEntity, EventEntity]
  1: 0x0025 [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0026   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                   5B 00  80 F8 FF FF 7F F8 FF FF        [.........
0030: 7F 64 6F 6E 30 00                                 .don0.          
```

#### Opcodes

```
  0: 0x0026 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "don0" with entities [EventEntity, EventEntity], work=2404*
  1: 0x0035 [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0036   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:                   53 F8  FF FF 7F F8 FF FF 7F 64        S........d
0040: 6F 6E 30 00                                       on0.            
```

#### Opcodes

```
  0: 0x0036 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "don0" with entities [EventEntity, EventEntity]
  1: 0x0043 [0x00] END_REQSTACK()
```

### Event 65535.5

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0044   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:             5B 00 80 F8  FF FF 7F F8 FF FF 7F 64      [..........d
0050: 6F 6E 31 00                                       on1.            
```

#### Opcodes

```
  0: 0x0044 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "don1" with entities [EventEntity, EventEntity], work=2404*
  1: 0x0053 [0x00] END_REQSTACK()
```

### Event 65535.6

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0054   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:             53 F8 FF FF  7F F8 FF FF 7F 64 6F 6E      S........don
0060: 31 00                                             1.              
```

#### Opcodes

```
  0: 0x0054 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "don1" with entities [EventEntity, EventEntity]
  1: 0x0061 [0x00] END_REQSTACK()
```

### Event 65535.7

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0062   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060:       5B 00 80 F8 FF FF  7F F8 FF FF 7F 64 70 63    [..........dpc
0070: 30 00                                             0.              
```

#### Opcodes

```
  0: 0x0062 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "dpc0" with entities [EventEntity, EventEntity], work=2404*
  1: 0x0071 [0x00] END_REQSTACK()
```

### Event 65535.8

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0072   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0070:       53 F8 FF FF 7F F8  FF FF 7F 64 70 63 30 00    S........dpc0.
```

#### Opcodes

```
  0: 0x0072 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "dpc0" with entities [EventEntity, EventEntity]
  1: 0x007F [0x00] END_REQSTACK()
```

### Event 65535.9

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0080   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0080: 5B 00 80 F8 FF FF 7F F8  FF FF 7F 64 70 63 31 00  [..........dpc1.
```

#### Opcodes

```
  0: 0x0080 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "dpc1" with entities [EventEntity, EventEntity], work=2404*
  1: 0x008F [0x00] END_REQSTACK()
```

### Event 65535.10

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0090   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0090: 53 F8 FF FF 7F F8 FF FF  7F 64 70 63 31 00        S........dpc1.  
```

#### Opcodes

```
  0: 0x0090 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "dpc1" with entities [EventEntity, EventEntity]
  1: 0x009D [0x00] END_REQSTACK()
```

### Event 65535.11

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x009E   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0090:                                            5B 01                [.
00A0: 80 F8 FF FF 7F F8 FF FF  7F 73 65 69 30 00        .........sei0.  
```

#### Opcodes

```
  0: 0x009E [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "sei0" with entities [EventEntity, EventEntity], work=2408*
  1: 0x00AD [0x00] END_REQSTACK()
```

### Event 65535.12

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00AE   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00A0:                                            53 F8                S.
00B0: FF FF 7F F8 FF FF 7F 73  65 69 30 00              .......sei0.    
```

#### Opcodes

```
  0: 0x00AE [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "sei0" with entities [EventEntity, EventEntity]
  1: 0x00BB [0x00] END_REQSTACK()
```

### Event 65535.13

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00BC   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00B0:                                      5B 01 80 F8              [...
00C0: FF FF 7F F8 FF FF 7F 73  65 69 31 00              .......sei1.    
```

#### Opcodes

```
  0: 0x00BC [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "sei1" with entities [EventEntity, EventEntity], work=2408*
  1: 0x00CB [0x00] END_REQSTACK()
```

### Event 65535.14

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00CC   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00C0:                                      53 F8 FF FF              S...
00D0: 7F F8 FF FF 7F 73 65 69  31 00                    .....sei1.      
```

#### Opcodes

```
  0: 0x00CC [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "sei1" with entities [EventEntity, EventEntity]
  1: 0x00D9 [0x00] END_REQSTACK()
```

### Event 65535.15

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00DA   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00D0:                                5B 01 80 F8 FF FF            [.....
00E0: 7F F8 FF FF 7F 73 72 61  30 00                    .....sra0.      
```

#### Opcodes

```
  0: 0x00DA [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "sra0" with entities [EventEntity, EventEntity], work=2408*
  1: 0x00E9 [0x00] END_REQSTACK()
```

### Event 65535.16

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00EA   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00E0:                                53 F8 FF FF 7F F8            S.....
00F0: FF FF 7F 73 72 61 30 00                           ...sra0.        
```

#### Opcodes

```
  0: 0x00EA [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "sra0" with entities [EventEntity, EventEntity]
  1: 0x00F7 [0x00] END_REQSTACK()
```

### Event 65535.17

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00F8   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00F0:                          5B 02 80 F8 FF FF 7F F8          [.......
0100: FF FF 7F 6B 61 6D 30 00                           ...kam0.        
```

#### Opcodes

```
  0: 0x00F8 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "kam0" with entities [EventEntity, EventEntity], work=2409*
  1: 0x0107 [0x00] END_REQSTACK()
```

### Event 65535.18

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0108   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0100:                          53 F8 FF FF 7F F8 FF FF          S.......
0110: 7F 6B 61 6D 30 00                                 .kam0.          
```

#### Opcodes

```
  0: 0x0108 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "kam0" with entities [EventEntity, EventEntity]
  1: 0x0115 [0x00] END_REQSTACK()
```

### Event 65535.19

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0116   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0110:                   5B 02  80 F8 FF FF 7F F8 FF FF        [.........
0120: 7F 6D 6F 74 30 00                                 .mot0.          
```

#### Opcodes

```
  0: 0x0116 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "mot0" with entities [EventEntity, EventEntity], work=2409*
  1: 0x0125 [0x00] END_REQSTACK()
```

### Event 65535.20

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0126   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0120:                   53 F8  FF FF 7F F8 FF FF 7F 6D        S........m
0130: 6F 74 30 00                                       ot0.            
```

#### Opcodes

```
  0: 0x0126 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "mot0" with entities [EventEntity, EventEntity]
  1: 0x0133 [0x00] END_REQSTACK()
```

### Event 65535.21

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0134   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0130:             5B 03 80 F8  FF FF 7F F8 FF FF 7F 6D      [..........m
0140: 6F 6E 30 00                                       on0.            
```

#### Opcodes

```
  0: 0x0134 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "mon0" with entities [EventEntity, EventEntity], work=2410*
  1: 0x0143 [0x00] END_REQSTACK()
```

### Event 65535.22

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0144   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0140:             53 F8 FF FF  7F F8 FF FF 7F 6D 6F 6E      S........mon
0150: 30 00                                             0.              
```

#### Opcodes

```
  0: 0x0144 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "mon0" with entities [EventEntity, EventEntity]
  1: 0x0151 [0x00] END_REQSTACK()
```

### Event 65535.23

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0152   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0150:       5B 03 80 F8 FF FF  7F F8 FF FF 7F 6D 6F 6E    [..........mon
0160: 31 00                                             1.              
```

#### Opcodes

```
  0: 0x0152 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "mon1" with entities [EventEntity, EventEntity], work=2410*
  1: 0x0161 [0x00] END_REQSTACK()
```

### Event 65535.24

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0162   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0160:       53 F8 FF FF 7F F8  FF FF 7F 6D 6F 6E 31 00    S........mon1.
```

#### Opcodes

```
  0: 0x0162 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "mon1" with entities [EventEntity, EventEntity]
  1: 0x016F [0x00] END_REQSTACK()
```

### Event 65535.25

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0170   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0170: 5B 04 80 F8 FF FF 7F F8  FF FF 7F 64 73 68 30 00  [..........dsh0.
```

#### Opcodes

```
  0: 0x0170 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "dsh0" with entities [EventEntity, EventEntity], work=2894*
  1: 0x017F [0x00] END_REQSTACK()
```

### Event 65535.26

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0180   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0180: 53 F8 FF FF 7F F8 FF FF  7F 64 73 68 30 00        S........dsh0.  
```

#### Opcodes

```
  0: 0x0180 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "dsh0" with entities [EventEntity, EventEntity]
  1: 0x018D [0x00] END_REQSTACK()
```

### Event 65535.27

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x018E   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0180:                                            5B 04                [.
0190: 80 F8 FF FF 7F F8 FF FF  7F 6E 79 72 30 00        .........nyr0.  
```

#### Opcodes

```
  0: 0x018E [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "nyr0" with entities [EventEntity, EventEntity], work=2894*
  1: 0x019D [0x00] END_REQSTACK()
```

### Event 65535.28

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x019E   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0190:                                            53 F8                S.
01A0: FF FF 7F F8 FF FF 7F 6E  79 72 30 00              .......nyr0.    
```

#### Opcodes

```
  0: 0x019E [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "nyr0" with entities [EventEntity, EventEntity]
  1: 0x01AB [0x00] END_REQSTACK()
```

### Event 65535.29

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x01AC   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
01A0:                                      5B 04 80 F8              [...
01B0: FF FF 7F F8 FF FF 7F 6E  79 72 31 00              .......nyr1.    
```

#### Opcodes

```
  0: 0x01AC [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "nyr1" with entities [EventEntity, EventEntity], work=2894*
  1: 0x01BB [0x00] END_REQSTACK()
```

### Event 65535.30

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x01BC   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
01B0:                                      53 F8 FF FF              S...
01C0: 7F F8 FF FF 7F 6E 79 72  31 00                    .....nyr1.      
```

#### Opcodes

```
  0: 0x01BC [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "nyr1" with entities [EventEntity, EventEntity]
  1: 0x01C9 [0x00] END_REQSTACK()
```

### Event 65535.31

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x01CA   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
01C0:                                5B 05 80 F8 FF FF            [.....
01D0: 7F F8 FF FF 7F 64 65 6D  31 00                    .....dem1.      
```

#### Opcodes

```
  0: 0x01CA [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "dem1" with entities [EventEntity, EventEntity], work=2895*
  1: 0x01D9 [0x00] END_REQSTACK()
```

### Event 65535.32

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x01DA   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
01D0:                                53 F8 FF FF 7F F8            S.....
01E0: FF FF 7F 64 65 6D 31 00                           ...dem1.        
```

#### Opcodes

```
  0: 0x01DA [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "dem1" with entities [EventEntity, EventEntity]
  1: 0x01E7 [0x00] END_REQSTACK()
```

### Event 65535.33

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x01E8   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
01E0:                          5B 05 80 F8 FF FF 7F F8          [.......
01F0: FF FF 7F 64 65 6D 32 00                           ...dem2.        
```

#### Opcodes

```
  0: 0x01E8 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "dem2" with entities [EventEntity, EventEntity], work=2895*
  1: 0x01F7 [0x00] END_REQSTACK()
```

### Event 65535.34

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x01F8   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
01F0:                          53 F8 FF FF 7F F8 FF FF          S.......
0200: 7F 64 65 6D 32 00                                 .dem2.          
```

#### Opcodes

```
  0: 0x01F8 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "dem2" with entities [EventEntity, EventEntity]
  1: 0x0205 [0x00] END_REQSTACK()
```
