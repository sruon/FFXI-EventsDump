# 17404442 - Mandragora Warden

## Common Data

| Field            | Value                      |
|------------------|----------------------------|
| Zone             | The Boyahda Tree (ID: 153) |
| Block Size       | 552 bytes                  |
| Total Events     | 26                         |
| References Count | 11                         |

## List of Events

| Event ID                   | Entrypoint   |   Size |   Instructions |
|----------------------------|--------------|--------|----------------|
| [65535](#event-65535)      | 0x0000       |      1 |              1 |
| [65535.1](#event-655351)   | 0x0001       |     16 |              2 |
| [65535.2](#event-655352)   | 0x0011       |     14 |              2 |
| [65535.3](#event-655353)   | 0x001F       |     16 |              2 |
| [65535.4](#event-655354)   | 0x002F       |     14 |              2 |
| [65535.5](#event-655355)   | 0x003D       |     16 |              2 |
| [65535.6](#event-655356)   | 0x004D       |     14 |              2 |
| [65535.7](#event-655357)   | 0x005B       |     16 |              2 |
| [65535.8](#event-655358)   | 0x006B       |     14 |              2 |
| [65535.9](#event-655359)   | 0x0079       |     16 |              2 |
| [65535.10](#event-6553510) | 0x0089       |     14 |              2 |
| [65535.11](#event-6553511) | 0x0097       |     16 |              2 |
| [65535.12](#event-6553512) | 0x00A7       |     14 |              2 |
| [65535.13](#event-6553513) | 0x00B5       |     16 |              2 |
| [65535.14](#event-6553514) | 0x00C5       |     14 |              2 |
| [65535.15](#event-6553515) | 0x00D3       |     14 |              2 |
| [65535.16](#event-6553516) | 0x00E1       |     14 |              2 |
| [65535.17](#event-6553517) | 0x00EF       |     16 |              2 |
| [65535.18](#event-6553518) | 0x00FF       |     14 |              2 |
| [32](#event-32)            | 0x010D       |      7 |              2 |
| [65535.19](#event-6553519) | 0x0114       |     22 |              8 |
| [65535.20](#event-6553520) | 0x012A       |     22 |              8 |
| [65535.21](#event-6553521) | 0x0140       |     29 |              3 |
| [65535.22](#event-6553522) | 0x015D       |     29 |              3 |
| [65535.23](#event-6553523) | 0x017A       |      5 |              2 |
| [65535.24](#event-6553524) | 0x017F       |      5 |              2 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0871      |        2161 |
|       1 | 0x0028      |          40 |
|       2 | 0x19708     |      104200 |
|       3 | 0x214CA     |      136394 |
|       4 | 0x2189      |        8585 |
|       5 | 0x000D      |          13 |
|       6 | 0x19760     |      104288 |
|       7 | 0x219D8     |      137688 |
|       8 | 0x2177      |        8567 |
|       9 | 0x0B8F      |        2959 |
|      10 | 0x012C      |         300 |

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
0000:    5B 00 80 F8 FF FF 7F  F8 FF FF 7F 74 6C 6B 30   [..........tlk0
0010: 00                                                .               
```

#### Opcodes

```
  0: 0x0001 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=2161*
  1: 0x0010 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0011   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:    53 F8 FF FF 7F F8 FF  FF 7F 74 6C 6B 30 00      S........tlk0. 
```

#### Opcodes

```
  0: 0x0011 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "tlk0" with entities [EventEntity, EventEntity]
  1: 0x001E [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x001F   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                                               5B                 [
0020: 00 80 F8 FF FF 7F F8 FF  FF 7F 74 6C 6B 31 00     ..........tlk1. 
```

#### Opcodes

```
  0: 0x001F [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tlk1" with entities [EventEntity, EventEntity], work=2161*
  1: 0x002E [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x002F   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                                               53                 S
0030: F8 FF FF 7F F8 FF FF 7F  74 6C 6B 31 00           ........tlk1.   
```

#### Opcodes

```
  0: 0x002F [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "tlk1" with entities [EventEntity, EventEntity]
  1: 0x003C [0x00] END_REQSTACK()
```

### Event 65535.5

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x003D   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:                                         5B 00 80               [..
0040: F8 FF FF 7F F8 FF FF 7F  62 69 6B 30 00           ........bik0.   
```

#### Opcodes

```
  0: 0x003D [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "bik0" with entities [EventEntity, EventEntity], work=2161*
  1: 0x004C [0x00] END_REQSTACK()
```

### Event 65535.6

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x004D   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                                         53 F8 FF               S..
0050: FF 7F F8 FF FF 7F 62 69  6B 30 00                 ......bik0.     
```

#### Opcodes

```
  0: 0x004D [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "bik0" with entities [EventEntity, EventEntity]
  1: 0x005A [0x00] END_REQSTACK()
```

### Event 65535.7

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x005B   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:                                   5B 00 80 F8 FF             [....
0060: FF 7F F8 FF FF 7F 62 69  6B 31 00                 ......bik1.     
```

#### Opcodes

```
  0: 0x005B [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "bik1" with entities [EventEntity, EventEntity], work=2161*
  1: 0x006A [0x00] END_REQSTACK()
```

### Event 65535.8

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x006B   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060:                                   53 F8 FF FF 7F             S....
0070: F8 FF FF 7F 62 69 6B 31  00                       ....bik1.       
```

#### Opcodes

```
  0: 0x006B [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "bik1" with entities [EventEntity, EventEntity]
  1: 0x0078 [0x00] END_REQSTACK()
```

### Event 65535.9

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0079   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0070:                             5B 00 80 F8 FF FF 7F           [......
0080: F8 FF FF 7F 77 68 74 30  00                       ....wht0.       
```

#### Opcodes

```
  0: 0x0079 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "wht0" with entities [EventEntity, EventEntity], work=2161*
  1: 0x0088 [0x00] END_REQSTACK()
```

### Event 65535.10

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0089   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0080:                             53 F8 FF FF 7F F8 FF           S......
0090: FF 7F 77 68 74 30 00                              ..wht0.         
```

#### Opcodes

```
  0: 0x0089 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "wht0" with entities [EventEntity, EventEntity]
  1: 0x0096 [0x00] END_REQSTACK()
```

### Event 65535.11

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0097   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0090:                      5B  00 80 F8 FF FF 7F F8 FF         [........
00A0: FF 7F 77 68 74 31 00                              ..wht1.         
```

#### Opcodes

```
  0: 0x0097 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "wht1" with entities [EventEntity, EventEntity], work=2161*
  1: 0x00A6 [0x00] END_REQSTACK()
```

### Event 65535.12

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00A7   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00A0:                      53  F8 FF FF 7F F8 FF FF 7F         S........
00B0: 77 68 74 31 00                                    wht1.           
```

#### Opcodes

```
  0: 0x00A7 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "wht1" with entities [EventEntity, EventEntity]
  1: 0x00B4 [0x00] END_REQSTACK()
```

### Event 65535.13

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00B5   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00B0:                5B 00 80  F8 FF FF 7F F8 FF FF 7F       [..........
00C0: 73 6B 79 30 00                                    sky0.           
```

#### Opcodes

```
  0: 0x00B5 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "sky0" with entities [EventEntity, EventEntity], work=2161*
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
00C0:                53 F8 FF  FF 7F F8 FF FF 7F 73 6B       S........sk
00D0: 79 30 00                                          y0.             
```

#### Opcodes

```
  0: 0x00C5 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "sky0" with entities [EventEntity, EventEntity]
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
00D0:          2C F8 FF FF 7F  F8 FF FF 7F 73 70 31 30     ,........sp10
00E0: 00                                                .               
```

#### Opcodes

```
  0: 0x00D3 [0x2C] CREATE_SCHEDULER_TASK: Create scheduler "sp10" with entities [EventEntity, EventEntity]
  1: 0x00E0 [0x00] END_REQSTACK()
```

### Event 65535.16

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00E1   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00E0:    53 F8 FF FF 7F F8 FF  FF 7F 73 70 31 30 00      S........sp10. 
```

#### Opcodes

```
  0: 0x00E1 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "sp10" with entities [EventEntity, EventEntity]
  1: 0x00EE [0x00] END_REQSTACK()
```

### Event 65535.17

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00EF   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00E0:                                               5B                 [
00F0: 00 80 F8 FF FF 7F F8 FF  FF 7F 73 68 74 31 00     ..........sht1. 
```

#### Opcodes

```
  0: 0x00EF [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "sht1" with entities [EventEntity, EventEntity], work=2161*
  1: 0x00FE [0x00] END_REQSTACK()
```

### Event 65535.18

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00FF   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00F0:                                               53                 S
0100: F8 FF FF 7F F8 FF FF 7F  73 68 74 31 00           ........sht1.   
```

#### Opcodes

```
  0: 0x00FF [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "sht1" with entities [EventEntity, EventEntity]
  1: 0x010C [0x00] END_REQSTACK()
```

### Event 32

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x010D  |
| Data Size    | 7 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0100:                                         92 01 F8               ...
0110: FF FF 7F 00                                       ....            
```

#### Opcodes

```
  0: 0x010D [0x92] EventEntity->Render.Flags3 ^= 0x01
  1: 0x0113 [0x00] END_REQSTACK()
```

### Event 65535.19

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0114   |
| Data Size    | 22 bytes |
| Instructions | 8        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0110:             32 01 80 1F  00 02 80 03 80 04 80 1F      2...........
0120: 01 6F 1E 0D 92 09 01 6F  70 00                    .o.....op.      
```

#### Opcodes

```
  0: 0x0114 [0x32] ExtData[1]->MainSpeed = 40* * 0.1
  1: 0x0117 [0x1F] MOVE_ENTITY: EventEntity moves to X=104.200*, Z=136.394*, Y=8.585*
  2: 0x011F [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0121 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x0122 [0x1E] EventEntity looks at Magh Bihu (ID: 17404429/0x0109920D) and starts talking
  5: 0x0127 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  6: 0x0128 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  7: 0x0129 [0x00] END_REQSTACK()
```

### Event 65535.20

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x012A   |
| Data Size    | 22 bytes |
| Instructions | 8        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0120:                                32 05 80 1F 00 06            2.....
0130: 80 07 80 08 80 1F 01 6F  1E 0D 92 09 01 6F 70 00  .......o.....op.
```

#### Opcodes

```
  0: 0x012A [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x012D [0x1F] MOVE_ENTITY: EventEntity moves to X=104.288*, Z=137.688*, Y=8.567*
  2: 0x0135 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0137 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x0138 [0x1E] EventEntity looks at Magh Bihu (ID: 17404429/0x0109920D) and starts talking
  5: 0x013D [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  6: 0x013E [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  7: 0x013F [0x00] END_REQSTACK()
```

### Event 65535.21

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0140   |
| Data Size    | 29 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0140: 5B 00 80 F8 FF FF 7F F8  FF FF 7F 73 6B 79 30 53  [..........sky0S
0150: F8 FF FF 7F F8 FF FF 7F  73 6B 79 30 00           ........sky0.   
```

#### Opcodes

```
  0: 0x0140 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "sky0" with entities [EventEntity, EventEntity], work=2161*
  1: 0x014F [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "sky0" with entities [EventEntity, EventEntity]
  2: 0x015C [0x00] END_REQSTACK()
```

### Event 65535.22

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x015D   |
| Data Size    | 29 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0150:                                         5B 00 80               [..
0160: F8 FF FF 7F F8 FF FF 7F  74 6C 6B 31 53 F8 FF FF  ........tlk1S...
0170: 7F F8 FF FF 7F 74 6C 6B  31 00                    .....tlk1.      
```

#### Opcodes

```
  0: 0x015D [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tlk1" with entities [EventEntity, EventEntity], work=2161*
  1: 0x016C [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "tlk1" with entities [EventEntity, EventEntity]
  2: 0x0179 [0x00] END_REQSTACK()
```

### Event 65535.23

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x017A  |
| Data Size    | 5 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0170:                                B6 00 09 80 00               ..... 
```

#### Opcodes

```
  0: 0x017A [0xB6] ENTITY_APPEARANCE_HANDLER(case=Hair style, value=2959*)
  1: 0x017E [0x00] END_REQSTACK()
```

### Event 65535.24

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x017F  |
| Data Size    | 5 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0170:                                               B6                 .
0180: 00 0A 80 00                                       ....            
```

#### Opcodes

```
  0: 0x017F [0xB6] ENTITY_APPEARANCE_HANDLER(case=Hair style, value=300*)
  1: 0x0183 [0x00] END_REQSTACK()
```
