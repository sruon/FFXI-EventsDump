# 17752271 - Gomada-Vulmada

## Common Data

| Field            | Value                     |
|------------------|---------------------------|
| Zone             | Windurst Waters (ID: 238) |
| Block Size       | 496 bytes                 |
| Total Events     | 21                        |
| References Count | 6                         |

## List of Events

| Event ID                   | Entrypoint   |   Size |   Instructions |
|----------------------------|--------------|--------|----------------|
| [65535](#event-65535)      | 0x0000       |      1 |              1 |
| [65535.1](#event-655351)   | 0x0001       |     16 |              2 |
| [65535.2](#event-655352)   | 0x0011       |     24 |              4 |
| [65535.3](#event-655353)   | 0x0029       |     16 |              2 |
| [65535.4](#event-655354)   | 0x0039       |     22 |              4 |
| [65535.5](#event-655355)   | 0x004F       |     22 |              3 |
| [65535.6](#event-655356)   | 0x0065       |     20 |              3 |
| [65535.7](#event-655357)   | 0x0079       |     22 |              3 |
| [65535.8](#event-655358)   | 0x008F       |     20 |              3 |
| [65535.9](#event-655359)   | 0x00A3       |     16 |              2 |
| [65535.10](#event-6553510) | 0x00B3       |     22 |              4 |
| [65535.11](#event-6553511) | 0x00C9       |     16 |              2 |
| [65535.12](#event-6553512) | 0x00D9       |     14 |              2 |
| [65535.13](#event-6553513) | 0x00E7       |     22 |              3 |
| [65535.14](#event-6553514) | 0x00FD       |     20 |              3 |
| [65535.15](#event-6553515) | 0x0111       |     41 |              5 |
| [65535.16](#event-6553516) | 0x013A       |     16 |              2 |
| [65535.17](#event-6553517) | 0x014A       |     22 |              4 |
| [65535.18](#event-6553518) | 0x0160       |      9 |              3 |
| [776](#event-776)          | 0x0169       |      1 |              1 |
| [65535.19](#event-6553519) | 0x016A       |     10 |              2 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0055      |          85 |
|       1 | 0x001E      |          30 |
|       2 | 0xFFFD11AB  |  4294775211 |
|       3 | 0xFFFE4E22  |  4294856226 |
|       4 | 0xFFFFD85B  |  4294957147 |
|       5 | 0x0DA2      |        3490 |

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
  0: 0x0001 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=85*
  1: 0x0010 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0011   |
| Data Size    | 24 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:    5B 00 80 F8 FF FF 7F  F8 FF FF 7F 74 6C 6B 30   [..........tlk0
0020: 5E 69 64 6C 30 1C 01 80  00                       ^idl0....       
```

#### Opcodes

```
  0: 0x0011 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=85*
  1: 0x0020 [0x5E] EventEntity goes idle (kills current action) (animation: "idl0")
  2: 0x0025 [0x1C] WAIT(30* ticks)
  3: 0x0028 [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0029   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                             5B 00 80 F8 FF FF 7F           [......
0030: F8 FF FF 7F 6E 61 69 30  00                       ....nai0.       
```

#### Opcodes

```
  0: 0x0029 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "nai0" with entities [EventEntity, EventEntity], work=85*
  1: 0x0038 [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0039   |
| Data Size    | 22 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:                             53 F8 FF FF 7F F8 FF           S......
0040: FF 7F 6E 61 69 30 5E 69  64 6C 30 1C 01 80 00     ..nai0^idl0.... 
```

#### Opcodes

```
  0: 0x0039 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "nai0" with entities [EventEntity, EventEntity]
  1: 0x0046 [0x5E] EventEntity goes idle (kills current action) (animation: "idl0")
  2: 0x004B [0x1C] WAIT(30* ticks)
  3: 0x004E [0x00] END_REQSTACK()
```

### Event 65535.5

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x004F   |
| Data Size    | 22 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                                               7C                 |
0050: 00 F8 FF FF 7F 5B 00 80  F8 FF FF 7F F8 FF FF 7F  .....[..........
0060: 74 6C 6B 32 00                                    tlk2.           
```

#### Opcodes

```
  0: 0x004F [0x7C] EventEntity->Render.Flags2 |= 0x00
  1: 0x0055 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tlk2" with entities [EventEntity, EventEntity], work=85*
  2: 0x0064 [0x00] END_REQSTACK()
```

### Event 65535.6

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0065   |
| Data Size    | 20 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060:                53 F8 FF  FF 7F F8 FF FF 7F 74 6C       S........tl
0070: 6B 32 7C 01 F8 FF FF 7F  00                       k2|......       
```

#### Opcodes

```
  0: 0x0065 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "tlk2" with entities [EventEntity, EventEntity]
  1: 0x0072 [0x7C] EventEntity->Render.Flags2 |= 0x01
  2: 0x0078 [0x00] END_REQSTACK()
```

### Event 65535.7

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0079   |
| Data Size    | 22 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0070:                             7C 00 F8 FF FF 7F 5B           |.....[
0080: 00 80 F8 FF FF 7F F8 FF  FF 7F 73 75 72 30 00     ..........sur0. 
```

#### Opcodes

```
  0: 0x0079 [0x7C] EventEntity->Render.Flags2 |= 0x00
  1: 0x007F [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "sur0" with entities [EventEntity, EventEntity], work=85*
  2: 0x008E [0x00] END_REQSTACK()
```

### Event 65535.8

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x008F   |
| Data Size    | 20 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0080:                                               53                 S
0090: F8 FF FF 7F F8 FF FF 7F  73 75 72 30 7C 01 F8 FF  ........sur0|...
00A0: FF 7F 00                                          ...             
```

#### Opcodes

```
  0: 0x008F [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "sur0" with entities [EventEntity, EventEntity]
  1: 0x009C [0x7C] EventEntity->Render.Flags2 |= 0x01
  2: 0x00A2 [0x00] END_REQSTACK()
```

### Event 65535.9

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00A3   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00A0:          5B 00 80 F8 FF  FF 7F F8 FF FF 7F 61 6E     [..........an
00B0: 67 30 00                                          g0.             
```

#### Opcodes

```
  0: 0x00A3 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "ang0" with entities [EventEntity, EventEntity], work=85*
  1: 0x00B2 [0x00] END_REQSTACK()
```

### Event 65535.10

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00B3   |
| Data Size    | 22 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00B0:          53 F8 FF FF 7F  F8 FF FF 7F 61 6E 67 30     S........ang0
00C0: 5E 69 64 6C 30 1C 01 80  00                       ^idl0....       
```

#### Opcodes

```
  0: 0x00B3 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "ang0" with entities [EventEntity, EventEntity]
  1: 0x00C0 [0x5E] EventEntity goes idle (kills current action) (animation: "idl0")
  2: 0x00C5 [0x1C] WAIT(30* ticks)
  3: 0x00C8 [0x00] END_REQSTACK()
```

### Event 65535.11

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00C9   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00C0:                             5B 00 80 F8 FF FF 7F           [......
00D0: F8 FF FF 7F 6A 6D 70 30  00                       ....jmp0.       
```

#### Opcodes

```
  0: 0x00C9 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "jmp0" with entities [EventEntity, EventEntity], work=85*
  1: 0x00D8 [0x00] END_REQSTACK()
```

### Event 65535.12

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00D9   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00D0:                             53 F8 FF FF 7F F8 FF           S......
00E0: FF 7F 6A 6D 70 30 00                              ..jmp0.         
```

#### Opcodes

```
  0: 0x00D9 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "jmp0" with entities [EventEntity, EventEntity]
  1: 0x00E6 [0x00] END_REQSTACK()
```

### Event 65535.13

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00E7   |
| Data Size    | 22 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00E0:                      7C  00 F8 FF FF 7F 5B 00 80         |.....[..
00F0: F8 FF FF 7F F8 FF FF 7F  62 61 6E 30 00           ........ban0.   
```

#### Opcodes

```
  0: 0x00E7 [0x7C] EventEntity->Render.Flags2 |= 0x00
  1: 0x00ED [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "ban0" with entities [EventEntity, EventEntity], work=85*
  2: 0x00FC [0x00] END_REQSTACK()
```

### Event 65535.14

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00FD   |
| Data Size    | 20 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00F0:                                         53 F8 FF               S..
0100: FF 7F F8 FF FF 7F 62 61  6E 30 7C 01 F8 FF FF 7F  ......ban0|.....
0110: 00                                                .               
```

#### Opcodes

```
  0: 0x00FD [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "ban0" with entities [EventEntity, EventEntity]
  1: 0x010A [0x7C] EventEntity->Render.Flags2 |= 0x01
  2: 0x0110 [0x00] END_REQSTACK()
```

### Event 65535.15

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0111   |
| Data Size    | 41 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0110:    7C 00 F8 FF FF 7F 5B  00 80 F8 FF FF 7F F8 FF   |.....[........
0120: FF 7F 62 61 6E 30 53 F8  FF FF 7F F8 FF FF 7F 62  ..ban0S........b
0130: 61 6E 30 7C 01 F8 FF FF  7F 00                    an0|......      
```

#### Opcodes

```
  0: 0x0111 [0x7C] EventEntity->Render.Flags2 |= 0x00
  1: 0x0117 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "ban0" with entities [EventEntity, EventEntity], work=85*
  2: 0x0126 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "ban0" with entities [EventEntity, EventEntity]
  3: 0x0133 [0x7C] EventEntity->Render.Flags2 |= 0x01
  4: 0x0139 [0x00] END_REQSTACK()
```

### Event 65535.16

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x013A   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0130:                                5B 00 80 F8 FF FF            [.....
0140: 7F F8 FF FF 7F 6B 6F 77  30 00                    .....kow0.      
```

#### Opcodes

```
  0: 0x013A [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "kow0" with entities [EventEntity, EventEntity], work=85*
  1: 0x0149 [0x00] END_REQSTACK()
```

### Event 65535.17

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x014A   |
| Data Size    | 22 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0140:                                53 F8 FF FF 7F F8            S.....
0150: FF FF 7F 6B 6F 77 30 5E  69 64 6C 30 1C 01 80 00  ...kow0^idl0....
```

#### Opcodes

```
  0: 0x014A [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "kow0" with entities [EventEntity, EventEntity]
  1: 0x0157 [0x5E] EventEntity goes idle (kills current action) (animation: "idl0")
  2: 0x015C [0x1C] WAIT(30* ticks)
  3: 0x015F [0x00] END_REQSTACK()
```

### Event 65535.18

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0160  |
| Data Size    | 9 bytes |
| Instructions | 3       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0160: 5E 69 64 6C 30 1C 01 80  00                       ^idl0....       
```

#### Opcodes

```
  0: 0x0160 [0x5E] EventEntity goes idle (kills current action) (animation: "idl0")
  1: 0x0165 [0x1C] WAIT(30* ticks)
  2: 0x0168 [0x00] END_REQSTACK()
```

### Event 776

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0169  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0160:                             00                             .      
```

#### Opcodes

```
  0: 0x0169 [0x00] END_REQSTACK()
```

### Event 65535.19

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x016A   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0160:                                37 02 80 03 80 04            7.....
0170: 80 05 80 00                                       ....            
```

#### Opcodes

```
  0: 0x016A [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=-192.085*, z=-111.070*, y=-10.149*, direction=306.7°*
  1: 0x0173 [0x00] END_REQSTACK()
```
