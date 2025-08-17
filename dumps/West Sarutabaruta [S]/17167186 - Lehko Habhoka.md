# 17167186 - Lehko Habhoka

## Common Data

| Field            | Value                          |
|------------------|--------------------------------|
| Zone             | West Sarutabaruta [S] (ID: 95) |
| Block Size       | 332 bytes                      |
| Total Events     | 13                             |
| References Count | 28                             |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [102](#event-102)        | 0x0001       |      1 |              1 |
| [103](#event-103)        | 0x0002       |      1 |              1 |
| [65535.1](#event-655351) | 0x0003       |     20 |              6 |
| [65535.2](#event-655352) | 0x0017       |     15 |              5 |
| [65535.3](#event-655353) | 0x0026       |      3 |              2 |
| [104](#event-104)        | 0x0029       |      1 |              1 |
| [65535.4](#event-655354) | 0x002A       |     15 |              5 |
| [65535.5](#event-655355) | 0x0039       |     18 |              6 |
| [65535.6](#event-655356) | 0x004B       |     29 |              7 |
| [65535.7](#event-655357) | 0x0068       |     23 |              7 |
| [65535.8](#event-655358) | 0x007F       |     20 |              6 |
| [65535.9](#event-655359) | 0x0093       |      4 |              2 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x000D      |          13 |
|       1 | 0xFFFA8F40  |  4294610752 |
|       2 | 0xFFF9F87A  |  4294572154 |
|       3 | 0x0F68      |        3944 |
|       4 | 0xFFFA906D  |  4294611053 |
|       5 | 0xFFF9E795  |  4294567829 |
|       6 | 0x0F9F      |        3999 |
|       7 | 0xFFFAA465  |  4294616165 |
|       8 | 0xFFFA6502  |  4294599938 |
|       9 | 0x0D8E      |        3470 |
|      10 | 0xFFFA2ADB  |  4294585051 |
|      11 | 0xFFF9731B  |  4294538011 |
|      12 | 0x243C      |        9276 |
|      13 | 0x07D0      |        2000 |
|      14 | 0x2364C     |      144972 |
|      15 | 0x513C9     |      332745 |
|      16 | 0xFFFF6AF8  |  4294929144 |
|      17 | 0x070C      |        1804 |
|      18 | 0x217D3     |      137171 |
|      19 | 0x510BD     |      331965 |
|      20 | 0xFFFF6E30  |  4294929968 |
|      21 | 0x2208C     |      139404 |
|      22 | 0x50C3F     |      330815 |
|      23 | 0xFFFF6D5C  |  4294929756 |
|      24 | 0x0005      |           5 |
|      25 | 0x23417     |      144407 |
|      26 | 0x51B31     |      334641 |
|      27 | 0xFFFF6BD9  |  4294929369 |

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

### Event 102

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

### Event 103

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0002  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:       00                                            .             
```

#### Opcodes

```
  0: 0x0002 [0x00] END_REQSTACK()
```

### Event 65535.1

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0003   |
| Data Size    | 20 bytes |
| Instructions | 6        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:          32 00 80 1F 00  01 80 02 80 03 80 1F 01     2............
0010: 6F 1E F0 FF FF 7F 00                              o......         
```

#### Opcodes

```
  0: 0x0003 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x0006 [0x1F] MOVE_ENTITY: EventEntity moves to X=-356.544*, Z=-395.142*, Y=3.944*
  2: 0x000E [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0010 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x0011 [0x1E] EventEntity looks at LocalPlayer and starts talking
  5: 0x0016 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0017   |
| Data Size    | 15 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                      32  00 80 1F 00 04 80 05 80         2........
0020: 06 80 1F 01 6F 00                                 ....o.          
```

#### Opcodes

```
  0: 0x0017 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x001A [0x1F] MOVE_ENTITY: EventEntity moves to X=-356.243*, Z=-399.467*, Y=3.999*
  2: 0x0022 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0024 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x0025 [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0026  |
| Data Size    | 3 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                   A4 01  00                             ...       
```

#### Opcodes

```
  0: 0x0026 [0xA4] EventEntity->Flags3.unknown_3_2 = 1
  1: 0x0028 [0x00] END_REQSTACK()
```

### Event 104

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0029  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                             00                             .      
```

#### Opcodes

```
  0: 0x0029 [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x002A   |
| Data Size    | 15 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                                32 00 80 1F 00 07            2.....
0030: 80 08 80 09 80 1F 01 6F  00                       .......o.       
```

#### Opcodes

```
  0: 0x002A [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x002D [0x1F] MOVE_ENTITY: EventEntity moves to X=-351.131*, Z=-367.358*, Y=3.470*
  2: 0x0035 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0037 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x0038 [0x00] END_REQSTACK()
```

### Event 65535.5

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0039   |
| Data Size    | 18 bytes |
| Instructions | 6        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:                             32 00 80 1F 00 0A 80           2......
0040: 0B 80 0C 80 1F 01 6F 39  0D 80 00                 ......o9...     
```

#### Opcodes

```
  0: 0x0039 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x003C [0x1F] MOVE_ENTITY: EventEntity moves to X=-382.245*, Z=-429.285*, Y=9.276*
  2: 0x0044 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0046 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x0047 [0x39] SET_ENTITY_DIRECTION(direction=11.0°*)
  5: 0x004A [0x00] END_REQSTACK()
```

### Event 65535.6

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x004B   |
| Data Size    | 29 bytes |
| Instructions | 7        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                                   37 0E 80 0F 80             7....
0050: 10 80 11 80 32 00 80 1F  00 12 80 13 80 14 80 1F  ....2...........
0060: 01 6F 1E F0 FF FF 7F 00                           .o......        
```

#### Opcodes

```
  0: 0x004B [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=144.972*, z=332.745*, y=-38.152*, direction=158.6°*
  1: 0x0054 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  2: 0x0057 [0x1F] MOVE_ENTITY: EventEntity moves to X=137.171*, Z=331.965*, Y=-37.328*
  3: 0x005F [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  4: 0x0061 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  5: 0x0062 [0x1E] EventEntity looks at LocalPlayer and starts talking
  6: 0x0067 [0x00] END_REQSTACK()
```

### Event 65535.7

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0068   |
| Data Size    | 23 bytes |
| Instructions | 7        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060:                          32 00 80 1F 00 15 80 16          2.......
0070: 80 17 80 1F 01 6F 1E F0  FF FF 7F 1C 18 80 00     .....o......... 
```

#### Opcodes

```
  0: 0x0068 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x006B [0x1F] MOVE_ENTITY: EventEntity moves to X=139.404*, Z=330.815*, Y=-37.540*
  2: 0x0073 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0075 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x0076 [0x1E] EventEntity looks at LocalPlayer and starts talking
  5: 0x007B [0x1C] WAIT(5* ticks)
  6: 0x007E [0x00] END_REQSTACK()
```

### Event 65535.8

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x007F   |
| Data Size    | 20 bytes |
| Instructions | 6        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0070:                                               32                 2
0080: 00 80 1F 00 19 80 1A 80  1B 80 1F 01 6F 1E F0 FF  ............o...
0090: FF 7F 00                                          ...             
```

#### Opcodes

```
  0: 0x007F [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x0082 [0x1F] MOVE_ENTITY: EventEntity moves to X=144.407*, Z=334.641*, Y=-37.927*
  2: 0x008A [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x008C [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x008D [0x1E] EventEntity looks at LocalPlayer and starts talking
  5: 0x0092 [0x00] END_REQSTACK()
```

### Event 65535.9

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0093  |
| Data Size    | 4 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0090:          39 0D 80 00                                 9...         
```

#### Opcodes

```
  0: 0x0093 [0x39] SET_ENTITY_DIRECTION(direction=11.0°*)
  1: 0x0096 [0x00] END_REQSTACK()
```
