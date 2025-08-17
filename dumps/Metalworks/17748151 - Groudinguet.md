# 17748151 - Groudinguet

## Common Data

| Field            | Value                |
|------------------|----------------------|
| Zone             | Metalworks (ID: 237) |
| Block Size       | 288 bytes            |
| Total Events     | 14                   |
| References Count | 20                   |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [908](#event-908)        | 0x0001       |      1 |              1 |
| [65535.1](#event-655351) | 0x0002       |     15 |              3 |
| [65535.2](#event-655352) | 0x0011       |     14 |              4 |
| [65535.3](#event-655353) | 0x001F       |     14 |              4 |
| [909](#event-909)        | 0x002D       |      1 |              1 |
| [65535.4](#event-655354) | 0x002E       |     15 |              3 |
| [65535.5](#event-655355) | 0x003D       |     14 |              4 |
| [65535.6](#event-655356) | 0x004B       |     14 |              4 |
| [910](#event-910)        | 0x0059       |      1 |              1 |
| [65535.7](#event-655357) | 0x005A       |     15 |              3 |
| [65535.8](#event-655358) | 0x0069       |     14 |              4 |
| [65535.9](#event-655359) | 0x0077       |     14 |              4 |
| [925](#event-925)        | 0x0085       |      1 |              1 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0xFFFF32EB  |  4294914795 |
|       1 | 0x5646      |       22086 |
|       2 | 0x0AD5      |        2773 |
|       3 | 0x0BC8      |        3016 |
|       4 | 0x000D      |          13 |
|       5 | 0xFFFF32D3  |  4294914771 |
|       6 | 0x5B23      |       23331 |
|       7 | 0xFFFFCDE1  |  4294954465 |
|       8 | 0xFFFFF120  |  4294963488 |
|       9 | 0x0000      |           0 |
|      10 | 0x07BD      |        1981 |
|      11 | 0xFFFFCA9B  |  4294953627 |
|      12 | 0xFFFFECAB  |  4294962347 |
|      13 | 0xFFFE91DD  |  4294873565 |
|      14 | 0xFFFFDC38  |  4294958136 |
|      15 | 0x07CF      |        1999 |
|      16 | 0x002E      |          46 |
|      17 | 0xFFFE9658  |  4294874712 |
|      18 | 0xFFFFDBB9  |  4294958009 |
|      19 | 0x07D0      |        2000 |

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

### Event 908

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
| Data Size    | 15 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:       37 00 80 01 80 02  80 03 80 80 F8 FF FF 7F    7.............
0010: 00                                                .               
```

#### Opcodes

```
  0: 0x0002 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=-52.501*, z=22.086*, y=2.773*, direction=265.1°*
  1: 0x000B [0x80] LOAD_WAIT(entity=EventEntity)
  2: 0x0010 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0011   |
| Data Size    | 14 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:    32 04 80 1F 00 05 80  06 80 02 80 1F 01 00      2............. 
```

#### Opcodes

```
  0: 0x0011 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x0014 [0x1F] MOVE_ENTITY: EventEntity moves to X=-52.525*, Z=23.331*, Y=2.773*
  2: 0x001C [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x001E [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x001F   |
| Data Size    | 14 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                                               32                 2
0020: 04 80 1F 00 00 80 01 80  02 80 1F 01 00           .............   
```

#### Opcodes

```
  0: 0x001F [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x0022 [0x1F] MOVE_ENTITY: EventEntity moves to X=-52.501*, Z=22.086*, Y=2.773*
  2: 0x002A [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x002C [0x00] END_REQSTACK()
```

### Event 909

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x002D  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                                         00                     .  
```

#### Opcodes

```
  0: 0x002D [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x002E   |
| Data Size    | 15 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                                            37 07                7.
0030: 80 08 80 09 80 0A 80 80  F8 FF FF 7F 00           .............   
```

#### Opcodes

```
  0: 0x002E [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=-12.831*, z=-3.808*, y=0.000*, direction=174.1°*
  1: 0x0037 [0x80] LOAD_WAIT(entity=EventEntity)
  2: 0x003C [0x00] END_REQSTACK()
```

### Event 65535.5

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x003D   |
| Data Size    | 14 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:                                         32 04 80               2..
0040: 1F 00 0B 80 0C 80 09 80  1F 01 00                 ...........     
```

#### Opcodes

```
  0: 0x003D [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x0040 [0x1F] MOVE_ENTITY: EventEntity moves to X=-13.669*, Z=-4.949*, Y=0.000*
  2: 0x0048 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x004A [0x00] END_REQSTACK()
```

### Event 65535.6

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x004B   |
| Data Size    | 14 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                                   32 04 80 1F 00             2....
0050: 07 80 08 80 09 80 1F 01  00                       .........       
```

#### Opcodes

```
  0: 0x004B [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x004E [0x1F] MOVE_ENTITY: EventEntity moves to X=-12.831*, Z=-3.808*, Y=0.000*
  2: 0x0056 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0058 [0x00] END_REQSTACK()
```

### Event 910

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0059  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:                             00                             .      
```

#### Opcodes

```
  0: 0x0059 [0x00] END_REQSTACK()
```

### Event 65535.7

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x005A   |
| Data Size    | 15 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:                                37 0D 80 0E 80 0F            7.....
0060: 80 10 80 80 F8 FF FF 7F  00                       .........       
```

#### Opcodes

```
  0: 0x005A [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=-93.731*, z=-9.160*, y=1.999*, direction=4.0°*
  1: 0x0063 [0x80] LOAD_WAIT(entity=EventEntity)
  2: 0x0068 [0x00] END_REQSTACK()
```

### Event 65535.8

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0069   |
| Data Size    | 14 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060:                             32 04 80 1F 00 11 80           2......
0070: 12 80 13 80 1F 01 00                              .......         
```

#### Opcodes

```
  0: 0x0069 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x006C [0x1F] MOVE_ENTITY: EventEntity moves to X=-92.584*, Z=-9.287*, Y=2.000*
  2: 0x0074 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0076 [0x00] END_REQSTACK()
```

### Event 65535.9

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0077   |
| Data Size    | 14 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0070:                      32  04 80 1F 00 0D 80 0E 80         2........
0080: 0F 80 1F 01 00                                    .....           
```

#### Opcodes

```
  0: 0x0077 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x007A [0x1F] MOVE_ENTITY: EventEntity moves to X=-93.731*, Z=-9.160*, Y=1.999*
  2: 0x0082 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0084 [0x00] END_REQSTACK()
```

### Event 925

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0085  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0080:                00                                      .          
```

#### Opcodes

```
  0: 0x0085 [0x00] END_REQSTACK()
```
