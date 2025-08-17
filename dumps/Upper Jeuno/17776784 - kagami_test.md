# 17776784 - kagami_test

## Common Data

| Field            | Value                 |
|------------------|-----------------------|
| Zone             | Upper Jeuno (ID: 244) |
| Block Size       | 436 bytes             |
| Total Events     | 23                    |
| References Count | 32                    |

## List of Events

| Event ID                   | Entrypoint   |   Size |   Instructions |
|----------------------------|--------------|--------|----------------|
| [65535](#event-65535)      | 0x0000       |      1 |              1 |
| [10044](#event-10044)      | 0x0001       |      1 |              1 |
| [65535.1](#event-655351)   | 0x0002       |     12 |              3 |
| [65535.2](#event-655352)   | 0x000E       |     12 |              3 |
| [65535.3](#event-655353)   | 0x001A       |     12 |              3 |
| [65535.4](#event-655354)   | 0x0026       |     12 |              3 |
| [65535.5](#event-655355)   | 0x0032       |     12 |              3 |
| [65535.6](#event-655356)   | 0x003E       |     12 |              3 |
| [10043](#event-10043)      | 0x004A       |      1 |              1 |
| [10046](#event-10046)      | 0x004B       |      1 |              1 |
| [65535.7](#event-655357)   | 0x004C       |     12 |              3 |
| [65535.8](#event-655358)   | 0x0058       |     12 |              3 |
| [65535.9](#event-655359)   | 0x0064       |     12 |              3 |
| [10064](#event-10064)      | 0x0070       |      1 |              1 |
| [65535.10](#event-6553510) | 0x0071       |     12 |              3 |
| [65535.11](#event-6553511) | 0x007D       |     12 |              3 |
| [65535.12](#event-6553512) | 0x0089       |     12 |              3 |
| [10072](#event-10072)      | 0x0095       |     12 |              3 |
| [10073](#event-10073)      | 0x00A1       |      1 |              1 |
| [10074](#event-10074)      | 0x00A2       |     10 |              3 |
| [65535.13](#event-6553513) | 0x00AC       |     12 |              3 |
| [65535.14](#event-6553514) | 0x00B8       |     12 |              3 |
| [10075](#event-10075)      | 0x00C4       |      1 |              1 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0xFFFF2B6E  |  4294912878 |
|       1 | 0xAA18      |       43544 |
|       2 | 0xFFFFFCDF  |  4294966495 |
|       3 | 0x0A93      |        2707 |
|       4 | 0xFFFFFA88  |  4294965896 |
|       5 | 0xFFFFF982  |  4294965634 |
|       6 | 0xFFFF2D9B  |  4294913435 |
|       7 | 0xACA8      |       44200 |
|       8 | 0xFFFFFE0B  |  4294966795 |
|       9 | 0x08BD      |        2237 |
|      10 | 0xAA49      |       43593 |
|      11 | 0x005D      |          93 |
|      12 | 0xFFFF2E01  |  4294913537 |
|      13 | 0xB04C      |       45132 |
|      14 | 0x0806      |        2054 |
|      15 | 0xFFFFF9AC  |  4294965676 |
|      16 | 0xFFFF30BD  |  4294914237 |
|      17 | 0xADA2      |       44450 |
|      18 | 0xFFFFFA24  |  4294965796 |
|      19 | 0xFFFFF8E4  |  4294965476 |
|      20 | 0xFFFF34E0  |  4294915296 |
|      21 | 0xB6D0      |       46800 |
|      22 | 0xFFFFFC18  |  4294966296 |
|      23 | 0x045C      |        1116 |
|      24 | 0xFFFF38C8  |  4294916296 |
|      25 | 0xAB18      |       43800 |
|      26 | 0xFFFFF642  |  4294964802 |
|      27 | 0xFFFFF321  |  4294964001 |
|      28 | 0xFFFFF8DF  |  4294965471 |
|      29 | 0x0000      |           0 |
|      30 | 0xFFFFF3E9  |  4294964201 |
|      31 | 0xFFFFF63C  |  4294964796 |

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

### Event 10044

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
| Data Size    | 12 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:       33 01 37 00 80 01  80 02 80 03 80 00          3.7.........  
```

#### Opcodes

```
  0: 0x0002 [0x33] EventEntity->Render.Flags0 |= 0x200000 // Bit 21 (flag=0x01)
  1: 0x0004 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=-54.418*, z=43.544*, y=-0.801*, direction=237.9°*
  2: 0x000D [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x000E   |
| Data Size    | 12 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                                            33 01                3.
0010: 37 00 80 01 80 04 80 03  80 00                    7.........      
```

#### Opcodes

```
  0: 0x000E [0x33] EventEntity->Render.Flags0 |= 0x200000 // Bit 21 (flag=0x01)
  1: 0x0010 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=-54.418*, z=43.544*, y=-1.400*, direction=237.9°*
  2: 0x0019 [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x001A   |
| Data Size    | 12 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                                33 01 37 00 80 01            3.7...
0020: 80 05 80 03 80 00                                 ......          
```

#### Opcodes

```
  0: 0x001A [0x33] EventEntity->Render.Flags0 |= 0x200000 // Bit 21 (flag=0x01)
  1: 0x001C [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=-54.418*, z=43.544*, y=-1.662*, direction=237.9°*
  2: 0x0025 [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0026   |
| Data Size    | 12 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                   33 01  37 06 80 07 80 08 80 09        3.7.......
0030: 80 00                                             ..              
```

#### Opcodes

```
  0: 0x0026 [0x33] EventEntity->Render.Flags0 |= 0x200000 // Bit 21 (flag=0x01)
  1: 0x0028 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=-53.861*, z=44.200*, y=-0.501*, direction=196.6°*
  2: 0x0031 [0x00] END_REQSTACK()
```

### Event 65535.5

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0032   |
| Data Size    | 12 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:       33 01 37 06 80 0A  80 04 80 0B 80 00          3.7.........  
```

#### Opcodes

```
  0: 0x0032 [0x33] EventEntity->Render.Flags0 |= 0x200000 // Bit 21 (flag=0x01)
  1: 0x0034 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=-53.861*, z=43.593*, y=-1.400*, direction=8.2°*
  2: 0x003D [0x00] END_REQSTACK()
```

### Event 65535.6

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x003E   |
| Data Size    | 12 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:                                            33 01                3.
0040: 37 06 80 0A 80 05 80 09  80 00                    7.........      
```

#### Opcodes

```
  0: 0x003E [0x33] EventEntity->Render.Flags0 |= 0x200000 // Bit 21 (flag=0x01)
  1: 0x0040 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=-53.861*, z=43.593*, y=-1.662*, direction=196.6°*
  2: 0x0049 [0x00] END_REQSTACK()
```

### Event 10043

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x004A  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                                00                           .     
```

#### Opcodes

```
  0: 0x004A [0x00] END_REQSTACK()
```

### Event 10046

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x004B  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                                   00                         .    
```

#### Opcodes

```
  0: 0x004B [0x00] END_REQSTACK()
```

### Event 65535.7

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x004C   |
| Data Size    | 12 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                                      33 01 37 0C              3.7.
0050: 80 0D 80 08 80 0E 80 00                           ........        
```

#### Opcodes

```
  0: 0x004C [0x33] EventEntity->Render.Flags0 |= 0x200000 // Bit 21 (flag=0x01)
  1: 0x004E [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=-53.759*, z=45.132*, y=-0.501*, direction=180.5°*
  2: 0x0057 [0x00] END_REQSTACK()
```

### Event 65535.8

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0058   |
| Data Size    | 12 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:                          33 01 37 0C 80 0D 80 04          3.7.....
0060: 80 0E 80 00                                       ....            
```

#### Opcodes

```
  0: 0x0058 [0x33] EventEntity->Render.Flags0 |= 0x200000 // Bit 21 (flag=0x01)
  1: 0x005A [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=-53.759*, z=45.132*, y=-1.400*, direction=180.5°*
  2: 0x0063 [0x00] END_REQSTACK()
```

### Event 65535.9

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0064   |
| Data Size    | 12 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060:             33 01 37 0C  80 0D 80 0F 80 0E 80 00      3.7.........
```

#### Opcodes

```
  0: 0x0064 [0x33] EventEntity->Render.Flags0 |= 0x200000 // Bit 21 (flag=0x01)
  1: 0x0066 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=-53.759*, z=45.132*, y=-1.620*, direction=180.5°*
  2: 0x006F [0x00] END_REQSTACK()
```

### Event 10064

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0070  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0070: 00                                                .               
```

#### Opcodes

```
  0: 0x0070 [0x00] END_REQSTACK()
```

### Event 65535.10

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0071   |
| Data Size    | 12 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0070:    33 01 37 10 80 11 80  08 80 0E 80 00            3.7.........   
```

#### Opcodes

```
  0: 0x0071 [0x33] EventEntity->Render.Flags0 |= 0x200000 // Bit 21 (flag=0x01)
  1: 0x0073 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=-53.059*, z=44.450*, y=-0.501*, direction=180.5°*
  2: 0x007C [0x00] END_REQSTACK()
```

### Event 65535.11

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x007D   |
| Data Size    | 12 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0070:                                         33 01 37               3.7
0080: 10 80 11 80 12 80 0E 80  00                       .........       
```

#### Opcodes

```
  0: 0x007D [0x33] EventEntity->Render.Flags0 |= 0x200000 // Bit 21 (flag=0x01)
  1: 0x007F [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=-53.059*, z=44.450*, y=-1.500*, direction=180.5°*
  2: 0x0088 [0x00] END_REQSTACK()
```

### Event 65535.12

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0089   |
| Data Size    | 12 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0080:                             33 01 37 0C 80 0D 80           3.7....
0090: 13 80 0E 80 00                                    .....           
```

#### Opcodes

```
  0: 0x0089 [0x33] EventEntity->Render.Flags0 |= 0x200000 // Bit 21 (flag=0x01)
  1: 0x008B [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=-53.759*, z=45.132*, y=-1.820*, direction=180.5°*
  2: 0x0094 [0x00] END_REQSTACK()
```

### Event 10072

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0095   |
| Data Size    | 12 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0090:                33 01 37  14 80 15 80 16 80 17 80       3.7........
00A0: 00                                                .               
```

#### Opcodes

```
  0: 0x0095 [0x33] EventEntity->Render.Flags0 |= 0x200000 // Bit 21 (flag=0x01)
  1: 0x0097 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=-52.000*, z=46.800*, y=-1.000*, direction=98.1°*
  2: 0x00A0 [0x00] END_REQSTACK()
```

### Event 10073

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x00A1  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00A0:    00                                              .              
```

#### Opcodes

```
  0: 0x00A1 [0x00] END_REQSTACK()
```

### Event 10074

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00A2   |
| Data Size    | 10 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00A0:       33 01 36 18 80 19  80 16 80 00                3.6.......    
```

#### Opcodes

```
  0: 0x00A2 [0x33] EventEntity->Render.Flags0 |= 0x200000 // Bit 21 (flag=0x01)
  1: 0x00A4 [0x36] SET_ENTITY_EVENT_POSITION(pos_x=-51.000*, pos_z=43.800*, pos_y=-1.000*)
  2: 0x00AB [0x00] END_REQSTACK()
```

### Event 65535.13

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00AC   |
| Data Size    | 12 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00A0:                                      33 01 37 1A              3.7.
00B0: 80 1B 80 1C 80 1D 80 00                           ........        
```

#### Opcodes

```
  0: 0x00AC [0x33] EventEntity->Render.Flags0 |= 0x200000 // Bit 21 (flag=0x01)
  1: 0x00AE [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=-2.494*, z=-3.295*, y=-1.825*, direction=0.0°*
  2: 0x00B7 [0x00] END_REQSTACK()
```

### Event 65535.14

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00B8   |
| Data Size    | 12 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00B0:                          33 01 37 1A 80 1E 80 1F          3.7.....
00C0: 80 1D 80 00                                       ....            
```

#### Opcodes

```
  0: 0x00B8 [0x33] EventEntity->Render.Flags0 |= 0x200000 // Bit 21 (flag=0x01)
  1: 0x00BA [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=-2.494*, z=-3.095*, y=-2.500*, direction=0.0°*
  2: 0x00C3 [0x00] END_REQSTACK()
```

### Event 10075

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x00C4  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00C0:             00                                        .           
```

#### Opcodes

```
  0: 0x00C4 [0x00] END_REQSTACK()
```
