# 17494802 - SaJho Shieldbreaker

## Common Data

| Field            | Value                                |
|------------------|--------------------------------------|
| Zone             | The Eldieme Necropolis [S] (ID: 175) |
| Block Size       | 312 bytes                            |
| Total Events     | 17                                   |
| References Count | 4                                    |

## List of Events

| Event ID                   | Entrypoint   |   Size |   Instructions |
|----------------------------|--------------|--------|----------------|
| [65535](#event-65535)      | 0x0000       |      1 |              1 |
| [48](#event-48)            | 0x0001       |      7 |              2 |
| [49](#event-49)            | 0x0008       |      7 |              2 |
| [65535.1](#event-655351)   | 0x000F       |      7 |              3 |
| [65535.2](#event-655352)   | 0x0016       |      7 |              3 |
| [65535.3](#event-655353)   | 0x001D       |     16 |              2 |
| [65535.4](#event-655354)   | 0x002D       |     14 |              2 |
| [65535.5](#event-655355)   | 0x003B       |     16 |              2 |
| [65535.6](#event-655356)   | 0x004B       |     14 |              2 |
| [65535.7](#event-655357)   | 0x0059       |     16 |              2 |
| [65535.8](#event-655358)   | 0x0069       |     14 |              2 |
| [65535.9](#event-655359)   | 0x0077       |     16 |              2 |
| [65535.10](#event-6553510) | 0x0087       |     14 |              2 |
| [65535.11](#event-6553511) | 0x0095       |     16 |              2 |
| [65535.12](#event-6553512) | 0x00A5       |     14 |              2 |
| [65535.13](#event-6553513) | 0x00B3       |     16 |              2 |
| [65535.14](#event-6553514) | 0x00C3       |     14 |              2 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0001      |           1 |
|       1 | 0x0000      |           0 |
|       2 | 0x04F2      |        1266 |
|       3 | 0x00E3      |         227 |

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

### Event 48

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

### Event 49

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0008  |
| Data Size    | 7 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                          92 01 F8 FF FF 7F 00             ....... 
```

#### Opcodes

```
  0: 0x0008 [0x92] EventEntity->Render.Flags3 ^= 0x01
  1: 0x000E [0x00] END_REQSTACK()
```

### Event 65535.1

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x000F  |
| Data Size    | 7 bytes |
| Instructions | 3       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                                               AB                 .
0010: 03 AC 01 00 80 00                                 ......          
```

#### Opcodes

```
  0: 0x000F [0xAB] EventEntity->Render.Flags0 ^= 0x20000 // Toggle bit 17
  1: 0x0011 [0xAC] EventEntity->StatusEvent = 1*
  2: 0x0015 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0016  |
| Data Size    | 7 bytes |
| Instructions | 3       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                   AC 01  01 80 AB 04 00                 .......   
```

#### Opcodes

```
  0: 0x0016 [0xAC] EventEntity->StatusEvent = 0*
  1: 0x001A [0xAB] EventEntity->Render.Flags0 |= 0x40000 // Set bit 18
  2: 0x001C [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x001D   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                                         5B 02 80               [..
0020: F8 FF FF 7F F8 FF FF 7F  70 76 30 30 00           ........pv00.   
```

#### Opcodes

```
  0: 0x001D [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "pv00" with entities [EventEntity, EventEntity], work=1266*
  1: 0x002C [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x002D   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                                         53 F8 FF               S..
0030: FF 7F F8 FF FF 7F 70 76  30 30 00                 ......pv00.     
```

#### Opcodes

```
  0: 0x002D [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "pv00" with entities [EventEntity, EventEntity]
  1: 0x003A [0x00] END_REQSTACK()
```

### Event 65535.5

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x003B   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:                                   5B 02 80 F8 FF             [....
0040: FF 7F F8 FF FF 7F 70 76  30 31 00                 ......pv01.     
```

#### Opcodes

```
  0: 0x003B [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "pv01" with entities [EventEntity, EventEntity], work=1266*
  1: 0x004A [0x00] END_REQSTACK()
```

### Event 65535.6

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x004B   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                                   53 F8 FF FF 7F             S....
0050: F8 FF FF 7F 70 76 30 31  00                       ....pv01.       
```

#### Opcodes

```
  0: 0x004B [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "pv01" with entities [EventEntity, EventEntity]
  1: 0x0058 [0x00] END_REQSTACK()
```

### Event 65535.7

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0059   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:                             5B 03 80 F8 FF FF 7F           [......
0060: F8 FF FF 7F 74 6C 6B 30  00                       ....tlk0.       
```

#### Opcodes

```
  0: 0x0059 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=227*
  1: 0x0068 [0x00] END_REQSTACK()
```

### Event 65535.8

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
0070: FF 7F 74 6C 6B 30 00                              ..tlk0.         
```

#### Opcodes

```
  0: 0x0069 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "tlk0" with entities [EventEntity, EventEntity]
  1: 0x0076 [0x00] END_REQSTACK()
```

### Event 65535.9

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0077   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0070:                      5B  03 80 F8 FF FF 7F F8 FF         [........
0080: FF 7F 74 6C 6B 31 00                              ..tlk1.         
```

#### Opcodes

```
  0: 0x0077 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tlk1" with entities [EventEntity, EventEntity], work=227*
  1: 0x0086 [0x00] END_REQSTACK()
```

### Event 65535.10

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0087   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0080:                      53  F8 FF FF 7F F8 FF FF 7F         S........
0090: 74 6C 6B 31 00                                    tlk1.           
```

#### Opcodes

```
  0: 0x0087 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "tlk1" with entities [EventEntity, EventEntity]
  1: 0x0094 [0x00] END_REQSTACK()
```

### Event 65535.11

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0095   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0090:                5B 03 80  F8 FF FF 7F F8 FF FF 7F       [..........
00A0: 65 76 61 30 00                                    eva0.           
```

#### Opcodes

```
  0: 0x0095 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "eva0" with entities [EventEntity, EventEntity], work=227*
  1: 0x00A4 [0x00] END_REQSTACK()
```

### Event 65535.12

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00A5   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00A0:                53 F8 FF  FF 7F F8 FF FF 7F 65 76       S........ev
00B0: 61 30 00                                          a0.             
```

#### Opcodes

```
  0: 0x00A5 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "eva0" with entities [EventEntity, EventEntity]
  1: 0x00B2 [0x00] END_REQSTACK()
```

### Event 65535.13

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00B3   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00B0:          5B 03 80 F8 FF  FF 7F F8 FF FF 7F 65 76     [..........ev
00C0: 62 30 00                                          b0.             
```

#### Opcodes

```
  0: 0x00B3 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "evb0" with entities [EventEntity, EventEntity], work=227*
  1: 0x00C2 [0x00] END_REQSTACK()
```

### Event 65535.14

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00C3   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00C0:          53 F8 FF FF 7F  F8 FF FF 7F 65 76 62 30     S........evb0
00D0: 00                                                .               
```

#### Opcodes

```
  0: 0x00C3 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "evb0" with entities [EventEntity, EventEntity]
  1: 0x00D0 [0x00] END_REQSTACK()
```
