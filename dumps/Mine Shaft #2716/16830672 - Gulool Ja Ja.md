# 16830672 - Gulool Ja Ja

## Common Data

| Field            | Value                     |
|------------------|---------------------------|
| Zone             | Mine Shaft #2716 (ID: 13) |
| Block Size       | 508 bytes                 |
| Total Events     | 27                        |
| References Count | 6                         |

## List of Events

| Event ID                   | Entrypoint   |   Size |   Instructions |
|----------------------------|--------------|--------|----------------|
| [65535](#event-65535)      | 0x0000       |      1 |              1 |
| [65535.1](#event-655351)   | 0x0001       |      7 |              3 |
| [65535.2](#event-655352)   | 0x0008       |      7 |              3 |
| [65535.3](#event-655353)   | 0x000F       |     16 |              2 |
| [65535.4](#event-655354)   | 0x001F       |     14 |              2 |
| [65535.5](#event-655355)   | 0x002D       |     16 |              2 |
| [65535.6](#event-655356)   | 0x003D       |     14 |              2 |
| [65535.7](#event-655357)   | 0x004B       |     16 |              2 |
| [65535.8](#event-655358)   | 0x005B       |     14 |              2 |
| [65535.9](#event-655359)   | 0x0069       |     16 |              2 |
| [65535.10](#event-6553510) | 0x0079       |     14 |              2 |
| [65535.11](#event-6553511) | 0x0087       |     16 |              2 |
| [65535.12](#event-6553512) | 0x0097       |     14 |              2 |
| [65535.13](#event-6553513) | 0x00A5       |     16 |              2 |
| [65535.14](#event-6553514) | 0x00B5       |     14 |              2 |
| [65535.15](#event-6553515) | 0x00C3       |     16 |              2 |
| [65535.16](#event-6553516) | 0x00D3       |     14 |              2 |
| [65535.17](#event-6553517) | 0x00E1       |     16 |              2 |
| [65535.18](#event-6553518) | 0x00F1       |     14 |              2 |
| [65535.19](#event-6553519) | 0x00FF       |     16 |              2 |
| [65535.20](#event-6553520) | 0x010F       |     14 |              2 |
| [65535.21](#event-6553521) | 0x011D       |     16 |              2 |
| [65535.22](#event-6553522) | 0x012D       |     14 |              2 |
| [65535.23](#event-6553523) | 0x013B       |     16 |              2 |
| [65535.24](#event-6553524) | 0x014B       |     14 |              2 |
| [8](#event-8)              | 0x0159       |      7 |              2 |
| [32001](#event-32001)      | 0x0160       |      7 |              2 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0001      |           1 |
|       1 | 0x0000      |           0 |
|       2 | 0x02D7      |         727 |
|       3 | 0x0383      |         899 |
|       4 | 0x03AC      |         940 |
|       5 | 0x03D6      |         982 |

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

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0001  |
| Data Size    | 7 bytes |
| Instructions | 3       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    AB 03 AC 01 00 80 00                            .......        
```

#### Opcodes

```
  0: 0x0001 [0xAB] EventEntity->Render.Flags0 ^= 0x20000 // Toggle bit 17
  1: 0x0003 [0xAC] EventEntity->StatusEvent = 1*
  2: 0x0007 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0008  |
| Data Size    | 7 bytes |
| Instructions | 3       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                          AC 01 01 80 AB 04 00             ....... 
```

#### Opcodes

```
  0: 0x0008 [0xAC] EventEntity->StatusEvent = 0*
  1: 0x000C [0xAB] EventEntity->Render.Flags0 |= 0x40000 // Set bit 18
  2: 0x000E [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x000F   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                                               5B                 [
0010: 02 80 F8 FF FF 7F F8 FF  FF 7F 77 61 72 30 00     ..........war0. 
```

#### Opcodes

```
  0: 0x000F [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "war0" with entities [EventEntity, EventEntity], work=727*
  1: 0x001E [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x001F   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                                               53                 S
0020: F8 FF FF 7F F8 FF FF 7F  77 61 72 30 00           ........war0.   
```

#### Opcodes

```
  0: 0x001F [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "war0" with entities [EventEntity, EventEntity]
  1: 0x002C [0x00] END_REQSTACK()
```

### Event 65535.5

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x002D   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                                         5B 03 80               [..
0030: F8 FF FF 7F F8 FF FF 7F  74 6C 66 30 00           ........tlf0.   
```

#### Opcodes

```
  0: 0x002D [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tlf0" with entities [EventEntity, EventEntity], work=899*
  1: 0x003C [0x00] END_REQSTACK()
```

### Event 65535.6

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x003D   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:                                         53 F8 FF               S..
0040: FF 7F F8 FF FF 7F 74 6C  66 30 00                 ......tlf0.     
```

#### Opcodes

```
  0: 0x003D [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "tlf0" with entities [EventEntity, EventEntity]
  1: 0x004A [0x00] END_REQSTACK()
```

### Event 65535.7

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x004B   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                                   5B 03 80 F8 FF             [....
0050: FF 7F F8 FF FF 7F 74 6C  66 31 00                 ......tlf1.     
```

#### Opcodes

```
  0: 0x004B [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tlf1" with entities [EventEntity, EventEntity], work=899*
  1: 0x005A [0x00] END_REQSTACK()
```

### Event 65535.8

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x005B   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:                                   53 F8 FF FF 7F             S....
0060: F8 FF FF 7F 74 6C 66 31  00                       ....tlf1.       
```

#### Opcodes

```
  0: 0x005B [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "tlf1" with entities [EventEntity, EventEntity]
  1: 0x0068 [0x00] END_REQSTACK()
```

### Event 65535.9

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0069   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060:                             5B 03 80 F8 FF FF 7F           [......
0070: F8 FF FF 7F 74 6C 6D 30  00                       ....tlm0.       
```

#### Opcodes

```
  0: 0x0069 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tlm0" with entities [EventEntity, EventEntity], work=899*
  1: 0x0078 [0x00] END_REQSTACK()
```

### Event 65535.10

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0079   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0070:                             53 F8 FF FF 7F F8 FF           S......
0080: FF 7F 74 6C 6D 30 00                              ..tlm0.         
```

#### Opcodes

```
  0: 0x0079 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "tlm0" with entities [EventEntity, EventEntity]
  1: 0x0086 [0x00] END_REQSTACK()
```

### Event 65535.11

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0087   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0080:                      5B  03 80 F8 FF FF 7F F8 FF         [........
0090: FF 7F 74 6C 6D 31 00                              ..tlm1.         
```

#### Opcodes

```
  0: 0x0087 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tlm1" with entities [EventEntity, EventEntity], work=899*
  1: 0x0096 [0x00] END_REQSTACK()
```

### Event 65535.12

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0097   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0090:                      53  F8 FF FF 7F F8 FF FF 7F         S........
00A0: 74 6C 6D 31 00                                    tlm1.           
```

#### Opcodes

```
  0: 0x0097 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "tlm1" with entities [EventEntity, EventEntity]
  1: 0x00A4 [0x00] END_REQSTACK()
```

### Event 65535.13

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00A5   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00A0:                5B 03 80  F8 FF FF 7F F8 FF FF 7F       [..........
00B0: 61 67 72 30 00                                    agr0.           
```

#### Opcodes

```
  0: 0x00A5 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "agr0" with entities [EventEntity, EventEntity], work=899*
  1: 0x00B4 [0x00] END_REQSTACK()
```

### Event 65535.14

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00B5   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00B0:                53 F8 FF  FF 7F F8 FF FF 7F 61 67       S........ag
00C0: 72 30 00                                          r0.             
```

#### Opcodes

```
  0: 0x00B5 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "agr0" with entities [EventEntity, EventEntity]
  1: 0x00C2 [0x00] END_REQSTACK()
```

### Event 65535.15

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00C3   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00C0:          5B 03 80 F8 FF  FF 7F F8 FF FF 7F 61 67     [..........ag
00D0: 72 31 00                                          r1.             
```

#### Opcodes

```
  0: 0x00C3 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "agr1" with entities [EventEntity, EventEntity], work=899*
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
00D0:          53 F8 FF FF 7F  F8 FF FF 7F 61 67 72 31     S........agr1
00E0: 00                                                .               
```

#### Opcodes

```
  0: 0x00D3 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "agr1" with entities [EventEntity, EventEntity]
  1: 0x00E0 [0x00] END_REQSTACK()
```

### Event 65535.17

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00E1   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00E0:    5B 04 80 F8 FF FF 7F  F8 FF FF 7F 74 61 69 30   [..........tai0
00F0: 00                                                .               
```

#### Opcodes

```
  0: 0x00E1 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tai0" with entities [EventEntity, EventEntity], work=940*
  1: 0x00F0 [0x00] END_REQSTACK()
```

### Event 65535.18

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00F1   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00F0:    53 F8 FF FF 7F F8 FF  FF 7F 74 61 69 30 00      S........tai0. 
```

#### Opcodes

```
  0: 0x00F1 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "tai0" with entities [EventEntity, EventEntity]
  1: 0x00FE [0x00] END_REQSTACK()
```

### Event 65535.19

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00FF   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00F0:                                               5B                 [
0100: 05 80 F8 FF FF 7F F8 FF  FF 7F 74 6C 66 32 00     ..........tlf2. 
```

#### Opcodes

```
  0: 0x00FF [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tlf2" with entities [EventEntity, EventEntity], work=982*
  1: 0x010E [0x00] END_REQSTACK()
```

### Event 65535.20

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x010F   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0100:                                               53                 S
0110: F8 FF FF 7F F8 FF FF 7F  74 6C 66 32 00           ........tlf2.   
```

#### Opcodes

```
  0: 0x010F [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "tlf2" with entities [EventEntity, EventEntity]
  1: 0x011C [0x00] END_REQSTACK()
```

### Event 65535.21

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x011D   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0110:                                         5B 05 80               [..
0120: F8 FF FF 7F F8 FF FF 7F  74 6C 6D 32 00           ........tlm2.   
```

#### Opcodes

```
  0: 0x011D [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tlm2" with entities [EventEntity, EventEntity], work=982*
  1: 0x012C [0x00] END_REQSTACK()
```

### Event 65535.22

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x012D   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0120:                                         53 F8 FF               S..
0130: FF 7F F8 FF FF 7F 74 6C  6D 32 00                 ......tlm2.     
```

#### Opcodes

```
  0: 0x012D [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "tlm2" with entities [EventEntity, EventEntity]
  1: 0x013A [0x00] END_REQSTACK()
```

### Event 65535.23

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x013B   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0130:                                   5B 05 80 F8 FF             [....
0140: FF 7F F8 FF FF 7F 74 66  6D 65 00                 ......tfme.     
```

#### Opcodes

```
  0: 0x013B [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tfme" with entities [EventEntity, EventEntity], work=982*
  1: 0x014A [0x00] END_REQSTACK()
```

### Event 65535.24

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x014B   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0140:                                   53 F8 FF FF 7F             S....
0150: F8 FF FF 7F 74 66 6D 65  00                       ....tfme.       
```

#### Opcodes

```
  0: 0x014B [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "tfme" with entities [EventEntity, EventEntity]
  1: 0x0158 [0x00] END_REQSTACK()
```

### Event 8

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0159  |
| Data Size    | 7 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0150:                             92 01 F8 FF FF 7F 00           .......
```

#### Opcodes

```
  0: 0x0159 [0x92] EventEntity->Render.Flags3 ^= 0x01
  1: 0x015F [0x00] END_REQSTACK()
```

### Event 32001

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0160  |
| Data Size    | 7 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0160: 92 01 F8 FF FF 7F 00                              .......         
```

#### Opcodes

```
  0: 0x0160 [0x92] EventEntity->Render.Flags3 ^= 0x01
  1: 0x0166 [0x00] END_REQSTACK()
```
