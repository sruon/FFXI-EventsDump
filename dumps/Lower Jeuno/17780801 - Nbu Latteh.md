# 17780801 - Nbu Latteh

## Common Data

| Field            | Value                 |
|------------------|-----------------------|
| Zone             | Lower Jeuno (ID: 245) |
| Block Size       | 580 bytes             |
| Total Events     | 29                    |
| References Count | 6                     |

## List of Events

| Event ID                   | Entrypoint   |   Size |   Instructions |
|----------------------------|--------------|--------|----------------|
| [65535](#event-65535)      | 0x0000       |      1 |              1 |
| [65535.1](#event-655351)   | 0x0001       |     16 |              2 |
| [65535.2](#event-655352)   | 0x0011       |      9 |              3 |
| [65535.3](#event-655353)   | 0x001A       |     22 |              3 |
| [65535.4](#event-655354)   | 0x0030       |     14 |              2 |
| [65535.5](#event-655355)   | 0x003E       |     16 |              2 |
| [65535.6](#event-655356)   | 0x004E       |     20 |              3 |
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
| [65535.19](#event-6553519) | 0x0116       |     28 |              4 |
| [65535.20](#event-6553520) | 0x0132       |     26 |              4 |
| [65535.21](#event-6553521) | 0x014C       |     16 |              2 |
| [65535.22](#event-6553522) | 0x015C       |     14 |              2 |
| [65535.23](#event-6553523) | 0x016A       |     16 |              2 |
| [65535.24](#event-6553524) | 0x017A       |     14 |              2 |
| [65535.25](#event-6553525) | 0x0188       |      9 |              3 |
| [10021](#event-10021)      | 0x0191       |      3 |              2 |
| [65535.26](#event-6553526) | 0x0194       |     19 |              5 |
| [10022](#event-10022)      | 0x01A7       |      1 |              1 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0032      |          50 |
|       1 | 0x001E      |          30 |
|       2 | 0x0034      |          52 |
|       3 | 0x0035      |          53 |
|       4 | 0x0008      |           8 |
|       5 | 0x1EFF      |        7935 |

## String References

- **7935**: Also known as the Scarlet Thunder of La Theine, rrright?

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
  0: 0x0001 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=50*
  1: 0x0010 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0011  |
| Data Size    | 9 bytes |
| Instructions | 3       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:    5E 69 64 6C 30 1C 01  80 00                     ^idl0....      
```

#### Opcodes

```
  0: 0x0011 [0x5E] EventEntity goes idle (kills current action) (animation: "idl0")
  1: 0x0016 [0x1C] WAIT(30* ticks)
  2: 0x0019 [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x001A   |
| Data Size    | 22 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                                81 00 F8 FF FF 7F            ......
0020: 66 00 80 F8 FF FF 7F F8  FF FF 7F 74 68 6B 31 00  f..........thk1.
```

#### Opcodes

```
  0: 0x001A [0x81] SET_ENTITY_BLINKING(blink_flag=0x00, entity=EventEntity)
  1: 0x0020 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "thk1" with entities [EventEntity, EventEntity], work=50*
  2: 0x002F [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0030   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030: 53 F8 FF FF 7F F8 FF FF  7F 74 68 6B 31 00        S........thk1.  
```

#### Opcodes

```
  0: 0x0030 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "thk1" with entities [EventEntity, EventEntity]
  1: 0x003D [0x00] END_REQSTACK()
```

### Event 65535.5

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x003E   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:                                            66 00                f.
0040: 80 F8 FF FF 7F F8 FF FF  7F 74 68 6B 32 00        .........thk2.  
```

#### Opcodes

```
  0: 0x003E [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "thk2" with entities [EventEntity, EventEntity], work=50*
  1: 0x004D [0x00] END_REQSTACK()
```

### Event 65535.6

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x004E   |
| Data Size    | 20 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                                            53 F8                S.
0050: FF FF 7F F8 FF FF 7F 74  68 6B 32 81 01 F8 FF FF  .......thk2.....
0060: 7F 00                                             ..              
```

#### Opcodes

```
  0: 0x004E [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "thk2" with entities [EventEntity, EventEntity]
  1: 0x005B [0x81] SET_ENTITY_BLINKING(blink_flag=0x01, entity=EventEntity)
  2: 0x0061 [0x00] END_REQSTACK()
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
0060:       66 02 80 F8 FF FF  7F F8 FF FF 7F 64 69 73    f..........dis
0070: 30 00                                             0.              
```

#### Opcodes

```
  0: 0x0062 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "dis0" with entities [EventEntity, EventEntity], work=52*
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
0070:       53 F8 FF FF 7F F8  FF FF 7F 64 69 73 30 00    S........dis0.
```

#### Opcodes

```
  0: 0x0072 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "dis0" with entities [EventEntity, EventEntity]
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
0080: 66 02 80 F8 FF FF 7F F8  FF FF 7F 74 6C 63 30 00  f..........tlc0.
```

#### Opcodes

```
  0: 0x0080 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlc0" with entities [EventEntity, EventEntity], work=52*
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
0090: 53 F8 FF FF 7F F8 FF FF  7F 74 6C 63 30 00        S........tlc0.  
```

#### Opcodes

```
  0: 0x0090 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "tlc0" with entities [EventEntity, EventEntity]
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
0090:                                            66 02                f.
00A0: 80 F8 FF FF 7F F8 FF FF  7F 74 6C 63 31 00        .........tlc1.  
```

#### Opcodes

```
  0: 0x009E [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlc1" with entities [EventEntity, EventEntity], work=52*
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
00B0: FF FF 7F F8 FF FF 7F 74  6C 63 31 00              .......tlc1.    
```

#### Opcodes

```
  0: 0x00AE [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "tlc1" with entities [EventEntity, EventEntity]
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
00B0:                                      66 03 80 F8              f...
00C0: FF FF 7F F8 FF FF 7F 74  6C 62 31 00              .......tlb1.    
```

#### Opcodes

```
  0: 0x00BC [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlb1" with entities [EventEntity, EventEntity], work=53*
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
00D0: 7F F8 FF FF 7F 74 6C 62  31 00                    .....tlb1.      
```

#### Opcodes

```
  0: 0x00CC [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "tlb1" with entities [EventEntity, EventEntity]
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
00D0:                                66 03 80 F8 FF FF            f.....
00E0: 7F F8 FF FF 7F 74 6C 62  32 00                    .....tlb2.      
```

#### Opcodes

```
  0: 0x00DA [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlb2" with entities [EventEntity, EventEntity], work=53*
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
00F0: FF FF 7F 74 6C 62 32 00                           ...tlb2.        
```

#### Opcodes

```
  0: 0x00EA [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "tlb2" with entities [EventEntity, EventEntity]
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
00F0:                          66 02 80 F8 FF FF 7F F8          f.......
0100: FF FF 7F 73 69 73 30 00                           ...sis0.        
```

#### Opcodes

```
  0: 0x00F8 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "sis0" with entities [EventEntity, EventEntity], work=52*
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
0110: 7F 73 69 73 30 00                                 .sis0.          
```

#### Opcodes

```
  0: 0x0108 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "sis0" with entities [EventEntity, EventEntity]
  1: 0x0115 [0x00] END_REQSTACK()
```

### Event 65535.19

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0116   |
| Data Size    | 28 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0110:                   7C 00  F8 FF FF 7F 81 00 F8 FF        |.........
0120: FF 7F 66 04 80 F8 FF FF  7F F8 FF FF 7F 61 6E 67  ..f..........ang
0130: 30 00                                             0.              
```

#### Opcodes

```
  0: 0x0116 [0x7C] EventEntity->Render.Flags2 |= 0x00
  1: 0x011C [0x81] SET_ENTITY_BLINKING(blink_flag=0x00, entity=EventEntity)
  2: 0x0122 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "ang0" with entities [EventEntity, EventEntity], work=8*
  3: 0x0131 [0x00] END_REQSTACK()
```

### Event 65535.20

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0132   |
| Data Size    | 26 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0130:       53 F8 FF FF 7F F8  FF FF 7F 61 6E 67 30 7C    S........ang0|
0140: 01 F8 FF FF 7F 81 01 F8  FF FF 7F 00              ............    
```

#### Opcodes

```
  0: 0x0132 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "ang0" with entities [EventEntity, EventEntity]
  1: 0x013F [0x7C] EventEntity->Render.Flags2 |= 0x01
  2: 0x0145 [0x81] SET_ENTITY_BLINKING(blink_flag=0x01, entity=EventEntity)
  3: 0x014B [0x00] END_REQSTACK()
```

### Event 65535.21

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x014C   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0140:                                      66 04 80 F8              f...
0150: FF FF 7F F8 FF FF 7F 61  77 77 30 00              .......aww0.    
```

#### Opcodes

```
  0: 0x014C [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "aww0" with entities [EventEntity, EventEntity], work=8*
  1: 0x015B [0x00] END_REQSTACK()
```

### Event 65535.22

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x015C   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0150:                                      53 F8 FF FF              S...
0160: 7F F8 FF FF 7F 61 77 77  30 00                    .....aww0.      
```

#### Opcodes

```
  0: 0x015C [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "aww0" with entities [EventEntity, EventEntity]
  1: 0x0169 [0x00] END_REQSTACK()
```

### Event 65535.23

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x016A   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0160:                                66 02 80 F8 FF FF            f.....
0170: 7F F8 FF FF 7F 70 6F 69  30 00                    .....poi0.      
```

#### Opcodes

```
  0: 0x016A [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "poi0" with entities [EventEntity, EventEntity], work=52*
  1: 0x0179 [0x00] END_REQSTACK()
```

### Event 65535.24

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x017A   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0170:                                53 F8 FF FF 7F F8            S.....
0180: FF FF 7F 70 6F 69 30 00                           ...poi0.        
```

#### Opcodes

```
  0: 0x017A [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "poi0" with entities [EventEntity, EventEntity]
  1: 0x0187 [0x00] END_REQSTACK()
```

### Event 65535.25

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0188  |
| Data Size    | 9 bytes |
| Instructions | 3       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0180:                          5E 69 64 6C 30 1C 01 80          ^idl0...
0190: 00                                                .               
```

#### Opcodes

```
  0: 0x0188 [0x5E] EventEntity goes idle (kills current action) (animation: "idl0")
  1: 0x018D [0x1C] WAIT(30* ticks)
  2: 0x0190 [0x00] END_REQSTACK()
```

### Event 10021

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0191  |
| Data Size    | 3 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0190:    22 00 00                                        "..            
```

#### Opcodes

```
  0: 0x0191 [0x22] ENTITY_HIDE_FLAG(enabled=0x00)
  1: 0x0193 [0x00] END_REQSTACK()
```

### Event 65535.26

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0194   |
| Data Size    | 19 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0190:             29 08 41 50  0F 01 05 1D 05 80 23 29      ).AP......#)
01A0: 08 41 50 0F 01 06 00                              .AP....         
```

#### Opcodes

```
  0: 0x0194 [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Nbu Latteh (ID: 17780801/0x010F5041), tag_num=0x05)
  1: 0x019B [0x1D] PRINT_EVENT_MESSAGE(message_id=7935*)
    → "Also known as the Scarlet Thunder of La Theine, rrright?"
  2: 0x019E [0x23] WAIT_FOR_DIALOG_INTERACTION
  3: 0x019F [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Nbu Latteh (ID: 17780801/0x010F5041), tag_num=0x06)
  4: 0x01A6 [0x00] END_REQSTACK()
```

### Event 10022

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x01A7  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
01A0:                      00                                  .        
```

#### Opcodes

```
  0: 0x01A7 [0x00] END_REQSTACK()
```
