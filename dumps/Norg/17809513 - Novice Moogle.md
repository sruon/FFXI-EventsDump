# 17809513 - Novice Moogle

## Common Data

| Field            | Value          |
|------------------|----------------|
| Zone             | Norg (ID: 252) |
| Block Size       | 964 bytes      |
| Total Events     | 38             |
| References Count | 11             |

## List of Events

| Event ID                   | Entrypoint   |   Size |   Instructions |
|----------------------------|--------------|--------|----------------|
| [65535](#event-65535)      | 0x0000       |      1 |              1 |
| [0](#event-0)              | 0x0001       |      1 |              1 |
| [65535.1](#event-655351)   | 0x0002       |     18 |              4 |
| [65535.2](#event-655352)   | 0x0014       |     10 |              2 |
| [65535.3](#event-655353)   | 0x001E       |      9 |              3 |
| [65535.4](#event-655354)   | 0x0027       |      9 |              3 |
| [65535.5](#event-655355)   | 0x0030       |     10 |              2 |
| [65535.6](#event-655356)   | 0x003A       |     10 |              2 |
| [211](#event-211)          | 0x0044       |      1 |              1 |
| [65535.7](#event-655357)   | 0x0045       |     10 |              2 |
| [65535.8](#event-655358)   | 0x004F       |     31 |              3 |
| [65535.9](#event-655359)   | 0x006E       |     14 |              2 |
| [65535.10](#event-6553510) | 0x007C       |     14 |              2 |
| [65535.11](#event-6553511) | 0x008A       |     14 |              2 |
| [65535.12](#event-6553512) | 0x0098       |     31 |              3 |
| [65535.13](#event-6553513) | 0x00B7       |     14 |              2 |
| [65535.14](#event-6553514) | 0x00C5       |     14 |              2 |
| [65535.15](#event-6553515) | 0x00D3       |     14 |              2 |
| [65535.16](#event-6553516) | 0x00E1       |     31 |              3 |
| [65535.17](#event-6553517) | 0x0100       |     14 |              2 |
| [65535.18](#event-6553518) | 0x010E       |     14 |              2 |
| [65535.19](#event-6553519) | 0x011C       |     14 |              2 |
| [65535.20](#event-6553520) | 0x012A       |     31 |              3 |
| [65535.21](#event-6553521) | 0x0149       |     14 |              2 |
| [65535.22](#event-6553522) | 0x0157       |     14 |              2 |
| [65535.23](#event-6553523) | 0x0165       |     14 |              2 |
| [65535.24](#event-6553524) | 0x0173       |     14 |              2 |
| [65535.25](#event-6553525) | 0x0181       |     14 |              2 |
| [65535.26](#event-6553526) | 0x018F       |     14 |              2 |
| [65535.27](#event-6553527) | 0x019D       |     14 |              2 |
| [65535.28](#event-6553528) | 0x01AB       |     31 |              3 |
| [65535.29](#event-6553529) | 0x01CA       |     14 |              2 |
| [65535.30](#event-6553530) | 0x01D8       |     14 |              2 |
| [65535.31](#event-6553531) | 0x01E6       |     14 |              2 |
| [65535.32](#event-6553532) | 0x01F4       |    183 |             15 |
| [65535.33](#event-6553533) | 0x02AB       |     40 |              4 |
| [65535.34](#event-6553534) | 0x02D3       |     14 |              2 |
| [65535.35](#event-6553535) | 0x02E1       |     12 |              4 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0000      |           0 |
|       1 | 0x0001      |           1 |
|       2 | 0x0080      |         128 |
|       3 | 0xFFFFE870  |  4294961264 |
|       4 | 0xFFFF5B21  |  4294925089 |
|       5 | 0xFFFFFC60  |  4294966368 |
|       6 | 0x0387      |         903 |
|       7 | 0x00BC      |         188 |
|       8 | 0xFFFFD9D8  |  4294957528 |
|       9 | 0xFFFF6801  |  4294928385 |
|      10 | 0xFFFFFD05  |  4294966533 |

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

### Event 65535.1

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0002   |
| Data Size    | 18 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:       22 00 2F 00 F8 FF  FF 7F 6C F8 FF FF 7F 00    "./.....l.....
0010: 80 01 80 00                                       ....            
```

#### Opcodes

```
  0: 0x0002 [0x22] ENTITY_HIDE_FLAG(enabled=0x00)
  1: 0x0004 [0x2F] EventEntity->Render.Flags0 &= ~0x80000 // Bit 19
  2: 0x000A [0x6C] FADE_ENTITY_COLOR(entity_id=EventEntity, end_alpha=0*, fade_time=1*)
  3: 0x0013 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0014   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:             6C F8 FF FF  7F 02 80 01 80 00            l.........  
```

#### Opcodes

```
  0: 0x0014 [0x6C] FADE_ENTITY_COLOR(entity_id=EventEntity, end_alpha=128*, fade_time=1*)
  1: 0x001D [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x001E  |
| Data Size    | 9 bytes |
| Instructions | 3       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                                            22 00                ".
0020: 2F 00 F8 FF FF 7F 00                              /......         
```

#### Opcodes

```
  0: 0x001E [0x22] ENTITY_HIDE_FLAG(enabled=0x00)
  1: 0x0020 [0x2F] EventEntity->Render.Flags0 &= ~0x80000 // Bit 19
  2: 0x0026 [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0027  |
| Data Size    | 9 bytes |
| Instructions | 3       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                      22  01 2F 01 F8 FF FF 7F 00         "./......
```

#### Opcodes

```
  0: 0x0027 [0x22] ENTITY_HIDE_FLAG(enabled=0x01)
  1: 0x0029 [0x2F] EventEntity->Render.Flags0 |= 0x80000 // Bit 19
  2: 0x002F [0x00] END_REQSTACK()
```

### Event 65535.5

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0030   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030: 6C F8 FF FF 7F 00 80 01  80 00                    l.........      
```

#### Opcodes

```
  0: 0x0030 [0x6C] FADE_ENTITY_COLOR(entity_id=EventEntity, end_alpha=0*, fade_time=1*)
  1: 0x0039 [0x00] END_REQSTACK()
```

### Event 65535.6

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x003A   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:                                6C F8 FF FF 7F 02            l.....
0040: 80 01 80 00                                       ....            
```

#### Opcodes

```
  0: 0x003A [0x6C] FADE_ENTITY_COLOR(entity_id=EventEntity, end_alpha=128*, fade_time=1*)
  1: 0x0043 [0x00] END_REQSTACK()
```

### Event 211

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0044  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:             00                                        .           
```

#### Opcodes

```
  0: 0x0044 [0x00] END_REQSTACK()
```

### Event 65535.7

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0045   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                37 03 80  04 80 05 80 06 80 00          7......... 
```

#### Opcodes

```
  0: 0x0045 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=-6.032*, z=-42.207*, y=-0.928*, direction=79.4°*
  1: 0x004E [0x00] END_REQSTACK()
```

### Event 65535.8

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x004F   |
| Data Size    | 31 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                                               45                 E
0050: 07 80 F0 FF FF 7F F0 FF  FF 7F 73 30 30 36 00 80  ..........s006..
0060: 2C F8 FF FF 7F F8 FF FF  7F 74 6C 6B 30 00        ,........tlk0.  
```

#### Opcodes

```
  0: 0x004F [0x45] LOAD_SCHEDULED_TASK: Load scheduler "s006" with entities [LocalPlayer, LocalPlayer], work=[188*, 0*]
  1: 0x0060 [0x2C] CREATE_SCHEDULER_TASK: Create scheduler "tlk0" with entities [EventEntity, EventEntity]
  2: 0x006D [0x00] END_REQSTACK()
```

### Event 65535.9

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x006E   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060:                                            53 F8                S.
0070: FF FF 7F F8 FF FF 7F 74  6C 6B 30 00              .......tlk0.    
```

#### Opcodes

```
  0: 0x006E [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "tlk0" with entities [EventEntity, EventEntity]
  1: 0x007B [0x00] END_REQSTACK()
```

### Event 65535.10

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x007C   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0070:                                      2C F8 FF FF              ,...
0080: 7F F8 FF FF 7F 74 6C 6B  31 00                    .....tlk1.      
```

#### Opcodes

```
  0: 0x007C [0x2C] CREATE_SCHEDULER_TASK: Create scheduler "tlk1" with entities [EventEntity, EventEntity]
  1: 0x0089 [0x00] END_REQSTACK()
```

### Event 65535.11

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x008A   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0080:                                53 F8 FF FF 7F F8            S.....
0090: FF FF 7F 74 6C 6B 31 00                           ...tlk1.        
```

#### Opcodes

```
  0: 0x008A [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "tlk1" with entities [EventEntity, EventEntity]
  1: 0x0097 [0x00] END_REQSTACK()
```

### Event 65535.12

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0098   |
| Data Size    | 31 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0090:                          45 07 80 F0 FF FF 7F F0          E.......
00A0: FF FF 7F 73 30 30 38 00  80 2C F8 FF FF 7F F8 FF  ...s008..,......
00B0: FF 7F 67 61 6B 30 00                              ..gak0.         
```

#### Opcodes

```
  0: 0x0098 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "s008" with entities [LocalPlayer, LocalPlayer], work=[188*, 0*]
  1: 0x00A9 [0x2C] CREATE_SCHEDULER_TASK: Create scheduler "gak0" with entities [EventEntity, EventEntity]
  2: 0x00B6 [0x00] END_REQSTACK()
```

### Event 65535.13

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
00C0: 67 61 6B 30 00                                    gak0.           
```

#### Opcodes

```
  0: 0x00B7 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "gak0" with entities [EventEntity, EventEntity]
  1: 0x00C4 [0x00] END_REQSTACK()
```

### Event 65535.14

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00C5   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00C0:                2C F8 FF  FF 7F F8 FF FF 7F 67 61       ,........ga
00D0: 6B 31 00                                          k1.             
```

#### Opcodes

```
  0: 0x00C5 [0x2C] CREATE_SCHEDULER_TASK: Create scheduler "gak1" with entities [EventEntity, EventEntity]
  1: 0x00D2 [0x00] END_REQSTACK()
```

### Event 65535.15

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00D3   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00D0:          53 F8 FF FF 7F  F8 FF FF 7F 67 61 6B 31     S........gak1
00E0: 00                                                .               
```

#### Opcodes

```
  0: 0x00D3 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "gak1" with entities [EventEntity, EventEntity]
  1: 0x00E0 [0x00] END_REQSTACK()
```

### Event 65535.16

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00E1   |
| Data Size    | 31 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00E0:    45 07 80 F0 FF FF 7F  F0 FF FF 7F 73 30 30 39   E..........s009
00F0: 00 80 2C F8 FF FF 7F F8  FF FF 7F 6A 6F 62 30 00  ..,........job0.
```

#### Opcodes

```
  0: 0x00E1 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "s009" with entities [LocalPlayer, LocalPlayer], work=[188*, 0*]
  1: 0x00F2 [0x2C] CREATE_SCHEDULER_TASK: Create scheduler "job0" with entities [EventEntity, EventEntity]
  2: 0x00FF [0x00] END_REQSTACK()
```

### Event 65535.17

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0100   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0100: 53 F8 FF FF 7F F8 FF FF  7F 6A 6F 62 30 00        S........job0.  
```

#### Opcodes

```
  0: 0x0100 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "job0" with entities [EventEntity, EventEntity]
  1: 0x010D [0x00] END_REQSTACK()
```

### Event 65535.18

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x010E   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0100:                                            2C F8                ,.
0110: FF FF 7F F8 FF FF 7F 6A  6F 62 31 00              .......job1.    
```

#### Opcodes

```
  0: 0x010E [0x2C] CREATE_SCHEDULER_TASK: Create scheduler "job1" with entities [EventEntity, EventEntity]
  1: 0x011B [0x00] END_REQSTACK()
```

### Event 65535.19

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x011C   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0110:                                      53 F8 FF FF              S...
0120: 7F F8 FF FF 7F 6A 6F 62  31 00                    .....job1.      
```

#### Opcodes

```
  0: 0x011C [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "job1" with entities [EventEntity, EventEntity]
  1: 0x0129 [0x00] END_REQSTACK()
```

### Event 65535.20

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x012A   |
| Data Size    | 31 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0120:                                45 07 80 F0 FF FF            E.....
0130: 7F F0 FF FF 7F 73 30 30  35 00 80 2C F8 FF FF 7F  .....s005..,....
0140: F8 FF FF 7F 68 61 70 30  00                       ....hap0.       
```

#### Opcodes

```
  0: 0x012A [0x45] LOAD_SCHEDULED_TASK: Load scheduler "s005" with entities [LocalPlayer, LocalPlayer], work=[188*, 0*]
  1: 0x013B [0x2C] CREATE_SCHEDULER_TASK: Create scheduler "hap0" with entities [EventEntity, EventEntity]
  2: 0x0148 [0x00] END_REQSTACK()
```

### Event 65535.21

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0149   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0140:                             53 F8 FF FF 7F F8 FF           S......
0150: FF 7F 68 61 70 30 00                              ..hap0.         
```

#### Opcodes

```
  0: 0x0149 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "hap0" with entities [EventEntity, EventEntity]
  1: 0x0156 [0x00] END_REQSTACK()
```

### Event 65535.22

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0157   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0150:                      2C  F8 FF FF 7F F8 FF FF 7F         ,........
0160: 68 61 70 31 00                                    hap1.           
```

#### Opcodes

```
  0: 0x0157 [0x2C] CREATE_SCHEDULER_TASK: Create scheduler "hap1" with entities [EventEntity, EventEntity]
  1: 0x0164 [0x00] END_REQSTACK()
```

### Event 65535.23

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0165   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0160:                53 F8 FF  FF 7F F8 FF FF 7F 68 61       S........ha
0170: 70 31 00                                          p1.             
```

#### Opcodes

```
  0: 0x0165 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "hap1" with entities [EventEntity, EventEntity]
  1: 0x0172 [0x00] END_REQSTACK()
```

### Event 65535.24

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0173   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0170:          2C F8 FF FF 7F  F8 FF FF 7F 6E 65 77 30     ,........new0
0180: 00                                                .               
```

#### Opcodes

```
  0: 0x0173 [0x2C] CREATE_SCHEDULER_TASK: Create scheduler "new0" with entities [EventEntity, EventEntity]
  1: 0x0180 [0x00] END_REQSTACK()
```

### Event 65535.25

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0181   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0180:    53 F8 FF FF 7F F8 FF  FF 7F 6E 65 77 30 00      S........new0. 
```

#### Opcodes

```
  0: 0x0181 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "new0" with entities [EventEntity, EventEntity]
  1: 0x018E [0x00] END_REQSTACK()
```

### Event 65535.26

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x018F   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0180:                                               2C                 ,
0190: F8 FF FF 7F F8 FF FF 7F  6E 65 77 31 00           ........new1.   
```

#### Opcodes

```
  0: 0x018F [0x2C] CREATE_SCHEDULER_TASK: Create scheduler "new1" with entities [EventEntity, EventEntity]
  1: 0x019C [0x00] END_REQSTACK()
```

### Event 65535.27

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x019D   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0190:                                         53 F8 FF               S..
01A0: FF 7F F8 FF FF 7F 6E 65  77 31 00                 ......new1.     
```

#### Opcodes

```
  0: 0x019D [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "new1" with entities [EventEntity, EventEntity]
  1: 0x01AA [0x00] END_REQSTACK()
```

### Event 65535.28

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x01AB   |
| Data Size    | 31 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
01A0:                                   45 07 80 F0 FF             E....
01B0: FF 7F F0 FF FF 7F 73 30  30 37 00 80 2C F8 FF FF  ......s007..,...
01C0: 7F F8 FF FF 7F 65 78 70  30 00                    .....exp0.      
```

#### Opcodes

```
  0: 0x01AB [0x45] LOAD_SCHEDULED_TASK: Load scheduler "s007" with entities [LocalPlayer, LocalPlayer], work=[188*, 0*]
  1: 0x01BC [0x2C] CREATE_SCHEDULER_TASK: Create scheduler "exp0" with entities [EventEntity, EventEntity]
  2: 0x01C9 [0x00] END_REQSTACK()
```

### Event 65535.29

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x01CA   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
01C0:                                53 F8 FF FF 7F F8            S.....
01D0: FF FF 7F 65 78 70 30 00                           ...exp0.        
```

#### Opcodes

```
  0: 0x01CA [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "exp0" with entities [EventEntity, EventEntity]
  1: 0x01D7 [0x00] END_REQSTACK()
```

### Event 65535.30

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x01D8   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
01D0:                          2C F8 FF FF 7F F8 FF FF          ,.......
01E0: 7F 65 78 70 31 00                                 .exp1.          
```

#### Opcodes

```
  0: 0x01D8 [0x2C] CREATE_SCHEDULER_TASK: Create scheduler "exp1" with entities [EventEntity, EventEntity]
  1: 0x01E5 [0x00] END_REQSTACK()
```

### Event 65535.31

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x01E6   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
01E0:                   53 F8  FF FF 7F F8 FF FF 7F 65        S........e
01F0: 78 70 31 00                                       xp1.            
```

#### Opcodes

```
  0: 0x01E6 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "exp1" with entities [EventEntity, EventEntity]
  1: 0x01F3 [0x00] END_REQSTACK()
```

### Event 65535.32

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x01F4    |
| Data Size    | 183 bytes |
| Instructions | 15        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
01F0:             2C F8 FF FF  7F F8 FF FF 7F 64 61 6E      ,........dan
0200: 30 53 F8 FF FF 7F F8 FF  FF 7F 64 61 6E 30 2C F8  0S........dan0,.
0210: FF FF 7F F8 FF FF 7F 64  61 6E 30 53 F8 FF FF 7F  .......dan0S....
0220: F8 FF FF 7F 64 61 6E 30  2C F8 FF FF 7F F8 FF FF  ....dan0,.......
0230: 7F 64 61 6E 31 53 F8 FF  FF 7F F8 FF FF 7F 64 61  .dan1S........da
0240: 6E 31 2C F8 FF FF 7F F8  FF FF 7F 64 61 6E 30 53  n1,........dan0S
0250: F8 FF FF 7F F8 FF FF 7F  64 61 6E 30 2C F8 FF FF  ........dan0,...
0260: 7F F8 FF FF 7F 64 61 6E  30 53 F8 FF FF 7F F8 FF  .....dan0S......
0270: FF 7F 64 61 6E 30 2C F8  FF FF 7F F8 FF FF 7F 64  ..dan0,........d
0280: 61 6E 32 53 F8 FF FF 7F  F8 FF FF 7F 64 61 6E 32  an2S........dan2
0290: 2C F8 FF FF 7F F8 FF FF  7F 64 61 6E 33 53 F8 FF  ,........dan3S..
02A0: FF 7F F8 FF FF 7F 64 61  6E 33 00                 ......dan3.     
```

#### Opcodes

```
  0: 0x01F4 [0x2C] CREATE_SCHEDULER_TASK: Create scheduler "dan0" with entities [EventEntity, EventEntity]
  1: 0x0201 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "dan0" with entities [EventEntity, EventEntity]
  2: 0x020E [0x2C] CREATE_SCHEDULER_TASK: Create scheduler "dan0" with entities [EventEntity, EventEntity]
  3: 0x021B [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "dan0" with entities [EventEntity, EventEntity]
  4: 0x0228 [0x2C] CREATE_SCHEDULER_TASK: Create scheduler "dan1" with entities [EventEntity, EventEntity]
  5: 0x0235 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "dan1" with entities [EventEntity, EventEntity]
  6: 0x0242 [0x2C] CREATE_SCHEDULER_TASK: Create scheduler "dan0" with entities [EventEntity, EventEntity]
  7: 0x024F [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "dan0" with entities [EventEntity, EventEntity]
  8: 0x025C [0x2C] CREATE_SCHEDULER_TASK: Create scheduler "dan0" with entities [EventEntity, EventEntity]
  9: 0x0269 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "dan0" with entities [EventEntity, EventEntity]
 10: 0x0276 [0x2C] CREATE_SCHEDULER_TASK: Create scheduler "dan2" with entities [EventEntity, EventEntity]
 11: 0x0283 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "dan2" with entities [EventEntity, EventEntity]
 12: 0x0290 [0x2C] CREATE_SCHEDULER_TASK: Create scheduler "dan3" with entities [EventEntity, EventEntity]
 13: 0x029D [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "dan3" with entities [EventEntity, EventEntity]
 14: 0x02AA [0x00] END_REQSTACK()
```

### Event 65535.33

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x02AB   |
| Data Size    | 40 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
02A0:                                   2C F8 FF FF 7F             ,....
02B0: F8 FF FF 7F 64 61 6E 33  53 F8 FF FF 7F F8 FF FF  ....dan3S.......
02C0: 7F 64 61 6E 33 2C F8 FF  FF 7F F8 FF FF 7F 64 61  .dan3,........da
02D0: 65 33 00                                          e3.             
```

#### Opcodes

```
  0: 0x02AB [0x2C] CREATE_SCHEDULER_TASK: Create scheduler "dan3" with entities [EventEntity, EventEntity]
  1: 0x02B8 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "dan3" with entities [EventEntity, EventEntity]
  2: 0x02C5 [0x2C] CREATE_SCHEDULER_TASK: Create scheduler "dae3" with entities [EventEntity, EventEntity]
  3: 0x02D2 [0x00] END_REQSTACK()
```

### Event 65535.34

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x02D3   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
02D0:          53 F8 FF FF 7F  F8 FF FF 7F 64 61 65 33     S........dae3
02E0: 00                                                .               
```

#### Opcodes

```
  0: 0x02D3 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "dae3" with entities [EventEntity, EventEntity]
  1: 0x02E0 [0x00] END_REQSTACK()
```

### Event 65535.35

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x02E1   |
| Data Size    | 12 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
02E0:    1F 00 08 80 09 80 0A  80 1F 01 6F 00            ..........o.   
```

#### Opcodes

```
  0: 0x02E1 [0x1F] MOVE_ENTITY: EventEntity moves to X=-9.768*, Z=-38.911*, Y=-0.763*
  1: 0x02E9 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  2: 0x02EB [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  3: 0x02EC [0x00] END_REQSTACK()
```
