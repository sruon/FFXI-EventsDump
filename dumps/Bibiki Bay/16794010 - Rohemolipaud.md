# 16794010 - Rohemolipaud

## Common Data

| Field            | Value              |
|------------------|--------------------|
| Zone             | Bibiki Bay (ID: 4) |
| Block Size       | 748 bytes          |
| Total Events     | 35                 |
| References Count | 15                 |

## List of Events

| Event ID                   | Entrypoint   |   Size |   Instructions |
|----------------------------|--------------|--------|----------------|
| [65535](#event-65535)      | 0x0000       |      1 |              1 |
| [43](#event-43)            | 0x0001       |     25 |              4 |
| [65535.1](#event-655351)   | 0x001A       |     16 |              2 |
| [65535.2](#event-655352)   | 0x002A       |     14 |              2 |
| [65535.3](#event-655353)   | 0x0038       |     16 |              2 |
| [65535.4](#event-655354)   | 0x0048       |     14 |              2 |
| [65535.5](#event-655355)   | 0x0056       |     16 |              2 |
| [65535.6](#event-655356)   | 0x0066       |     14 |              2 |
| [65535.7](#event-655357)   | 0x0074       |     16 |              2 |
| [65535.8](#event-655358)   | 0x0084       |     14 |              2 |
| [65535.9](#event-655359)   | 0x0092       |     16 |              2 |
| [65535.10](#event-6553510) | 0x00A2       |     14 |              2 |
| [65535.11](#event-6553511) | 0x00B0       |     16 |              2 |
| [65535.12](#event-6553512) | 0x00C0       |     14 |              2 |
| [65535.13](#event-6553513) | 0x00CE       |     16 |              2 |
| [65535.14](#event-6553514) | 0x00DE       |     14 |              2 |
| [65535.15](#event-6553515) | 0x00EC       |     16 |              2 |
| [65535.16](#event-6553516) | 0x00FC       |     14 |              2 |
| [65535.17](#event-6553517) | 0x010A       |     16 |              2 |
| [65535.18](#event-6553518) | 0x011A       |     14 |              2 |
| [65535.19](#event-6553519) | 0x0128       |     16 |              2 |
| [65535.20](#event-6553520) | 0x0138       |     14 |              2 |
| [65535.21](#event-6553521) | 0x0146       |     16 |              2 |
| [65535.22](#event-6553522) | 0x0156       |     14 |              2 |
| [65535.23](#event-6553523) | 0x0164       |     16 |              2 |
| [65535.24](#event-6553524) | 0x0174       |     14 |              2 |
| [65535.25](#event-6553525) | 0x0182       |     16 |              2 |
| [65535.26](#event-6553526) | 0x0192       |     14 |              2 |
| [65535.27](#event-6553527) | 0x01A0       |     16 |              2 |
| [65535.28](#event-6553528) | 0x01B0       |     14 |              2 |
| [65535.29](#event-6553529) | 0x01BE       |     16 |              2 |
| [65535.30](#event-6553530) | 0x01CE       |     14 |              2 |
| [40](#event-40)            | 0x01DC       |      1 |              1 |
| [65535.31](#event-6553531) | 0x01DD       |     42 |              4 |
| [65535.32](#event-6553532) | 0x0207       |     10 |              2 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0xFFFAED22  |  4294634786 |
|       1 | 0xFFF12883  |  4293994627 |
|       2 | 0xFFFFF32D  |  4294964013 |
|       3 | 0x071D      |        1821 |
|       4 | 0x0000      |           0 |
|       5 | 0x0014      |          20 |
|       6 | 0x0015      |          21 |
|       7 | 0x001A      |          26 |
|       8 | 0x001B      |          27 |
|       9 | 0x001D      |          29 |
|      10 | 0x002A      |          42 |
|      11 | 0xFFF69732  |  4294350642 |
|      12 | 0xFFF5FC56  |  4294310998 |
|      13 | 0xFFFFFAF0  |  4294966000 |
|      14 | 0x0873      |        2163 |

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

### Event 43

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 25 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    92 01 F8 FF FF 7F 37  00 80 01 80 02 80 03 80   ......7........
0010: 6C F8 FF FF 7F 04 80 04  80 00                    l.........      
```

#### Opcodes

```
  0: 0x0001 [0x92] EventEntity->Render.Flags3 ^= 0x01
  1: 0x0007 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=-332.510*, z=-972.669*, y=-3.283*, direction=160.0°*
  2: 0x0010 [0x6C] FADE_ENTITY_COLOR(entity_id=EventEntity, end_alpha=0*, fade_time=0*)
  3: 0x0019 [0x00] END_REQSTACK()
```

### Event 65535.1

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x001A   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                                66 05 80 F8 FF FF            f.....
0020: 7F F8 FF FF 7F 74 6C 6B  30 00                    .....tlk0.      
```

#### Opcodes

```
  0: 0x001A [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=20*
  1: 0x0029 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x002A   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                                53 F8 FF FF 7F F8            S.....
0030: FF FF 7F 74 6C 6B 30 00                           ...tlk0.        
```

#### Opcodes

```
  0: 0x002A [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "tlk0" with entities [EventEntity, EventEntity]
  1: 0x0037 [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0038   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:                          66 05 80 F8 FF FF 7F F8          f.......
0040: FF FF 7F 74 6C 6B 31 00                           ...tlk1.        
```

#### Opcodes

```
  0: 0x0038 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk1" with entities [EventEntity, EventEntity], work=20*
  1: 0x0047 [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0048   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                          53 F8 FF FF 7F F8 FF FF          S.......
0050: 7F 74 6C 6B 31 00                                 .tlk1.          
```

#### Opcodes

```
  0: 0x0048 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "tlk1" with entities [EventEntity, EventEntity]
  1: 0x0055 [0x00] END_REQSTACK()
```

### Event 65535.5

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0056   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:                   66 05  80 F8 FF FF 7F F8 FF FF        f.........
0060: 7F 74 68 6B 31 00                                 .thk1.          
```

#### Opcodes

```
  0: 0x0056 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "thk1" with entities [EventEntity, EventEntity], work=20*
  1: 0x0065 [0x00] END_REQSTACK()
```

### Event 65535.6

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0066   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060:                   53 F8  FF FF 7F F8 FF FF 7F 74        S........t
0070: 68 6B 31 00                                       hk1.            
```

#### Opcodes

```
  0: 0x0066 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "thk1" with entities [EventEntity, EventEntity]
  1: 0x0073 [0x00] END_REQSTACK()
```

### Event 65535.7

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0074   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0070:             66 05 80 F8  FF FF 7F F8 FF FF 7F 74      f..........t
0080: 68 6B 32 00                                       hk2.            
```

#### Opcodes

```
  0: 0x0074 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "thk2" with entities [EventEntity, EventEntity], work=20*
  1: 0x0083 [0x00] END_REQSTACK()
```

### Event 65535.8

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0084   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0080:             53 F8 FF FF  7F F8 FF FF 7F 74 68 6B      S........thk
0090: 32 00                                             2.              
```

#### Opcodes

```
  0: 0x0084 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "thk2" with entities [EventEntity, EventEntity]
  1: 0x0091 [0x00] END_REQSTACK()
```

### Event 65535.9

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0092   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0090:       66 05 80 F8 FF FF  7F F8 FF FF 7F 70 61 73    f..........pas
00A0: 30 00                                             0.              
```

#### Opcodes

```
  0: 0x0092 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "pas0" with entities [EventEntity, EventEntity], work=20*
  1: 0x00A1 [0x00] END_REQSTACK()
```

### Event 65535.10

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00A2   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00A0:       53 F8 FF FF 7F F8  FF FF 7F 70 61 73 30 00    S........pas0.
```

#### Opcodes

```
  0: 0x00A2 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "pas0" with entities [EventEntity, EventEntity]
  1: 0x00AF [0x00] END_REQSTACK()
```

### Event 65535.11

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00B0   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00B0: 66 06 80 F8 FF FF 7F F8  FF FF 7F 70 6F 69 30 00  f..........poi0.
```

#### Opcodes

```
  0: 0x00B0 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "poi0" with entities [EventEntity, EventEntity], work=21*
  1: 0x00BF [0x00] END_REQSTACK()
```

### Event 65535.12

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00C0   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00C0: 53 F8 FF FF 7F F8 FF FF  7F 70 6F 69 30 00        S........poi0.  
```

#### Opcodes

```
  0: 0x00C0 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "poi0" with entities [EventEntity, EventEntity]
  1: 0x00CD [0x00] END_REQSTACK()
```

### Event 65535.13

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00CE   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00C0:                                            66 06                f.
00D0: 80 F8 FF FF 7F F8 FF FF  7F 70 6F 69 31 00        .........poi1.  
```

#### Opcodes

```
  0: 0x00CE [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "poi1" with entities [EventEntity, EventEntity], work=21*
  1: 0x00DD [0x00] END_REQSTACK()
```

### Event 65535.14

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00DE   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00D0:                                            53 F8                S.
00E0: FF FF 7F F8 FF FF 7F 70  6F 69 31 00              .......poi1.    
```

#### Opcodes

```
  0: 0x00DE [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "poi1" with entities [EventEntity, EventEntity]
  1: 0x00EB [0x00] END_REQSTACK()
```

### Event 65535.15

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00EC   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00E0:                                      66 06 80 F8              f...
00F0: FF FF 7F F8 FF FF 7F 64  69 73 30 00              .......dis0.    
```

#### Opcodes

```
  0: 0x00EC [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "dis0" with entities [EventEntity, EventEntity], work=21*
  1: 0x00FB [0x00] END_REQSTACK()
```

### Event 65535.16

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00FC   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00F0:                                      53 F8 FF FF              S...
0100: 7F F8 FF FF 7F 64 69 73  30 00                    .....dis0.      
```

#### Opcodes

```
  0: 0x00FC [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "dis0" with entities [EventEntity, EventEntity]
  1: 0x0109 [0x00] END_REQSTACK()
```

### Event 65535.17

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x010A   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0100:                                66 07 80 F8 FF FF            f.....
0110: 7F F8 FF FF 7F 6F 72 6F  30 00                    .....oro0.      
```

#### Opcodes

```
  0: 0x010A [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "oro0" with entities [EventEntity, EventEntity], work=26*
  1: 0x0119 [0x00] END_REQSTACK()
```

### Event 65535.18

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x011A   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0110:                                53 F8 FF FF 7F F8            S.....
0120: FF FF 7F 6F 72 6F 30 00                           ...oro0.        
```

#### Opcodes

```
  0: 0x011A [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "oro0" with entities [EventEntity, EventEntity]
  1: 0x0127 [0x00] END_REQSTACK()
```

### Event 65535.19

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0128   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0120:                          66 07 80 F8 FF FF 7F F8          f.......
0130: FF FF 7F 6F 72 6F 31 00                           ...oro1.        
```

#### Opcodes

```
  0: 0x0128 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "oro1" with entities [EventEntity, EventEntity], work=26*
  1: 0x0137 [0x00] END_REQSTACK()
```

### Event 65535.20

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0138   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0130:                          53 F8 FF FF 7F F8 FF FF          S.......
0140: 7F 6F 72 6F 31 00                                 .oro1.          
```

#### Opcodes

```
  0: 0x0138 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "oro1" with entities [EventEntity, EventEntity]
  1: 0x0145 [0x00] END_REQSTACK()
```

### Event 65535.21

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0146   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0140:                   66 08  80 F8 FF FF 7F F8 FF FF        f.........
0150: 7F 74 6C 62 30 00                                 .tlb0.          
```

#### Opcodes

```
  0: 0x0146 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlb0" with entities [EventEntity, EventEntity], work=27*
  1: 0x0155 [0x00] END_REQSTACK()
```

### Event 65535.22

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0156   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0150:                   53 F8  FF FF 7F F8 FF FF 7F 74        S........t
0160: 6C 62 30 00                                       lb0.            
```

#### Opcodes

```
  0: 0x0156 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "tlb0" with entities [EventEntity, EventEntity]
  1: 0x0163 [0x00] END_REQSTACK()
```

### Event 65535.23

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0164   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0160:             66 08 80 F8  FF FF 7F F8 FF FF 7F 74      f..........t
0170: 6C 62 31 00                                       lb1.            
```

#### Opcodes

```
  0: 0x0164 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlb1" with entities [EventEntity, EventEntity], work=27*
  1: 0x0173 [0x00] END_REQSTACK()
```

### Event 65535.24

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0174   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0170:             53 F8 FF FF  7F F8 FF FF 7F 74 6C 62      S........tlb
0180: 31 00                                             1.              
```

#### Opcodes

```
  0: 0x0174 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "tlb1" with entities [EventEntity, EventEntity]
  1: 0x0181 [0x00] END_REQSTACK()
```

### Event 65535.25

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0182   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0180:       66 09 80 F8 FF FF  7F F8 FF FF 7F 73 69 74    f..........sit
0190: 30 00                                             0.              
```

#### Opcodes

```
  0: 0x0182 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "sit0" with entities [EventEntity, EventEntity], work=29*
  1: 0x0191 [0x00] END_REQSTACK()
```

### Event 65535.26

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0192   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0190:       53 F8 FF FF 7F F8  FF FF 7F 73 69 74 30 00    S........sit0.
```

#### Opcodes

```
  0: 0x0192 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "sit0" with entities [EventEntity, EventEntity]
  1: 0x019F [0x00] END_REQSTACK()
```

### Event 65535.27

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x01A0   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
01A0: 66 09 80 F8 FF FF 7F F8  FF FF 7F 73 69 74 31 00  f..........sit1.
```

#### Opcodes

```
  0: 0x01A0 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "sit1" with entities [EventEntity, EventEntity], work=29*
  1: 0x01AF [0x00] END_REQSTACK()
```

### Event 65535.28

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x01B0   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
01B0: 53 F8 FF FF 7F F8 FF FF  7F 73 69 74 31 00        S........sit1.  
```

#### Opcodes

```
  0: 0x01B0 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "sit1" with entities [EventEntity, EventEntity]
  1: 0x01BD [0x00] END_REQSTACK()
```

### Event 65535.29

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x01BE   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
01B0:                                            66 09                f.
01C0: 80 F8 FF FF 7F F8 FF FF  7F 73 69 74 6C 00        .........sitl.  
```

#### Opcodes

```
  0: 0x01BE [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "sitl" with entities [EventEntity, EventEntity], work=29*
  1: 0x01CD [0x00] END_REQSTACK()
```

### Event 65535.30

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x01CE   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
01C0:                                            53 F8                S.
01D0: FF FF 7F F8 FF FF 7F 73  69 74 6C 00              .......sitl.    
```

#### Opcodes

```
  0: 0x01CE [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "sitl" with entities [EventEntity, EventEntity]
  1: 0x01DB [0x00] END_REQSTACK()
```

### Event 40

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x01DC  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
01D0:                                      00                       .   
```

#### Opcodes

```
  0: 0x01DC [0x00] END_REQSTACK()
```

### Event 65535.31

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x01DD   |
| Data Size    | 42 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
01D0:                                         66 0A 80               f..
01E0: F8 FF FF 7F F8 FF FF 7F  77 6F 6E 32 2C F8 FF FF  ........won2,...
01F0: 7F F8 FF FF 7F 6C 63 30  33 53 F8 FF FF 7F F8 FF  .....lc03S......
0200: FF 7F 6C 63 30 33 00                              ..lc03.         
```

#### Opcodes

```
  0: 0x01DD [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "won2" with entities [EventEntity, EventEntity], work=42*
  1: 0x01EC [0x2C] CREATE_SCHEDULER_TASK: Create scheduler "lc03" with entities [EventEntity, EventEntity]
  2: 0x01F9 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "lc03" with entities [EventEntity, EventEntity]
  3: 0x0206 [0x00] END_REQSTACK()
```

### Event 65535.32

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0207   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0200:                      37  0B 80 0C 80 0D 80 0E 80         7........
0210: 00                                                .               
```

#### Opcodes

```
  0: 0x0207 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=-616.654*, z=-656.298*, y=-1.296*, direction=190.1°*
  1: 0x0210 [0x00] END_REQSTACK()
```
