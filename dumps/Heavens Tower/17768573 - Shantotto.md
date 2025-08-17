# 17768573 - Shantotto

## Common Data

| Field            | Value                   |
|------------------|-------------------------|
| Zone             | Heavens Tower (ID: 242) |
| Block Size       | 676 bytes               |
| Total Events     | 32                      |
| References Count | 19                      |

## List of Events

| Event ID                   | Entrypoint   |   Size |   Instructions |
|----------------------------|--------------|--------|----------------|
| [65535](#event-65535)      | 0x0000       |      1 |              1 |
| [65535.1](#event-655351)   | 0x0001       |     16 |              2 |
| [65535.2](#event-655352)   | 0x0011       |     22 |              4 |
| [65535.3](#event-655353)   | 0x0027       |     16 |              2 |
| [65535.4](#event-655354)   | 0x0037       |     22 |              4 |
| [65535.5](#event-655355)   | 0x004D       |     16 |              2 |
| [65535.6](#event-655356)   | 0x005D       |     14 |              2 |
| [65535.7](#event-655357)   | 0x006B       |     16 |              2 |
| [65535.8](#event-655358)   | 0x007B       |     14 |              2 |
| [65535.9](#event-655359)   | 0x0089       |     16 |              2 |
| [65535.10](#event-6553510) | 0x0099       |     14 |              2 |
| [65535.11](#event-6553511) | 0x00A7       |     16 |              2 |
| [65535.12](#event-6553512) | 0x00B7       |     14 |              2 |
| [65535.13](#event-6553513) | 0x00C5       |     16 |              2 |
| [65535.14](#event-6553514) | 0x00D5       |     14 |              2 |
| [65535.15](#event-6553515) | 0x00E3       |     16 |              2 |
| [65535.16](#event-6553516) | 0x00F3       |     14 |              2 |
| [65535.17](#event-6553517) | 0x0101       |     16 |              2 |
| [65535.18](#event-6553518) | 0x0111       |     14 |              2 |
| [65535.19](#event-6553519) | 0x011F       |      9 |              3 |
| [65535.20](#event-6553520) | 0x0128       |     16 |              2 |
| [65535.21](#event-6553521) | 0x0138       |     14 |              2 |
| [65535.22](#event-6553522) | 0x0146       |     16 |              2 |
| [65535.23](#event-6553523) | 0x0156       |     14 |              2 |
| [441](#event-441)          | 0x0164       |      1 |              1 |
| [65535.24](#event-6553524) | 0x0165       |     15 |              5 |
| [455](#event-455)          | 0x0174       |      1 |              1 |
| [65535.25](#event-6553525) | 0x0175       |     14 |              4 |
| [65535.26](#event-6553526) | 0x0183       |     14 |              4 |
| [65535.27](#event-6553527) | 0x0191       |     15 |              5 |
| [65535.28](#event-6553528) | 0x01A0       |     22 |              8 |
| [65535.29](#event-6553529) | 0x01B6       |     15 |              5 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0153      |         339 |
|       1 | 0x001E      |          30 |
|       2 | 0x0151      |         337 |
|       3 | 0x0036      |          54 |
|       4 | 0x000D      |          13 |
|       5 | 0x095B      |        2395 |
|       6 | 0x68B7      |       26807 |
|       7 | 0x01F3      |         499 |
|       8 | 0x026B      |         619 |
|       9 | 0x5799      |       22425 |
|      10 | 0xFFFFFF06  |  4294967046 |
|      11 | 0x0668      |        1640 |
|      12 | 0x76E7      |       30439 |
|      13 | 0x0000      |           0 |
|      14 | 0x06E1      |        1761 |
|      15 | 0x7585      |       30085 |
|      16 | 0x0640      |        1600 |
|      17 | 0x729B      |       29339 |
|      18 | 0x00F9      |         249 |

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
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    5B 00 80 F8 FF FF 7F  F8 FF FF 7F 6F 68 68 30   [..........ohh0
0010: 00                                                .               
```

#### Opcodes

```
  0: 0x0001 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "ohh0" with entities [EventEntity, EventEntity], work=339*
  1: 0x0010 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0011   |
| Data Size    | 22 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:    53 F8 FF FF 7F F8 FF  FF 7F 6F 68 68 30 5E 69   S........ohh0^i
0020: 64 6C 30 1C 01 80 00                              dl0....         
```

#### Opcodes

```
  0: 0x0011 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "ohh0" with entities [EventEntity, EventEntity]
  1: 0x001E [0x5E] EventEntity goes idle (kills current action) (animation: "idl0")
  2: 0x0023 [0x1C] WAIT(30* ticks)
  3: 0x0026 [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0027   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                      5B  02 80 F8 FF FF 7F F8 FF         [........
0030: FF 7F 74 6C 6B 30 00                              ..tlk0.         
```

#### Opcodes

```
  0: 0x0027 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=337*
  1: 0x0036 [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0037   |
| Data Size    | 22 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:                      53  F8 FF FF 7F F8 FF FF 7F         S........
0040: 74 6C 6B 30 5E 69 64 6C  30 1C 01 80 00           tlk0^idl0....   
```

#### Opcodes

```
  0: 0x0037 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "tlk0" with entities [EventEntity, EventEntity]
  1: 0x0044 [0x5E] EventEntity goes idle (kills current action) (animation: "idl0")
  2: 0x0049 [0x1C] WAIT(30* ticks)
  3: 0x004C [0x00] END_REQSTACK()
```

### Event 65535.5

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x004D   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                                         5B 02 80               [..
0050: F8 FF FF 7F F8 FF FF 7F  74 68 6B 31 00           ........thk1.   
```

#### Opcodes

```
  0: 0x004D [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "thk1" with entities [EventEntity, EventEntity], work=337*
  1: 0x005C [0x00] END_REQSTACK()
```

### Event 65535.6

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x005D   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:                                         53 F8 FF               S..
0060: FF 7F F8 FF FF 7F 74 68  6B 31 00                 ......thk1.     
```

#### Opcodes

```
  0: 0x005D [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "thk1" with entities [EventEntity, EventEntity]
  1: 0x006A [0x00] END_REQSTACK()
```

### Event 65535.7

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x006B   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060:                                   5B 02 80 F8 FF             [....
0070: FF 7F F8 FF FF 7F 74 68  6B 32 00                 ......thk2.     
```

#### Opcodes

```
  0: 0x006B [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "thk2" with entities [EventEntity, EventEntity], work=337*
  1: 0x007A [0x00] END_REQSTACK()
```

### Event 65535.8

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x007B   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0070:                                   53 F8 FF FF 7F             S....
0080: F8 FF FF 7F 74 68 6B 32  00                       ....thk2.       
```

#### Opcodes

```
  0: 0x007B [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "thk2" with entities [EventEntity, EventEntity]
  1: 0x0088 [0x00] END_REQSTACK()
```

### Event 65535.9

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0089   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0080:                             5B 02 80 F8 FF FF 7F           [......
0090: F8 FF FF 7F 70 6F 69 30  00                       ....poi0.       
```

#### Opcodes

```
  0: 0x0089 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "poi0" with entities [EventEntity, EventEntity], work=337*
  1: 0x0098 [0x00] END_REQSTACK()
```

### Event 65535.10

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0099   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0090:                             53 F8 FF FF 7F F8 FF           S......
00A0: FF 7F 70 6F 69 30 00                              ..poi0.         
```

#### Opcodes

```
  0: 0x0099 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "poi0" with entities [EventEntity, EventEntity]
  1: 0x00A6 [0x00] END_REQSTACK()
```

### Event 65535.11

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00A7   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00A0:                      5B  02 80 F8 FF FF 7F F8 FF         [........
00B0: FF 7F 70 61 73 30 00                              ..pas0.         
```

#### Opcodes

```
  0: 0x00A7 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "pas0" with entities [EventEntity, EventEntity], work=337*
  1: 0x00B6 [0x00] END_REQSTACK()
```

### Event 65535.12

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
00C0: 70 61 73 30 00                                    pas0.           
```

#### Opcodes

```
  0: 0x00B7 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "pas0" with entities [EventEntity, EventEntity]
  1: 0x00C4 [0x00] END_REQSTACK()
```

### Event 65535.13

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00C5   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00C0:                5B 02 80  F8 FF FF 7F F8 FF FF 7F       [..........
00D0: 69 72 6F 30 00                                    iro0.           
```

#### Opcodes

```
  0: 0x00C5 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "iro0" with entities [EventEntity, EventEntity], work=337*
  1: 0x00D4 [0x00] END_REQSTACK()
```

### Event 65535.14

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00D5   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00D0:                53 F8 FF  FF 7F F8 FF FF 7F 69 72       S........ir
00E0: 6F 30 00                                          o0.             
```

#### Opcodes

```
  0: 0x00D5 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "iro0" with entities [EventEntity, EventEntity]
  1: 0x00E2 [0x00] END_REQSTACK()
```

### Event 65535.15

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00E3   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00E0:          5B 00 80 F8 FF  FF 7F F8 FF FF 7F 73 68     [..........sh
00F0: 6B 30 00                                          k0.             
```

#### Opcodes

```
  0: 0x00E3 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "shk0" with entities [EventEntity, EventEntity], work=339*
  1: 0x00F2 [0x00] END_REQSTACK()
```

### Event 65535.16

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00F3   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00F0:          53 F8 FF FF 7F  F8 FF FF 7F 73 68 6B 30     S........shk0
0100: 00                                                .               
```

#### Opcodes

```
  0: 0x00F3 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "shk0" with entities [EventEntity, EventEntity]
  1: 0x0100 [0x00] END_REQSTACK()
```

### Event 65535.17

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0101   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0100:    5B 02 80 F8 FF FF 7F  F8 FF FF 7F 64 69 73 30   [..........dis0
0110: 00                                                .               
```

#### Opcodes

```
  0: 0x0101 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "dis0" with entities [EventEntity, EventEntity], work=337*
  1: 0x0110 [0x00] END_REQSTACK()
```

### Event 65535.18

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0111   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0110:    53 F8 FF FF 7F F8 FF  FF 7F 64 69 73 30 00      S........dis0. 
```

#### Opcodes

```
  0: 0x0111 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "dis0" with entities [EventEntity, EventEntity]
  1: 0x011E [0x00] END_REQSTACK()
```

### Event 65535.19

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x011F  |
| Data Size    | 9 bytes |
| Instructions | 3       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0110:                                               5E                 ^
0120: 69 64 6C 30 1C 01 80 00                           idl0....        
```

#### Opcodes

```
  0: 0x011F [0x5E] EventEntity goes idle (kills current action) (animation: "idl0")
  1: 0x0124 [0x1C] WAIT(30* ticks)
  2: 0x0127 [0x00] END_REQSTACK()
```

### Event 65535.20

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0128   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0120:                          5B 03 80 F8 FF FF 7F F8          [.......
0130: FF FF 7F 6D 67 69 30 00                           ...mgi0.        
```

#### Opcodes

```
  0: 0x0128 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "mgi0" with entities [EventEntity, EventEntity], work=54*
  1: 0x0137 [0x00] END_REQSTACK()
```

### Event 65535.21

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
0140: 7F 6D 67 69 30 00                                 .mgi0.          
```

#### Opcodes

```
  0: 0x0138 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "mgi0" with entities [EventEntity, EventEntity]
  1: 0x0145 [0x00] END_REQSTACK()
```

### Event 65535.22

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0146   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0140:                   5B 03  80 F8 FF FF 7F F8 FF FF        [.........
0150: 7F 6D 67 69 31 00                                 .mgi1.          
```

#### Opcodes

```
  0: 0x0146 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "mgi1" with entities [EventEntity, EventEntity], work=54*
  1: 0x0155 [0x00] END_REQSTACK()
```

### Event 65535.23

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0156   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0150:                   53 F8  FF FF 7F F8 FF FF 7F 6D        S........m
0160: 67 69 31 00                                       gi1.            
```

#### Opcodes

```
  0: 0x0156 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "mgi1" with entities [EventEntity, EventEntity]
  1: 0x0163 [0x00] END_REQSTACK()
```

### Event 441

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0164  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0160:             00                                        .           
```

#### Opcodes

```
  0: 0x0164 [0x00] END_REQSTACK()
```

### Event 65535.24

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0165   |
| Data Size    | 15 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0160:                32 04 80  1F 00 05 80 06 80 07 80       2..........
0170: 1F 01 6F 00                                       ..o.            
```

#### Opcodes

```
  0: 0x0165 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x0168 [0x1F] MOVE_ENTITY: EventEntity moves to X=2.395*, Z=26.807*, Y=0.499*
  2: 0x0170 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0172 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x0173 [0x00] END_REQSTACK()
```

### Event 455

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0174  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0170:             00                                        .           
```

#### Opcodes

```
  0: 0x0174 [0x00] END_REQSTACK()
```

### Event 65535.25

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0175   |
| Data Size    | 14 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0170:                32 04 80  1F 00 08 80 09 80 0A 80       2..........
0180: 1F 01 00                                          ...             
```

#### Opcodes

```
  0: 0x0175 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x0178 [0x1F] MOVE_ENTITY: EventEntity moves to X=0.619*, Z=22.425*, Y=-0.250*
  2: 0x0180 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0182 [0x00] END_REQSTACK()
```

### Event 65535.26

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0183   |
| Data Size    | 14 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0180:          32 04 80 5A 00  0B 80 0C 80 0D 80 5A 01     2..Z.......Z.
0190: 00                                                .               
```

#### Opcodes

```
  0: 0x0183 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x0186 [0x5A] UPDATE_EVENT_POSITION: Set EventEntity MovePosition to X=1.640*, Z=30.439*, Y=0.000*
  2: 0x018E [0x5A] UPDATE_EVENT_POSITION: Move EventEntity incrementally towards MovePosition
  3: 0x0190 [0x00] END_REQSTACK()
```

### Event 65535.27

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0191   |
| Data Size    | 15 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0190:    32 04 80 1F 00 0E 80  0F 80 0D 80 1F 01 6F 00   2............o.
```

#### Opcodes

```
  0: 0x0191 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x0194 [0x1F] MOVE_ENTITY: EventEntity moves to X=1.761*, Z=30.085*, Y=0.000*
  2: 0x019C [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x019E [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x019F [0x00] END_REQSTACK()
```

### Event 65535.28

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x01A0   |
| Data Size    | 22 bytes |
| Instructions | 8        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
01A0: 32 04 80 1F 00 10 80 11  80 12 80 1F 01 6F 1E F0  2............o..
01B0: FF FF 7F 6F 70 00                                 ...op.          
```

#### Opcodes

```
  0: 0x01A0 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x01A3 [0x1F] MOVE_ENTITY: EventEntity moves to X=1.600*, Z=29.339*, Y=0.249*
  2: 0x01AB [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x01AD [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x01AE [0x1E] EventEntity looks at LocalPlayer and starts talking
  5: 0x01B3 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  6: 0x01B4 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  7: 0x01B5 [0x00] END_REQSTACK()
```

### Event 65535.29

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x01B6   |
| Data Size    | 15 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
01B0:                   32 04  80 1F 00 08 80 09 80 0A        2.........
01C0: 80 1F 01 6F 00                                    ...o.           
```

#### Opcodes

```
  0: 0x01B6 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x01B9 [0x1F] MOVE_ENTITY: EventEntity moves to X=0.619*, Z=22.425*, Y=-0.250*
  2: 0x01C1 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x01C3 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x01C4 [0x00] END_REQSTACK()
```
