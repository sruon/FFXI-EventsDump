# 17199696 - Lewenhart

## Common Data

| Field            | Value                   |
|------------------|-------------------------|
| Zone             | Valkurm Dunes (ID: 103) |
| Block Size       | 328 bytes               |
| Total Events     | 12                      |
| References Count | 10                      |

## List of Events

| Event ID                   | Entrypoint   |   Size |   Instructions |
|----------------------------|--------------|--------|----------------|
| [65535](#event-65535)      | 0x0000       |     15 |              4 |
| [2](#event-2)              | 0x000F       |      1 |              1 |
| [65535.1](#event-655351)   | 0x0010       |     11 |              3 |
| [65535.2](#event-655352)   | 0x001B       |     19 |              3 |
| [65535.3](#event-655353)   | 0x002E       |     29 |              3 |
| [65535.4](#event-655354)   | 0x004B       |     19 |              3 |
| [65535.5](#event-655355)   | 0x005E       |     29 |              3 |
| [65535.6](#event-655356)   | 0x007B       |     25 |              4 |
| [65535.7](#event-655357)   | 0x0094       |     35 |              4 |
| [65535.8](#event-655358)   | 0x00B7       |     29 |              3 |
| [65535.9](#event-655359)   | 0x00D4       |      9 |              3 |
| [65535.10](#event-6553510) | 0x00DD       |      1 |              1 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x000D      |          13 |
|       1 | 0xFFF4F824  |  4294244388 |
|       2 | 0x19C99     |      105625 |
|       3 | 0xFFFFE33A  |  4294959930 |
|       4 | 0x0087      |         135 |
|       5 | 0xFFF506A5  |  4294248101 |
|       6 | 0x19721     |      104225 |
|       7 | 0xFFFFE36A  |  4294959978 |
|       8 | 0x0000      |           0 |
|       9 | 0x003C      |          60 |

## Events

### Event 65535

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0000   |
| Data Size    | 15 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000: 22 01 32 00 80 37 01 80  02 80 03 80 04 80 00     ".2..7......... 
```

#### Opcodes

```
  0: 0x0000 [0x22] ENTITY_HIDE_FLAG(enabled=0x01)
  1: 0x0002 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  2: 0x0005 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=-722.908*, z=105.625*, y=-7.366*, direction=11.9°*
  3: 0x000E [0x00] END_REQSTACK()
```

### Event 2

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x000F  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                                               00                 .
```

#### Opcodes

```
  0: 0x000F [0x00] END_REQSTACK()
```

### Event 65535.1

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0010   |
| Data Size    | 11 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010: 1F 00 05 80 06 80 07 80  1F 01 00                 ...........     
```

#### Opcodes

```
  0: 0x0010 [0x1F] MOVE_ENTITY: EventEntity moves to X=-719.195*, Z=104.225*, Y=-7.318*
  1: 0x0018 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  2: 0x001A [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x001B   |
| Data Size    | 19 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                                   66 08 80 F8 FF             f....
0020: FF 7F F8 FF FF 7F 74 6C  6B 30 1C 09 80 00        ......tlk0....  
```

#### Opcodes

```
  0: 0x001B [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=0*
  1: 0x002A [0x1C] WAIT(60* ticks)
  2: 0x002D [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x002E   |
| Data Size    | 29 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                                            66 08                f.
0030: 80 F8 FF FF 7F F8 FF FF  7F 74 65 6E 30 53 F8 FF  .........ten0S..
0040: FF 7F F8 FF FF 7F 74 65  6E 30 00                 ......ten0.     
```

#### Opcodes

```
  0: 0x002E [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "ten0" with entities [EventEntity, EventEntity], work=0*
  1: 0x003D [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "ten0" with entities [EventEntity, EventEntity]
  2: 0x004A [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x004B   |
| Data Size    | 19 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                                   66 08 80 F8 FF             f....
0050: FF 7F F8 FF FF 7F 74 6C  6B 31 1C 09 80 00        ......tlk1....  
```

#### Opcodes

```
  0: 0x004B [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk1" with entities [EventEntity, EventEntity], work=0*
  1: 0x005A [0x1C] WAIT(60* ticks)
  2: 0x005D [0x00] END_REQSTACK()
```

### Event 65535.5

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x005E   |
| Data Size    | 29 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:                                            66 08                f.
0060: 80 F8 FF FF 7F F8 FF FF  7F 74 65 6E 31 53 F8 FF  .........ten1S..
0070: FF 7F F8 FF FF 7F 74 65  6E 31 00                 ......ten1.     
```

#### Opcodes

```
  0: 0x005E [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "ten1" with entities [EventEntity, EventEntity], work=0*
  1: 0x006D [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "ten1" with entities [EventEntity, EventEntity]
  2: 0x007A [0x00] END_REQSTACK()
```

### Event 65535.6

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x007B   |
| Data Size    | 25 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0070:                                   81 00 F8 FF FF             .....
0080: 7F 66 08 80 F8 FF FF 7F  F8 FF FF 7F 74 68 6B 31  .f..........thk1
0090: 1C 09 80 00                                       ....            
```

#### Opcodes

```
  0: 0x007B [0x81] SET_ENTITY_BLINKING(blink_flag=0x00, entity=EventEntity)
  1: 0x0081 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "thk1" with entities [EventEntity, EventEntity], work=0*
  2: 0x0090 [0x1C] WAIT(60* ticks)
  3: 0x0093 [0x00] END_REQSTACK()
```

### Event 65535.7

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0094   |
| Data Size    | 35 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0090:             81 01 F8 FF  FF 7F 66 08 80 F8 FF FF      ......f.....
00A0: 7F F8 FF FF 7F 74 68 6B  32 53 F8 FF FF 7F F8 FF  .....thk2S......
00B0: FF 7F 74 68 6B 32 00                              ..thk2.         
```

#### Opcodes

```
  0: 0x0094 [0x81] SET_ENTITY_BLINKING(blink_flag=0x01, entity=EventEntity)
  1: 0x009A [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "thk2" with entities [EventEntity, EventEntity], work=0*
  2: 0x00A9 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "thk2" with entities [EventEntity, EventEntity]
  3: 0x00B6 [0x00] END_REQSTACK()
```

### Event 65535.8

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00B7   |
| Data Size    | 29 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00B0:                      66  08 80 F8 FF FF 7F F8 FF         f........
00C0: FF 7F 64 69 73 30 53 F8  FF FF 7F F8 FF FF 7F 64  ..dis0S........d
00D0: 69 73 30 00                                       is0.            
```

#### Opcodes

```
  0: 0x00B7 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "dis0" with entities [EventEntity, EventEntity], work=0*
  1: 0x00C6 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "dis0" with entities [EventEntity, EventEntity]
  2: 0x00D3 [0x00] END_REQSTACK()
```

### Event 65535.9

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x00D4  |
| Data Size    | 9 bytes |
| Instructions | 3       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00D0:             5E 69 64 6C  30 1C 09 80 00               ^idl0....   
```

#### Opcodes

```
  0: 0x00D4 [0x5E] EventEntity goes idle (kills current action) (animation: "idl0")
  1: 0x00D9 [0x1C] WAIT(60* ticks)
  2: 0x00DC [0x00] END_REQSTACK()
```

### Event 65535.10

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x00DD  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00D0:                                         00                     .  
```

#### Opcodes

```
  0: 0x00DD [0x00] END_REQSTACK()
```
