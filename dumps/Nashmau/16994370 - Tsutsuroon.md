# 16994370 - Tsutsuroon

## Common Data

| Field            | Value            |
|------------------|------------------|
| Zone             | Nashmau (ID: 53) |
| Block Size       | 200 bytes        |
| Total Events     | 10               |
| References Count | 19               |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [291](#event-291)        | 0x0001       |      1 |              1 |
| [65535.1](#event-655351) | 0x0002       |     10 |              2 |
| [65535.2](#event-655352) | 0x000C       |     10 |              2 |
| [65535.3](#event-655353) | 0x0016       |     10 |              2 |
| [65535.4](#event-655354) | 0x0020       |     14 |              4 |
| [65535.5](#event-655355) | 0x002E       |     10 |              2 |
| [65535.6](#event-655356) | 0x0038       |     10 |              2 |
| [311](#event-311)        | 0x0042       |      1 |              1 |
| [312](#event-312)        | 0x0043       |      1 |              1 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x31D5      |       12757 |
|       1 | 0xFFFF63A1  |  4294927265 |
|       2 | 0x0000      |           0 |
|       3 | 0x0D25      |        3365 |
|       4 | 0x2469      |        9321 |
|       5 | 0xFFFF4CF0  |  4294921456 |
|       6 | 0x0F6C      |        3948 |
|       7 | 0x32C1      |       12993 |
|       8 | 0xFFFF4744  |  4294920004 |
|       9 | 0x0B58      |        2904 |
|      10 | 0x000D      |          13 |
|      11 | 0x323C      |       12860 |
|      12 | 0xFFFF50A2  |  4294922402 |
|      13 | 0x08CC      |        2252 |
|      14 | 0xFFFF610B  |  4294926603 |
|      15 | 0x0CF7      |        3319 |
|      16 | 0x0D34      |        3380 |
|      17 | 0xFFFF7F0D  |  4294934285 |
|      18 | 0x094E      |        2382 |

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

### Event 291

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0001  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    00                                              .              
```

#### Opcodes

```
  0: 0x0001 [0x00] END_REQSTACK()
```

### Event 65535.1

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0002   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:       37 00 80 01 80 02  80 03 80 00                7.........    
```

#### Opcodes

```
  0: 0x0002 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=12.757*, z=-40.031*, y=0.000*, direction=295.7°*
  1: 0x000B [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x000C   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                                      37 04 80 05              7...
0010: 80 02 80 06 80 00                                 ......          
```

#### Opcodes

```
  0: 0x000C [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=9.321*, z=-45.840*, y=0.000*, direction=347.0°*
  1: 0x0015 [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0016   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                   37 07  80 08 80 02 80 09 80 00        7.........
```

#### Opcodes

```
  0: 0x0016 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=12.993*, z=-47.292*, y=0.000*, direction=255.2°*
  1: 0x001F [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0020   |
| Data Size    | 14 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020: 32 0A 80 1F 00 0B 80 0C  80 02 80 1F 01 00        2.............  
```

#### Opcodes

```
  0: 0x0020 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x0023 [0x1F] MOVE_ENTITY: EventEntity moves to X=12.860*, Z=-44.894*, Y=0.000*
  2: 0x002B [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x002D [0x00] END_REQSTACK()
```

### Event 65535.5

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x002E   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                                            37 0D                7.
0030: 80 0E 80 02 80 0F 80 00                           ........        
```

#### Opcodes

```
  0: 0x002E [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=2.252*, z=-40.693*, y=0.000*, direction=291.7°*
  1: 0x0037 [0x00] END_REQSTACK()
```

### Event 65535.6

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0038   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:                          37 10 80 11 80 02 80 12          7.......
0040: 80 00                                             ..              
```

#### Opcodes

```
  0: 0x0038 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=3.380*, z=-33.011*, y=0.000*, direction=209.3°*
  1: 0x0041 [0x00] END_REQSTACK()
```

### Event 311

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0042  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:       00                                            .             
```

#### Opcodes

```
  0: 0x0042 [0x00] END_REQSTACK()
```

### Event 312

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0043  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:          00                                          .            
```

#### Opcodes

```
  0: 0x0043 [0x00] END_REQSTACK()
```
