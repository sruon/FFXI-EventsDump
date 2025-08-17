# 17780806 - Nanaa Mihgo

## Common Data

| Field            | Value                 |
|------------------|-----------------------|
| Zone             | Lower Jeuno (ID: 245) |
| Block Size       | 712 bytes             |
| Total Events     | 33                    |
| References Count | 25                    |

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
| [65535.9](#event-655359)   | 0x0079       |     22 |              3 |
| [65535.10](#event-6553510) | 0x008F       |     14 |              2 |
| [65535.11](#event-6553511) | 0x009D       |     16 |              2 |
| [65535.12](#event-6553512) | 0x00AD       |     20 |              3 |
| [65535.13](#event-6553513) | 0x00C1       |     16 |              2 |
| [65535.14](#event-6553514) | 0x00D1       |     14 |              2 |
| [65535.15](#event-6553515) | 0x00DF       |     16 |              2 |
| [65535.16](#event-6553516) | 0x00EF       |     14 |              2 |
| [65535.17](#event-6553517) | 0x00FD       |     16 |              2 |
| [65535.18](#event-6553518) | 0x010D       |     14 |              2 |
| [65535.19](#event-6553519) | 0x011B       |     16 |              2 |
| [65535.20](#event-6553520) | 0x012B       |     14 |              2 |
| [65535.21](#event-6553521) | 0x0139       |     16 |              2 |
| [65535.22](#event-6553522) | 0x0149       |     14 |              2 |
| [65535.23](#event-6553523) | 0x0157       |     16 |              2 |
| [65535.24](#event-6553524) | 0x0167       |     14 |              2 |
| [65535.25](#event-6553525) | 0x0175       |      9 |              3 |
| [10021](#event-10021)      | 0x017E       |      3 |              2 |
| [10022](#event-10022)      | 0x0181       |      3 |              2 |
| [65535.26](#event-6553526) | 0x0184       |     10 |              2 |
| [65535.27](#event-6553527) | 0x018E       |     26 |              6 |
| [65535.28](#event-6553528) | 0x01A8       |     10 |              2 |
| [65535.29](#event-6553529) | 0x01B2       |     14 |              4 |
| [65535.30](#event-6553530) | 0x01C0       |     14 |              4 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0172      |         370 |
|       1 | 0x0166      |         358 |
|       2 | 0x0168      |         360 |
|       3 | 0x001E      |          30 |
|       4 | 0x4B8E      |       19342 |
|       5 | 0xFFFFE67B  |  4294960763 |
|       6 | 0xFFFFFF9C  |  4294967196 |
|       7 | 0x0D99      |        3481 |
|       8 | 0x4E79      |       20089 |
|       9 | 0xFFFFEB9C  |  4294962076 |
|      10 | 0xFFFFFF91  |  4294967185 |
|      11 | 0x0D9F      |        3487 |
|      12 | 0x0050      |          80 |
|      13 | 0x000D      |          13 |
|      14 | 0x52A4      |       21156 |
|      15 | 0xFFFFF347  |  4294964039 |
|      16 | 0x5D53      |       23891 |
|      17 | 0xFFFFF875  |  4294965365 |
|      18 | 0xFFFFFF9B  |  4294967195 |
|      19 | 0x0B83      |        2947 |
|      20 | 0x5694      |       22164 |
|      21 | 0x0240      |         576 |
|      22 | 0x53D8      |       21464 |
|      23 | 0x0700      |        1792 |
|      24 | 0xFFFFFF9D  |  4294967197 |

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
  0: 0x0001 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=370*
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
  0: 0x001F [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tlk1" with entities [EventEntity, EventEntity], work=370*
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
0040: F8 FF FF 7F F8 FF FF 7F  69 74 74 30 00           ........itt0.   
```

#### Opcodes

```
  0: 0x003D [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "itt0" with entities [EventEntity, EventEntity], work=370*
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
0050: FF 7F F8 FF FF 7F 69 74  74 30 00                 ......itt0.     
```

#### Opcodes

```
  0: 0x004D [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "itt0" with entities [EventEntity, EventEntity]
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
0050:                                   5B 01 80 F8 FF             [....
0060: FF 7F F8 FF FF 7F 69 74  74 31 00                 ......itt1.     
```

#### Opcodes

```
  0: 0x005B [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "itt1" with entities [EventEntity, EventEntity], work=358*
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
0070: F8 FF FF 7F 69 74 74 31  00                       ....itt1.       
```

#### Opcodes

```
  0: 0x006B [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "itt1" with entities [EventEntity, EventEntity]
  1: 0x0078 [0x00] END_REQSTACK()
```

### Event 65535.9

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0079   |
| Data Size    | 22 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0070:                             81 00 F8 FF FF 7F 5B           ......[
0080: 00 80 F8 FF FF 7F F8 FF  FF 7F 6E 74 6F 30 00     ..........nto0. 
```

#### Opcodes

```
  0: 0x0079 [0x81] SET_ENTITY_BLINKING(blink_flag=0x00, entity=EventEntity)
  1: 0x007F [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "nto0" with entities [EventEntity, EventEntity], work=370*
  2: 0x008E [0x00] END_REQSTACK()
```

### Event 65535.10

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x008F   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0080:                                               53                 S
0090: F8 FF FF 7F F8 FF FF 7F  6E 74 6F 30 00           ........nto0.   
```

#### Opcodes

```
  0: 0x008F [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "nto0" with entities [EventEntity, EventEntity]
  1: 0x009C [0x00] END_REQSTACK()
```

### Event 65535.11

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x009D   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0090:                                         5B 00 80               [..
00A0: F8 FF FF 7F F8 FF FF 7F  6E 74 6F 31 00           ........nto1.   
```

#### Opcodes

```
  0: 0x009D [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "nto1" with entities [EventEntity, EventEntity], work=370*
  1: 0x00AC [0x00] END_REQSTACK()
```

### Event 65535.12

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00AD   |
| Data Size    | 20 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00A0:                                         53 F8 FF               S..
00B0: FF 7F F8 FF FF 7F 6E 74  6F 31 81 01 F8 FF FF 7F  ......nto1......
00C0: 00                                                .               
```

#### Opcodes

```
  0: 0x00AD [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "nto1" with entities [EventEntity, EventEntity]
  1: 0x00BA [0x81] SET_ENTITY_BLINKING(blink_flag=0x01, entity=EventEntity)
  2: 0x00C0 [0x00] END_REQSTACK()
```

### Event 65535.13

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00C1   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00C0:    5B 01 80 F8 FF FF 7F  F8 FF FF 7F 74 68 6B 31   [..........thk1
00D0: 00                                                .               
```

#### Opcodes

```
  0: 0x00C1 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "thk1" with entities [EventEntity, EventEntity], work=358*
  1: 0x00D0 [0x00] END_REQSTACK()
```

### Event 65535.14

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00D1   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00D0:    53 F8 FF FF 7F F8 FF  FF 7F 74 68 6B 31 00      S........thk1. 
```

#### Opcodes

```
  0: 0x00D1 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "thk1" with entities [EventEntity, EventEntity]
  1: 0x00DE [0x00] END_REQSTACK()
```

### Event 65535.15

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00DF   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00D0:                                               5B                 [
00E0: 01 80 F8 FF FF 7F F8 FF  FF 7F 74 68 6B 32 00     ..........thk2. 
```

#### Opcodes

```
  0: 0x00DF [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "thk2" with entities [EventEntity, EventEntity], work=358*
  1: 0x00EE [0x00] END_REQSTACK()
```

### Event 65535.16

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
00F0: F8 FF FF 7F F8 FF FF 7F  74 68 6B 32 00           ........thk2.   
```

#### Opcodes

```
  0: 0x00EF [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "thk2" with entities [EventEntity, EventEntity]
  1: 0x00FC [0x00] END_REQSTACK()
```

### Event 65535.17

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00FD   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00F0:                                         5B 01 80               [..
0100: F8 FF FF 7F F8 FF FF 7F  70 6F 69 30 00           ........poi0.   
```

#### Opcodes

```
  0: 0x00FD [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "poi0" with entities [EventEntity, EventEntity], work=358*
  1: 0x010C [0x00] END_REQSTACK()
```

### Event 65535.18

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x010D   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0100:                                         53 F8 FF               S..
0110: FF 7F F8 FF FF 7F 70 6F  69 30 00                 ......poi0.     
```

#### Opcodes

```
  0: 0x010D [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "poi0" with entities [EventEntity, EventEntity]
  1: 0x011A [0x00] END_REQSTACK()
```

### Event 65535.19

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x011B   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0110:                                   5B 02 80 F8 FF             [....
0120: FF 7F F8 FF FF 7F 70 6F  69 31 00                 ......poi1.     
```

#### Opcodes

```
  0: 0x011B [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "poi1" with entities [EventEntity, EventEntity], work=360*
  1: 0x012A [0x00] END_REQSTACK()
```

### Event 65535.20

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x012B   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0120:                                   53 F8 FF FF 7F             S....
0130: F8 FF FF 7F 70 6F 69 31  00                       ....poi1.       
```

#### Opcodes

```
  0: 0x012B [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "poi1" with entities [EventEntity, EventEntity]
  1: 0x0138 [0x00] END_REQSTACK()
```

### Event 65535.21

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0139   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0130:                             5B 02 80 F8 FF FF 7F           [......
0140: F8 FF FF 7F 70 6F 69 33  00                       ....poi3.       
```

#### Opcodes

```
  0: 0x0139 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "poi3" with entities [EventEntity, EventEntity], work=360*
  1: 0x0148 [0x00] END_REQSTACK()
```

### Event 65535.22

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
0150: FF 7F 70 6F 69 33 00                              ..poi3.         
```

#### Opcodes

```
  0: 0x0149 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "poi3" with entities [EventEntity, EventEntity]
  1: 0x0156 [0x00] END_REQSTACK()
```

### Event 65535.23

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0157   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0150:                      5B  02 80 F8 FF FF 7F F8 FF         [........
0160: FF 7F 64 69 73 30 00                              ..dis0.         
```

#### Opcodes

```
  0: 0x0157 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "dis0" with entities [EventEntity, EventEntity], work=360*
  1: 0x0166 [0x00] END_REQSTACK()
```

### Event 65535.24

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0167   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0160:                      53  F8 FF FF 7F F8 FF FF 7F         S........
0170: 64 69 73 30 00                                    dis0.           
```

#### Opcodes

```
  0: 0x0167 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "dis0" with entities [EventEntity, EventEntity]
  1: 0x0174 [0x00] END_REQSTACK()
```

### Event 65535.25

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0175  |
| Data Size    | 9 bytes |
| Instructions | 3       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0170:                5E 69 64  6C 30 1C 03 80 00             ^idl0....  
```

#### Opcodes

```
  0: 0x0175 [0x5E] EventEntity goes idle (kills current action) (animation: "idl0")
  1: 0x017A [0x1C] WAIT(30* ticks)
  2: 0x017D [0x00] END_REQSTACK()
```

### Event 10021

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x017E  |
| Data Size    | 3 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0170:                                            22 00                ".
0180: 00                                                .               
```

#### Opcodes

```
  0: 0x017E [0x22] ENTITY_HIDE_FLAG(enabled=0x00)
  1: 0x0180 [0x00] END_REQSTACK()
```

### Event 10022

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0181  |
| Data Size    | 3 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0180:    22 00 00                                        "..            
```

#### Opcodes

```
  0: 0x0181 [0x22] ENTITY_HIDE_FLAG(enabled=0x00)
  1: 0x0183 [0x00] END_REQSTACK()
```

### Event 65535.26

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0184   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0180:             37 04 80 05  80 06 80 07 80 00            7.........  
```

#### Opcodes

```
  0: 0x0184 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=19.342*, z=-6.533*, y=-0.100*, direction=305.9°*
  1: 0x018D [0x00] END_REQSTACK()
```

### Event 65535.27

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x018E   |
| Data Size    | 26 bytes |
| Instructions | 6        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0180:                                            37 08                7.
0190: 80 09 80 0A 80 0B 80 1C  0C 80 32 0D 80 1F 00 0E  ..........2.....
01A0: 80 0F 80 06 80 1F 01 00                           ........        
```

#### Opcodes

```
  0: 0x018E [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=20.089*, z=-5.220*, y=-0.111*, direction=306.5°*
  1: 0x0197 [0x1C] WAIT(80* ticks)
  2: 0x019A [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  3: 0x019D [0x1F] MOVE_ENTITY: EventEntity moves to X=21.156*, Z=-3.257*, Y=-0.100*
  4: 0x01A5 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  5: 0x01A7 [0x00] END_REQSTACK()
```

### Event 65535.28

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x01A8   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
01A0:                          37 10 80 11 80 12 80 13          7.......
01B0: 80 00                                             ..              
```

#### Opcodes

```
  0: 0x01A8 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=23.891*, z=-1.931*, y=-0.101*, direction=259.0°*
  1: 0x01B1 [0x00] END_REQSTACK()
```

### Event 65535.29

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x01B2   |
| Data Size    | 14 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
01B0:       32 0D 80 1F 00 14  80 15 80 0A 80 1F 01 00    2.............
```

#### Opcodes

```
  0: 0x01B2 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x01B5 [0x1F] MOVE_ENTITY: EventEntity moves to X=22.164*, Z=0.576*, Y=-0.111*
  2: 0x01BD [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x01BF [0x00] END_REQSTACK()
```

### Event 65535.30

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x01C0   |
| Data Size    | 14 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
01C0: 32 0D 80 1F 00 16 80 17  80 18 80 1F 01 00        2.............  
```

#### Opcodes

```
  0: 0x01C0 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x01C3 [0x1F] MOVE_ENTITY: EventEntity moves to X=21.464*, Z=1.792*, Y=-0.099*
  2: 0x01CB [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x01CD [0x00] END_REQSTACK()
```
