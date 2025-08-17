# 17752287 - Talking Doll

## Common Data

| Field            | Value                     |
|------------------|---------------------------|
| Zone             | Windurst Waters (ID: 238) |
| Block Size       | 280 bytes                 |
| Total Events     | 16                        |
| References Count | 16                        |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [804](#event-804)        | 0x0001       |     10 |              2 |
| [805](#event-805)        | 0x000B       |      8 |              2 |
| [806](#event-806)        | 0x0013       |      8 |              2 |
| [807](#event-807)        | 0x001B       |      8 |              2 |
| [808](#event-808)        | 0x0023       |      8 |              2 |
| [809](#event-809)        | 0x002B       |      8 |              2 |
| [810](#event-810)        | 0x0033       |      8 |              2 |
| [811](#event-811)        | 0x003B       |      8 |              2 |
| [812](#event-812)        | 0x0043       |      8 |              2 |
| [813](#event-813)        | 0x004B       |      8 |              2 |
| [1156](#event-1156)      | 0x0053       |      1 |              1 |
| [65535.1](#event-655351) | 0x0054       |     16 |              2 |
| [65535.2](#event-655352) | 0x0064       |     22 |              4 |
| [65535.3](#event-655353) | 0x007A       |      5 |              2 |
| [1173](#event-1173)      | 0x007F       |      7 |              2 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x25538     |      152888 |
|       1 | 0x3668C     |      222860 |
|       2 | 0xFFFFF63C  |  4294964796 |
|       3 | 0x0FD0      |        4048 |
|       4 | 0x385CC     |      230860 |
|       5 | 0x3A50C     |      238860 |
|       6 | 0x2410B     |      147723 |
|       7 | 0x3B4DA     |      242906 |
|       8 | 0xFFFFE13D  |  4294959421 |
|       9 | 0x385E5     |      230885 |
|      10 | 0x29ABD     |      170685 |
|      11 | 0x2AF73     |      175987 |
|      12 | 0xFFFFF5D7  |  4294964695 |
|      13 | 0x00FC      |         252 |
|      14 | 0x001E      |          30 |
|      15 | 0x00AC      |         172 |

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

### Event 804

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    37 00 80 01 80 02 80  03 80 00                  7.........     
```

#### Opcodes

```
  0: 0x0001 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=152.888*, z=222.860*, y=-2.500*, direction=355.8°*
  1: 0x000A [0x00] END_REQSTACK()
```

### Event 805

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x000B  |
| Data Size    | 8 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                                   36 00 80 04 80             6....
0010: 02 80 00                                          ...             
```

#### Opcodes

```
  0: 0x000B [0x36] SET_ENTITY_EVENT_POSITION(pos_x=152.888*, pos_z=230.860*, pos_y=-2.500*)
  1: 0x0012 [0x00] END_REQSTACK()
```

### Event 806

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0013  |
| Data Size    | 8 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:          36 00 80 05 80  02 80 00                    6.......     
```

#### Opcodes

```
  0: 0x0013 [0x36] SET_ENTITY_EVENT_POSITION(pos_x=152.888*, pos_z=238.860*, pos_y=-2.500*)
  1: 0x001A [0x00] END_REQSTACK()
```

### Event 807

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x001B  |
| Data Size    | 8 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                                   36 06 80 07 80             6....
0020: 08 80 00                                          ...             
```

#### Opcodes

```
  0: 0x001B [0x36] SET_ENTITY_EVENT_POSITION(pos_x=147.723*, pos_z=242.906*, pos_y=-7.875*)
  1: 0x0022 [0x00] END_REQSTACK()
```

### Event 808

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0023  |
| Data Size    | 8 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:          36 06 80 09 80  08 80 00                    6.......     
```

#### Opcodes

```
  0: 0x0023 [0x36] SET_ENTITY_EVENT_POSITION(pos_x=147.723*, pos_z=230.885*, pos_y=-7.875*)
  1: 0x002A [0x00] END_REQSTACK()
```

### Event 809

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x002B  |
| Data Size    | 8 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                                   36 0A 80 07 80             6....
0030: 08 80 00                                          ...             
```

#### Opcodes

```
  0: 0x002B [0x36] SET_ENTITY_EVENT_POSITION(pos_x=170.685*, pos_z=242.906*, pos_y=-7.875*)
  1: 0x0032 [0x00] END_REQSTACK()
```

### Event 810

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0033  |
| Data Size    | 8 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:          36 0A 80 09 80  08 80 00                    6.......     
```

#### Opcodes

```
  0: 0x0033 [0x36] SET_ENTITY_EVENT_POSITION(pos_x=170.685*, pos_z=230.885*, pos_y=-7.875*)
  1: 0x003A [0x00] END_REQSTACK()
```

### Event 811

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x003B  |
| Data Size    | 8 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:                                   36 0B 80 05 80             6....
0040: 0C 80 00                                          ...             
```

#### Opcodes

```
  0: 0x003B [0x36] SET_ENTITY_EVENT_POSITION(pos_x=175.987*, pos_z=238.860*, pos_y=-2.601*)
  1: 0x0042 [0x00] END_REQSTACK()
```

### Event 812

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0043  |
| Data Size    | 8 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:          36 0B 80 04 80  0C 80 00                    6.......     
```

#### Opcodes

```
  0: 0x0043 [0x36] SET_ENTITY_EVENT_POSITION(pos_x=175.987*, pos_z=230.860*, pos_y=-2.601*)
  1: 0x004A [0x00] END_REQSTACK()
```

### Event 813

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x004B  |
| Data Size    | 8 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                                   36 0B 80 01 80             6....
0050: 0C 80 00                                          ...             
```

#### Opcodes

```
  0: 0x004B [0x36] SET_ENTITY_EVENT_POSITION(pos_x=175.987*, pos_z=222.860*, pos_y=-2.601*)
  1: 0x0052 [0x00] END_REQSTACK()
```

### Event 1156

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0053  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:          00                                          .            
```

#### Opcodes

```
  0: 0x0053 [0x00] END_REQSTACK()
```

### Event 65535.1

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0054   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:             5B 0D 80 F8  FF FF 7F F8 FF FF 7F 62      [..........b
0060: 72 75 30 00                                       ru0.            
```

#### Opcodes

```
  0: 0x0054 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "bru0" with entities [EventEntity, EventEntity], work=252*
  1: 0x0063 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0064   |
| Data Size    | 22 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060:             53 F8 FF FF  7F F8 FF FF 7F 62 72 75      S........bru
0070: 30 5E 69 64 6C 30 1C 0E  80 00                    0^idl0....      
```

#### Opcodes

```
  0: 0x0064 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "bru0" with entities [EventEntity, EventEntity]
  1: 0x0071 [0x5E] EventEntity goes idle (kills current action) (animation: "idl0")
  2: 0x0076 [0x1C] WAIT(30* ticks)
  3: 0x0079 [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x007A  |
| Data Size    | 5 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0070:                                B6 00 0F 80 00               ..... 
```

#### Opcodes

```
  0: 0x007A [0xB6] ENTITY_APPEARANCE_HANDLER(case=Hair style, value=172*)
  1: 0x007E [0x00] END_REQSTACK()
```

### Event 1173

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x007F  |
| Data Size    | 7 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0070:                                               92                 .
0080: 01 F8 FF FF 7F 00                                 ......          
```

#### Opcodes

```
  0: 0x007F [0x92] EventEntity->Render.Flags3 ^= 0x01
  1: 0x0085 [0x00] END_REQSTACK()
```
