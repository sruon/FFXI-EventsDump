# 16982470 - Rongelouts

## Common Data

| Field            | Value                         |
|------------------|-------------------------------|
| Zone             | Aht Urhgan Whitegate (ID: 50) |
| Block Size       | 300 bytes                     |
| Total Events     | 18                            |
| References Count | 18                            |

## List of Events

| Event ID                  | Entrypoint   |   Size |   Instructions |
|---------------------------|--------------|--------|----------------|
| [65535](#event-65535)     | 0x0000       |      1 |              1 |
| [5071](#event-5071)       | 0x0001       |      1 |              1 |
| [5073](#event-5073)       | 0x0002       |      1 |              1 |
| [65535.1](#event-65535-1) | 0x0003       |     18 |              6 |
| [65535.2](#event-65535-2) | 0x0015       |     14 |              4 |
| [65535.3](#event-65535-3) | 0x0023       |     47 |              8 |
| [65535.4](#event-65535-4) | 0x0052       |     47 |              8 |
| [5075](#event-5075)       | 0x0081       |      1 |              1 |
| [5076](#event-5076)       | 0x0082       |      1 |              1 |
| [5077](#event-5077)       | 0x0083       |      1 |              1 |
| [5078](#event-5078)       | 0x0084       |      1 |              1 |
| [5080](#event-5080)       | 0x0085       |      1 |              1 |
| [5081](#event-5081)       | 0x0086       |      1 |              1 |
| [5082](#event-5082)       | 0x0087       |      1 |              1 |
| [5083](#event-5083)       | 0x0088       |      1 |              1 |
| [5084](#event-5084)       | 0x0089       |      1 |              1 |
| [5085](#event-5085)       | 0x008A       |      1 |              1 |
| [5086](#event-5086)       | 0x008B       |      1 |              1 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x000D      |          13 |
|       1 | 0xFFF75462  |  4294399074 |
|       2 | 0xF171      |       61809 |
|       3 | 0x0000      |           0 |
|       4 | 0x003C      |          60 |
|       5 | 0xFFF753B9  |  4294398905 |
|       6 | 0xB0B3      |       45235 |
|       7 | 0x07CF      |        1999 |
|       8 | 0xFFF75B69  |  4294400873 |
|       9 | 0xA409      |       41993 |
|      10 | 0x07D0      |        2000 |
|      11 | 0xFFF75CF7  |  4294401271 |
|      12 | 0x9287      |       37511 |
|      13 | 0xFFF75C8B  |  4294401163 |
|      14 | 0x94F4      |       38132 |
|      15 | 0x050C      |        1292 |
|      16 | 0xFFF75D51  |  4294401361 |
|      17 | 0xA6B9      |       42681 |

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

### Event 5071

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

### Event 5073

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
| Data Size    | 18 bytes |
| Instructions | 6        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:          32 00 80 1F 00  01 80 02 80 03 80 1F 01     2............
0010: 6F 1C 04 80 00                                    o....           
```

#### Opcodes

```
  0: 0x0003 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x0006 [0x1F] MOVE_ENTITY: EventEntity moves to X=-568.222*, Z=61.809*, Y=0.000*
  2: 0x000E [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0010 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x0011 [0x1C] WAIT(60* ticks)
  5: 0x0014 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0015   |
| Data Size    | 14 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                32 00 80  1F 00 05 80 06 80 07 80       2..........
0020: 1F 01 00                                          ...             
```

#### Opcodes

```
  0: 0x0015 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x0018 [0x1F] MOVE_ENTITY: EventEntity moves to X=-568.391*, Z=45.235*, Y=1.999*
  2: 0x0020 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0022 [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0023   |
| Data Size    | 47 bytes |
| Instructions | 8        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:          BA C6 21 03 01  08 80 09 80 07 80 0A 80     ..!..........
0030: 32 00 80 79 00 C6 21 03  01 D3 20 03 01 1F 00 0B  2..y..!... .....
0040: 80 0C 80 07 80 1F 01 6F  4A C6 21 03 01 D3 20 03  .......oJ.!... .
0050: 01 00                                             ..              
```

#### Opcodes

```
  0: 0x0023 [0xBA] SET_ENTITY_POSITION(entity_id=Rongelouts (ID: 16982470/0x010321C6), pos_x=-566.423*, pos_z=41.993*, pos_y=1.999*, direction=175.8°*)
  1: 0x0030 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  2: 0x0033 [0x79] Rongelouts (ID: 16982470/0x010321C6) looks at Falzum (ID: 16982227/0x010320D3) (Basic look)
  3: 0x003D [0x1F] MOVE_ENTITY: EventEntity moves to X=-566.025*, Z=37.511*, Y=1.999*
  4: 0x0045 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  5: 0x0047 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  6: 0x0048 [0x4A] Rongelouts (ID: 16982470/0x010321C6) looks at Falzum (ID: 16982227/0x010320D3)
  7: 0x0051 [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0052   |
| Data Size    | 47 bytes |
| Instructions | 8        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:       BA C6 21 03 01 0D  80 0E 80 07 80 0F 80 32    ..!..........2
0060: 00 80 79 00 C6 21 03 01  CB 21 03 01 1F 00 10 80  ..y..!...!......
0070: 11 80 07 80 1F 01 6F 4A  C6 21 03 01 CB 21 03 01  ......oJ.!...!..
0080: 00                                                .               
```

#### Opcodes

```
  0: 0x0052 [0xBA] SET_ENTITY_POSITION(entity_id=Rongelouts (ID: 16982470/0x010321C6), pos_x=-566.133*, pos_z=38.132*, pos_y=1.999*, direction=113.6°*)
  1: 0x005F [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  2: 0x0062 [0x79] Rongelouts (ID: 16982470/0x010321C6) looks at Neosaliat (ID: 16982475/0x010321CB) (Basic look)
  3: 0x006C [0x1F] MOVE_ENTITY: EventEntity moves to X=-565.935*, Z=42.681*, Y=1.999*
  4: 0x0074 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  5: 0x0076 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  6: 0x0077 [0x4A] Rongelouts (ID: 16982470/0x010321C6) looks at Neosaliat (ID: 16982475/0x010321CB)
  7: 0x0080 [0x00] END_REQSTACK()
```

### Event 5075

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0081  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0080:    00                                              .              
```

#### Opcodes

```
  0: 0x0081 [0x00] END_REQSTACK()
```

### Event 5076

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0082  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0080:       00                                            .             
```

#### Opcodes

```
  0: 0x0082 [0x00] END_REQSTACK()
```

### Event 5077

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0083  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0080:          00                                          .            
```

#### Opcodes

```
  0: 0x0083 [0x00] END_REQSTACK()
```

### Event 5078

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0084  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0080:             00                                        .           
```

#### Opcodes

```
  0: 0x0084 [0x00] END_REQSTACK()
```

### Event 5080

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

### Event 5081

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0086  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0080:                   00                                    .         
```

#### Opcodes

```
  0: 0x0086 [0x00] END_REQSTACK()
```

### Event 5082

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0087  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0080:                      00                                  .        
```

#### Opcodes

```
  0: 0x0087 [0x00] END_REQSTACK()
```

### Event 5083

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0088  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0080:                          00                               .       
```

#### Opcodes

```
  0: 0x0088 [0x00] END_REQSTACK()
```

### Event 5084

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0089  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0080:                             00                             .      
```

#### Opcodes

```
  0: 0x0089 [0x00] END_REQSTACK()
```

### Event 5085

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x008A  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0080:                                00                           .     
```

#### Opcodes

```
  0: 0x008A [0x00] END_REQSTACK()
```

### Event 5086

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x008B  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0080:                                   00                         .    
```

#### Opcodes

```
  0: 0x008B [0x00] END_REQSTACK()
```
