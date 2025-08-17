# 17388034 - Atarefaunet

## Common Data

| Field            | Value           |
|------------------|-----------------|
| Zone             | Davoi (ID: 149) |
| Block Size       | 648 bytes       |
| Total Events     | 33              |
| References Count | 9               |

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
| [65535.15](#event-6553515) | 0x00D3       |     16 |              2 |
| [65535.16](#event-6553516) | 0x00E3       |     14 |              2 |
| [65535.17](#event-6553517) | 0x00F1       |     16 |              2 |
| [65535.18](#event-6553518) | 0x0101       |     14 |              2 |
| [65535.19](#event-6553519) | 0x010F       |     16 |              2 |
| [65535.20](#event-6553520) | 0x011F       |     14 |              2 |
| [65535.21](#event-6553521) | 0x012D       |     16 |              2 |
| [65535.22](#event-6553522) | 0x013D       |     14 |              2 |
| [65535.23](#event-6553523) | 0x014B       |     16 |              2 |
| [65535.24](#event-6553524) | 0x015B       |     14 |              2 |
| [65535.25](#event-6553525) | 0x0169       |     16 |              2 |
| [65535.26](#event-6553526) | 0x0179       |     14 |              2 |
| [65535.27](#event-6553527) | 0x0187       |     16 |              2 |
| [65535.28](#event-6553528) | 0x0197       |     14 |              2 |
| [65535.29](#event-6553529) | 0x01A5       |     16 |              2 |
| [65535.30](#event-6553530) | 0x01B5       |     14 |              2 |
| [126](#event-126)          | 0x01C3       |      1 |              1 |
| [65535.31](#event-6553531) | 0x01C4       |     10 |              2 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0014      |          20 |
|       1 | 0x0015      |          21 |
|       2 | 0x001A      |          26 |
|       3 | 0x001B      |          27 |
|       4 | 0x001D      |          29 |
|       5 | 0xBAE4      |       47844 |
|       6 | 0x6ED0      |       28368 |
|       7 | 0xFFFFA24A  |  4294943306 |
|       8 | 0x0BC0      |        3008 |

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
0000:    66 00 80 F8 FF FF 7F  F8 FF FF 7F 74 6C 6B 30   f..........tlk0
0010: 00                                                .               
```

#### Opcodes

```
  0: 0x0001 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=20*
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
0010:                                               66                 f
0020: 00 80 F8 FF FF 7F F8 FF  FF 7F 74 6C 6B 31 00     ..........tlk1. 
```

#### Opcodes

```
  0: 0x001F [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk1" with entities [EventEntity, EventEntity], work=20*
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
0030:                                         66 00 80               f..
0040: F8 FF FF 7F F8 FF FF 7F  74 68 6B 31 00           ........thk1.   
```

#### Opcodes

```
  0: 0x003D [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "thk1" with entities [EventEntity, EventEntity], work=20*
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
0050: FF 7F F8 FF FF 7F 74 68  6B 31 00                 ......thk1.     
```

#### Opcodes

```
  0: 0x004D [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "thk1" with entities [EventEntity, EventEntity]
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
0050:                                   66 00 80 F8 FF             f....
0060: FF 7F F8 FF FF 7F 74 68  6B 32 00                 ......thk2.     
```

#### Opcodes

```
  0: 0x005B [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "thk2" with entities [EventEntity, EventEntity], work=20*
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
0070: F8 FF FF 7F 74 68 6B 32  00                       ....thk2.       
```

#### Opcodes

```
  0: 0x006B [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "thk2" with entities [EventEntity, EventEntity]
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
0070:                             66 00 80 F8 FF FF 7F           f......
0080: F8 FF FF 7F 70 61 73 30  00                       ....pas0.       
```

#### Opcodes

```
  0: 0x0079 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "pas0" with entities [EventEntity, EventEntity], work=20*
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
0090: FF 7F 70 61 73 30 00                              ..pas0.         
```

#### Opcodes

```
  0: 0x0089 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "pas0" with entities [EventEntity, EventEntity]
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
0090:                      66  01 80 F8 FF FF 7F F8 FF         f........
00A0: FF 7F 70 6F 69 30 00                              ..poi0.         
```

#### Opcodes

```
  0: 0x0097 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "poi0" with entities [EventEntity, EventEntity], work=21*
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
00B0: 70 6F 69 30 00                                    poi0.           
```

#### Opcodes

```
  0: 0x00A7 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "poi0" with entities [EventEntity, EventEntity]
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
00B0:                66 01 80  F8 FF FF 7F F8 FF FF 7F       f..........
00C0: 70 6F 69 31 00                                    poi1.           
```

#### Opcodes

```
  0: 0x00B5 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "poi1" with entities [EventEntity, EventEntity], work=21*
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
00C0:                53 F8 FF  FF 7F F8 FF FF 7F 70 6F       S........po
00D0: 69 31 00                                          i1.             
```

#### Opcodes

```
  0: 0x00C5 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "poi1" with entities [EventEntity, EventEntity]
  1: 0x00D2 [0x00] END_REQSTACK()
```

### Event 65535.15

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00D3   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00D0:          66 01 80 F8 FF  FF 7F F8 FF FF 7F 64 69     f..........di
00E0: 73 30 00                                          s0.             
```

#### Opcodes

```
  0: 0x00D3 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "dis0" with entities [EventEntity, EventEntity], work=21*
  1: 0x00E2 [0x00] END_REQSTACK()
```

### Event 65535.16

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00E3   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00E0:          53 F8 FF FF 7F  F8 FF FF 7F 64 69 73 30     S........dis0
00F0: 00                                                .               
```

#### Opcodes

```
  0: 0x00E3 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "dis0" with entities [EventEntity, EventEntity]
  1: 0x00F0 [0x00] END_REQSTACK()
```

### Event 65535.17

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00F1   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00F0:    66 02 80 F8 FF FF 7F  F8 FF FF 7F 6F 72 6F 30   f..........oro0
0100: 00                                                .               
```

#### Opcodes

```
  0: 0x00F1 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "oro0" with entities [EventEntity, EventEntity], work=26*
  1: 0x0100 [0x00] END_REQSTACK()
```

### Event 65535.18

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0101   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0100:    53 F8 FF FF 7F F8 FF  FF 7F 6F 72 6F 30 00      S........oro0. 
```

#### Opcodes

```
  0: 0x0101 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "oro0" with entities [EventEntity, EventEntity]
  1: 0x010E [0x00] END_REQSTACK()
```

### Event 65535.19

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x010F   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0100:                                               66                 f
0110: 02 80 F8 FF FF 7F F8 FF  FF 7F 6F 72 6F 31 00     ..........oro1. 
```

#### Opcodes

```
  0: 0x010F [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "oro1" with entities [EventEntity, EventEntity], work=26*
  1: 0x011E [0x00] END_REQSTACK()
```

### Event 65535.20

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x011F   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0110:                                               53                 S
0120: F8 FF FF 7F F8 FF FF 7F  6F 72 6F 31 00           ........oro1.   
```

#### Opcodes

```
  0: 0x011F [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "oro1" with entities [EventEntity, EventEntity]
  1: 0x012C [0x00] END_REQSTACK()
```

### Event 65535.21

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x012D   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0120:                                         66 03 80               f..
0130: F8 FF FF 7F F8 FF FF 7F  74 6C 62 30 00           ........tlb0.   
```

#### Opcodes

```
  0: 0x012D [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlb0" with entities [EventEntity, EventEntity], work=27*
  1: 0x013C [0x00] END_REQSTACK()
```

### Event 65535.22

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x013D   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0130:                                         53 F8 FF               S..
0140: FF 7F F8 FF FF 7F 74 6C  62 30 00                 ......tlb0.     
```

#### Opcodes

```
  0: 0x013D [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "tlb0" with entities [EventEntity, EventEntity]
  1: 0x014A [0x00] END_REQSTACK()
```

### Event 65535.23

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x014B   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0140:                                   66 03 80 F8 FF             f....
0150: FF 7F F8 FF FF 7F 74 6C  62 31 00                 ......tlb1.     
```

#### Opcodes

```
  0: 0x014B [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlb1" with entities [EventEntity, EventEntity], work=27*
  1: 0x015A [0x00] END_REQSTACK()
```

### Event 65535.24

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x015B   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0150:                                   53 F8 FF FF 7F             S....
0160: F8 FF FF 7F 74 6C 62 31  00                       ....tlb1.       
```

#### Opcodes

```
  0: 0x015B [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "tlb1" with entities [EventEntity, EventEntity]
  1: 0x0168 [0x00] END_REQSTACK()
```

### Event 65535.25

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0169   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0160:                             66 04 80 F8 FF FF 7F           f......
0170: F8 FF FF 7F 73 69 74 30  00                       ....sit0.       
```

#### Opcodes

```
  0: 0x0169 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "sit0" with entities [EventEntity, EventEntity], work=29*
  1: 0x0178 [0x00] END_REQSTACK()
```

### Event 65535.26

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0179   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0170:                             53 F8 FF FF 7F F8 FF           S......
0180: FF 7F 73 69 74 30 00                              ..sit0.         
```

#### Opcodes

```
  0: 0x0179 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "sit0" with entities [EventEntity, EventEntity]
  1: 0x0186 [0x00] END_REQSTACK()
```

### Event 65535.27

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0187   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0180:                      66  04 80 F8 FF FF 7F F8 FF         f........
0190: FF 7F 73 69 74 31 00                              ..sit1.         
```

#### Opcodes

```
  0: 0x0187 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "sit1" with entities [EventEntity, EventEntity], work=29*
  1: 0x0196 [0x00] END_REQSTACK()
```

### Event 65535.28

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0197   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0190:                      53  F8 FF FF 7F F8 FF FF 7F         S........
01A0: 73 69 74 31 00                                    sit1.           
```

#### Opcodes

```
  0: 0x0197 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "sit1" with entities [EventEntity, EventEntity]
  1: 0x01A4 [0x00] END_REQSTACK()
```

### Event 65535.29

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x01A5   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
01A0:                66 04 80  F8 FF FF 7F F8 FF FF 7F       f..........
01B0: 73 69 74 6C 00                                    sitl.           
```

#### Opcodes

```
  0: 0x01A5 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "sitl" with entities [EventEntity, EventEntity], work=29*
  1: 0x01B4 [0x00] END_REQSTACK()
```

### Event 65535.30

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x01B5   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
01B0:                53 F8 FF  FF 7F F8 FF FF 7F 73 69       S........si
01C0: 74 6C 00                                          tl.             
```

#### Opcodes

```
  0: 0x01B5 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "sitl" with entities [EventEntity, EventEntity]
  1: 0x01C2 [0x00] END_REQSTACK()
```

### Event 126

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x01C3  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
01C0:          00                                          .            
```

#### Opcodes

```
  0: 0x01C3 [0x00] END_REQSTACK()
```

### Event 65535.31

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x01C4   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
01C0:             37 05 80 06  80 07 80 08 80 00            7.........  
```

#### Opcodes

```
  0: 0x01C4 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=47.844*, z=28.368*, y=-23.990*, direction=264.4°*
  1: 0x01CD [0x00] END_REQSTACK()
```
