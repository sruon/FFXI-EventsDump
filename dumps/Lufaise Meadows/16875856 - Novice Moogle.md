# 16875856 - Novice Moogle

## Common Data

| Field            | Value                    |
|------------------|--------------------------|
| Zone             | Lufaise Meadows (ID: 24) |
| Block Size       | 660 bytes                |
| Total Events     | 29                       |
| References Count | 14                       |

## List of Events

| Event ID                   | Entrypoint   |   Size |   Instructions |
|----------------------------|--------------|--------|----------------|
| [65535](#event-65535)      | 0x0000       |      1 |              1 |
| [65535.1](#event-655351)   | 0x0001       |     31 |              3 |
| [65535.2](#event-655352)   | 0x0020       |     14 |              2 |
| [65535.3](#event-655353)   | 0x002E       |     14 |              2 |
| [65535.4](#event-655354)   | 0x003C       |     14 |              2 |
| [65535.5](#event-655355)   | 0x004A       |     31 |              3 |
| [65535.6](#event-655356)   | 0x0069       |     14 |              2 |
| [65535.7](#event-655357)   | 0x0077       |     14 |              2 |
| [65535.8](#event-655358)   | 0x0085       |     14 |              2 |
| [65535.9](#event-655359)   | 0x0093       |     31 |              3 |
| [65535.10](#event-6553510) | 0x00B2       |     14 |              2 |
| [65535.11](#event-6553511) | 0x00C0       |     14 |              2 |
| [65535.12](#event-6553512) | 0x00CE       |     14 |              2 |
| [65535.13](#event-6553513) | 0x00DC       |     31 |              3 |
| [65535.14](#event-6553514) | 0x00FB       |     14 |              2 |
| [65535.15](#event-6553515) | 0x0109       |     14 |              2 |
| [65535.16](#event-6553516) | 0x0117       |     14 |              2 |
| [65535.17](#event-6553517) | 0x0125       |     14 |              2 |
| [65535.18](#event-6553518) | 0x0133       |     14 |              2 |
| [65535.19](#event-6553519) | 0x0141       |     14 |              2 |
| [65535.20](#event-6553520) | 0x014F       |     14 |              2 |
| [65535.21](#event-6553521) | 0x015D       |     31 |              3 |
| [65535.22](#event-6553522) | 0x017C       |     14 |              2 |
| [65535.23](#event-6553523) | 0x018A       |     14 |              2 |
| [65535.24](#event-6553524) | 0x0198       |     14 |              2 |
| [4](#event-4)              | 0x01A6       |      1 |              1 |
| [65535.25](#event-6553525) | 0x01A7       |     10 |              2 |
| [65535.26](#event-6553526) | 0x01B1       |     22 |              8 |
| [65535.27](#event-6553527) | 0x01C7       |     15 |              5 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x00BC      |         188 |
|       1 | 0x0000      |           0 |
|       2 | 0x6A55D     |      435549 |
|       3 | 0xFFFFAEE8  |  4294946536 |
|       4 | 0xFFFFFE20  |  4294966816 |
|       5 | 0x0780      |        1920 |
|       6 | 0x000D      |          13 |
|       7 | 0x68AD6     |      428758 |
|       8 | 0xFFFFA53B  |  4294944059 |
|       9 | 0xFFFFF984  |  4294965636 |
|      10 | 0x0028      |          40 |
|      11 | 0x66DCA     |      421322 |
|      12 | 0xFFFF71D4  |  4294930900 |
|      13 | 0x04D9      |        1241 |

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
| Data Size    | 31 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    45 00 80 F0 FF FF 7F  F0 FF FF 7F 73 30 30 36   E..........s006
0010: 01 80 2C F8 FF FF 7F F8  FF FF 7F 74 6C 6B 30 00  ..,........tlk0.
```

#### Opcodes

```
  0: 0x0001 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "s006" with entities [LocalPlayer, LocalPlayer], work=[188*, 0*]
  1: 0x0012 [0x2C] CREATE_SCHEDULER_TASK: Create scheduler "tlk0" with entities [EventEntity, EventEntity]
  2: 0x001F [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0020   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020: 53 F8 FF FF 7F F8 FF FF  7F 74 6C 6B 30 00        S........tlk0.  
```

#### Opcodes

```
  0: 0x0020 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "tlk0" with entities [EventEntity, EventEntity]
  1: 0x002D [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x002E   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                                            2C F8                ,.
0030: FF FF 7F F8 FF FF 7F 74  6C 6B 31 00              .......tlk1.    
```

#### Opcodes

```
  0: 0x002E [0x2C] CREATE_SCHEDULER_TASK: Create scheduler "tlk1" with entities [EventEntity, EventEntity]
  1: 0x003B [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x003C   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:                                      53 F8 FF FF              S...
0040: 7F F8 FF FF 7F 74 6C 6B  31 00                    .....tlk1.      
```

#### Opcodes

```
  0: 0x003C [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "tlk1" with entities [EventEntity, EventEntity]
  1: 0x0049 [0x00] END_REQSTACK()
```

### Event 65535.5

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x004A   |
| Data Size    | 31 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                                45 00 80 F0 FF FF            E.....
0050: 7F F0 FF FF 7F 73 30 30  38 01 80 2C F8 FF FF 7F  .....s008..,....
0060: F8 FF FF 7F 67 61 6B 30  00                       ....gak0.       
```

#### Opcodes

```
  0: 0x004A [0x45] LOAD_SCHEDULED_TASK: Load scheduler "s008" with entities [LocalPlayer, LocalPlayer], work=[188*, 0*]
  1: 0x005B [0x2C] CREATE_SCHEDULER_TASK: Create scheduler "gak0" with entities [EventEntity, EventEntity]
  2: 0x0068 [0x00] END_REQSTACK()
```

### Event 65535.6

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0069   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060:                             53 F8 FF FF 7F F8 FF           S......
0070: FF 7F 67 61 6B 30 00                              ..gak0.         
```

#### Opcodes

```
  0: 0x0069 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "gak0" with entities [EventEntity, EventEntity]
  1: 0x0076 [0x00] END_REQSTACK()
```

### Event 65535.7

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0077   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0070:                      2C  F8 FF FF 7F F8 FF FF 7F         ,........
0080: 67 61 6B 31 00                                    gak1.           
```

#### Opcodes

```
  0: 0x0077 [0x2C] CREATE_SCHEDULER_TASK: Create scheduler "gak1" with entities [EventEntity, EventEntity]
  1: 0x0084 [0x00] END_REQSTACK()
```

### Event 65535.8

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0085   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0080:                53 F8 FF  FF 7F F8 FF FF 7F 67 61       S........ga
0090: 6B 31 00                                          k1.             
```

#### Opcodes

```
  0: 0x0085 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "gak1" with entities [EventEntity, EventEntity]
  1: 0x0092 [0x00] END_REQSTACK()
```

### Event 65535.9

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0093   |
| Data Size    | 31 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0090:          45 00 80 F0 FF  FF 7F F0 FF FF 7F 73 30     E..........s0
00A0: 30 39 01 80 2C F8 FF FF  7F F8 FF FF 7F 6A 6F 62  09..,........job
00B0: 30 00                                             0.              
```

#### Opcodes

```
  0: 0x0093 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "s009" with entities [LocalPlayer, LocalPlayer], work=[188*, 0*]
  1: 0x00A4 [0x2C] CREATE_SCHEDULER_TASK: Create scheduler "job0" with entities [EventEntity, EventEntity]
  2: 0x00B1 [0x00] END_REQSTACK()
```

### Event 65535.10

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00B2   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00B0:       53 F8 FF FF 7F F8  FF FF 7F 6A 6F 62 30 00    S........job0.
```

#### Opcodes

```
  0: 0x00B2 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "job0" with entities [EventEntity, EventEntity]
  1: 0x00BF [0x00] END_REQSTACK()
```

### Event 65535.11

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00C0   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00C0: 2C F8 FF FF 7F F8 FF FF  7F 6A 6F 62 31 00        ,........job1.  
```

#### Opcodes

```
  0: 0x00C0 [0x2C] CREATE_SCHEDULER_TASK: Create scheduler "job1" with entities [EventEntity, EventEntity]
  1: 0x00CD [0x00] END_REQSTACK()
```

### Event 65535.12

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00CE   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00C0:                                            53 F8                S.
00D0: FF FF 7F F8 FF FF 7F 6A  6F 62 31 00              .......job1.    
```

#### Opcodes

```
  0: 0x00CE [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "job1" with entities [EventEntity, EventEntity]
  1: 0x00DB [0x00] END_REQSTACK()
```

### Event 65535.13

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00DC   |
| Data Size    | 31 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00D0:                                      45 00 80 F0              E...
00E0: FF FF 7F F0 FF FF 7F 73  30 30 35 01 80 2C F8 FF  .......s005..,..
00F0: FF 7F F8 FF FF 7F 68 61  70 30 00                 ......hap0.     
```

#### Opcodes

```
  0: 0x00DC [0x45] LOAD_SCHEDULED_TASK: Load scheduler "s005" with entities [LocalPlayer, LocalPlayer], work=[188*, 0*]
  1: 0x00ED [0x2C] CREATE_SCHEDULER_TASK: Create scheduler "hap0" with entities [EventEntity, EventEntity]
  2: 0x00FA [0x00] END_REQSTACK()
```

### Event 65535.14

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00FB   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00F0:                                   53 F8 FF FF 7F             S....
0100: F8 FF FF 7F 68 61 70 30  00                       ....hap0.       
```

#### Opcodes

```
  0: 0x00FB [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "hap0" with entities [EventEntity, EventEntity]
  1: 0x0108 [0x00] END_REQSTACK()
```

### Event 65535.15

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0109   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0100:                             2C F8 FF FF 7F F8 FF           ,......
0110: FF 7F 68 61 70 31 00                              ..hap1.         
```

#### Opcodes

```
  0: 0x0109 [0x2C] CREATE_SCHEDULER_TASK: Create scheduler "hap1" with entities [EventEntity, EventEntity]
  1: 0x0116 [0x00] END_REQSTACK()
```

### Event 65535.16

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0117   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0110:                      53  F8 FF FF 7F F8 FF FF 7F         S........
0120: 68 61 70 31 00                                    hap1.           
```

#### Opcodes

```
  0: 0x0117 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "hap1" with entities [EventEntity, EventEntity]
  1: 0x0124 [0x00] END_REQSTACK()
```

### Event 65535.17

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0125   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0120:                2C F8 FF  FF 7F F8 FF FF 7F 6E 65       ,........ne
0130: 77 30 00                                          w0.             
```

#### Opcodes

```
  0: 0x0125 [0x2C] CREATE_SCHEDULER_TASK: Create scheduler "new0" with entities [EventEntity, EventEntity]
  1: 0x0132 [0x00] END_REQSTACK()
```

### Event 65535.18

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0133   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0130:          53 F8 FF FF 7F  F8 FF FF 7F 6E 65 77 30     S........new0
0140: 00                                                .               
```

#### Opcodes

```
  0: 0x0133 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "new0" with entities [EventEntity, EventEntity]
  1: 0x0140 [0x00] END_REQSTACK()
```

### Event 65535.19

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0141   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0140:    2C F8 FF FF 7F F8 FF  FF 7F 6E 65 77 31 00      ,........new1. 
```

#### Opcodes

```
  0: 0x0141 [0x2C] CREATE_SCHEDULER_TASK: Create scheduler "new1" with entities [EventEntity, EventEntity]
  1: 0x014E [0x00] END_REQSTACK()
```

### Event 65535.20

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x014F   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0140:                                               53                 S
0150: F8 FF FF 7F F8 FF FF 7F  6E 65 77 31 00           ........new1.   
```

#### Opcodes

```
  0: 0x014F [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "new1" with entities [EventEntity, EventEntity]
  1: 0x015C [0x00] END_REQSTACK()
```

### Event 65535.21

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x015D   |
| Data Size    | 31 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0150:                                         45 00 80               E..
0160: F0 FF FF 7F F0 FF FF 7F  73 30 30 37 01 80 2C F8  ........s007..,.
0170: FF FF 7F F8 FF FF 7F 65  78 70 30 00              .......exp0.    
```

#### Opcodes

```
  0: 0x015D [0x45] LOAD_SCHEDULED_TASK: Load scheduler "s007" with entities [LocalPlayer, LocalPlayer], work=[188*, 0*]
  1: 0x016E [0x2C] CREATE_SCHEDULER_TASK: Create scheduler "exp0" with entities [EventEntity, EventEntity]
  2: 0x017B [0x00] END_REQSTACK()
```

### Event 65535.22

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x017C   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0170:                                      53 F8 FF FF              S...
0180: 7F F8 FF FF 7F 65 78 70  30 00                    .....exp0.      
```

#### Opcodes

```
  0: 0x017C [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "exp0" with entities [EventEntity, EventEntity]
  1: 0x0189 [0x00] END_REQSTACK()
```

### Event 65535.23

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x018A   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0180:                                2C F8 FF FF 7F F8            ,.....
0190: FF FF 7F 65 78 70 31 00                           ...exp1.        
```

#### Opcodes

```
  0: 0x018A [0x2C] CREATE_SCHEDULER_TASK: Create scheduler "exp1" with entities [EventEntity, EventEntity]
  1: 0x0197 [0x00] END_REQSTACK()
```

### Event 65535.24

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0198   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0190:                          53 F8 FF FF 7F F8 FF FF          S.......
01A0: 7F 65 78 70 31 00                                 .exp1.          
```

#### Opcodes

```
  0: 0x0198 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "exp1" with entities [EventEntity, EventEntity]
  1: 0x01A5 [0x00] END_REQSTACK()
```

### Event 4

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x01A6  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
01A0:                   00                                    .         
```

#### Opcodes

```
  0: 0x01A6 [0x00] END_REQSTACK()
```

### Event 65535.25

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x01A7   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
01A0:                      37  02 80 03 80 04 80 05 80         7........
01B0: 00                                                .               
```

#### Opcodes

```
  0: 0x01A7 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=435.549*, z=-20.760*, y=-0.480*, direction=168.7°*
  1: 0x01B0 [0x00] END_REQSTACK()
```

### Event 65535.26

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x01B1   |
| Data Size    | 22 bytes |
| Instructions | 8        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
01B0:    32 06 80 1F 00 07 80  08 80 09 80 1F 01 6F 1E   2............o.
01C0: 4F 81 01 01 6F 70 00                              O...op.         
```

#### Opcodes

```
  0: 0x01B1 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x01B4 [0x1F] MOVE_ENTITY: EventEntity moves to X=428.758*, Z=-23.237*, Y=-1.660*
  2: 0x01BC [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x01BE [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x01BF [0x1E] EventEntity looks at Sanctia (ID: 16875855/0x0101814F) and starts talking
  5: 0x01C4 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  6: 0x01C5 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  7: 0x01C6 [0x00] END_REQSTACK()
```

### Event 65535.27

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x01C7   |
| Data Size    | 15 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
01C0:                      32  0A 80 1F 00 0B 80 0C 80         2........
01D0: 0D 80 1F 01 6F 00                                 ....o.          
```

#### Opcodes

```
  0: 0x01C7 [0x32] ExtData[1]->MainSpeed = 40* * 0.1
  1: 0x01CA [0x1F] MOVE_ENTITY: EventEntity moves to X=421.322*, Z=-36.396*, Y=1.241*
  2: 0x01D2 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x01D4 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x01D5 [0x00] END_REQSTACK()
```
